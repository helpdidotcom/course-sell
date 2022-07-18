from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class LoginForm(AuthenticationForm):

    username = forms.EmailField(max_length=50, required=True, label='Email Address')

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = None
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username, password=password)
            if (result is not None):
                return result
            else:
                raise ValidationError("Email or Password Invalid")
        except:
            raise ValidationError("Email or Password Invalid")
