from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class AboutUsView(TemplateView):
    """docstring for AboutUsView"""
    template_name = 'about/index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'About us',
                },
            'page_title': 'About us',
        }
        context.update(info)
        return context