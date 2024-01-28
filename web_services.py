from flask import Flask, jsonify, request, session, send_file
import model.repositorio_tienda as repo_tienda
from flask_session import Session
from app import app
import os
import re
ruta_webservices = "/web-services/"


@app.route(f"{ruta_webservices}")
def ws():
    return "web service de python en funcionamiento"



@app.route(f"{ruta_webservices}obtener-videojuegos", methods = ["POST"])
def ws_obtener_videojuegos():
    #Comprobamos si viene algun parametro de busqueda
    if request.get_json():
        busqueda = request.get_json()["busqueda"]
    else:
        busqueda = None
    return jsonify(repo_tienda.obtener_videojuegos(busqueda))



@app.route(f"{ruta_webservices}obtener-videojuego-id/<int:id>")
def ws_obtener_videojuego_id(id):
    return jsonify(repo_tienda.obtener_videojuego_por_id(id))



@app.route(f'{ruta_webservices}obtener-productos-carrito')
def obtener_productos_carrito():
    return jsonify(repo_tienda.obtener_productos_carrito(session["productos"]))


@app.route(f"{ruta_webservices}agregar-al-carrito", methods = ["POST"])
def ws_agregar_al_carrito():
    # no podemos modificar directamente listas o colecciones
    # o elemento similares en la sesion, la sesion es muy especial
    # en flask, y es mejor actualizar sus datos de la siguiente manera:
    id = request.get_json()["id"]
    cantidad = request.get_json()["cantidad"]
    if "productos" not in session:
        session["productos"] = []
    productos = session["productos"]

    encontrado = False
    for p in productos:
        if p["id_producto"] == id:
            encontrado = True
            p["cantidad_producto"] += cantidad

    if not encontrado:
        producto = {
            "id_producto": id,
            "cantidad_producto": cantidad
        }
        productos.append(producto)
    session["productos"] = productos
    print(session)
    return jsonify(["ok"])



@app.route(f'{ruta_webservices}borrar-producto', methods = ["POST"])
def borrar_producto():
    id = request.get_json()["id"]
    if "productos" in session:
        productos = session["productos"]
        for p in productos:
            if p["id_producto"] == id:
                productos.remove(p)
        session["productos"] = productos
    return jsonify("ok")


@app.route(f"{ruta_webservices}vaciar-carrito")
def ws_vaciar_carrito():
    session.clear()
    return jsonify(["ok"])



@app.route(f"{ruta_webservices}registrar-pedido", methods = ["POST"])
def realizar_pedido():
    pedido = request.get_json()
    nombre = pedido["nombre"]
    apellidos = pedido["apellidos"]
    direccion = pedido["direccion"]
    tarjeta = pedido["tarjeta"]
    comentario = pedido["comentario"]
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    repo_tienda.registrar_pedido(nombre, apellidos, direccion, tarjeta, comentario, ip, user_agent, session["productos"])
    return jsonify(["ok"])





