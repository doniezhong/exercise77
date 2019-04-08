# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^search_business/$', 'search_business'),
)
