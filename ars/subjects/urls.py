from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', view=views.ListSubjectView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', view=views.DetailSubjectView.as_view(), name='detail'),
]
