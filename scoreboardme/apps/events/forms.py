from django import forms

from .models import Event, Score


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("title", "description", "public", "bet_amount")
