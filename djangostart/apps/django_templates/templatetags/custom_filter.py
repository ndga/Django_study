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
    # 把arg替换成空
    return value.replace(arg, '')

# # 注册的第二种方式
def lower0(value, ):
    return value.lower()
register.filter("lower0", lower0)

"""
{{ project_name | lower0 }}
{{ project_name | cut0:"A" }}
"""