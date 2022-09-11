import sqlite3

class Registro_datos:

    def __init__(self):
        self.mi_conexion = None
        try:
            mi_conexion = sqlite3.connect(r"C:\Users\luis_\PycharmProjects\Python-PyQt5\PyQtDB.db")
        except Exception as ex:
            print(ex)


    ### Defino todos los métodos que contienen las queries ###


    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cursor = self.mi_conexion.cursor()
        sql = """INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD)
        VALUES('{}','{}','{}','{}','{}')""".format(codigo, nombre, modelo, precio, cantidad)
        cursor.execute(sql)
        self.mi_conexion.commit()
        cursor.close()

    def mostrar_productos(self):
        cursor = self.mi_conexion.cursor()
        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def buscar_productos(self, nombre_producto):
        cursor = self.mi_conexion.cursor()
        sql = "SELECT * from productos WHERE NOMBRE = {}".format(nombre_producto)
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def elimina_productos(self, nombre):
        cursor = self.mi_conexion.cursor()
        sql = "DELETE FROM productos WHERE NOMBRE = {}".format(nombre)
        cursor.execute(sql)
        eliminado = cursor.rowcount     # devuelve 0 o 1 si elimina o no la fila
        self.mi_conexion.commit()
        return eliminado

    def actualizar_productos(self, codigo, nombre, modelo, precio, cantidad):
        cursor = self.mi_conexion.cursor()
        sql = """UPDATE productos SET CODIGO =' {}', MODELO = '{}', PRECIO = '{}', CANTIDAD = '{}'
        WHERE NOMBRE = '{}' """.format(codigo, modelo, precio, cantidad, nombre)
        cursor.execute(sql)
        datos = cursor.rowcount
        self.mi_conexion.commit()
        cursor.close()
        return datos



#if __name__ == '__main__':
#    nuevo = Registro_datos()
#    nuevo.inserta_producto("123","luis","buezo","9990","1")
#    nuevo.buscar_productos("luis")
#    print(nuevo)
