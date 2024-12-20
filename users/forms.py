from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BodyMeasurement, UserProfile

class UserProfileCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'weight', 'height', 'shoulders', 'chest', 'waist', 'biceps', 'forearm', 'glutes']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', required=True)
class BodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurement
        fields = ['weight', 'height', 'shoulders', 'chest', 'waist', 'biceps', 'forearm', 'glutes']
        
