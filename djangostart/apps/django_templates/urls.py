"""
@file:url.py
@author:李霞丹
@date：2019/07/25
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
]