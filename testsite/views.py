from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def main_page(request):
    
    return HttpResponseRedirect('/login')
	
def logout_page(request):
	"""
	Log users out and re-direct them to the main page.
	"""
	logout(request)
	return HttpResponseRedirect('/login')

def about_page(request):
	"""
	lets user view what we're about
	"""
	return render_to_response('about.html')#, HttpResponseRedirect('/about')

def contact_us_page(request):
	"""
	lets user contact us
	"""
	return render_to_response('contact_us.html')#, HttpResponseRedirect('/contact')
