from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=64)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    email = forms.EmailField(label='Email', max_length=64)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8, max_length=64)


class UpdateForm(forms.Form):
    password = forms.CharField(label='Change password', widget=forms.PasswordInput(), min_length=8, max_length=64)
