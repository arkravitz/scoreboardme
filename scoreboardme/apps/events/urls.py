from django.conf.urls import patterns, include, url

from . import views
from . import forms

urlpatterns = patterns('',
    url(r'^create_event/$', views.CreateEventView.as_view(), name='create_event'),
    url(r'^(?P<pk>\d+)/$', views.EventView.as_view(), name='event'),
    url(r'^update_event/(?P<pk>\d+)/$', views.UpdateEventView.as_view(), name='update_event'),
    url(r'^event_response/(?P<pk>\d+)/$', views.EventResponseView.as_view(), name='event_response'),

)
