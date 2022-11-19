from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class UserCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2',
                    'profile_image', 'phone_number', 'address', 'social_instagram',
                    'social_facebook', 'social_twitter']

class UserUpdateForm(forms.ModelForm):
    """
    A form for updating users.
    """

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'profile_image',
                    'phone_number', 'address', 'social_instagram', 'social_facebook',
                    'social_twitter', 'show_default_friends']