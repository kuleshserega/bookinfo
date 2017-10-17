# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    avatar = models.ImageField(
        upload_to='static/media/images/avatars/',
        null=True, blank=True, verbose_name=_('User profile image'))
    user = models.OneToOneField(
        User, verbose_name=_('User entity'), on_delete=models.CASCADE)
