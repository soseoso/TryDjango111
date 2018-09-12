from django import forms

class RestaurantCreateForm(forms.Form):
    name            = forms.CharField()
    location        = forms.CharField(required='True')
    category        = forms.CharField()
   