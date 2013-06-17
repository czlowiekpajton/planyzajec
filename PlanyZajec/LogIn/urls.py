'''
Created on 17 Jun 2013

@author: Magdalena
'''
from django.conf.urls import patterns, url

from LogIn import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index')
)