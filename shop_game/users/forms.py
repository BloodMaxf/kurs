from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Personal_area


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

class UserPersonalArea(forms.ModelForm):
    class Meta:
        model = Personal_area
        fields = ('title', 'key')