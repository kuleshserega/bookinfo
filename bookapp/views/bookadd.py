# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.edit import FormView

from bookapp.forms.book import BookForm


class BookUploadView(FormView):
    form_class = BookForm
    success_url = "/profile"
    template_name = "bookupload.html"

    def form_valid(self, form):
        form.save()
        return super(BookUploadView, self).form_valid(form)
