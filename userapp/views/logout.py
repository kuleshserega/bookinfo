# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login")
