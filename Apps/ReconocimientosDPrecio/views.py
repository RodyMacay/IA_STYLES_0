from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from Apps.ReconocimientosDPrecio.models import Imagenes
from Apps.Usuario.models import Perfil
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_protect
def Vender(resquest):
    perfil = get_object_or_404(Perfil, usuario=resquest.user)
    if resquest.method == 'POST':
        new_img = resquest.FILES.get('ImagenDprenda')
        if not new_img:
            # Si no se seleccionó ninguna imagen, muestra un mensaje de error
            messages.error(resquest, 'Debe seleccionar al menos una imagen.')
            return redirect('vender')
        nuevaImg = Imagenes(usuario=perfil, ImagenDprenda=new_img)
        nuevaImg.save()
        return redirect('detalleIA', imagen_id = nuevaImg.id)
    return render(resquest, 'vender.html')

def DetalleIA (request, imagen_id):
    imagen = get_object_or_404(Imagenes, id=imagen_id)

    return render(request,'DetalleIA.html', {
        'imagen': imagen})
