import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):  # Pass an argument as a request
	num = random.randint(0, 10000000)
	return render(request, "base.html", {'html_var' : True, 'num': num})  # some sort of responses
						   # templates   # extra context - dict