from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect to the home page or dashboard
    else:
        form = UserCreationForm()
    return render(request, 'customers/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to the home page or dashboard
        else:
            return redirect('login')  # re-direct to login page
    return render(request, 'customers/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')