from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    creator = models.ForeignKey('UserProfile', related_name='created_events')
    description = models.TextField()
    ended = models.BooleanField(default=False)
    title = models.CharField(max_length=70)
    public = models.BooleanField(default=True)
    bet_amount = models.IntegerField()

    def __unicode__(self):
        return u"%s %s" % (self.title, self.creator.user.username)


class Score(models.Model):
    event = models.ForeignKey(Event)
    participant = models.ForeignKey('UserProfile')
    score = models.IntegerField()

    def __unicode__(self):
        return u"%s %s score: %d" % (self.event.title, self.participant.user.username, self.score)

    class Meta:
        unique_together = ('event', 'participant')

default_currency = 1000


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    events = models.ManyToManyField(Event, related_name='profiles', blank=True)
    currency = models.IntegerField(default=default_currency)
    event_requests = models.ManyToManyField(
        Event, through='events.EventRequest', related_name='requested_users')
    scores = models.ManyToManyField(
        Event, through='Score', related_name='scores')

    def get_active_events(self):
        return self.events.filter(ended=False)

    def get_completed_events(self):
        return self.events.filter(ended=True)

    def __unicode__(self):
        return self.user.username
