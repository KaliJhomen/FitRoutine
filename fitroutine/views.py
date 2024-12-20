from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def welcome_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')
    return render(request, 'welcome.html')

def home_view(request):
    return render(request, 'home.html')
