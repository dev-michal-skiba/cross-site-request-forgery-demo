from django.conf import settings
from django.shortcuts import redirect


def only_anonymous_view(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.HOME_URL)
        return func(request, *args, **kwargs)
    return inner


def protected_view(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(settings.HOME_URL)
        return func(request, *args, **kwargs)
    return inner


def csrf_switch(func):
    def inner(request, *args, **kwargs):
        context = kwargs.pop('context', {})
        context.update({'csrf_switch': settings.IS_CSRF_MIDDLEWARE_ON})
        return func(request, context=context, *args, **kwargs)
    return inner


def auth(func):
    def inner(request, *args, **kwargs):
        context = kwargs.pop('context', {})
        context.update({'logged_in': request.user.is_authenticated})
        return func(request, context=context, *args, **kwargs)
    return inner
