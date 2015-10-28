from django.views.generic import ListView

from ars.subjects.models import Subject
from ars.categories.models import Category
from ars.core.views import BaseView

class CategoriesView(BaseView, ListView):
    model = Subject
    template_name = 'categories/index.html'
    # paginate_by = 6
    context_object_name = 'list_subject'

    def get_queryset(self):
        return Subject.objects.filter(categories__id=self.kwargs['pk']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': Category.objects.get(id=self.kwargs['pk']).name,
                },
            'page_title': Category.objects.get(id=self.kwargs['pk']).name,
        }
        context.update(info)
        return context