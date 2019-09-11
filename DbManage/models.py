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
    name = models.CharField(max_length=50, verbose_name='数据库名')
    db_type = models.ForeignKey('DbCfgType', on_delete=models.DO_NOTHING, db_constraint=False, db_column='db_type',
                                verbose_name='数据库类型')
    ip_address = models.GenericIPAddressField(verbose_name='IP地址')
    port = models.IntegerField(verbose_name='端口号')
    user_name = models.CharField(max_length=50,verbose_name='用户名')
    pass_word = models.CharField(max_length=2000,verbose_name='密码')
    db_cfg = models.CharField(max_length=2000,verbose_name='附加信息')
    is_enable = models.BooleanField(default=True,verbose_name='是否生效')
    create_date = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modify_date = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    class Meta:
        db_table = "db_cfg_detail"
