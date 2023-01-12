from django.shortcuts import render

from account.decorators import csrf_switch, auth


@csrf_switch
@auth
def home(request, context):
    return render(request, 'home.html', context)
