from django.conf.urls import *

#don't know difference between previous line and 
from django.conf.urls.defaults import *

from testsite.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),


	#MY STUFF
	(r'^$', main_page),
	#Login / logout
	(r'^login/$', 'django.contrib.auth.views.login'),
	(r'^logout/$', logout_page),
	
	#Web portal
	(r'^portal/', include('portal.urls')),
	(r'^confirm/', include('portal.urls')),
	
	# Serve static content
	#Not sure how this works
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': 'static'}),
)
