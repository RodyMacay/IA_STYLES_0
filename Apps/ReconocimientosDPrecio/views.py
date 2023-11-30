import cv2
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import DetalleIAForm
from Apps.ReconocimientosDPrecio.models import Imagenes
from Apps.Usuario.models import Perfil
from django.shortcuts import get_object_or_404
import os
from ..IA_models.procesamiento import prediccion_prenda
from ..PublicacionDprendas.models import Publicacion


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
        print(f'Imagen guardada correctamente: {nuevaImg.ImagenDprenda}')
        return redirect('detalleIA', imagen_id = nuevaImg.id)
    return render(resquest, 'vender.html')


def DetalleIA (request, imagen_id):
    imagen = get_object_or_404(Imagenes, id=imagen_id)
    image_path = os.path.join('media', str(imagen.ImagenDprenda))
    print(imagen)
    form = ""
    prediction_result = prediccion_prenda(image_path)
    if request.method == 'POST':
        form = DetalleIAForm(request.POST)
        if form.is_valid():
            detalles = form.save(commit=False)
            detalles.imagen_id=imagen_id
            detalles.save()
            New_publicacion=Publicacion (DetalleIA=detalles)
            New_publicacion.save()
            messages.success(request, 'DETALLES ENVIADOS EXITOSAMENTE.')
            return redirect('inicio')
        else:
            print('error')
    else:
        print('error')
    return render(request,'DetalleIA.html', {
        'imagen': imagen,
        'resultado_prediccion': prediction_result,
        'form': form
    })
