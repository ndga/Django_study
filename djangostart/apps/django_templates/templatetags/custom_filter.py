"""
@file:custom_filter.py
@author:李霞丹
@date：2019/07/26
"""
from django import template

# 注册到template库里面
register = template.Library()

# 注册的第一种方式
@register.filter
def cut0(value, arg):
    return value.replace(arg, '')

# # 注册的第二种方式
# @register.f1ilter
# def cut0(value, arg):
#     return value.replace(arg, '')