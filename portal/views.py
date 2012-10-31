from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def portal_main_page(request):
	"""
	If users are authenticated, direct them tot he main page. Otherwise, take
	them to the login page.
	"""
	return render_to_response('portal/index.html')
	
def logout_page(request):
	'''
	Log user out and re-direct them to the main page.
	'''
	logout(request)
	return HttpResponseRedirect('/')
