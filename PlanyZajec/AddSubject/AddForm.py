#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
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