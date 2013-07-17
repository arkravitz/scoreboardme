from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.RedirectLoginView.as_view(success_url="/profile/"), name='login'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
)
