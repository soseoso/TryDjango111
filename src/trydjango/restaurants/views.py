from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):  # Pass an argument as a request
	return HttpResponse("hello")
	# return render(request, "home.html", {})  # some sort of responses