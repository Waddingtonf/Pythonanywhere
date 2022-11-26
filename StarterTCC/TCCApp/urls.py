from django.urls import path, reverse_lazy
from TCCApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('login', views.logar, name='login'),
    path('dologin/', views.dologin, name='dologin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/', views.perfil, name='perfil'),
    path('logouts/', views.logouts, name='logouts'),
    path('dochanging/', views.dochanging, name='dochanging'),
    path('servicos/', views.servicos, name='servicos'),
    path('estampa/', views.estampa, name='estampa'),
    path('produtospage/', views.produtospage, name='produtos'),
    path('upload/', views.upload, name='upload'),
    path('domockup/', views.domockup, name='domockup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html", success_url = reverse_lazy("password_reset_done")), name='reset_password'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "./registration/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="./registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="./registration/password_reset_complete.html"), name="password_reset_complete"),
]
