from django import forms
from .models import RestaurantLocation

# class RestaurantCreateForm(forms.Form):
#     name            = forms.CharField()
#     location        = forms.CharField(required='True')
#     category        = forms.CharField()
    
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if name == 'Hello':
#             raise forms.ValidationError('Not a valid name')
#         return name

class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name', 
            'location',
            'category'
        ]
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name