from django import forms
from .models import UserReport

class UserReportForm(forms.ModelForm):
    class Meta:
        model = UserReport
        fields = ['report_type', 'description', 'photo', 'bin']

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class Registratin_form(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']