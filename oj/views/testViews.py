__author__ = 'yazhu'
from oj.forms import AuthorForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from oj.models import Author


# example and testing only
class AuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    #fields = ['name']


class AuthorUpdate(generic.UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')