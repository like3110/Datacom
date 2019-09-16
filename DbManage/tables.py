# -*-coding:utf-8-*-
import django_tables2 as tables
from .models import DbCfgDetail


class DbCfgDetailTable(tables.Table):
    # link = tables.LinkColumn(viewname="get_db_cfg_detail", text="修改", verbose_name='操作', args=[A("pk")])
    action = tables.TemplateColumn(
        "<div class=\"butt-group\"><a href=\"{% url 'modify_db' record.pk %}\">"
        "<button class=\"btn btn-primary\" type=\"button\">修改</button></a>"
        "<a href=\"{% url 'delete_db' record.pk%}\">"
        "<button class=\"btn btn-primary\" type=\"button\">删除</button></a></div>",
        verbose_name="操作", orderable=False)

    class Meta:
        model = DbCfgDetail
        exclude = ("id", "pass_word",
                   "create_date", "modify_date")
        attrs = {"class": "table table-bordered"}
        # template_name = 'django_tables2/bootstrap.html'
