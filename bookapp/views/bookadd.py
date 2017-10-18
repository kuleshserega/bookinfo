# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.views.generic.edit import FormView

from bookapp.forms.book import BookForm


class BookUploadView(FormView):
    form_class = BookForm
    success_url = "/profile"
    template_name = "bookupload.html"

    def form_valid(self, form):
        form_add_book = form.save(commit=False)
        form_add_book.owner_id = self.request.user.id
        form_add_book.date_added = datetime.now().date()
        form_add_book.save()
        return super(BookUploadView, self).form_valid(form)
