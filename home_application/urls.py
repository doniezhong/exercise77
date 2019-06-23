# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^qrcode/$', 'qrcode'),
    (r'^generate_qrcode/$', 'generate_qrcode'),
    (r'^download_qrcode/$', 'download_qrcode'),
    (r'^cc/search_business$', 'search_business'),
)
