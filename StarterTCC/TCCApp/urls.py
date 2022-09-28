from django.urls import path
from TCCApp import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('docad/',views.docad, name='docad'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    # path('register', views.register, name='register'),
]