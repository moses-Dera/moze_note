from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to the home page.
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context) 

# def logoutUser(request):
#     return HttpResponseRedirect(reverse("users:login"))
#     logout(request)
# Use this as custom logout view instead of what you used in urls.py
# Create your views here.
