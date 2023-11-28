from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Usuario
from .forms import Register_user, Login_user

def Login(request):
    mensaje_error = ''
    if request.method == 'POST':
        form = Login_user(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or '/'
                return redirect(next_url)
            else:
                mensaje_error = 'Credenciales inválidas.'
    else:
        form = Login_user()

    return render(request, 'Usuario/login.html', {'form': form, 'mensaje_error': mensaje_error})

from django.contrib.auth import authenticate, login
from .forms import Register_user

def Registro(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            # Verifica si el correo electrónico ya está registrado
            if Usuario.objects.filter(correo=form.cleaned_data['correo']).exists():
                form.add_error('correo', 'Este correo electrónico ya está registrado.')
            else:
                # Utiliza 'password1' para establecer la contraseña del usuario
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()

                # Autentica y realiza el inicio de sesión
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)

                return redirect('login')
    else:
        form = Register_user()
        print('hubo un error')
    return render(request, 'Usuario/registro.html', {'form': form})

def Perfil (request):
    return render(request, 'Usuario/perfil.html')
