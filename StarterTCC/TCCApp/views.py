from django.shortcuts import render, redirect
from TCCApp.forms import UsersForm
# Create your views here.

def home(request):
	return render(request,'main.html',{})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html', data)

def docad(request):
	form = UsersForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cadastro')

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
