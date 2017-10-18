# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from bookapp.models.book import Book


class BookForm(forms.models.ModelForm):
    name = forms.CharField(label=_("Book title"))
    author = forms.CharField(label=_("Author name"))
    description = forms.CharField(label=_("Description"), widget=forms.Textarea)
    cover = forms.ImageField(label=_("Book cover"))
    owner_id = forms.CharField(widget=forms.HiddenInput)

    use_required_attribute = False

    class Meta:
        model = Book
        fields = (
            "name", "author", "description", "cover", "owner_id")

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'autocomplete': 'off',
            })

        self.fields['cover'].widget.attrs.update({
            'class': 'form-control form-file-input',
            'title': 'Add book cover'
        })
