from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileCreationForm, UserProfileUpdateForm, BodyMeasurementForm, CustomPasswordChangeForm
from .models import UserProfile, BodyMeasurement

def user_register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirecciona a "home" después de registrarse
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
            return redirect('home')  # Redirecciona a "home" después de logearse
        else:
            messages.error(request, 'Correo o contraseña incorrectos')    
    return render(request, 'registration/login.html')

def update_profile_view(request):
    if request.method == 'POST':
        profile_form = UserProfileUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        
        if profile_form.is_valid():
            profile_form.save()
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Mantener la sesión iniciada después de cambiar la contraseña
        
        return redirect('users:profile')
    else:
        profile_form = UserProfileUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'update_profile.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })

def update_body_measurement_view(request):
    if request.method == 'POST':
        measurement_form = BodyMeasurementForm(request.POST)
        if measurement_form.is_valid():
            body_measurement = measurement_form.save(commit=False)
            body_measurement.user = request.user
            body_measurement.save()
            return redirect('users:profile')
    else:
        measurement_form = BodyMeasurementForm()
    
    return render(request, 'update_body_measurement.html', {
        'measurement_form': measurement_form,
    })
@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(id=request.user.id)
    body_measurements = BodyMeasurement.objects.filter(user=user_profile).last()  
    return render(request, 'profile.html', {'profile': user_profile, 'body_measurements': body_measurements})

@login_required
def update_profile(request):
    user_profile = UserProfile.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  
    else:
        form = UserProfileCreationForm(instance=user_profile)
    return render(request, 'update_profile.html', {'form': form})