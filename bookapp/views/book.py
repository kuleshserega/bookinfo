# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from django.http import HttpResponseRedirect

from bookapp.models import Book


class BookView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'bookupload.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        return super(BookView, self).get(*args, **kwargs)
