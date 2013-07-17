from django.db import models
from django.contrib.auth.models import User


default_currency = 1000


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    events = models.ManyToManyField('events.Event', through='events.Score', related_name='profiles', blank=True)
    currency = models.IntegerField(default=default_currency)
    event_requests = models.ManyToManyField(
        'events.Event', through='events.EventRequest', related_name='requested_users')

    def get_active_events(self):
        return self.events.filter(ended=False)

    def get_completed_events(self):
        return self.events.filter(ended=True)

    def __unicode__(self):
        return self.user.username
