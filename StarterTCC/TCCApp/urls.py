from django.urls import path
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
    path('dochanging/', views.dochanging, name='dochanging'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('logouts/', views.logouts, name='logouts'),
]
