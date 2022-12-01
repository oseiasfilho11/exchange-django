from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import *

def index(request):
    return render(request, 'exchange/index.html')

def viewLogin(request):
    return render(request, 'exchange/login.html')

def login(request):

    print(request)
    userEmail_ = str(request.POST.get("userEmail"))
    userPassword_ = str(request.POST.get("userPassword"))

    print(userEmail_ + " " +userPassword_)

    user = ""
    userLista = User.objects.filter(userEmail = userEmail_, passWord = userPassword_)
    if len(userLista) > 0:
        user = userLista[0]
        return details(request, user.id)
    else:
        return HttpResponse("Nao encontrado")
    


def details(request, user_id):

    user = User.objects.get(id=user_id)

    wallet_user = Wallet.objects.get(user = user)

    actives = Active.objects.filter(wallet__id = wallet_user.id)

    context = {'user' : user, 'wallet' :  wallet_user, 'actives' : actives,}

    return render(request, 'exchange/user_details.html', context)


    '''active_string = "<br>".join([w.__str__() for w in actives])

    return HttpResponse(template_div(f'{user.__str__()}<br><br> {wallet_user.__str__()} <br><br> {active_string}'))
'''

def formUser(request):
    return render(request, 'exchange/add_user.html')

def addUser(request):

    userName_ = str(request.POST.get("userName"))
    userPassword_ = str(request.POST.get("passWord"))
    userEmail_ =  str(request.POST.get("userEmail"))

    new_user = User()

    new_user.userName = userName_
    new_user.passWord = userPassword_
    new_user.userEmail = userEmail_

    new_user.save()
    
    return HttpResponse(new_user)


def detail_wallet(request, user_id):

    user = User.objects.get(id=user_id)
    wallet_user = Wallet.objects.get(user = user)

    return HttpResponse(f'{wallet_user.__str__()}')

'''def detail_name(request, user_name):
    user = User.objects.get(userName = user_name)
    print(user)
    return HttpResponse(f"{user.__str__()}")'''

def template_div(text):
    return f"<div style='text-align:center'>{text}</div>"

