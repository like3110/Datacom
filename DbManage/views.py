# -*-coding:utf-8-*-

from django.shortcuts import render, get_object_or_404
from DbManage.models import DbCfgDetail, DbCfgType


# Create your views here.
def get_db_list(request):
    context = {'db_list': DbCfgDetail.objects.all(), 'db_types': DbCfgType.objects.all()}
    return render(request, "db_cfg_list.html", context)


def get_db_cfg_detail(request, db_id):
    context = {'db_cfg': get_object_or_404(DbCfgDetail, pk=db_id)}
    return render(request, "db_cfg_detail.html", context)


def get_db_list_with_type(request, db_type):
    context = {'db_type': get_object_or_404(DbCfgType, pk=db_type),'db_types': DbCfgType.objects.all()}
    context['db_list']=DbCfgDetail.objects.filter(db_type=db_type)
    return render(request, "db_cfg_list_type.html", context)
