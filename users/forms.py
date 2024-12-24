from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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
        fields = ['email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = UserProfile
        fields = ['old_password', 'new_password1', 'new_password2']
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', required=True)
    
class BodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurement
        fields = ['weight', 'height', 'shoulders', 'chest', 'waist', 'biceps', 'forearm', 'glutes']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
            'height': forms.NumberInput(attrs={'step': '0.01'}),
            'shoulders': forms.NumberInput(attrs={'step': '0.01'}),
            'chest': forms.NumberInput(attrs={'step': '0.01'}),
            'waist': forms.NumberInput(attrs={'step': '0.01'}),
            'biceps': forms.NumberInput(attrs={'step': '0.01'}),
            'forearm': forms.NumberInput(attrs={'step': '0.01'}),
            'glutes': forms.NumberInput(attrs={'step': '0.01'}),
        }
    
    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight < 0:
            raise ValidationError('El peso no puede ser negativo.')
        return weight

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height < 0:
            raise ValidationError('La altura no puede ser negativa.')
        return height

    def clean_shoulders(self):
        shoulders = self.cleaned_data.get('shoulders')
        if shoulders is not None and shoulders < 0:
            raise ValidationError('Los hombros no pueden ser negativos.')
        return shoulders

    def clean_chest(self):
        chest = self.cleaned_data.get('chest')
        if chest is not None and chest < 0:
            raise ValidationError('El pecho no puede ser negativo.')
        return chest

    def clean_waist(self):
        waist = self.cleaned_data.get('waist')
        if waist is not None and waist < 0:
            raise ValidationError('La cintura no puede ser negativa.')
        return waist

    def clean_biceps(self):
        biceps = self.cleaned_data.get('biceps')
        if biceps is not None and biceps < 0:
            raise ValidationError('Los bíceps no pueden ser negativos.')
        return biceps

    def clean_forearm(self):
        forearm = self.cleaned_data.get('forearm')
        if forearm is not None and forearm < 0:
            raise ValidationError('El antebrazo no puede ser negativo.')
        return forearm

    def clean_glutes(self):
        glutes = self.cleaned_data.get('glutes')
        if glutes is not None and glutes < 0:
            raise ValidationError('Los glúteos no pueden ser negativos.')
        return glutes
