from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view

def home(request):  # Pass an argument as a request
	html_var = 'using f strings'
	html_ = f"""  # python f string <- from python 3.6
	<!DOCTYPE html>
	<html lang = en>
	<head>
	</head>
	<body>
		<h1>Hello, World!</h1>
		<p> This is html comming through {html_var}</p>
	</body>
	</html>
	"""  # python string
	return HttpResponse(html_)
	# return render(request, "home.html", {})  # some sort of responses