from flask import send_file
from app import app
import os

ruta_videos = "/video-videojuego/"

#Ruta que devuelve el video del videojuego por su id
@app.route(f"{ruta_videos}/<string:nombre>", methods=['GET'])
def obtener_video(nombre):
    ruta_actual = os.path.dirname(__file__)
    for extension in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.webm']:
        ruta_video = os.path.join(ruta_actual, 'static/vid/videojuegos', f'{nombre}{extension}')
        if os.path.isfile(ruta_video):
            return send_file(ruta_video, mimetype='video/*')
    return "Video no encontrado", 404
