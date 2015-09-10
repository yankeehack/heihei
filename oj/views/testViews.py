__author__ = 'yazhu'
from oj.forms.testForms import AuthorForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from oj.models import Author
from oj.celery.celeryconfig import app
import logging, time

logger = logging.getLogger(__name__)


# example and testing only
class AuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'

    @app.task(bind=True)
    def asyncCall(self):
        logger.info('hehe')
        time.sleep(5)
        logger.info('hehe ni mei')
        return 0

    def get(self, request, *args, **kwargs):
        result = self.asyncCall.delay()
        logger.info('main thread continue')
        return super(generic.CreateView, self).get(request, *args, **kwargs)


class AuthorUpdate(generic.UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')