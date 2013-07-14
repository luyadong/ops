from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^manage/$', 'device.views.manage'),
    url(r'^list/$', 'device.views.list'),
    url(r'^list/(?P<nei_ip>.*)$', 'device.views.every'),
    url(r'^search/$', 'device.views.search'),
)
