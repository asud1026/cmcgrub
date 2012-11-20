from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from portal.models import *
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.core.context_processors import csrf

#hub terminal view
@login_required
def hub(request):
    latest_notes_list = Note.objects.all().order_by('-pub_date')[:20]
    return render_to_response('portal/hub.html', {'latest_notes_list': latest_notes_list})
