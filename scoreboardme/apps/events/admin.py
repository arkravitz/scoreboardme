from django.contrib import admin

from django_extensions.admin import ForeignKeyAutocompleteAdmin

from .models import EventRequest


admin.site.register(EventRequest)
