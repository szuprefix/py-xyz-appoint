# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from xyz_restful.decorators import register
from xyz_restful.mixins import UserApiMixin

from . import models

@register()
class PolicyViewSet(UserApiMixin, viewsets.ModelViewSet):
    queryset = models.Policy.objects.all()
    # serializer_class = serializers.PolicySerializer


