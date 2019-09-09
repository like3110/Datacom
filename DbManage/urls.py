# -*-coding:utf-8-*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_db_list, name="db_home"),
    path('list', views.get_db_list, name="get_db_cfg_list"),
    path('detail/type/<int:db_type>', views.get_db_list_with_type, name="get_db_cfg_with_type"),
    path('detail/<int:db_id>', views.get_db_cfg_detail, name="get_db_cfg_detail"),
]
