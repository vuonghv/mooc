from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
                        {'next_page': '/admin/login/'}, name='logout'),

    #############################################################
    #############################################################
    #############################################################
    # Url category
    url(r'^category/$', views.CategoryView.as_view(), name='list_category'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='create_category'),
    url(r'^category/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(), 
                                                                    name='update_category'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$', views.CategoryDeleteView.as_view(), 
                                                                    name='delete_category'),

    #############################################################
    #############################################################
    #############################################################
    # Url course
    url(r'^course/$', views.CourseView.as_view(), name='list_course'),
    url(r'^course/create/$', views.CourseCreateView.as_view(), name='create_course'),
    url(r'^course/update/(?P<pk>[0-9]+)/$', views.CourseUpdateView.as_view(), 
                                                                    name='update_course'),
    url(r'^course/delete/(?P<pk>[0-9]+)/$', views.CourseDeleteView.as_view(), 
                                                                    name='delete_course'),

    #############################################################
    #############################################################
    #############################################################
    # Url subject
    url(r'^subject/$', views.SubjectView.as_view(), name='list_subject'),
    url(r'^subject/create/$', views.SubjectCreateView.as_view(), name='create_subject'),
    url(r'^subject/update/(?P<pk>[0-9]+)/$', views.SubjectUpdateView.as_view(), 
                                                                    name='update_subject'),
    url(r'^subject/detail/(?P<pk>[0-9]+)/$', views.SubjectDetailView.as_view(), 
                                                                    name='detail_subject'),    
    url(r'^subject/delete/(?P<pk>[0-9]+)/$', views.SubjectDeleteView.as_view(), 
                                                                    name='delete_subject'),

    url(r'^session/create/$', views.SessionCreateView.as_view(), name='create_session'),
    url(r'^task/create/$', views.TaskCreateView.as_view(), name='create_task'),
    url(r'^task/delete/(?P<pk>[0-9]+)/$', views.TaskDeleteView.as_view(), name='delete_task'),
]