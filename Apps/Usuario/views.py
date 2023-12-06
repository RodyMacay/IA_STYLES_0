from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Usuario, Perfil
from .forms import Register_user, Login_user, UpdateUsuarioForm,UpdatePerfilform
from django.db import IntegrityError

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

def PerfilUser (request):
    perfil = get_object_or_404(Perfil,usuario=request.user)
    print(perfil)
    return render(request, 'Usuario/perfil.html', {
        'datos':perfil
    })
def Editar_perfil(request):
    form_perfil = ''
    form_usuario = ''
    perfil = get_object_or_404(Perfil, usuario=request.user)

    if request.method == 'POST':
        form_perfil = UpdatePerfilform(request.POST, request.FILES, instance=perfil)
        form_usuario = UpdateUsuarioForm(request.POST, instance=request.user)

        if form_perfil.is_valid() and form_usuario.is_valid():
            datos_perfil = form_perfil.save(commit=False)
            datos_perfil.usuario = request.user
            datos_perfil.save()

            datos_usuario = form_usuario.save()

            # Actualizar manualmente el username en el perfil
            perfil.usuario.username = datos_usuario.username
            perfil.usuario.save()

            return redirect('perfil')

    else:
        form_perfil = UpdatePerfilform(instance=perfil)
        form_usuario = UpdateUsuarioForm(instance=request.user)

    return render(request, 'Usuario/editar_perfil.html', {
        'perfil': perfil,
        'form_perfil': form_perfil,
        'form_usuario': form_usuario,
    })