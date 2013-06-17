#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django.http import HttpResponse
from django.template import RequestContext, loader
from LogIn.models import Users
from LoginForm import LogForm
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore

def index(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        t = loader.get_template('LogIn/index.html')
        c = RequestContext(request, {'form' : form})
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            u = Users.objects.filter(login = login, password = password)

            if(len(u) != 0):
                request.session['login'] = login
                return HttpResponseRedirect("/SubjectList/")
            else:
                t = loader.get_template('LogIn/index.html')
                c = RequestContext(request, {'form' : LogForm(),'message' : 'Podałeś niepoprawne hasło'})
                return HttpResponse(t.render(c))                        
    else:
        form = LogForm()
        t = loader.get_template('LogIn/index.html')
        c = RequestContext(request, {'form' : form})
    return HttpResponse(t.render(c))

def logout(request):
    print 'siema'
    del request.session['login']
    print 'pooo'
    return HttpResponseRedirect("/SubjectList/")
