from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ..core.models import UserProfile, Event


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("title", "description", "public", "bet_amount")
