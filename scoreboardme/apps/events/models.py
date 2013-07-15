from django.db import models
from django.contrib.auth.models import User

from scoreboardme.apps.core.models import UserProfile, Event

class EventRequest(models.Model):
    event_request = models.ForeignKey(Event)
    request_to = models.ForeignKey(UserProfile)
    optional_message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.event_request.title
