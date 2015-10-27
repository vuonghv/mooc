from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^signup/$', views.SignupStudentView.as_view(), name='signup'),
    url(r'^login/$', views.LoginStudentView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutStudentView.as_view(), name='logout'),
]
