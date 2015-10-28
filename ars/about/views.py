from django.views.generic import TemplateView

from ars.core.views import BaseView


class AboutUsView(BaseView, TemplateView):
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
