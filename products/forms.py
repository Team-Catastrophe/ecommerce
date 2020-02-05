from django import forms
from .models import ProductComments,Product,ProductSeller


class comment_form(forms.ModelForm):
    product = forms.CharField(widget = forms.HiddenInput(), required = False)
    user    = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta():
        model= ProductComments
        fields = ['user','product','comment','rating']

class ProductForm(forms.ModelForm):
    class Meta():
        model= Product
        fields = [
                    'user',
                    'category',      
                    'title',                  
                    'description',   
                    'price',         
                    'image',         
                    'active',        
                ]

class ProductSellerForm(forms.ModelForm):
    class Meta():
        model= ProductSeller
        fields = [
                    'user',
                    'product',      
                    'price'
                ]

