# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from xyz_util import modelutils

class Policy(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "约定"

    key = models.CharField("标识", max_length=16, blank=True, unique=True)
    name = models.CharField("名称", max_length=64, blank=True, default='')
    user = models.ForeignKey('auth.user', related_name='xauth_appointments', on_delete=models.PROTECT)
    app_model = models.CharField("应用模块", max_length=64)
    action = models.CharField("应用模块", max_length=64)
    context = modelutils.JSONField("上下文", blank=True, default={})
    is_active = models.BooleanField('有效', blank=True, default=True)
    session_max_age = models.CharField("单次过期时间", blank=True, default='7d')
    expire_time = models.DateTimeField("过期时间", blank=True, null=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    modify_time = models.DateTimeField("修改时间", auto_now=True)

    def __str__(self):
        return '%s:%s' % (self.user, self.name)

    def save(self, **kwargs):
        if not self.key:
            from django.utils.crypto import get_random_string
            self.key = get_random_string(16)
        super(Policy, self).save(**kwargs)
