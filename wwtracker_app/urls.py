"""wwtracker_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from states.views import StateList
from waters.views import WaterList
from measurements.views import MeasurementList
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view()),
    url(r'^api/states/$', StateList.as_view(), name="states"),
    url(r'^api/water/(?P<state>.+)/$', WaterList.as_view(), name="water"),
    url(r'^api/measurement/(?P<bodyId>.+)/$', MeasurementList.as_view(), name="measurement"),
)

