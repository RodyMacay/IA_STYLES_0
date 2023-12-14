import cv2
from googletrans import Translator
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image


def quitar_fondo(imagen):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral para obtener una máscara de fondo
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # Encontrar el contorno del objeto
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una máscara para el objeto
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, contours, 0, (255), thickness=cv2.FILLED)

    # Extraer el objeto de la imagen original usando la máscara
    resultado = cv2.bitwise_and(imagen, imagen, mask=mask)

    return resultado


def clasificar_color(imagen_sin_fondo):
    # Convertir la imagen sin fondo a espacio de color HSV
    img = cv2.cvtColor(imagen_sin_fondo, cv2.COLOR_BGR2HSV)

    # Calcular el color dominante
    color_dominante = np.mean(img, axis=(0, 1))

    return color_dominante


def obtener_nombre_color(color_clasificado):
    # Mapear los valores HSV a nombres de colores
    nombre_colores = {
        'rojo': ([0, 100, 100], [10, 255, 255]),
        'rojo_oscuro': ([160, 100, 100], [180, 255, 255]),
        'verde': ([40, 40, 40], [80, 255, 255]),
        'azul': ([100, 40, 40], [140, 255, 255]),
        'blanco': ([0, 0, 200], [180, 50, 255]),
        'negro': ([0, 0, 0], [180, 255, 30]),
        'amarillo': ([20, 100, 100], [40, 255, 255]),
        'naranja': ([10, 100, 100], [20, 255, 255]),
        'rosa': ([140, 100, 100], [160, 255, 255]),
        'morado': ([120, 40, 40], [140, 255, 255]),
        'marron': ([0, 60, 60], [30, 255, 255]),
        'gris': ([0, 0, 80], [180, 20, 200]),
        'cafe': ([10, 60, 60], [30, 160, 160]),
    }

    # Verificar el color clasificado
    for nombre, (lower, upper) in nombre_colores.items():
        if np.all(color_clasificado >= lower) and np.all(color_clasificado <= upper):
            return nombre

    # Si no se encuentra un color específico, devolver 'Desconocido'
    return 'Desconocido'

def cargar_modelo():
    return ResNet50(weights='imagenet')


def clasificar_tipo(imagen_path):
    img = image.load_img(imagen_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Usar el modelo_resnet directamente aquí
    predictions = modelo_resnet.predict(img_array)

    decoded_predictions = decode_predictions(predictions, top=1)[0]
    tipo_label = ""
    nombre_color = ""
    for imagenet_id, label, score in decoded_predictions:
        tipo_nombre_legible = ' '.join([word.capitalize() for word in label.split('_')])
        try:
            translator = Translator()
            descripcion_espanol = translator.translate(tipo_nombre_legible, src='en', dest='es')
            if descripcion_espanol.text:
                tipo_label = descripcion_espanol.text
            else:
                tipo_label = f"La respuesta de la traducción no es válida. Descripción predeterminada: {tipo_nombre_legible} color {nombre_color}"
        except Exception as e:
            tipo_label = f"Error al traducir: {e}. Descripción predeterminada: {tipo_nombre_legible} color {nombre_color}"
    return tipo_label, decoded_predictions[0][2]


def predecir_estado_y_precio(tipo_label):
    # Mapear tipos de prendas a estados y precios
    tipos_a_estados_y_precios = {
        'Vestido': {'estado': 'Nuevo', 'precio': 50},
        'Camiseta': {'estado': 'Usado', 'precio': 20},
        'Jersey': {'estado': 'Nuevo', 'precio': 30},
        # Agregar más tipos de prendas según sea necesario
    }

    # Obtener el estado y precio para el tipo de prenda clasificado
    if tipo_label in tipos_a_estados_y_precios:
        resultado = tipos_a_estados_y_precios[tipo_label]
    else:
        # Si el tipo de prenda no está en el mapeo, asignar un valor predeterminado
        resultado = {'estado': 'usado', 'precio': 0}

    return resultado

def prediccion_prenda(imagen_path):
    imagen_original = cv2.imread(imagen_path)
    imagen_sin_fondo = quitar_fondo(imagen_original)
    color_clasificado = clasificar_color(imagen_sin_fondo)
    nombre_color = obtener_nombre_color(color_clasificado)
    tipo_label, tipo_score = clasificar_tipo(imagen_path)

    tipo_nombre_legible = ' '.join([word.capitalize() for word in tipo_label.split('_')])
    translator = Translator()
    precio = 0
    talla = 0
    marca = ""
    estado_y_precio = predecir_estado_y_precio(tipo_label)

    try:
        descripcion_espanol = translator.translate(tipo_nombre_legible, src='en', dest='es')
        if descripcion_espanol.text:
            description = f"{descripcion_espanol.text} color {nombre_color}"
        else:
            description = f"La respuesta de la traducción no es válida. Descripción predeterminada: {tipo_nombre_legible} {nombre_color}"
    except Exception as e:
        description = f"Error al traducir: {e}. Descripción predeterminada: {tipo_nombre_legible} {nombre_color}"

    return {
        'color': nombre_color,
        'tipo': tipo_nombre_legible,
        'descripcion': description,
        'precio': estado_y_precio['precio'],
        'talla': talla,
        'marca': marca,
        'estado': estado_y_precio['estado'],
    }

modelo_resnet = cargar_modelo()