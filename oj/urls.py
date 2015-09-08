
from django.conf.urls import include, url
from oj.views import memberViews, testViews, homeViews


urlpatterns = [
    url(r'^$', homeViews.homeView.as_view(), name='home'),
    url(r'^signout$', memberViews.index.as_view(), name='index'),
    url(r'^signup', memberViews.SignupView.as_view(), name='signup'),
    url(r'^signin', memberViews.SigninView.as_view(), name='signin'),


    url(r'author/add/$', testViews.AuthorCreate.as_view(), name='author_add'),
    url(r'author/(?P<pk>[0-9]+)/$', testViews.AuthorUpdate.as_view(), name='author_update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', testViews.AuthorDelete.as_view(), name='author_delete'),
    ]