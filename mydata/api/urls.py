from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^smal_data_authentication/', views.smal_data_authentication , name='smal_data_authentication'),
    url(r'^user_daily_mobility_segments/', views.user_daily_mobility_segments , name='user_daily_mobility_segments'),

)
