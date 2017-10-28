from django.contrib.auth.models import User
from django import forms


# creating a blue print which will be used while making user forms(override few of the stuff from user form)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

