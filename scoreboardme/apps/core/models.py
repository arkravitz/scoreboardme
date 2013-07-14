from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    creator = models.ForeignKey('UserProfile')
    description = models.TextField()
    ended = models.BooleanField(default=False)
    title = models.CharField(max_length=70)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s %s" % (self.title, self.creator.user.username)


class Score(models.Model):
    event = models.ForeignKey(Event)
    participant = models.ForeignKey('UserProfile')
    score = models.IntegerField()

    def __unicode__(self):
        return u"%s %s score: %d" % (self.event.title, self.participant.user.username, self.score)


default_currency = 1000


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    events = models.ManyToManyField(Event, related_name='events', blank=True)
    currency = models.IntegerField(default=default_currency)

    def __unicode__(self):
        self.user.username
