from django import forms
from .models import *
class normal(forms.Form):
    name=forms.CharField(max_length=10)
    phone=forms.IntegerField()
    email=forms.EmailField()
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=10)

class modelform(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'
