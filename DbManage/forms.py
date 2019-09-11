# -*-coding:utf-8-*-
from django import forms
from .models import DbCfgType, DbCfgDetail


class CreateDbForm(forms.Form):
    name = forms.CharField(label='数据库名', max_length=30, min_length=5,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入5-30位数据库名'}))
    ip = forms.GenericIPAddressField(label='数据库IP',
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入数据库ip'}))
    port = forms.IntegerField(label='数据库端口',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入数据库端口'}))
    username = forms.CharField(label='数据库用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入数据库用户名'}))
    pass_wd = forms.CharField(label='数据库密码',
                                          widget=forms.PasswordInput(
                                              attrs={'class': 'form-control', 'placeholder': '请输入数据库密码'}))
    db_type = forms.ModelChoiceField(label='数据库类型',queryset=DbCfgType.objects.all(), widget=forms.Select(attrs={'class':"form-control"}))
    db_cfg = forms.CharField(label='数据库配置',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入数据库配置信息'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if DbCfgDetail.objects.filter(name=name).exists():
            raise forms.ValidationError('用户名已存在')
        return name
