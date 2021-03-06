from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^manage/$', 'project.views.manage'),
    url(r'^list/$', 'project.views.list'),
    url(r'^list/(?P<proname>.*)$', 'project.views.every'),
    url(r'^search/$', 'project.views.search'),
)
