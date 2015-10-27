from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.admin.forms import AdminAuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (
        FormView, View, CreateView, DetailView,
        UpdateView, DeleteView, TemplateView, ListView,
    )

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login

from ars.categories.models import Category
from ars.courses.models import Course, TeacherCourse
from ars.subjects.models import Subject, Session
from ars.reviews.models import Review

from . import forms

# Create your views here.
class AdminRequiredMixin(object):
    """docstring for AdminRequiredMixin"""
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class LoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)

class DashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'admin/dashboard_index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        info = {
            'title': 'Dashboard - TMS',
            'sidebar': ['dashboard']
        }
        context['info'] = info
        return context

# Categories Management

class CategoryView(AdminRequiredMixin, ListView):
    """docstring for CategoryView"""
    model = Category
    context_object_name = 'list_category'
    template_name = 'admin/category_index.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        info = {
            'title': 'Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

class CategoryCreateView(AdminRequiredMixin, CreateView):
    """docstring for CategoryCreateView"""
    model = Category
    template_name = 'admin/category_create.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')

class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    """docstring for CategoryUpdateView"""
    model = Category 
    template_name = 'admin/category_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Category - TMS',
            'sidebar': ['category']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_category')

class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for CategoryDeleteView"""
    model = Category

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_category')
        

# Courses Management

class CourseView(AdminRequiredMixin, ListView):
    """docstring for CourseView"""
    model = Course
    context_object_name = 'list_course'
    template_name = 'admin/course_index.html'

    def get_queryset(self):
        return Course.objects.filter(
                teachers=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        info = {
            'title': 'Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context

class CourseCreateView(AdminRequiredMixin, CreateView):
    """docstring for CourseCreateView"""
    model = Course
    template_name = 'admin/course_create.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context

    def form_valid(self, form):
        course = form.save()
        TeacherCourse.objects.create(
                                teacher=self.request.user.profile.teacher,
                                course=course, is_creator=True)
        return super(CourseCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:list_course')

class CourseUpdateView(AdminRequiredMixin, UpdateView):
    """docstring for CourseUpdateView"""
    model = Course 
    template_name = 'admin/course_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Course - TMS',
            'sidebar': ['course']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_course')

class CourseDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for CourseDeleteView"""
    model = Course

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_course')


# Subjects Management

class SubjectView(AdminRequiredMixin, ListView):
    """docstring for SubjectView"""
    model = Subject
    context_object_name = 'list_subject'
    template_name = 'admin/subject_index.html'

    def get_queryset(self):
        return Subject.objects.filter(
                course__teachers=self.request.user.profile.teacher).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SubjectView, self).get_context_data(**kwargs)
        info = {
            'title': 'Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context

class SubjectCreateView(AdminRequiredMixin, CreateView):
    """docstring for SubjectCreateView"""
    model = Subject
    template_name = 'admin/subject_create.html'
    form_class = forms.SubjectForm

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Create Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_subject')

class SubjectUpdateView(AdminRequiredMixin, UpdateView):
    """docstring for SubjectUpdateView"""
    model = Subject 
    template_name = 'admin/subject_update.html'
    form_class = forms.SubjectForm

    def get_context_data(self, **kwargs):
        context = super(SubjectUpdateView, self).get_context_data(**kwargs)
        info = {
            'title': 'Update Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        return context

    def get_success_url(self):
        return reverse('admin:list_subject')

class SubjectDetailView(AdminRequiredMixin, DetailView):
    """docstring for SubjectDetailView"""
    model = Subject 
    template_name = 'admin/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        info = {
            'title': 'Detail Subject - TMS',
            'sidebar': ['subject']
        }
        context['info'] = info
        context['reviews'] = Review.objects.filter(
                                    subject=self.object, 
                                    subject__course__teachers=self.request.user.profile.teacher
                                    ).order_by('-id')
        context['sessions'] = Session.objects.filter(subject=self.object)
        return context

class SubjectDeleteView(AdminRequiredMixin, DeleteView):
    """docstring for SubjectDeleteView"""
    model = Subject

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:list_subject')


class SessionCreateView(AdminRequiredMixin, CreateView):
    """docstring for SessionCreateView"""
    model = Session
    fields = ['subject', 'start_date', 'end_date']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('object: ', self.object)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super(SessionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('admin:detail_subject' , kwargs={ 'pk': self.object.subject.pk })
        
