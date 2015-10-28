from django.views.generic import ListView, DetailView

from ars.blog.models import Blog
from ars.core.views import BaseView
from ars.comments.models import Comment

# Create your views here.
class BlogView(BaseView, ListView):
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

class BlogDetailView(BaseView, DetailView):
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
            'comments': Comment.objects.filter(profile=self.request.user.profile,
                                                blog=self.object).order_by('-id')
        }
        context.update(info)
        return context
        