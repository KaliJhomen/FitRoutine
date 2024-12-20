from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileCreationForm, UserProfileUpdateForm
from .models import UserProfile, BodyMeasurement

def user_register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to workouts page after registration
    else:
        form = UserProfileCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to workouts page after login
        else:
            messages.error(request, 'Correo o contraseña incorrectos')    
    return render(request, 'registration/login.html')

@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(id=request.user.id)
    body_measurements = BodyMeasurement.objects.filter(user=user_profile).last()  # Obtener la última medición corporal
    return render(request, 'profile.html', {'profile': user_profile, 'body_measurements': body_measurements})

@login_required
def update_profile(request):
    user_profile = UserProfile.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Redirect to profile page after update
    else:
        form = UserProfileCreationForm(instance=user_profile)
    return render(request, 'update_profile.html', {'form': form})