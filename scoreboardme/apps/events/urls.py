from django.conf.urls import patterns, include, url

from class_based_auth_views.views import LoginView, LogoutView

from . import views
from . import forms

urlpatterns = patterns('',
    url(),
)
