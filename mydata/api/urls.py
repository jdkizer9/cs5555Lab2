from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^user_daily_mobility_segments/', views.user_daily_mobility_segments , name='user_daily_mobility_segments'),
    url(r'^user_daily_mobility_summary/', views.user_daily_mobility_summary , name='user_daily_mobility_summary'),
    url(r'^user_pam_data/', views.user_pam_data , name='user_pam_data'),

)
