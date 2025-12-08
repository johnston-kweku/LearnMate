from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.contrib import messages
from learning_logs.forms import CustomUserCreationForm


# Create your views here.

def logout(request):
    """Log the user out."""
    auth_logout(request)

    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register new user."""
    if request.method != 'POST':
        # Display blank registration form
        form = CustomUserCreationForm()
    else:
        # Process completed form
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "Registration successful.")
            # Log the user in and redirect to homepage.
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)

