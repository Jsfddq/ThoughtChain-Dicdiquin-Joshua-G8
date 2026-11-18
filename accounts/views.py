from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser

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

class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ['username', 'email'] # Users can edit these fields
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')

    # This ensures a user can ONLY edit their own profile
    def get_object(self, queryset=None):
        return self.request.user