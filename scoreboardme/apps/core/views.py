from django.views.generic import DetailView, TemplateView, FormView

from braces.views import LoginRequiredMixin

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


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "core/profile.html"
    login_url = "/login/"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user.profile
