from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard_redirect(request):
    if request.user.role == 'admin':
        return render(request, 'accounts/admin_dashboard.html')
    else:
        return render(request, 'accounts/member_dashboard.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')