__author__ = 'yazhu'
from oj.models import Author
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']