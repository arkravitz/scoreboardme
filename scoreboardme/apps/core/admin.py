from django.contrib import admin

from django_extensions.admin import ForeignKeyAutocompleteAdmin

from .models import UserProfile
from ..events.models import EventRequest, Score, Event

class EventRequestInline(admin.TabularInline):
    model = EventRequest

class ScoreInline(admin.StackedInline):
    model = Score

class EventsInline(admin.TabularInline):
    model = UserProfile.events.through

class UserProfileAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
        'user': ('username', 'email',),
    }
    inlines = [
        EventsInline,
        EventRequestInline,
        ScoreInline,
    ]

class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventsInline,
        EventRequestInline,
        ScoreInline,
    ]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Score)
