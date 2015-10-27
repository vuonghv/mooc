from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ars.subjects.models import Subject


class ListSubjectView(ListView):
    model = Subject
    template_name = 'subjects/index.html'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Subjects List',
                },
            'page_title': 'Subjects List',
        }
        context.update(info)
        return context

class DetailSubjectView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Subject Detail',
                },
            'page_title': 'Subject',
        }
        context.update(info)
        return context
