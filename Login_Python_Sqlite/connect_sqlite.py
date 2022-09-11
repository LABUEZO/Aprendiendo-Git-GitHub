import sqlite3
import os

class Conexion:

    def __init__(self):
        if os.path.exists("accounts.db"):
            self.conn = sqlite3.connect("accounts.db")
            print("Conexion establecida.")
        else:
            self.conn = sqlite3.connect("accounts.db")
            self.conn.execute("""CREATE TABLE `login` (`USER` TEXT NOT NULL UNIQUE, `PASSWORD` TEXT NOT NUL)""")
            print("Conexion creada.")


    def insertar(self, username, password):
        try:
            sql = "INSERT INTO login(USER, PASSWORD) VALUES('{}','{}')".format(username, password)
            self.conn.execute(sql)
            self.conn.commit()
            self.conn.close()
            print("La cuenta ha sido creada correctamente!")
        except Exception as e:
            print("Error al almacenar los datos: {}".format(e))

    def acceder(self, username, password):
        sql = "SELECT * FROM login WHERE (USER=? and PASSWORD=?)"
        data = self.conn.execute(sql, [username, password])
        if(data.fetchone()) == None:
            print("Datos incorrectos.")
        else:
            print("Login Exitoso!")



#if __name__ == '__main__':
#    nuevo = Conexion()
#    nuevo.insertar("vanesaflores, Vaju3965")
#    print(type(nuevo))