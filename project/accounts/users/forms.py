from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Role

class CustomUserCreationForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), empty_label="Select Role", required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role',)

class CustomAuthenticationForm(AuthenticationForm):
    pass