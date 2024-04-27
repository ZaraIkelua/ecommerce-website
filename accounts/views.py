from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, SignInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, str(form.errors))
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and not user.is_superuser:
                login(request, user)
                return redirect('homepage')
            else:
                form.add_error(None, 'Username or Password not correct')
        else:
            messages.error(request, str(form.errors))
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})
