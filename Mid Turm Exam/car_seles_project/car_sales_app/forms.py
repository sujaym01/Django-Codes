from django import forms
from .models import Car, Comment,Order
   
class CarForm(forms.ModelForm):
    class Meta: 
        model = Car
        fields = '__all__'
        # exclude = ['.....']
        
class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'comment']
