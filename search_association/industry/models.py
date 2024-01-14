
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GbIndustry(models.Model):
    updated_at = models.TimeField(db_comment='数据更新时间')
    name = models.CharField(max_length=50)
    code = models.CharField(unique=True, max_length=10, db_comment='国标行业编码（2017）')
    father_code = models.CharField(blank=True, null=True, max_length=10, db_comment='上级行业编码')
    root_code = models.CharField(blank=True, null=True, max_length=10, db_comment='一级行业编码')
    desc = models.TextField(blank=True, null=True, db_comment='描述')
    level = models.IntegerField(blank=True, null=True, db_comment='行业级别：门类0，大类1，中类2，小类3')

    class Meta:
        managed = False
        db_table = 'gb_industry'
        db_table_comment = '国标行业分类表'
