# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from bookapp.models import Book
from userapp.models import UserProfile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        try:
            profile = UserProfile.objects.get(user_id=self.request.user.id)
            context['profile_picture'] = profile.avatar
        except UserProfile.DoesNotExist:
            context['profile_picture'] = None

        context['user_books'] = Book.objects.filter(owner=self.request.user)

        return context
