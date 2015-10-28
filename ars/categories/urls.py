from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', view=views.CategoriesView.as_view(), name='index'),
]
