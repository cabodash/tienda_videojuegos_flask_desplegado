from flask import send_file
from app import app
import os

ruta_imagenes = "/imagen-videojuego/"

#Ruta que devuelve la imagen del videojuego por su id
@app.route(f"{ruta_imagenes}/<string:nombre>", methods=['GET'])
def obtener_imagen(nombre):
    ruta_actual = os.path.dirname(__file__)
    for extension in ['.jpg', '.png', '.jpeg', '.gif', '.webp']:
        ruta_imagen = os.path.join(ruta_actual, 'static/img/videojuegos', f'{nombre}{extension}')
        if os.path.isfile(ruta_imagen):
            return send_file(ruta_imagen, mimetype='image/ *')
    return "Imagen no encontrada", 404