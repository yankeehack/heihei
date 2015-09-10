__author__ = 'yazhu'
from oj.base.baseViews import BaseTemplateView
from oj.base import authenticated


class homeView(BaseTemplateView):
    template_name = 'home.html'

    @authenticated
    def get(self, request, *args, **kwargs):
        return super(BaseTemplateView, self).get(request, *args, **kwargs)