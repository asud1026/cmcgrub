from django.conf.urls.defaults import *
from portal.views import *
from models import Note

urlpatterns = patterns('', 

	#Main web portal entrance.
	(r'^confirm/$', confirm),


	(r'^$', portal_main_page),
	
)
