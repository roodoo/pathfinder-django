from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pfdj.views.home', name='home'),
    # url(r'^pfdj/', include('pfdj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template':'index.html'}),

    url(r'^prd/', include('prd.urls')),
    url(r'^spells/', include('spells.urls')),
    url(r'^creatures/', include('creatures.urls')),

    url(r'^toee/', include('toee.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT, 'show_indexes' : True})

    )
