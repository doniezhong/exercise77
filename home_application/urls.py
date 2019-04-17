# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^api/test$', 'test'),
    (r'^cc/search_business$', 'search_business'),
    (r'^cc/search_host$', 'search_host'),
)
