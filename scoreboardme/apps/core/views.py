from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"

"""
class UserView(TemplateView):
    template_name = "core/user.html"
"""
