# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TLog(models.Model):
    pk_id = models.AutoField(db_column='PK_ID', primary_key=True)  # Field name made lowercase.
    level_name = models.CharField(db_column='LEVEL_NAME', max_length=30, db_comment='日志等级')  # Field name made lowercase.
    module = models.CharField(db_column='MODULE', max_length=100, blank=True, null=True, db_comment='模块')  # Field name made lowercase.
    thread_name = models.CharField(db_column='THREAD_NAME', max_length=100, blank=True, null=True, db_comment='线程名')  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=100, blank=True, null=True, db_comment='文件名')  # Field name made lowercase.
    func_name = models.CharField(db_column='FUNC_NAME', max_length=100, blank=True, null=True, db_comment='函数名')  # Field name made lowercase.
    line_no = models.IntegerField(db_column='LINE_NO', blank=True, null=True, db_comment='行数')  # Field name made lowercase.
    process = models.IntegerField(db_column='PROCESS', blank=True, null=True, db_comment='进程号')  # Field name made lowercase.
    process_name = models.CharField(db_column='PROCESS_NAME', max_length=100, blank=True, null=True, db_comment='进程名')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=1000, blank=True, null=True, db_comment='内容')  # Field name made lowercase.
    extra = models.JSONField(db_column='EXTRA', blank=True, null=True, db_comment='额外信息')  # Field name made lowercase.
    fk_task_id = models.CharField(db_column='FK_TASK_ID', max_length=50, blank=True, null=True, db_comment='英雄ID')  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', db_comment='创建时间')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T_LOG'


class Heros(models.Model):
    name = models.CharField(max_length=255)
    hp_max = models.FloatField(blank=True, null=True)
    hp_growth = models.FloatField(blank=True, null=True)
    hp_start = models.FloatField(blank=True, null=True)
    mp_max = models.FloatField(blank=True, null=True)
    mp_growth = models.FloatField(blank=True, null=True)
    mp_start = models.FloatField(blank=True, null=True)
    attack_max = models.FloatField(blank=True, null=True)
    attack_growth = models.FloatField(blank=True, null=True)
    attack_start = models.FloatField(blank=True, null=True)
    defense_max = models.FloatField(blank=True, null=True)
    defense_growth = models.FloatField(blank=True, null=True)
    defense_start = models.FloatField(blank=True, null=True)
    hp_5s_max = models.FloatField(blank=True, null=True)
    hp_5s_growth = models.FloatField(blank=True, null=True)
    hp_5s_start = models.FloatField(blank=True, null=True)
    mp_5s_max = models.FloatField(blank=True, null=True)
    mp_5s_growth = models.FloatField(blank=True, null=True)
    mp_5s_start = models.FloatField(blank=True, null=True)
    attack_speed_max = models.FloatField(blank=True, null=True)
    attack_range = models.CharField(max_length=255, blank=True, null=True)
    role_main = models.CharField(max_length=255, blank=True, null=True)
    role_assist = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heros'
