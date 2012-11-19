from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from models import Note
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.core.context_processors import csrf

@login_required
def portal_main_page(request):
	"""
	If users are authenticated, direct them to the main page. Otherwise, take
	them to the login page.
	"""
	return render_to_response('portal/form.html')
	
def logout_page(request):
	'''
	Log user out and re-direct them to the main page.
	'''
	logout(request)
	return HttpResponseRedirect('/')

def confirm(request):
    error_msg = u"No POST data sent."
    if request.method == "POST":
        post = request.POST.copy()
        if post.has_key('order') and post.has_key('name'):
            order = post['order']
        else:
            error_msg = u"Insufficient POST data (need 'name' and 'title'!)"
    return (render_to_response('portal/confirm.html'), RequestContext(request))

