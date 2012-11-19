from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from portal.models import *
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.core.context_processors import csrf

@login_required
def portal_main_page(request):
	"""
	If users are authenticated, direct them to the main page. Otherwise, take
	them to the login page.
	"""
        form = NoteForm(request.POST)	
	return render_to_response('portal/add.html', {'form': form,}, context_instance=RequestContext(request))
	
def logout_page(request):
	'''
	Log user out and re-direct them to the main page.
	'''
	logout(request)
	return HttpResponseRedirect('/')

#main order form view
@login_required
def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/portal/confirm/') # Redirect after POST
	else:
	    return HttpResponseRedirect('/portal/') 
    else:
     	    form = NoteForm() # An unbound form
    return render_to_response('portal/add.html', {'form': form,}, context_instance=RequestContext(request))

#confirmation page after placing order
def confirm(request):
    return render_to_response('portal/confirm.html')

