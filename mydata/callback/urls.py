from django.conf.urls import patterns, url

from callback import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^github', views.github_callback, name='github callback'),



)
