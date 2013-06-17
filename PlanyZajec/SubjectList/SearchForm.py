#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django import forms
from SubjectList import models
from SubjectList.models import *

class SearchingForm(forms.Form):
    semester = forms.ChoiceField([ (o.id, str(o.level) + ' ' + o.type + ' (' + o.spec + ')') for o in Semesters.objects.all()])
    