# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from django.contrib import admin
from . import models


@admin.register(models.Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'app_model', 'expire_time', 'create_time', 'modify_time')
    raw_id_fields = ('user',)
