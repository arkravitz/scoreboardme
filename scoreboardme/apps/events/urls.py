from django.conf.urls import patterns, include, url

from . import views
from . import forms

urlpatterns = patterns('',
    url(r'^create_event/$', views.CreateEventView.as_view(), name='create_event'),
)