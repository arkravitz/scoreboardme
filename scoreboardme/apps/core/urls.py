from django.conf.urls import patterns, include, url

from class_based_auth_views.views import LoginView

from . import views
from . import forms

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(form_class=forms.LoginForm, success_url="/profile"), name='login'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),

)
