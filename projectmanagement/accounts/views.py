from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SingUpForm

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SingUpForm()
    return render(request, 'signup.html', {'form': form})
