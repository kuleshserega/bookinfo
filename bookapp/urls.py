# -*- coding: utf-8 -*-
from django.conf.urls import url
from bookapp import views


urlpatterns = [
    url(r'^list/$', views.BooksListView.as_view(), name='books_list'),
    url(r'^upload/$', views.BookUploadView.as_view(), name='book_upload'),
    url(r'^(?P<pk>\d+)/$', views.BookView.as_view(), name='bookinfo'),
]
