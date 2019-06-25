# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^curd/$', 'curd'),
    (r'^api_test$', 'api_test'),
    (r'^cc/search_business$', 'search_business'),
)
