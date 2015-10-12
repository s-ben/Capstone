from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<question_id>[0-9]+)$', views.details ),
    url(r'^list/$', views.list, name='list'),
#     url(r'^lists/', views.list, name='index'),
] 
# name='detail'
# (?P<question_id>[0-9]+)/$

# -*- coding: utf-8 -*-
# from django.conf.urls import patterns, url
# 
# urlpatterns = patterns('subtractor.audio_process.views',
#     url(r'^list/$', 'list', name='list'),
# )