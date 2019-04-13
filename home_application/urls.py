# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from home_application.ph import execute_job

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^api/test$', 'test'),
    (r'^cc/search_business$', 'search_business'),
    (r'^cc/search_host$', 'search_cc_host'),
    (r'^get_ph_by_ip$', 'get_ph_by_ip'),
    (r'^update_ip_config$', 'update_ip_config'),
    (r'^demo/search_ph_host$', 'search_ph_host'),
    (r'^demo/search_ph_list_by_ip$', 'search_ph_list_by_ip')
)
