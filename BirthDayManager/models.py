from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
import datetime
import uuid

# Create your models here.
CurrentUser = settings.AUTH_USER_MODEL

class FriendDetail(models.Model):

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(max_length=200, blank=False, null=False)
    phone_number = PhoneNumberField(blank=True)
    city = models.CharField(max_length=50, blank=False, null=False)

    email = models.EmailField(max_length=500, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null = True, blank= True, upload_to = 'profiles/friends-profile/',
        default='profiles/default-images/user-default.png'
    )

    # This will be foreign key to map which Friend belongs to whom.
    member_friend = models.ForeignKey(CurrentUser, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["member_friend"]

    @property
    def remaining_days(self):
        x = datetime.datetime.now()
        days_remaining = (self.birth_date.replace(x.year) - x.date()).days
        if days_remaining < 0:
            days_remaining = (self.birth_date.replace(x.year+1) - x.date()).days
        return days_remaining

class DefaultFriend(models.Model):

    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(max_length=200, blank=False, null=False)
    phone_number = PhoneNumberField(blank=True)
    city = models.CharField(max_length=50, blank=False, null=False)

    email = models.EmailField(max_length=500, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(
        null = True, blank= True, upload_to = 'profiles/default-images/',
        default='profiles/default-images/user-default.png'
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def remaining_days(self):
        x = datetime.datetime.now()
        days_remaining = (self.birth_date.replace(x.year) - x.date()).days
        if days_remaining < 0:
            days_remaining = (self.birth_date.replace(x.year+1) - x.date()).days
        return days_remaining

