# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Comment(models.Model):
    text = models.TextField(verbose_name=_('Text of comment'))
    date_added = models.DateTimeField(verbose_name=_('Date of comment added'))
    who_added = models.ForeignKey(User, verbose_name=_('Who added comment'))
    for_book = models.ForeignKey('Book', verbose_name=_('Commented book'))

    def __str__(self):
        return '%s' % self.text
