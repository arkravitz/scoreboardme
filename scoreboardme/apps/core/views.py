from django.views.generic import TemplateView, FormView

from .forms import RegistrationForm

class IndexView(TemplateView):
    template_name = "core/index.html"


class RegistrationView(FormView):
    template_name = "registration/register.html"
    success_url = "/profile"
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)
