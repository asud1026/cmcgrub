from django.conf.urls.defaults import *
from portal.views import *
from hub.views import *
from portal.views import *
from portal.models import Note

urlpatterns = patterns('hub.views', 

	#Main web portal entrance.	
	(r'^$', 'hub'),
)	
