# -*-coding:utf-8-*-

from django.contrib import admin
from DbManage import models


# Register your models here.
@admin.register(models.DbCfgType)
class db_cfg_typesAdmin(admin.ModelAdmin):
    list_display = ("id", "db_type_name")
    ordering = ("id",)


@admin.register(models.DbCfgDetail)
class db_cfg_detailAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "db_type", "ip_address", "port", "user_name", "pass_word", "db_cfg", "is_enable", "create_date",
        "modify_date")
    ordering = ("id",)
