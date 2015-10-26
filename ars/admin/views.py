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
        