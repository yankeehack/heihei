__author__ = 'yazhu'
import functools
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from celery import Celery

def unauthenticated(method):
    """Decorate methods with this to require that user be NOT logged in"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.get_current_user():
            if self.request.method in ("GET", "HEAD"):
                return HttpResponseRedirect(reverse('home'))
            return HttpResponseNotAllowed()
        return method(self, *args, **kwargs)
    return wrapper


def authenticated(method):
    """Decorate methods with this to require that the user be logged in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.get_current_user():
            if self.request.method in ("GET", "HEAD"):
                return HttpResponseRedirect(reverse('signin'))
            raise HttpResponseNotAllowed()
        return method(self, *args, **kwargs)
    return wrapper


# def asynchronous(method):
#     """Decorate methods with this to make the call async.
#    """
#     @functools.wraps(method)
#     @app.task
#     def wrapper(self, *args, **kwargs):
#         return method(self, *args, **kwargs)
#     return wrapper