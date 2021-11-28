from django import forms
from django.contrib.auth import (authenticate
, get_user_model)

from .models import *

User = get_user_model ( )


class UserLoginForms (forms.Form):
    username = forms.CharField (max_length=255, widget=forms.TextInput (attrs={'class': 'form-control'}))
    password = forms.CharField (max_length=255, widget=forms.PasswordInput (attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get ('username')
        password = self.cleaned_data.get ('password')
        if username and password:
            user = authenticate (username=username, password=password)
            if not user:
                raise forms.ValidationError ("Username or Password Not Valid")
            if not user.check_password (password):
                raise forms.ValidationError ("password is not correct")
            if not user.is_active:
                raise forms.ValidationError ("This user does not exist")
        return super (UserLoginForms, self).clean (*args, **kwargs)

