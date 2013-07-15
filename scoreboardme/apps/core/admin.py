from django.contrib import admin

from django_extensions.admin import ForeignKeyAutocompleteAdmin

from .models import UserProfile, Score
from ..events.models import Event

class UserProfileAdmin(ForeignKeyAutocompleteAdmin):
    related_search_fields = {
        'user': ('username', 'email',),
    }


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event)
admin.site.register(Score)
