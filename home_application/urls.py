# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from home_application import views

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^demo/$', 'demo'),
    (r'^curd/$', 'curd'),
    (r'^form/$', 'form'),
    (r'^api_test$', 'api_test'),
    (r'^cc/search_business$', 'search_business'),
)


# for view, view_obj in views.__dict__.items():
#     if not callable(view_obj):
#         continue
#
#     view_name_split = view.split('_')
#     if len(view_name_split) > 1:
#         view_name = "_".join(view_name_split[1:])
#         if view_name_split[0] == 'aget':
#             url_str = r'^%s$' % (view_name + r"/")
#         elif view_name_split[0] == 'apost':
#             url_str = r'^%s$' % view_name
#         else:
#             continue
#
#         urlpatterns.append(url(url_str, view_obj))
