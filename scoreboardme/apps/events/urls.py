from django.conf.urls import patterns, include, url

from . import views
from . import forms

urlpatterns = patterns('',
    url(r'^create_event/$', views.CreateEventView.as_view(), name='create_event'),
    url(r'^(?P<pk>\d+)/$', views.EventView.as_view(), name='event'),

)
