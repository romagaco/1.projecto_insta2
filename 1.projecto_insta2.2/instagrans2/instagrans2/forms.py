
from django import forms
# import user form 
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = [
            "first_name",
            "username",
            "email",
            "password"
        ]

    
    def save(self):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()

        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
