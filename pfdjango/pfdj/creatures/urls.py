from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('creatures.views',

    url(r'^$', 'index', name='creatures'),

    url(r'^details/(?P<creature_id>\d+)/$', 'creature_details', name='creatures-details'),
    url(r'^edit/(?P<creature_id>\d+)/$', 'creature_edit', name='creatures-edit'),
    url(r'^create/$', 'creature_create', name='creatures-create'),

)

