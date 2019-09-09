# -*-coding:utf-8-*-

from django.db import models


# Create your models here.
class DbCfgType(models.Model):
    id = models.AutoField(primary_key=True)
    db_type_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.db_type_name

    class Meta:
        db_table = "db_cfg_types"


class DbCfgDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    db_type = models.ForeignKey('DbCfgType', on_delete=models.DO_NOTHING, db_constraint=False,db_column='db_type')
    ip_address = models.GenericIPAddressField()
    port = models.IntegerField()
    user_name = models.CharField(max_length=50)
    pass_word = models.CharField(max_length=2000)
    db_cfg = models.CharField(max_length=2000)
    is_enable = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "db_cfg_detail"
