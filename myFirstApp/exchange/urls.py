from django.urls import path

from . import views

urlpatterns = [ 
    #Quando roda o server ele vai na porta padrao localhost:8080, porem só funciona se se for localhost:8080/polls porque no arquivo 
    #urls.py da pasta de cima o primeiro path tem /polls no primeiro path
    path('', views.index, name='index'),
    path('<int:user_id>/',views.detail, name='detail')
]