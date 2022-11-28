from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse("Hello World")

def detail(request, user_id):

    user = User.objects.get(id=user_id)

    wallet = Wallet.objects.get(user = user)

    actives = Active.objects.get(id = wallet.id)

    return HttpResponse(f"You are looking at user {user.__str__()}<br> {wallet.__str__()} <br> {type(actives)}")



