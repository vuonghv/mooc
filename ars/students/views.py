from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView, FormView, CreateView, View
from django.apps import apps as djapps
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse, reverse_lazy

from ars.students.models import Student
from ars.core.models import UserProfile

class SignupStudentView(CreateView):
    model = djapps.get_model(settings.AUTH_USER_MODEL)
    template_name = 'students/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('students:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        profile = UserProfile.objects.create(user=self.object)
        profile.save()
        student = Student.objects.create(profile=profile)
        student.save()
        
        messages.success(self.request, "You signed up successfully,\
                                    You can log in now.")

        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Signup - Student'
            },
            'page_title': 'Sign Up',
        }
        context.update(info)
        return context


class LoginStudentView(FormView):
    template_name = 'students/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.success_url)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Login - Student'
            },
            'page_title': 'Login',
        }
        context.update(info)
        return context

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class LogoutStudentView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))
