from django.views.generic import DetailView

from ars.core.views import BaseView
from ars.teachers.models import Teacher


class DetailTeacherView(BaseView, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'

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
