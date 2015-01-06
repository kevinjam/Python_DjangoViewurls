from django.shortcuts import render

#from django.shortcuts import render_to_response
#from django.http import HttpResponseRedirect
#from django.contrib import auth
#from django.core.context_processors import csrf

#Creating a login view method
#def login(request):
 #c ={}
  #c.update(csrf(request))
   #return  render_to_response('login.html', c)

#Define a home page default where is picking from the templates
def home(request):
       return render(request, "home.html")