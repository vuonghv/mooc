from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect, HttpResponse

from ars.subjects.models import Subject
from ars.core.views import LoginRequiredMixin
from ars.subjects.models import Enroll


class ListSubjectView(ListView):
    model = Subject
    template_name = 'subjects/index.html'
    paginate_by = 6

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


class EnrollSubjectView(LoginRequiredMixin, CreateView):
    model = Enroll
    fields = ['session']

    def get(self, request, *args, **kwargs):
        return HttpResponse()

    def get_success_url(self):
        return reverse('subjects:detail',
                    kwargs={'pk': self.object.session.subject.pk})
    
    def form_valid(self, form):
        form.instance.student = self.request.user.profile.student
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
