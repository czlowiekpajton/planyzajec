#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, re
from django import forms
from AddSubject import models
from AddSubject.models import *


class AddSubjectForm(forms.Form):
    name = forms.CharField(max_length=200)
    freq = forms.ChoiceField([('1', 'Co tydzień'), 
                              ('2', 'Tydzień przestępny'), 
                              ('3', 'Tydzień nieprzestępny')], 
                             initial=[1])
    type = forms.ChoiceField([('W', 'Wykład'),
                              ('CW', 'Ćwiczenia'),
                              ('PS', 'Pracownia specjalistyczna'),
                              ('SEM', 'Seminarium')])
    group = forms.CharField(max_length=2)
    starttime = forms.CharField(max_length=5)
    endtime = forms.CharField(max_length=5)
    weekday = forms.ChoiceField([ (o.id, o.name) for o in Weekdays.objects.all()])
    semester = forms.ChoiceField([ (o.id, str(o.level) + ' ' + o.type + ' (' + o.spec + ')') for o in Semesters.objects.all()])
    room = forms.ChoiceField([ (o.id, o.number) for o in Rooms.objects.all()])
    lector = forms.ChoiceField([ (o.id, o.lastname + ' ' + o.firstname) for o in Lectures.objects.all().order_by('lastname')])
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match (u'[a-zA-Z0-9ĘęÓóĄąŚśŁłŻżŹźĆćŃń.-]+$', name):
            raise forms.ValidationError('Nieprawidłowa nazwa przedmiotu')
        return name
    def clean_group(self):
        group = self.cleaned_data['group']
        if not re.match (r'[0-9]+$', group):
            raise forms.ValidationError('Nieprawidłowy numer grupy')
        return group
    def clean_starttime(self):
        starttime = self.cleaned_data['starttime']
        if not re.match (r'^(([1-9]{1})|([0-1][0-9])|([1-2][0-3])):([0-5][0-9])$', starttime):
            raise forms.ValidationError('Nieprawidłowa godzina rozpoczęcia zajęć')
        return starttime
    def clean_endtime(self):
        endtime = self.cleaned_data['endtime']
        if not re.match (r'^(([1-9]{1})|([0-1][0-9])|([1-2][0-3])):([0-5][0-9])$', endtime):
            raise forms.ValidationError('Nieprawidłowa godzina zakończenia zajęć')
        return endtime    