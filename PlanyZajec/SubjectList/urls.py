from django.conf.urls import patterns, url

from SubjectList import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
