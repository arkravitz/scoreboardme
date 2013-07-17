from django.views.generic import DetailView, TemplateView, FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin
from class_based_auth_views.views import LoginView

from .forms import RegistrationForm
from .models import UserProfile


class IndexView(TemplateView):
    template_name = "core/index.html"


class RegistrationView(FormView):
    template_name = "registration/register.html"
    success_url = "/profile"
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user)
        new_user = authenticate(username=user.username,
                                password=self.request.POST.get('password1', ''))
        login(self.request, new_user)

        return super(RegistrationView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "core/profile.html"
    login_url = "/login/"
    context_object_name = "profile"

    def get_object(self):
        return self.request.user.profile


class RedirectLoginView(LoginView):
    def render_to_response(self, context):
        if self.request.user.is_authenticated():
            return redirect('/profile')

        return super(LoginView, self).render_to_response(context)
