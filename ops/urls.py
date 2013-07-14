from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ops.views.home', name='home'),
    # url(r'^ops/', include('ops.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ops.views.index'),
    url(r'^login/$', 'ops.views.user_login'),
    url(r'^logout/$', 'ops.views.user_logout'),
    url(r'^device/', include('device.urls')),
    url(r'^project/', include('project.urls')),
)
