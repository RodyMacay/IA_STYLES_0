from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from Apps.ReconocimientosDPrecio.forms import ImagenForm
from Apps.Usuario.models import Perfil
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_protect
def Vender(resquest):
    perfil = get_object_or_404(Perfil, usuario=resquest.user)
    form = ImagenForm()

    if resquest.method == 'POST':
        form = ImagenForm(resquest.POST, resquest.FILES)
        if form.is_valid():
            new_img = form.save(commit=False)
            new_img.idperfil = perfil
            new_img.save()
            return redirect('vender')

    return render(resquest, 'vender.html', {'form': form})

