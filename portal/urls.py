from django.conf.urls.defaults import *
from portal.views import *
from models import Note

urlpatterns = patterns('portal.views', 

	#Main web portal entrance.	
	(r'^$', 'portal_main_page'),
	(r'^add/$', 'add'),
	(r'^confirm/$', 'confirm'),
	
)
