# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from userapp.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = "/login"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/bookslist')
        else:
            return super(RegisterView, self).dispatch(
                request, *args, **kwargs)
