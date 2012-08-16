from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('prd.views',

    url(r'^$', 'template_path', name='prd'),

    url(r'^(?P<path>.*)$', 'template_path', name='prd-template-path'),

)
