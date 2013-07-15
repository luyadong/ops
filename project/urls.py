from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^manage/$', 'project.views.manage'),
    url(r'^list/$', 'project.views.list'),
<<<<<<< HEAD
=======
    url(r'^list/(?P<proname>.*)$', 'project.views.every'),
>>>>>>> 014fd640e68a21181bf5e8af274e6b6b04baf351
    url(r'^search/$', 'project.views.search'),
)
