from django.db import models

# Create your models here.


class Museum(models.Model):
    gid = models.AutoField(primary_key=True)
    instname = models.CharField(max_length=254, db_comment='博物馆名')
    summary = models.TextField(blank=True, null=True, db_comment='简介')
    museumprop = models.CharField(max_length=254, blank=True, null=True)
    level = models.CharField(max_length=254, blank=True, null=True)
    exact = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=36, blank=True, null=True)
    province_name = models.CharField(max_length=32, blank=True, null=True, db_comment='省份名(冗余字段)')
    province_code = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=36, blank=True, null=True)
    county_name = models.CharField(max_length=36, blank=True, null=True)
    county_code = models.IntegerField(blank=True, null=True, db_comment='县级市编码')
    citycode = models.IntegerField(blank=True, null=True, db_comment='地级市编码')
    ordertel = models.CharField(max_length=254, blank=True, null=True)
    opentime = models.CharField(max_length=254, blank=True, null=True, db_comment='开放时间')
    quality_level = models.CharField(max_length=9, blank=True, null=True, db_comment='质量等级')
    isfreename = models.CharField(max_length=3, blank=True, null=True)
    traffic_info = models.CharField(max_length=254, blank=True, null=True, db_comment='交通信息')
    geo = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.TimeField(blank=True, null=True)
    del_flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'museum'
        db_table_comment = '博物馆表'


class Antique(models.Model):
    anqid = models.TextField(db_column='anqId', blank=True, null=True, db_comment='文物ID')  # Field name made lowercase.
    antiquename = models.TextField(db_column='antiqueName', blank=True, null=True, db_comment='文物名')  # Field name made lowercase.
    age = models.BigIntegerField(blank=True, null=True, db_comment='年代')
    culturalclass = models.BigIntegerField(db_column='culturalClass', blank=True, null=True, db_comment='文物类别')  # Field name made lowercase.
    museumname = models.CharField(db_column='museumName', max_length=100, blank=True, null=True, db_comment='博物馆名')  # Field name made lowercase.
    agename = models.TextField(db_column='ageName', blank=True, null=True, db_comment='年代名')  # Field name made lowercase.
    provincename = models.CharField(db_column='provinceName', max_length=100, blank=True, null=True, db_comment='省份名')  # Field name made lowercase.
    culturalclassname = models.CharField(db_column='culturalClassName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    museum_id = models.UUIDField(blank=True, null=True)
    cityname = models.CharField(db_column='cityName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    countyname = models.CharField(db_column='countyName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    citycode = models.BigIntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    provincecode = models.IntegerField(db_column='provinceCode', blank=True, null=True)  # Field name made lowercase.
    countycode = models.BigIntegerField(db_column='countyCode', blank=True, null=True)  # Field name made lowercase.
    update_time = models.TimeField()
    del_flag = models.BooleanField(db_comment='删除标识')

    class Meta:
        managed = False
        db_table = 'antique'
        db_table_comment = '文物表'
