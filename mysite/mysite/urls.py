"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("polls/",include('polls.urls')),
    # 函数 include() 允许引用其它 URLconfs。
    # 每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。

    path('admin/', admin.site.urls),
    # 当 Django 匹配上了一个 route 以后，会带个一个  HttpRequest 对象的参数来访问这个 view func
    # 如果 route 里面有参数，那么参数会作为 kwargs 传入
]
