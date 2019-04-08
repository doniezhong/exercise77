# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from home_application.ph import execute_job

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^api/test$', 'test'),
    (r'^test$', execute_job),
    (r'^cc/search_business$', 'search_business'),
    (r'^cc/search_set$', 'search_set'),
    (r'^cc/search_host$', 'search_cc_host'),
    (r'^search_host$', 'search_host'),
    (r'^add_host$', 'add_host'),
    (r'^update_host$', 'update_host'),
    (r'^del_host$', 'del_host'),
    (r'^demo/search_ph$', 'search_ph'),
    (r'^demo/get_mem$', 'get_mem'),
    (r'^demo/get_disk$', 'get_disk')
)
