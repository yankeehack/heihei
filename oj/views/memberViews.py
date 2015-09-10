from django.core.urlresolvers import reverse_lazy

from django.views import generic
from oj.base.baseViews import EntryView
from oj.base.mixins import userMixin
from oj.forms.signForms import SignupForm, SigninForm
# Create your views here.


class index(generic.TemplateView, userMixin):
    template_name = 'base_site.html'

    def render_to_response(self, context, **args):
        if "self" in args.keys():
            args.pop("self")
        response = super(generic.TemplateView, self).render_to_response(context, **args)
        self.clear_auth_cookies(response)
        return response


class SigninView(EntryView):
    template_name = 'signin.html'
    form_class = SigninForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(generic.CreateView, self).form_valid(form)
        self.create_auth(form.cleaned_data.get('member'))
        return self.set_cookies(response)



class SignupView(EntryView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(generic.CreateView, self).form_valid(form)
        self.create_auth(self.object)#self.object will be the saved model in createView
        return self.set_cookies(response)



