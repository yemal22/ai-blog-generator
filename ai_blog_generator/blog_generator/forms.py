from django import forms

class signupForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Enter your username',
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Enter your email',
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Enter your password',
            }
        )
    )
    confirm_password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Confirm your password',
            }
        )
    )

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Enter your username',
            }
        )
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "p-2 border w-full rounded",
                'placeholder': 'Enter your password',
            }
        )
    )