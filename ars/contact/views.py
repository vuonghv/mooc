from django.views.generic import TemplateView

from ars.core.views import BaseView


class ContactView(BaseView, TemplateView):
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
