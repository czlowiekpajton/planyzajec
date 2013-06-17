# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Lectures(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    firstname = models.CharField(max_length=50L, db_column='FIRSTNAME') # Field name made lowercase.
    lastname = models.CharField(max_length=100L, db_column='LASTNAME') # Field name made lowercase.
    class Meta:
        db_table = 'LECTURES'

class Rooms(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    number = models.CharField(max_length=10L, db_column='NUMBER') # Field name made lowercase.
    class Meta:
        db_table = 'ROOMS'

class Semesters(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL') # Field name made lowercase.
    type = models.CharField(max_length=50L, db_column='TYPE') # Field name made lowercase.
    spec = models.CharField(max_length=100L, db_column='SPEC') # Field name made lowercase.
    class Meta:
        db_table = 'SEMESTERS'

class Subjects(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=500L, db_column='NAME') # Field name made lowercase.
    evenweek = models.IntegerField(null=True, db_column='EVENWEEK', blank=True) # Field name made lowercase.
    starttime = models.TextField(db_column='STARTTIME', blank=True) # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='ENDTIME', blank=True) # Field name made lowercase. This field type is a guess.
    group = models.IntegerField(db_column='GROUP') # Field name made lowercase.
    type = models.CharField(max_length=50L, db_column='TYPE') # Field name made lowercase.
    lecturesid = models.ForeignKey(Lectures, db_column='LECTURESID') # Field name made lowercase.
    roomsid = models.ForeignKey(Rooms, db_column='ROOMSID') # Field name made lowercase.
    semestersid = models.ForeignKey(Semesters, db_column='SEMESTERSID') # Field name made lowercase.
    weekdaysid = models.ForeignKey('Weekdays', db_column='WEEKDAYSID') # Field name made lowercase.
    class Meta:
        db_table = 'SUBJECTS'

class Users(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    login = models.CharField(max_length=50L, db_column='LOGIN') # Field name made lowercase.
    password = models.CharField(max_length=600L, db_column='PASSWORD') # Field name made lowercase.
    class Meta:
        db_table = 'USERS'

class Weekdays(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L, db_column='NAME') # Field name made lowercase.
    class Meta:
        db_table = 'WEEKDAYS'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'