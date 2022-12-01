from django.urls import path

from . import views


app_name = 'exchange'
urlpatterns = [ 
    #Quando roda o server ele vai na porta padrao localhost:8080, porem só funciona se se for localhost:8080/polls porque no arquivo 
    #urls.py da pasta de cima o primeiro path tem /polls no primeiro path
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('telaLogin/',views.viewLogin, name="viewLogin"),
    path('details/<int:user_id>/',views.details, name='details'),
    path('wallet/<int:user_id>/', views.detail_wallet,name='wallet'),
    path('formUser/', views.formUser, name='formUser'),
    path('addUser/',views.addUser,name='addUser')
    #path('<str:user_name>/',views.detail_name, name='name')
]