import json

from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision_v1p3beta1 import types
from googletrans import Translator


def prediccion_prenda_vision(imagen_path):
    # Configura el cliente de la API de Google Vision
    credenciales_path = 'C:\IA_STYLES_0\APIKEY.json'
    cliente_vision = vision.ImageAnnotatorClient.from_service_account_file(credenciales_path)

    # Carga la imagen desde el archivo
    with open(imagen_path, 'rb') as imagen_archivo:
        contenido_imagen = imagen_archivo.read()

    # Crea una instancia de la clase Image
    imagen_google = types.Image(content=contenido_imagen)

    # Realiza la solicitud de análisis de imagen
    respuesta = cliente_vision.label_detection(image=imagen_google)

    # Procesa los resultados
    labels = [label.description for label in respuesta.label_annotations]
    print(labels)
    # Lógica para obtener color, tipo, descripción, etc.
    color = obtener_color(['White', 'Product', 'Dress shirt', 'Sleeve', 'Baby & toddler clothing', 'Collar', 'Button', 'Font', 'Pattern', 'T-shirt'])
    tipo = obtener_tipo(labels)
    descripcion = 'Descripción predeterminada'  # Puedes implementar la lógica para obtener la descripción
    precio = estimar_precio(imagen_path)
    talla = 0  # Puedes implementar la lógica para obtener la talla
    marca = ''  # Puedes implementar la lógica para obtener la marca
    estado = estimar_estado(labels)
    print(tipo)
    print(color)
    return {
        'color': color,
        'tipo': tipo,
        'descripcion': descripcion,
        'precio': precio,
        'talla': talla,
        'marca': marca,
        'estado': estado,
    }


def obtener_color(labels):
    # Puedes definir un diccionario de mapeo de etiquetas a colores

    try:
        # Traduce cada etiqueta y agrega el resultado a una lista

        mapeo_colores = {
            'rojo': 'Rojo',
            'azul': 'Azul',
            'verde': 'Verde',
            # Agrega más mapeos según sea necesario
        }

        # Encuentra la primera etiqueta que tenga un mapeo a color
        for label in mapeo_colores:
            if label.lower() in mapeo_colores:
                return mapeo_colores[label.lower()]

    except Exception as e:
        print(f"Error al traducir etiquetas: {e}")

    # Si no se encuentra ningún mapeo o hay un error, devuelve 'Desconocido'
    return 'Desconocido'

def obtener_tipo(labels):
    # Cargar el mapeo de tipos desde el archivo JSON
    with open('tipo.json', 'r') as file:
        mapeo_tipos = json.load(file)

    # Iterar sobre cada palabra en la descripción
    for palabra in labels:
        palabra_lower = palabra.lower()

        # Buscar directamente la palabra clave en lugar de contar ocurrencias
        for tipo, keywords in mapeo_tipos.items():
            for keyword in keywords:
                if keyword.lower() == palabra_lower:
                    # Imprimir la palabra clave encontrada y salir del bucle
                    print(keyword.lower())
                    return

    # Imprimir 'Desconocido' si no se encuentra ninguna palabra clave
    print('Desconocido')



def estimar_precio(imagen_path):
    # Puedes utilizar algún método para estimar el precio, como el tamaño de la imagen, colores, etc.
    # Esta es una implementación de ejemplo basada en el tamaño de la imagen
    import os

    tamano_imagen = os.path.getsize(imagen_path)  # Obtén el tamaño en bytes
    precio_estimado = tamano_imagen / 1024  # Estimación simple, puedes ajustar según tus necesidades

    return precio_estimado

def estimar_estado(labels):
    # Puedes utilizar algún método para estimar el estado, como la presencia de etiquetas específicas, colores oscuros, etc.
    # Esta es una implementación de ejemplo basada en la presencia de la palabra 'oscuro' en las etiquetas
    for label in labels:
        if 'oscuro' in label.lower():
            return 'Usado'

    # Si no se encuentra ninguna indicación, devuelve 'Nuevo'
    return 'Nuevo'
