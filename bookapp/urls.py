# -*- coding: utf-8 -*-
from django.conf.urls import url
from bookapp import views


urlpatterns = [
    url(r'^$', views.BookView.as_view(), name='index'),
    url(r'^list/$', views.BooksListView.as_view(), name='book_list'),
    # url(r'^file/(?P<pk>\d+)/$', views.get_file, name='download_book'),
]
