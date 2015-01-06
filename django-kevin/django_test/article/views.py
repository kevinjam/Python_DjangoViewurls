from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


# Create your views here.

def hello (request):
	name = "Kevin"
	html ="<html> <body> Hi %s , this seems to have worked1</body></html" % name
	return HttpResponse(html)

#def hello_template(request):
#		name = "Kevin"
#		t = get_template('hello.html')
#		html = t.render(Context({'name' : name}))
#	return HttpResponse(html)
