from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Authentication.models import Profile


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone',
            'address',
            'date_of_birth',
            'gender',
            'height',
            'current_weight',
            'fitness_goal',
            'allergies'
        ]

        #to select date of birth from a calendar instead of typing it in manually
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            )
        }