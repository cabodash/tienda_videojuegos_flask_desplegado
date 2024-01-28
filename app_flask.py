from flask import Flask, render_template, request, redirect, url_for, send_file
import model.repositorio_tienda as repo_tienda
from flask_session import Session
import os

from app import app

#-----   Ruta de Inicio o raiz   -----#
@app.route("/")
def inicio():
    return render_template("index.html")


# Importa los módulos que definen las rutas después de crear la aplicación
import admin
import web_services
import video_service
import image_service

app.run(debug=True)