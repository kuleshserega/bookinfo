# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    name = models.CharField(max_length=240, verbose_name=_('Book name'))
    author = models.CharField(max_length=120, verbose_name=_('Author name'))
    description = models.TextField(verbose_name=_('Book description'))
    date_added = models.DateField(verbose_name=_('Date added'))
    owner = models.ForeignKey(User, verbose_name=_('Who added book'))

    def __str__(self):
        return '%s' % self.name
