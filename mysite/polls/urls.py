
"""
mysite 项目的 polls 应用的 URLconf
这个文件不是 manage.py startapp polls 生成的
是需要自己写的
"""
from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name='index'),


]