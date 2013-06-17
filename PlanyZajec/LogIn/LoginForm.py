#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django import forms

class LogForm(forms.Form):
    login = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

