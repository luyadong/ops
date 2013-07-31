from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^manage/$', 'device.views.manage'),
    url(r'^list/$', 'device.views.list'),
    url(r'^list/(?P<id>.*)$', 'device.views.every'),
    url(r'^del/$', 'device.views.delete'),
    url(r'^search/$', 'device.views.search'),
    url(r'^update/$', 'device.views.update'),
)
