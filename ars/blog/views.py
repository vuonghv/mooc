from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from ars.blog.models import Blog

# Create your views here.
class BlogView(ListView):
    """docstring for BlogView"""
    model = Blog
    context_object_name = "list_blog"
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Blog',
                },
            'page_title': 'Blog',
        }
        context.update(info)
        return context

class BlogDetailView(DetailView):
    """docstring for BlogDetailView"""
    model = Blog
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.title,
                },
            'page_title': 'Blog',
        }
        context.update(info)
        return context
        