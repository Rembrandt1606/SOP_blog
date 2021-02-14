from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
# Create your views here.

def index(request):
   value = 'This is a test'
   context = {
       'value': value
   }
   #return HttpResponse("<h1>TEST</h1>")
   return render(request, 'page/index.html', context)