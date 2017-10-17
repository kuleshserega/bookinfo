# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from bookapp.models.book import Book


class BookForm(forms.models.ModelForm):
    name = forms.CharField(label="Book title")
    author = forms.CharField(label="Author name")
    description = forms.CharField(label="Description", widget=forms.Textarea)
    date_added = forms.DateField(label="Date added")

    use_required_attribute = False

    class Meta:
        model = Book
        fields = ("name", "author", "description", "date_added")

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'autocomplete': 'off',
            })
