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
    starttime = models.TextField(db_column='STARTTIME') # Field name made lowercase. This field type is a guess.
    endtime = models.TextField(db_column='ENDTIME') # Field name made lowercase. This field type is a guess.
    group = models.IntegerField(db_column='GROUP') # Field name made lowercase.
    type = models.CharField(max_length=50L, db_column='TYPE') # Field name made lowercase.
    lecturesid = models.ForeignKey(Lectures, db_column='LECTURESID') # Field name made lowercase.
    roomsid = models.ForeignKey(Rooms, db_column='ROOMSID') # Field name made lowercase.
    semestersid = models.ForeignKey(Semesters, db_column='SEMESTERSID') # Field name made lowercase.
    weekdaysid = models.ForeignKey('Weekdays', db_column='WEEKDAYSID') # Field name made lowercase.
    class Meta:
        db_table = 'SUBJECTS'
        
class Weekdays(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50L, db_column='NAME') # Field name made lowercase.
    class Meta:
        db_table = 'WEEKDAYS'
