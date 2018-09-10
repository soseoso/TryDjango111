from django.db.models import Q
import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category__iexact=slug) | Q(category__contains=slug))
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset	

class SearchRestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		print(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category__iexact=slug) | Q(category__contains=slug))
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset
