from django.conf.urls import *
from django.conf import settings
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
	(r'^order/', include('portal.urls')),

	#Hub portal
	(r'^hub/', include('hub.urls')),
	(r'^confirm/', include('portal.urls')),
	
	# Serve static content
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       
	#(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
	#{'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        
	#Registration
	(r'^accounts/', include('registration.backends.default.urls')),

	#about and contact
	(r'^about/', about_page),
	(r'^contact/', contact_us_page),

)
