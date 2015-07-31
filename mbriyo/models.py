# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models


class Models(models.Model):
    id = models.AutoField(primary_key=True)
    station_name = models.TextField(db_column='station', blank=False, unique=True)  # Field name made lowercase.
    #station= models.ManyToManyField(Station, blank=True)

    class Meta:
        db_table = 'models'

class Station(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.TextField(db_column='station', blank=False,)  # Field name made lowercase
    time = models.TimeField(blank=False)
    class Meta:
        db_table = 'station'