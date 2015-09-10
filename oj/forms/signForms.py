__author__ = 'yazhu'

from oj.models import Member
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class SigninForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for key in self.fields:
        #if key != 'id': #skip id
            self.fields[key].required = True

    class Meta:
        model = Member
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs = {'placeholder': 'Password'}),
            'email': forms.EmailInput(attrs = {'placeholder': 'Email'}),
            }

    def save(self, commit=False):#not commit this change in db
        return super(ModelForm, self).save(commit)

    def clean(self):
        data = super(ModelForm, self).clean()
        if len(self.errors) == 0:
            email_exists = Member.objects.all().filter(
                email=data.get('email')
            ).exists()
            if not email_exists: #or (self.fields['email'].error_messages is None):
                raise forms.ValidationError({'email':[forms.ValidationError(_('User is not existing, please signup'), code='invalid')]})
            else:
                member = Member.objects.all().get(email=data.get('email'))
                password_correct = member.password == data.get('password')
                if not password_correct:
                    raise forms.ValidationError({'password': [forms.ValidationError(_('Password is wrong, please retry'), code='invalid'),]})
                data['member'] = member # this field will be stored in cleaned_data in form
        return data


class SignupForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = Member
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs = {'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs = {'placeholder': 'Password'}),
            'email': forms.EmailInput(attrs = {'placeholder': 'Email'})
        }

    def clean(self):
        data = super(ModelForm, self).clean()
        email_exists = Member.objects.all().filter(
            email=data.get('email')
        ).exists()
        if email_exists and len(self.errors) == 0:
            raise forms.ValidationError({'email':[forms.ValidationError(_('User is already existing, please signin or choose a different email'), code='invalid')]})
        return data