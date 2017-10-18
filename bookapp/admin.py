# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from bookapp.models import Book, Comment
from userapp.forms import EmailAuthenticationForm


admin.site.register(Book)
admin.site.register(Comment)
admin.site.login_form = EmailAuthenticationForm
admin.site.login_template = 'admin_login.html'
