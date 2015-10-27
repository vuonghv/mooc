from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', view=views.BlogView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.BlogDetailView.as_view(), name='detail'),
]
