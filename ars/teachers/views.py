from django.views.generic import DetailView, ListView

from ars.core.views import BaseView
from ars.teachers.models import Teacher


class DetailTeacherView(BaseView, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.username,
            },
            'page_title': self.object.username,
        }
        context.update(info)
        return context


class ListTeacherView(BaseView, ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Teachers',
            },
            'page_title': 'Teachers',
        }
        context.update(info)
        return context
