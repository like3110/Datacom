# -*-coding:utf-8-*-

from django.shortcuts import render, get_object_or_404, redirect
from DbManage.models import DbCfgDetail, DbCfgType
from django.contrib.auth.decorators import login_required
from .forms import CreateDbForm
from django.urls import reverse
from utils import PasswdUtil
from django_tables2 import RequestConfig
from .tables import DbCfgDetailTable


# Create your views here.
@login_required()
def get_db_list(request):
    table = DbCfgDetailTable(DbCfgDetail.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    context = {'db_types': DbCfgType.objects.all(), 'table': table, }
    return render(request, 'db_cfg_list.html', context)


@login_required()
def get_db_cfg_detail(request, db_id):
    context = {'db_cfg': get_object_or_404(DbCfgDetail, pk=db_id)}
    return render(request, "db_cfg_detail.html", context)


@login_required()
def get_db_list_with_type(request, db_type):
    table = DbCfgDetailTable(DbCfgDetail.objects.filter(db_type=db_type))
    context = {'db_type': get_object_or_404(DbCfgType, pk=db_type), 'db_types': DbCfgType.objects.all(),
               'table': table, }
    return render(request, "db_cfg_list_type.html", context)

@login_required()
def delete_db(request, db_id):
    DbCfgDetail.objects.filter(pk=db_id).delete()
    return redirect(reverse('get_db_cfg_list'))


@login_required()
def create_db(request):
    if request.method == 'POST':
        create_db_form = CreateDbForm(request.POST)
        db_cfg_detail = DbCfgDetail()
        if create_db_form.is_valid():
            db_cfg_detail.name = create_db_form.cleaned_data['name']
            db_cfg_detail.ip_address = create_db_form.cleaned_data['ip']
            db_cfg_detail.port = create_db_form.cleaned_data['port']
            db_cfg_detail.db_type = create_db_form.cleaned_data['db_type']
            db_cfg_detail.db_cfg = create_db_form.cleaned_data['db_cfg']
            db_cfg_detail.user_name = create_db_form.cleaned_data['username']
            pass_word = create_db_form.cleaned_data['pass_wd']
            pass_word = PasswdUtil.encrypt(pass_word)
            db_cfg_detail.pass_word = pass_word
            # 创建数据库配置
            db_cfg_detail.save()
            return redirect(reverse('get_db_cfg_list'))
    else:
        create_db_form = CreateDbForm()
    context = {'create_db_form': create_db_form}
    return render(request, 'db_create.html', context)


@login_required()
def modify_db(request, db_id):
    if request.method == 'POST':
        create_db_form = CreateDbForm(request.POST)
        db_cfg_detail = get_object_or_404(DbCfgDetail, pk=db_id)
        #print(create_db_form.data['name'])
        #print(get_object_or_404(DbCfgDetail, pk=db_id).name)
        if create_db_form.data['name'] == get_object_or_404(DbCfgDetail, pk=db_id).name:
            db_cfg_detail.name = create_db_form.data['name']
            db_cfg_detail.ip_address = create_db_form.data['ip']
            db_cfg_detail.port = create_db_form.data['port']
            db_cfg_detail.db_type = get_object_or_404(DbCfgType, pk=create_db_form.data['db_type'])
            db_cfg_detail.db_cfg = create_db_form.data['db_cfg']
            db_cfg_detail.user_name = create_db_form.data['username']
            pass_word = create_db_form.data['pass_wd']
            pass_word = PasswdUtil.encrypt(pass_word)
            db_cfg_detail.pass_word = pass_word
            # 创建数据库配置
            db_cfg_detail.save()
            return redirect(reverse('get_db_cfg_list'))
        if create_db_form.is_valid():
            db_cfg_detail.name = create_db_form.cleaned_data['name']
            db_cfg_detail.ip_address = create_db_form.cleaned_data['ip']
            db_cfg_detail.port = create_db_form.cleaned_data['port']
            db_cfg_detail.db_type = get_object_or_404(DbCfgType, pk=create_db_form.cleaned_data['db_type'])
            print(create_db_form.cleaned_data['db_type'])
            db_cfg_detail.db_cfg = create_db_form.cleaned_data['db_cfg']
            db_cfg_detail.user_name = create_db_form.cleaned_data['username']
            pass_word = create_db_form.cleaned_data['pass_wd']
            pass_word = PasswdUtil.encrypt(pass_word)
            db_cfg_detail.pass_word = pass_word
            # 创建数据库配置
            db_cfg_detail.save()
            return redirect(reverse('get_db_cfg_list'))
    else:
        datas = get_object_or_404(DbCfgDetail, pk=db_id)
        data_set = {}
        data_set['name'] = datas.name
        data_set['ip'] = datas.ip_address
        data_set['port'] = datas.port
        data_set['username'] = datas.user_name
        data_set['pass_wd'] = datas.pass_word
        data_set['db_cfg'] = datas.db_cfg
        data_set['db_type'] = datas.db_type
        create_db_form = CreateDbForm(initial=data_set)
    context = {'create_db_form': create_db_form}
    return render(request, 'db_modify.html', context)


@login_required()
def delete_db(request, db_id):
    DbCfgDetail.objects.filter(pk=db_id).delete()
    return redirect(reverse('get_db_cfg_list'))


