from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = "email")
    first_name = forms.CharField(label="first name")
    last_name = forms.CharField(label="last name")
  
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
