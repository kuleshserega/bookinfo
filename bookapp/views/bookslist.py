# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.http import HttpResponseRedirect

from bookapp.models.book import Book


class BooksListView(ListView):
    model = Book
    context_object_name = 'bookslist'
    template_name = 'bookslist.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        return super(BooksListView, self).get(*args, **kwargs)