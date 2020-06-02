"""django_stu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path
import stu.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',stu.views.index),
    path('class/',stu.views.classall),
    path('addinfo/',stu.views.addInfo),
    path('del_class/',stu.views.del_class),
    path('addinfo_window/',stu.views.addInfo_window),
    path('edit_class/',stu.views.edit_class),
    path('student/',stu.views.student),
    path('teacher/',stu.views.teacher),
    path('login/',stu.views.login),
    path('signin/',stu.views.signin),
    path('tea_cla/',stu.views.tea_cla),
]


# handler404 = 'stu.views.page404'
