__author__ = 'yazhu'
import functools
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponseNotAllowed

def unauthenticated(method):
    """Decorate methods with this to require that user be NOT logged in"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.get_current_user():
            if self.request.method in ("GET", "HEAD"):
                return HttpResponseRedirect(reverse('index'))
            return HttpResponseNotAllowed()
        return method(self, *args, **kwargs)
    return wrapper