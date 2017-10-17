# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/profile')
        else:
            return HttpResponseRedirect('/login')
