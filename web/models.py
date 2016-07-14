# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import CharField, AutoField, DateTimeField,\
    IntegerField, BooleanField, NullBooleanField
from django.db.models.fields.related import ForeignKey
from Crypto.Random.random import choice

import django.utils.timezone
# Create your models here.
class users(models.Model):
    Level_Choice = (
                    (u'1',u'普通用户'),
                    (u'2',u'管理员'),
                    (u'3',u'超级管理员')
                    )
    
    id = AutoField(primary_key=True)
    name = CharField(max_length=50,null=True)
    password = CharField(max_length=50,null=True)
    c_time = DateTimeField(auto_now_add=True)
    u_time = DateTimeField(auto_now=True)
    age = IntegerField(default=0,null=True)
    gender = NullBooleanField()
    type = CharField(max_length=1,choices = Level_Choice,null = True)
    


    

    

















