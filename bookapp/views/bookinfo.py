# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from bookapp.models import Book, Comment
from bookapp.forms import CommentForm


class BookView(FormMixin, DetailView):
    model = Book
    form_class = CommentForm
    context_object_name = 'book'
    template_name = 'bookinfo.html'

    def get_success_url(self):
        return reverse('bookapp:bookinfo', args=(self.kwargs['pk'],))

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        return super(BookView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BookView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            for_book_id=self.kwargs.get('pk')).order_by('-id')
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form_add_comment = form.save(commit=False)
        form_add_comment.who_added_id = self.request.user.id
        form_add_comment.for_book_id = self.kwargs.get('pk')
        form_add_comment.date_added = datetime.now()
        form_add_comment.save()
        return super(BookView, self).form_valid(form)
