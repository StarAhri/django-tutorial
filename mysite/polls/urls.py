
"""
mysite 项目的 polls 应用的 URLconf
"""
from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name='index'),


]