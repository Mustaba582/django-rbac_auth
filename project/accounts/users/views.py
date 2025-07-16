from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages as message # Keep your messages import
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser, Role # Import CustomUser and Role

def register(request): # Renamed from register_view for consistency with guide
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            message.success(request, "Registration successful!") # Optional: add success message
            return redirect('dashboard') # Redirect to dashboard after successful registration
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    message.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request): # Renamed from login_view for consistency with guide
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message.success(request, f"Welcome back, {user.username}!") # Optional: add success message
                return redirect('dashboard') # Redirect to dashboard after successful login
            else:
                message.error(request, "Invalid username or password.") # Keep your existing error message
        else:
            message.error(request, "Invalid form submission.") # General error for invalid form
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request): # Renamed from logout_view for consistency with guide
    logout(request)
    message.info(request, "You have been logged out.") # Optional: add info message
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

# Role-based access control helper functions
def is_admin(user):
    return user.is_authenticated and user.role and user.role.name == 'admin'

def is_staff(user):
    return user.is_authenticated and user.role and user.role.name == 'staff'

def is_member(user):
    return user.is_authenticated and user.role and user.role.name == 'member'

@login_required
@user_passes_test(is_admin)
def admin_page(request):
    return render(request, 'users/admin_page.html')

@login_required
@user_passes_test(is_staff)
def staff_page(request):
    return render(request, 'users/staff_page.html')

@login_required
@user_passes_test(is_member)
def member_page(request):
    return render(request, 'users/member_page.html')