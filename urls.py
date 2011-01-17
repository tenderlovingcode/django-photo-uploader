from django.conf.urls.defaults import *

import os.path

urlpatterns = patterns('',
	(r'^upload/', include('photouploader.urls')),
	(r'^(?P<path>.*)$', 'django.views.static.serve',
	{'document_root': os.path.join(os.path.dirname(__file__), 'public')}),
)
