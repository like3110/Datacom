# -*-coding:utf-8-*-
from django.shortcuts import render, get_object_or_404


def get_home_page(request):
    context = {'msg': '数据接入平台'}
    return render(request, "home.html", context)
