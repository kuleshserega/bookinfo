# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

register = template.Library()


@register.filter
def glyphicon_tags(value):
    """
    Get icons by user fields name
    """
    tags = [
        ('first_name', 'user'),
        ('last_name', 'user'),
        ('email', 'envelope'),
        ('work_from_date', 'calendar'),
        ('avatar', 'picture'),
    ]

    if 'password' in value:
        return 'lock'

    for search, replace in tags:
        value = value.replace(search, replace)

    return value
