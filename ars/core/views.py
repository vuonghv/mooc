from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    """docstring for LoginRequiredMixin"""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
