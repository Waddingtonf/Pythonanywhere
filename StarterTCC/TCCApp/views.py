from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from TCCApp import *
import hashlib
import base64
import binascii
import os
import requests
import http.client


# configurações de api

conn = http.client.HTTPSConnection("api.mediamodifier.com")
headers = { 'Content-Type': "application/json",
            'api_key': "4cb1d7d9-36d3-45f7-837e-2dd1358081d0"
        }

# Request api gets
def produtos(request):

    conn.request("GET", "/mockups", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data)


#Exemplo de testes

def mockup(request):

    payload = "{\n  \"nr\": 6323,\n  \"layer_inputs\": [\n    {\n      \"id\": \"f579b00b-9841-4d33-bcc7-d6dab6606998\",\n      \"data\": \"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAocA...\",\n      \"crop\": {\n        \"x\": 0,\n        \"y\": 0,\n        \"width\": 647,\n        \"height\": 1400\n      },\n      \"checked\": true\n    },\n    {\n      \"id\": \"ea18e8f6-1e41-4a5e-bbe2-a469e2fea45d\",\n      \"checked\": true,\n      \"color\": {\n        \"red\": 254,\n        \"green\": 186,\n        \"blue\": 227\n      }\n    }\n  ]\n}"

    conn.request("POST", "/mockup/render", payload, headers)

    res = conn.getresponse()
    data = res.read()

#Pesquisa dos tipos de mockup

def searchmockup(request):

    if search.POST is None:
        return render(request, 'searchmockup.html')

    pesquisa = str(search.POST)
    conn.request("GET", "/mockups/search?q=f{pesquisa}", headers=headers)

    res = conn.getresponse()
    data = res.read()


# Create your views here.

def home(request):
	return render(request,'main.html')

def cadastro(request):
    # Direcionador de Página de Cadastro
#	data = {}
#	data['form'] = UsersForm()
	return render(request,'cadastro.html')

def docad(request):
    # Realizar Cadastro
    data = {}

    if request.POST['usuario'] is None:
        data['msg'] = 'Campo Usuário Vazio'
        data['class'] = 'is-danger'
        return render(request,'cadastro.html', data)

    if(request.POST['senha'] != request.POST['confirmarsenha']):
        data['msg'] = 'Senha e Confirmação de Senha diferentes!'
        data['class'] = 'is-danger'
        return render(request,'cadastro.html', data)
    else:
        user = User.objects.create_user(request.POST['usuario'], request.POST['email'], request.POST['senha'])
        user.first_name = request.POST['nome']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso!'
        data['class'] = 'is-success'
        return render(request,'cadastro.html', data)

def logar(request):
    return render(request,'login.html')

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['usuario'], password = request.POST['senha'])
    print(user)
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha Incorretos!'
        data['class'] = 'is-danger'
    return render(request,'login.html', data)

def dashboard(request):
    return render(request, 'dashboard/home.html')

def perfil(request):
    return render(request, 'dashboard/perfil.html')

def dochanging(request):
    data = {}

    hashed_pwd = make_password(request.POST['confirmar-senha'])
    passwd = check_password(request.POST['confirmar-senha'], hashed_pwd)

    user = None

    if request.user.is_authenticated is True:
        user = request.user.username

    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        if passwd is True:
            if request.POST['senha'] is not None:
                user.set_password(request.POST['senha'])
            else:
                user.set_password(user.password)
                return render(request, 'home.html', data)


            if request.POST['email'] is not None:
                user.email = request.POST['email']
            else:
                user.email = user.email

            if request.POST['nome'] is not None:
                user.first_name = request.POST['nome']
            else:
                user.first_name = user.first_name

            user.save()

            data['msg'] = 'Usuário Atualizado!'
            data['class'] = 'is-sucess'
            return render(request,'dashboard/perfil.html', data)

        else:
            return redirect('home')

def logouts(request):
    logout(request)
    return redirect('/home')

def password_reset_request(request):
    if request.method == "POST":
        form_resetpassword = PasswordResetForm(request.POST)
        if form_resetpassword.is_valid():
            data = form_resetpassword.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = "Reset de Senha"
                    email_template_name = "registration/password_reset_text.txt"
                    parameters = {
                        'email' : user.email,
                        'domain': 'studiomockup3d.pythonanywhere.com',
                        'site_name': 'Studio3DMockup',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                        }

                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Email Inválido')
                    return redirect('password_reset_done')

    else:
        form_resetpassword = PasswordResetForm(request.POST)

    context = {
        'form_resetpassword': form_resetpassword,
    }

    return render(request, "registration/password_reset.html", context)

# def password_reset_request(request):
#	if request.method == "POST":
#		password_reset_form = PasswordResetForm(request.POST)
#		if password_reset_form.is_valid():
#			data = password_reset_form.cleaned_data['email']
#			associated_users = User.objects.filter(Q(email=data))
#			if associated_users.exists():
#				for user in associated_users:
#					subject = "Solicitação de Request de Senha"
#					email_template_name = "registration/password_reset_email.txt"
#					c = {
#					"email":user.email,
#					'domain':'127.0.0.1:8000',
#					'site_name': 'Website',
#					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
#					"user": user,
#					'token': default_token_generator.make_token(user),
#					'protocol': 'http',
#					}
#					email = render_to_string(email_template_name, c)
#					try:
#						send_mail(subject, email, 'noreply@studio3dmockup.com' , [user.email], fail_silently=False)
#					except BadHeaderError:
#						return HttpResponse('Invalid header found.')
#					return redirect ("/password_reset/done/")
#	password_reset_form = PasswordResetForm()
#	return render(request=request, template_name="registration/password_reset.html", context)
#
#
##	form = UsersForm(request.POST or None)
##	if form.is_valid():
#		form.save()
#		return redirect('cadastro')

# def register(request):
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         pwd = request.form['password']

#         user = UsersForm(name, email, pwd)
#         db.session.add(user)
#         db.session.commit()

#     return render('register.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.form['email']
#         pwd = request.form['password']

#         user = UsersForm.query.filter_by(email=email).first()

#         if not user or not user.verify_password(pwd):
#             flash("Email ou Senha Incorreta")
#             return redirect(url_for('login'))

#         login_user(user)
#         return redirect('home')

#     return render('login.html')

# def logout():
#     logout_user()
#     flash("Usuário Deslogado")
#     return redirect(login)
