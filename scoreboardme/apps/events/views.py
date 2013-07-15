from django.views.generic import FormView
from django.contrib.auth import authenticate

from braces.views import LoginRequiredMixin

from .forms import CreateEventForm

class CreateEventView(LoginRequiredMixin, FormView):
    template_name = "core/create_event.html"
    success_url = "/event"
    form_class = CreateEventForm
    login_url = "/login/"

    def form_valid(self, form):
        event = form.save(commit=False)
        event.creator = self.user.profile
        event.save()
        return super(CreateEventView, self).form_valid(form)