from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', view=views.AboutUsView.as_view(), name='index'),
]
