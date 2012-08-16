from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',

    url(r'^$', direct_to_template, {"template": "toee/default.html"}),
    url(r'^creatures/$', direct_to_template, {"template": "toee/creatures.html"}, name='toee-creatures'),

)

