from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BodyMeasurement
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', required=True)
class BodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurement
        fields = ['weight', 'height', 'shoulders', 'chest', 'waist', 'biceps', 'forearm', 'glutes']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')