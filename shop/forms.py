from django import forms
from .models import item

class product(forms.ModelForm):
    class Meta:
        model = item
        fields = "__all__"
        labels={
            'name':'Product Name', 'price':'Product Price', 'brand':'Product Brand'
        }