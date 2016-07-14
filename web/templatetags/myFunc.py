# -*- coding=utf-8 -*-
# filepath: E:/share/project/myDjango/web/templatetags/myFunc.py
# user: Administrator
# date: Jul 14, 2016

from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError
 
register = template.Library()
 
@register.simple_tag
def mytagfunc(v1):
    return  v1*1000
 





