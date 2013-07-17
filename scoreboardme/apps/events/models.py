from django.db import models


class Event(models.Model):
    creator = models.ForeignKey(
        'core.UserProfile', related_name='created_events')
    description = models.TextField()
    ended = models.BooleanField(default=False)
    title = models.CharField(max_length=70)
    public = models.BooleanField(default=True)
    bet_amount = models.IntegerField()

    def __unicode__(self):
        return u"%s %s" % (self.title, self.creator.user.username)


class EventRequest(models.Model):
    event_request = models.ForeignKey(Event)
    request_to = models.ForeignKey('core.UserProfile')
    optional_message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.event_request.title


class Score(models.Model):
    event = models.ForeignKey('Event')
    participant = models.ForeignKey('core.UserProfile')
    score = models.IntegerField()

    def __unicode__(self):
        return u"%s %s score: %d" % (self.event.title, self.participant.user.username, self.score)

    class Meta:
        unique_together = ('event', 'participant')
