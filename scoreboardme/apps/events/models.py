from django.db import models
from django.contrib.auth.models import User

from ..core.models import UserProfile, Event

class EventRequest(models.Model):
    event = models.ForeignKey(Event, related_name='eventrequests')
    request_to = models.ForeignKey(UserProfile, related_name='eventrequests_to')
    optional_message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.event.title
