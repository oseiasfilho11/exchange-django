from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse("Hello World")

def detail(request, user_id):

    user = User.objects.get(id=user_id)

    wallet_user = Wallet.objects.get(user = user)

    actives = Active.objects.filter(wallet__id = wallet_user.id)

    active_string = "<br>".join([w.__str__() for w in actives])

    return HttpResponse(template_div(f'{user.__str__()}<br><br> {wallet_user.__str__()} <br><br> {active_string}'))

def detail_wallet(request, user_id):

    user = User.objects.get(id=user_id)
    wallet_user = Wallet.objects.get(user = user)

    return HttpResponse(f'{wallet_user.__str__()}')

def detail_name(request, user_name):
    user = User.objects.get(userName = user_name)
    print(user)
    return HttpResponse(f"{user.__str__()}")

def template_div(text):
    return f"<div style='text-align:center'>{text}</div>"

