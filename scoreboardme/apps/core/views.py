from django.views.generic import DetailView, TemplateView, FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin
from class_based_auth_views.views import LoginView

from .forms import RegistrationForm
from .models import UserProfile


class RedirectAuthenticatedMixin(object):
    redirect_url = '/profile'

    def render_to_response(self, context):
        if self.request.user.is_authenticated():
            return redirect(self.redirect_url)

        return super(RedirectAuthenticatedMixin, self).render_to_response(context)


class IndexView(RedirectAuthenticatedMixin, TemplateView):
    template_name = "core/index.html"

class RegistrationView(RedirectAuthenticatedMixin, FormView):
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

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['completed_events'] = self.request.user.profile.get_completed_events()
        context['active_events'] = self.request.user.profile.get_active_events()
        return context


    def get_object(self):
        return self.request.user.profile


class RedirectLoginView(RedirectAuthenticatedMixin, LoginView):
    pass
