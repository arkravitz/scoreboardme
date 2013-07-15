from django.views.generic import FormView
from django.contrib.auth import authenticate

from braces.views import LoginRequiredMixin

from .forms import CreateEventForm
from .models import EventRequest
from ..core.models import UserProfile


class CreateEventView(LoginRequiredMixin, FormView):
    template_name = "events/create_event.html"
    success_url = "/event/%(id)s/"
    form_class = CreateEventForm
    login_url = "/login/"

    def get_selected_users(self):
        requested_users = self.request.POST.getlist("request_to")
        try:
            requested_users = map(int, requested_users)
        except:
            pass

        return UserProfile.objects.filter(pk__in=requested_users)

    def form_valid(self, form):
        event = form.save(commit=False)
        event.creator = self.request.user.profile
        event.save()

        # Add users to event requests that creator picked
        users_requested = self.get_selected_users()
        for user in users_requested:
            EventRequest.objects.create(
                event=event, request_to=user, optional_message='')
        return super(CreateEventView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CreateEventView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profiles'] = UserProfile.objects.all()
        return context