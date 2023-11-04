# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TGame(models.Model):
    pk_id = models.AutoField(db_column='PK_ID', primary_key=True)  # Field name made lowercase.
    game_id = models.IntegerField(db_column='GAME_ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    name_zh = models.CharField(db_column='NAME_ZH', max_length=40)  # Field name made lowercase.
    name_en = models.CharField(db_column='NAME_EN', max_length=80)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=40)  # Field name made lowercase.
    developer = models.CharField(db_column='DEVELOPER', max_length=40)  # Field name made lowercase.
    platform = models.CharField(db_column='PLATFORM', max_length=40)  # Field name made lowercase.
    rate = models.FloatField(db_column='RATE')  # Field name made lowercase.
    catrgories = models.CharField(db_column='CATRGORIES', max_length=50)  # Field name made lowercase.
    url = models.CharField(db_column='URL', unique=True, max_length=80)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(db_column='INTRODUCTION', max_length=450)  # Field name made lowercase.
    publish = models.DateTimeField(db_column='PUBLISH', blank=True, null=True)  # Field name made lowercase.
    datasource = models.CharField(db_column='DATASOURCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=200)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='UPDATED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_GAME'


class TReview(models.Model):
    pk_id = models.AutoField(db_column='PK_ID', primary_key=True)  # Field name made lowercase.
    fk_uid = models.IntegerField(db_column='FK_UID', blank=True, null=True)  # Field name made lowercase.
    fk_gid = models.IntegerField(db_column='FK_GID', blank=True, null=True)  # Field name made lowercase.
    rate = models.IntegerField(db_column='RATE')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=600, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_REVIEW'


class TUser(models.Model):
    pk_id = models.AutoField(db_column='PK_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40)  # Field name made lowercase.
    group = models.CharField(db_column='GROUP', max_length=40)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=20)  # Field name made lowercase.
    sign = models.CharField(db_column='SIGN', max_length=20)  # Field name made lowercase.
    impact = models.IntegerField(db_column='IMPACT')  # Field name made lowercase.
    register_time = models.DateTimeField(db_column='REGISTER_TIME')  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.
    updated = models.DateTimeField(db_column='UPDATED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_USER'
