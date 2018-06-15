import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):  # Pass an argument as a request
	num = None
	some_list = [
		random.randint(0, 10000000), 
		random.randint(0, 10000000), 
		random.randint(0, 10000000)
	]
	condition_bool_item = True
	# The logic should actually exist in the view function itself
	# not so much in the template.
	if condition_bool_item:
		num = random.randint(0, 10000000)
	
	context = {
		'num': num, 
		'some_list': some_list
	}  # 길어서, context라는 변수에 저장.
	return render(request, "base.html", context)  # some sort of responses
						   