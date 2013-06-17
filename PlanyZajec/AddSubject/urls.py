from django.conf.urls import patterns, url

from AddSubject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)