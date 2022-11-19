from django import forms
from .models import FriendDetail, DefaultFriend


class FriendDetailForm(forms.ModelForm):
    class Meta:
        model = FriendDetail
        fields = [
            'first_name', 'last_name', 'birth_date', 'phone_number', 'city', 'email',
                'social_instagram', 'social_facebook', 'social_twitter', 'profile_image'
        ]
        

class DefaultFriendForm(forms.ModelForm):
    class Meta:
        model = DefaultFriend
        fields = [
            'first_name', 'last_name', 'birth_date', 'phone_number', 'city', 'email',
                'social_instagram', 'social_facebook', 'social_twitter', 'profile_image'
        ]

class UpdateFriendForm(forms.ModelForm):
    class Meta:
        model = FriendDetail
        fields = ['first_name', 'last_name', 'birth_date', 'phone_number', 'city', 'email',
                'social_instagram', 'social_facebook', 'social_twitter', 'profile_image'
        ]
        