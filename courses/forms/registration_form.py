from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def clean_email(self):
        user = None
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except:
            return email

        if user is not None:
            raise ValidationError("User Already Exists!")
