from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^manage/$', 'project.views.manage'),
    url(r'^list/$', 'project.views.list'),
    url(r'^list/(?P<id>.*)/$', 'project.views.every'),
    url(r'^del/$', 'project.views.delete'),
    url(r'^search/$', 'project.views.search'),
    url(r'^update/$', 'project.views.update'),
)
