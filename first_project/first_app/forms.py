from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    gender = forms.CharField(max_length=6)
