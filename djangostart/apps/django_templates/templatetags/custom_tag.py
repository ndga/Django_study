"""
@file:custom_tag.py
@author:李霞丹
@date：2019/07/26
"""

from django import template
from django.conf import settings

# 注册到template库里面
register = template.Library()

@register.simple_tag
def mystatic(value):
    # STATIC_URL + value
    return settings.STATIC_URL+value