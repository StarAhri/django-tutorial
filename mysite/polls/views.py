from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Django 最简单的 view
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")