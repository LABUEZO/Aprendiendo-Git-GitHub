import sqlite3

class Comunicacion:
    def __init__(self):
        self.conexion = sqlite3.connect("base_datos_login2.db")
        print("conexion_sqlite:Comunicacion: conexion establecida con la BD")
        # https://www.w3resource.com/python-exercises/sqlite/python-sqlite-exercise-6.php

    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        print("inserta_producto: se crea cursor")
        bd = "INSERT INTO tabla_datos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) VALUES (?, ?, ?, ?, ?)"
        data = (codigo, nombre, modelo, precio, cantidad)
        cursor.execute(bd, data)
        print("inserta_producto: se ejecuta query bd")
        self.conexion.commit()
        cursor.close()
        print("datos insertados en la BD")

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        bd = "SElECT * FROM tabla_datos"
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_productos(self, nombre_producto):
        cursor = self.conexion.cursor()
        print("busca_productos: se crea cursor")
        bd = """ SELECT * FROM tabla_datos WHERE NOMBRE = {}""".format(nombre_producto)
        cursor.execute(bd)
        print("busca_productos: se ejecuta query Select")
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX

    def elimina_productos(self, nombre):
        cursor = self.conexion.cursor()
        print("conexion_sqlite:elimina_productos: dato a borrar: {}".format(nombre))
        bd = """ DELETE FROM tabla_datos WHERE NOMBRE = {} """.format(nombre)
        cursor.execute(bd)
        print("conexion_sqlite:elimina_productos: datos borrados de la BD")
        self.conexion.commit()
        cursor.close()

    def actualiza_productos(self, id, codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = """ UPDATE tabla_datos SET CODIGO ='{}', NOMBRE='{}', MODELO='{}', PRECIO='{}', CANTIDAD='{}' WHERE ID='{}' """.format(codigo, nombre, modelo, precio, cantidad, id)
        cursor.execute(bd)
        print("conexion_sqlite:actualiza_productos: query ejecutada correctamente.")
        a = cursor.rowcount # Devuelve 1 si actualizó correctamente. sino devuelve 0
        self.conexion.commit()
        cursor.close()
        return a
