from flask import Flask, render_template, request, redirect, url_for
import model.repositorio_tienda as repo_tienda
from app import app
import os

ruta_admin = "/admin"


#-----   Rutas Administracion   -----#
@app.route(f"{ruta_admin}/")
def inicio_admin():
    return render_template("index_admin.html")

@app.route(f"{ruta_admin}/registrar-videojuego")
def registrar_videojuego():
    return render_template("registrar_videojuego.html")

@app.route(f"{ruta_admin}/guardar-nuevo-videojuego", methods=["POST"])
def guardar_nuevo_videojuego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    plataforma = request.form["plataforma"]
    genero = request.form["genero"]
    desarrollador = request.form["desarrollador"]
    fecha_lanzamiento = request.form["fecha_lanzamiento"]
    imagen_vj = request.files["fotoPortada"]
    id_videojuego = repo_tienda.registrar_videojuego(nombre, descripcion , precio , plataforma, genero, desarrollador, fecha_lanzamiento)
    # Guardar la foto
    ruta_actual = os.path.dirname(__file__)
    # Sacar la extension de la foto
    extension = os.path.splitext(imagen_vj.filename)[1]
    ruta_img = os.path.join(ruta_actual, 'static/img', f'{id_videojuego}{extension}')
    imagen_vj.save(ruta_img)
    return render_template("registrar_videojuego_ok.html")

@app.route(f"{ruta_admin}/listar-videojuegos")
def listar_videojuegos():
    videojuegos_bd = repo_tienda.obtener_videojuegos()
    return render_template("listado_videojuegos.html", videojuegos = videojuegos_bd)

@app.route(f"{ruta_admin}/borrar-videojuego/<int:id>")
def borrar_videojuego(id):
    print(f"[i] -Borrar videojuego con id: {id}")
    # Borrar la imagen asociada al videojuego si existe
    ruta_actual = os.path.dirname(__file__)
    for extension in ['.jpg', '.png', '.jpeg', '.gif', '.webp']:
        ruta_imagen = os.path.join(ruta_actual, 'static/img', f'{id}{extension}')
        if os.path.isfile(ruta_imagen):
            os.remove(ruta_imagen)
            print(f"[i] -Borrando imagen para el videojuego con id: {id}, y extension: {extension}")
            break
        else:
            print(f"[i] -No se encontró imagen para el videojuego con id: {id}, y extension: {extension}")
    # Borrar el videojuego de la base de datos
    repo_tienda.borrar_videojuego(id)
    return redirect(url_for("listar_videojuegos"))


@app.route(f"{ruta_admin}/listar-pedidos")
def listar_pedidos():
    pedidos_completo = repo_tienda.obtener_pedidos()
    return render_template("listar_pedidos.html", pedidos = pedidos_completo)



