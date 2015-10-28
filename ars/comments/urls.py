from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', view=views.CreateCommentView.as_view(), name='create'),
]
