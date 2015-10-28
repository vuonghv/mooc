from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailTeacherView.as_view(), name='detail'),
]
