from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .decorators import auth, csrf_switch, only_anonymous_view, protected_view
from .forms import LoginForm, RegisterForm, UpdateForm


@only_anonymous_view
@csrf_switch
@auth
def login(request, context):
    error_message = ''
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(settings.HOME_URL)
            error_message = 'Incorrect username or password'
    context.update({'form': login_form, 'btn_text': 'Log In', 'error_message': error_message})
    return render(request, 'account_form.html', context)


@protected_view
@csrf_switch
@auth
def logout(request, context):
    auth_logout(request)
    return redirect(settings.HOME_URL)


@only_anonymous_view
@csrf_switch
@auth
def register(request, context):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            if user is not None:
                auth_login(request, user)
                return redirect(settings.HOME_URL)
    context.update({'form': register_form, 'btn_text': 'Register'})
    return render(request, 'account_form.html', context)


@protected_view
@csrf_switch
@auth
def update(request, context):
    success_message = ''
    if request.method == 'POST':
        update_form = UpdateForm(request.POST)
        if update_form.is_valid():
            password = update_form.cleaned_data['password']
            request.user.set_password(password)
            request.user.save()
            user = authenticate(request, username=request.user.username, password=password)
            if user is not None:
                auth_login(request, user)
                success_message = 'Password changed'
    update_form = UpdateForm()
    context.update({'form': update_form, 'btn_text': 'Update', 'success_message': success_message})
    return render(request, 'account_form.html', context)
