# Ejemplo de uso de una bd mysql con python

import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "bd_tienda_flask"
    )
    if conexion:
        print("[i] -conexion ok")
        return conexion
    else: 
        print("[e] -No se pudo conectar con la base de datos, comprueba los datos de conexion")

if __name__ == "__main__":
    conexion = conectar()
    sql = "select * from videojuegos"
    cur = conexion.cursor(dictionary = True)
    cur.execute(sql)
    videojuegos = cur.fetchall()
    print("Videojuegos de la tienda: ")
    print(videojuegos)
    conexion.close()