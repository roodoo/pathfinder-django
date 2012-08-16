from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('spells.views',

    url(r'^$', 'spells', name='spells'),

    url(r'^list/(?P<class_slug>[\w_]+)/', 'spell_list', name='spells-list'),
    url(r'^list/(?P<class_slug>[\w_]+)/(?P<level>\d+)/', 'spell_list', name='spells-list'),

    url(r'^details/(?P<spell_id>\d+)/', 'spell_details', name='spells-details'),
    url(r'^edit/(?P<spell_id>\d+)/$', 'spell_edit', name='spells-edit'),

)
