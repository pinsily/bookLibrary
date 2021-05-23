from django.conf.urls import url
from django.urls import re_path

from library import views

app_name = "library"

urlpatterns = [
    url("index/", views.index, name="index"),
    url(r'^book/(?P<book_id>\d+)$', views.detail, name='detail'),
    url(r'^borrow_book/(?P<book_id>\d+)$', views.borrow_book, name='borrow_book'),
    url(r'^return_book/(?P<book_id>\d+)$', views.return_book, name='return_book'),
    url('my_books/', views.my_book, name='my_book'),

]
