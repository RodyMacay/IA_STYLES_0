from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuarios
from .forms import Register_user, Login_user
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.sessions.models import Session


@csrf_protect
def Login(request):
    mensaje_error = ''
    if request.method == 'POST':
        try:
            nomusuario = request.POST['nomusuario']
            contra = request.POST['contra']
        except MultiValueDictKeyError:
            mensaje_error = 'Campos de formulario incompletos.'
            return render(request, 'login.html', {'mensaje_error': mensaje_error})

        try:
            user = Usuarios.objects.get(nomusuario=nomusuario)
            print(user)
            if user.check_password(contra):
                login(request, user)
                next_url = request.POST.get('next') or '/'
                print(next_url, 'recibido desde POST')
                # La contraseña es válida, redirige al usuario a la página de inicio.
                return redirect(next_url)
            else:
                mensaje_error = 'Contraseña incorrecta.'
                print('Contraseña incorrecta.')
        except Usuarios.DoesNotExist:
            mensaje_error = 'El usuario no existe.'
            print('Usuario no existe.')



    next_url = request.GET.get('next')
    print('la url es \n', next_url)
    return render(request, 'login.html', {
        'mensaje_error': mensaje_error,
        'next': next_url
    })

@csrf_protect
def Registro(request):
    form = Register_user()
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['contra'])
            user.save()
            return redirect('login')

    return render(request, 'registro.html', {'form': form})



