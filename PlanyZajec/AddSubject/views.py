#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from AddForm import AddSubjectForm
from AddSubject.models import Subjects, Lectures, Rooms, Semesters, Weekdays

@csrf_protect
def index(request):
    if('login' not in request.session):
        template = 'AddSubject/failure.html'
        context = {'message' : 'Nie masz uprawnień do przeglądania tej strony.'}
        return render(request, template, context)
    
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        
        if form.is_valid():                      
            subject = Subjects()
            subject.name = form.cleaned_data['name']
            subject.evenweek = form.cleaned_data['freq']
            subject.starttime = form.cleaned_data['starttime']
            subject.endtime = form.cleaned_data['endtime']
            subject.group = form.cleaned_data['group']
            subject.type = form.cleaned_data['type']
            subject.lecturesid = Lectures.objects.filter(id=form.cleaned_data['lector'])[0]
            subject.roomsid = Rooms.objects.filter(id=form.cleaned_data['room'])[0]
            subject.semestersid = Semesters.objects.filter(id=form.cleaned_data['semester'])[0]
            subject.weekdaysid = Weekdays.objects.filter(id=form.cleaned_data['weekday'])[0]
            
            doesExist = Subjects.objects.filter(starttime=subject.starttime, roomsid=subject.roomsid.id)
            
            if not doesExist:
                subject.save() 
                template = 'AddSubject/success.html'
                context = {}  
            else:
                template = 'AddSubject/failure.html'
                context = {'message' : 'Inne zajęcia są już zarejestrowane w tej sali o tej godzinie'}
    else:
        form = AddSubjectForm()
        template = 'AddSubject/index.html'
        context = {'form': form}   
        
    return render(request, template, context)