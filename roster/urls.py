#app urls roster/urls.py
from django.conf.urls import patterns, url
from roster import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='roster_home'),
	url(r'^course/$', views.course, name='roster_course'),
	url(r'^student/$', views.student, name='roster_student'),
)