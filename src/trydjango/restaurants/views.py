import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
# can get rid of all of function based views
# for class based views!

class HomeView(TemplateView):
	template_name = 'home.html'

	# going to add an overriding method called get_context_data
	def get_context_data(self, *args, **kwargs):
		# call that default method using the super call
		# super(HomeView, self) --> TemplateView
		context = super(HomeView, self).get_context_data(*args, **kwargs)
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
		return context

# def about(request):
#	context = {
#
#	}
#	return render(request, 'about.html', context)


# def contact(request):
#	context = {
#
#	}
#	return render(request, 'contact.html', context)

# class ContactView(TemplateView):
#	def get(self, request, *args, **kwargs):
#		context = {}
#		return render(request, 'contact.html', context)

# class AboutView(TemplateView):
# 	template_name = 'about.html'

# class ContactView(TemplateView):
# 	template_name = 'contact.html'