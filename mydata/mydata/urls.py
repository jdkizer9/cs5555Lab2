from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^callback/', include('callback.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
