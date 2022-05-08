# -*- coding:utf-8 -*-
from rest_framework.authentication import   TokenAuthentication
__author__ = 'denishuang'

from .models import Policy

class AppointAuthentication(TokenAuthentication):
    model = Appointment

    def authenticate_credentials(self, key):
        from .helper import check_appoint_token
        user, appointment = super(AppointAuthentication, self).authenticate_credentials(key)

