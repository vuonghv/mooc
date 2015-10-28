from django.shortcuts import render
from django.views.generic import FormView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse

from ars.comments.models import Comment
from ars.core.views import LoginRequiredMixin

# Create your views here.
class CreateCommentView(LoginRequiredMixin, CreateView):
    """docstring for CreateCommentView"""
    model = Comment
    fields = ['blog', 'content']

    def get(self, request, *agrs, **kwargs):
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *agrs, **kwargs):
        return super(CreateCommentView, self).post(request, *agrs, **kwargs)

    def form_valid(self, form):
        self.blog = form.cleaned_data['blog']
        self.object = form.save(commit=False)
        self.object.profile = self.request.user.profile
        self.object.blog = self.blog
        self.object.save()
        return super(CreateCommentView, self).form_valid(form)

    def form_invalid(self, form):
        self.blog = form.cleaned_data['blog']
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={ 'pk': self.blog.pk, 'slug': self.blog.slug })