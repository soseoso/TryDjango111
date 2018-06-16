import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
# function based view
def home(request):  
	num = None
	some_list = [
		random.randint(0, 10000000), 
		random.randint(0, 10000000), 
		random.randint(0, 10000000)
	]
	condition_bool_item = True

	if condition_bool_item:
		num = random.randint(0, 10000000)
	
	context = {
		'num': num, 
		'some_list': some_list
	}  
	return render(request, "home.html", context)  
						   
def about(request):  
	context = {
	} 
	return render(request, "about.html", context) 

def contact(request):  
	context = {
	} 
	return render(request, "contact.html", context)  

class ContactView(View):
	def get(self, request, *args, **kwargs):  
		# the request is still an argument to this get method
		# add 'arguments' and 'keyword arguments' -- will be explained 
		# almost default put in class based view
		print(kwargs)
		context = {}
		return render(request, 'contact.html', context)