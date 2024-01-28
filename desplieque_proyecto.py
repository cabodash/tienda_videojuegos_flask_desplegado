import os, shutil, glob

ruta_origen = './'
ruta_angular = 'dist/angular/browser'
ruta_destino = 'z_archivos_desplegado'
ruta_templates = "templates"
ruta_css = "static/css"
ruta_js = "static/js"

# Asegurarse de que el directorio de destino principal existe
os.makedirs(ruta_destino, exist_ok=True)

for archivo in os.listdir(ruta_origen):
    if archivo in ['static', 'templates', 'model'] or archivo.endswith('.py'):
        ruta_completa = os.path.join(ruta_origen, archivo)
        destino_final = os.path.join(ruta_destino, archivo)
        
        # Verificar si el directorio de destino ya existe y eliminarlo si es necesario
        if os.path.exists(destino_final):
            if os.path.isdir(destino_final):
                shutil.rmtree(destino_final)
            else:
                os.remove(destino_final)
        
        # Copiar el árbol de directorios o archivo
        if os.path.isdir(ruta_completa):
            shutil.copytree(ruta_completa, destino_final)
        else:
            # Asegurarse de que el directorio donde se copiará el archivo exista
            os.makedirs(os.path.dirname(destino_final), exist_ok=True)
            shutil.copy(ruta_completa, destino_final)
    if archivo == 'angular':
        # Definir las rutas completas de origen y destino para los archivos específicos
        archivos_origen = {
            'index.html': os.path.join(ruta_origen, archivo, ruta_angular, 'index.html'),
            'styles.css': os.path.join(ruta_origen, archivo, ruta_angular, 'styles.css'),
            'main.js': os.path.join(ruta_origen, archivo, ruta_angular, 'main.js'),
            'polyfills.js': os.path.join(ruta_origen, archivo, ruta_angular, 'polyfills.js')
        }
        archivos_destino = {
            'index.html': os.path.join(ruta_destino, ruta_templates, 'index.html'),
            'styles.css': os.path.join(ruta_destino, ruta_css, 'styles.css'),
            'main.js': os.path.join(ruta_destino, ruta_js, 'main.js'),
            'polyfills.js': os.path.join(ruta_destino, ruta_js, 'polyfills.js')
        }
        
        # Crear los directorios de destino si no existen y copiar los archivos correspondientes
        for nombre_archivo, ruta_o in archivos_origen.items():
            ruta_d = archivos_destino[nombre_archivo]
            print(ruta_o)
            print(ruta_d)
            os.makedirs(os.path.dirname(ruta_d), exist_ok=True)
            shutil.copy(ruta_o, ruta_d)
