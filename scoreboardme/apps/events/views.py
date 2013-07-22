from django.views.generic import FormView, DetailView, TemplateView
from django.contrib.auth import authenticate
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin
from extra_views import InlineFormSetView

from .forms import CreateEventForm
from .models import EventRequest, Event, Score
from ..core.models import UserProfile


class CreateEventView(LoginRequiredMixin, FormView):
    template_name = "events/create_event.html"
    form_class = CreateEventForm

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
                event=event, participant=user, optional_message='')

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
        context['sorted_scores'] = self.object.score_set.order_by('-score')
        return context

    def render_to_response(self, context, **response_kwargs):
        current_profile = self.request.user.profile
        self.object = self.get_object()
        creator = self.object.creator
        public = self.object.public
        profiles = self.object.participants
        requested_users = self.object.requested_users

        '''
        This checks for your own event, or if it's public, or if
        you're included in the event.
        '''
        if current_profile != creator \
            and not public \
                and not current_profile in profiles \
                and not current_profile in requested_users:
                    return redirect("/profile/")

        return super(EventView, self).render_to_response(context, **response_kwargs)


class UpdateEventView(LoginRequiredMixin, InlineFormSetView):
    model = Event
    inline_model = Score
    template_name = 'events/update_event.html'
    can_delete = False
    fields = ('score',)
    extra = 0

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super(UpdateEventView, self).get_queryset().filter(pk=pk)


class EventResponseView(LoginRequiredMixin, TemplateView):
    template_name = 'events/event_response.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        current_user = request.user.profile
        try:
            event_id = int(self.kwargs['pk'])
            event = Event.objects.get(pk=event_id)
        except:
            return redirect('/profile/')

        if event not in current_user.event_requests.all():
            return redirect('/profile/')

        if '_accept' in request.POST:
            Score.objects.create(event=event, participant=current_user)

            EventRequest.objects.get(
                event=event, participant=current_user).delete()

            return redirect('event', pk=event_id)
        elif '_reject' in request.POST:
            EventRequest.objects.get(
                event=event, participant=current_user).delete()
            return redirect('/profile/')

        else:
            return self.render_to_response(context)
