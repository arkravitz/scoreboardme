from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ..core.models import UserProfile, Event


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("title", "public", "description")

    def save(self, commit=True):
        event = super(CreateEventForm, self).save(commit=False)
        """
        event.title = self.cleaned_data['title']
        event.public = self.cleaned_data['public']
        event.description = self.cleaned_data['description']
        """
        if commit:
            .save()
            user_profile = UserProfile(user=user)
            user_profile.save()
        return event