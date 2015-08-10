from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^book/(?P<pk>[0-9]+)/$', views.book_detail),
    url(r'^authors/$', views.author_list),
    url(r'^author/(?P<pk>[0-9]+)/$', views.author_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
