# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth import login

from userapp.forms import EmailAuthenticationForm


class LoginView(FormView):
    form_class = EmailAuthenticationForm
    template_name = "login.html"
    success_url = "/profile"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/profile')
        else:
            return super(LoginView, self).dispatch(
                request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)
