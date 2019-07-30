"""
@file:url.py
@author:李霞丹
@date：2019/07/25
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    # url(regex:正则，view:视图, kwgs:传递给视图的参数， name:为url/视图命名
    # http://localhost:8000/route_base/index/
    # route_base/index/ => 跟regex匹配
    # 1. ^route_base/ => 剩下index/
    # 2. ^index/$ => 匹配上了

    # url(r'zoos1/(\d+)/', views.zoos, name='zoos1'),
    # url(r'/zoos2/(?P<id>\d+)/', views.zoos2)
]
"""
注意：
1. 除了include包含，建议都要加$
2. 注意URL尾部的/
3. 路由匹配顺序 => 执行第一条匹配上的规则
"""