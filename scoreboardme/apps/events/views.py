from django.views.generic import FormView, DetailView
from django.contrib.auth import authenticate

from braces.views import LoginRequiredMixin

from .forms import CreateEventForm
from .models import EventRequest, Event, Score
from ..core.models import UserProfile


class CreateEventView(LoginRequiredMixin, FormView):
    template_name = "events/create_event.html"
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
        print users_requested, '\n\n\n\n\n\n'
        for user in users_requested:
            EventRequest.objects.create(
                event_request=event, request_to=user, optional_message='')

        self.success_url = "/events/%d/" % event.id

        return super(CreateEventView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CreateEventView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profiles'] = UserProfile.objects.all()
        return context


class EventView(LoginRequiredMixin, DetailView):
    '''
    This is the view for rendering the event view page.
    It adds sorted scores to the context data, and makes sure
    the event is viewable by the current user.
    '''
    model = Event
    template_name = "events/event.html"
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()

        context = super(EventView, self).get_context_data(**kwargs)
        context['sorted_scores'] = self.object.score_set.order_by('score')
        return context

    def render_to_response(self, context, **response_kwargs):
        current_profile = self.request.user.profile
        self.object = self.get_object()
        creator = self.object.creator
        public = self.object.public
        profiles = self.object.profiles

        '''
        This checks for your own event, or if it's public, or if
        you're included in the event.
        '''
        if not current_profile == creator \
            and not public \
                and not current_profile in profiles:
                    return redirect("/profile/")

        return super(EventView, self).render_to_response(context, **response_kwargs)
