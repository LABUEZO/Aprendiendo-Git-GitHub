from connect_sqlite import Conexion
import crypt

class Loggin:

    def __init__(self):
        self.conn = Conexion()
        self.opcion = None

    def opciones(self):
        print("""
        [1]. Crear una Cuenta.
        [2]. Logearse.""")
        self.opcion = int(input("Debe elegir una opción: "))
        return self.opcion

    def acc_or_log(self):
        if self.opcion == 1:
            username = str(input("Ingrese un nombre de usuario nuevo: "))
            password = str(input("Ingrese una contraseña nueva: "))
            self.conn.insertar(username, password)

        elif self.opcion == 2:
            username = input("Ingrese el Usuario: ")
            password = input("Ingrese la contraseña: ")
            self.conn.acceder(username, password)

        else:
            print("Debe elegir una opción.")




