from django.conf.urls.defaults import *

urlpatterns = patterns('',
	#preview/verification URL
	(r'^p/(?P<token>\w+)$', 'photouploader.views.preview'),
)
