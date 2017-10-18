# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from bookapp.models.comment import Comment


class CommentForm(forms.models.ModelForm):
    text = forms.CharField(
        label=_('Add comment'), widget=forms.Textarea(attrs={'rows': 3}))

    use_required_attribute = False

    class Meta:
        model = Comment
        fields = ("text",)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
                'autocomplete': 'off',
            })
