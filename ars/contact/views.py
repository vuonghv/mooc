from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class ContactView(TemplateView):
    """docstring for ContactView"""
    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Contact us',
                },
            'page_title': 'Contact us',
        }
        context.update(info)
        return context