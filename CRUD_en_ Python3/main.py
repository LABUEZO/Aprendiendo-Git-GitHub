import sqlite3

import conexion as conn
from os import system
import time

# Conexión a la Base de Datos

db = conn.DB()


# Función de validación de DNI

def verif_dni(num_dni):
    if num_dni.isdigit() and len(num_dni) in [7, 8]:   # Si la cadena esta compuesta de numeros y mide 7 o 8 caracteres
        return True
    return False

def opcion_update():
    try:
        modificar = input("Qué opción desea modificar?: ")
        if(modificar == 'A' or modificar == 'a'):
            modificar = "DNI"
            dni = input("Escriba el DNI: ")
            if verif_dni(dni) is True:
                return dni, modificar
        elif (modificar == 'B' or modificar == 'b'):
            modificar = "NOMBRE"
            name = str(input("Escriba el NOMBRE: "))
            if(len(name) !=''):
                return name, modificar
        elif (modificar == 'C' or modificar == 'c'):
            modificar = "APELLIDO"
            last_name = str(input("Escriba el APELLIDO: "))
            if(len(last_name) !=''):
                return last_name, modificar
        elif (modificar == 'D' or modificar == 'd'):
            modificar = "EMAIL"
            email = str(input("Escriba el EMAIL: "))
            if(len(email) !=''):
                return email, modificar
        elif (modificar == 'E' or modificar == 'e'):
            modificar = "DIRECCION"
            address = str(input("Escriba la DIRECCION: "))
            if(len(address) !=''):
                return address
        elif (modificar == 'F' or modificar == 'f'):
            modificar = "LOCALIDAD"
            locate = str(input("Escriba la LOCALIDAD: "))
            if(len(locate) !=''):
                return locate, modificar
    except Exception as e:
        print("Error al ingresar los datos: {}".format(e))


# Funciones del CRUD

def create():
    dni = input("Escriba el DNI: ")
    if verif_dni(dni) is True:
        name = str(input("Escriba el nombre: "))
        last_name = str(input("Escriba el apellido: "))
        email = str(input("Escriba el email: "))
        address = str(input("Escriba la dirección: "))
        location = str(input("Escriba la Localidad: "))
        if(len(name) >0 and len(last_name) >0 and len(email) >0 and len(address) >0 and len(location) >0):
            sql = "INSERT INTO fichero(DNI, NOMBRE, APELLIDO, EMAIL, DIRECCION, LOCALIDAD) VALUES(?,?,?,?,?,?)"
            parametros = (dni, name, last_name, email, address, location)
            db.ejecutar_consulta(sql, parametros)
            print("Datos Insertados correctamente!")
        else:
            print("Al menos uno de los campos está vacío, debe completar todos los campos.")
    else:
        print(f'El DNI {dni} NO es Válido')

def read():
    datos = db.ejecutar_consulta("SELECT * FROM fichero")
    for data in datos:
        print("""
        DNI : {}
        NOMBRE : {}
        APELLIDO : {}
        EMAIL : {}
        DIRECCION : {}
        LOCALIDAD : {}""".format(data[0], data[1], data[2], data[3], data[4], data[5]))

def update():
    dni = search()
    print("""
    Elija qué celda modificar: 
    [A]. DNI
    [B]. NOMBRE
    [C]. APELLIDO
    [D]. EMAIL
    [E]. DIRECCION
    [F]. LOCALIDAD 
    """)
    dato_retornado = opcion_update()
    sql = "UPDATE fichero SET {}=? WHERE DNI=?".format(dato_retornado[1])
    parametros = (dato_retornado[0], dni)
    db.ejecutar_consulta(sql, parametros)
    print("Datos Actualizados correctamente!")


def delete():
    dni = input("Ingrese el DNI: ")
    if verif_dni(dni) is True:
        sql = "DELETE FROM fichero WHERE DNI=?"
        parametros = (dni,)
        db.ejecutar_consulta(sql, parametros)
        print("Datos Eliminados correctamente!")
    else:
        print(f'El DNI {dni} NO es Válido')

def search():
    dni = input("Escriba el DNI: ")
    if verif_dni(dni) is True:
        sql = "SELECT * FROM fichero WHERE DNI=?"
        parametros = (dni,)
        datos = db.ejecutar_consulta(sql, parametros)
        for data in datos:
            print("""
                    DNI : {}
                    NOMBRE : {}
                    APELLIDO : {}
                    EMAIL : {}
                    DIRECCION : {}
                    LOCALIDAD : {}""".format(data[0], data[1], data[2], data[3], data[4], data[5]))
            return data[0]
    else:
        print(f'El DNI {dni} NO es Válido')


# Programa

while True:
    print("=================================")
    print("\tCRUD EN PYTHON3")
    print("=================================")
    print("\t[1] Insertar registro")
    print("\t[2] Mostrar registros")
    print("\t[3] Actualizar registro")
    print("\t[4] Eliminar registro")
    print("\t[5] Buscar registro")
    print("\t[6] Salir")
    print("=================================")

    try:
        opcion = int(input("Seleccionar una opción: "))
        if(opcion == 1):
            create()
            time.sleep(2)
            system("cls")
        elif (opcion == 2):
            read()
        elif (opcion == 3):
            update()
            time.sleep(2)
            system("cls")
        elif (opcion == 4):
            delete()
            time.sleep(2)
            system("cls")
        elif (opcion == 5):
            search()
        elif(opcion == 6):
            break

    except sqlite3.IntegrityError:
        print("El DNI ya se encuentra registrado.")
    except Exception as e:
        print("ocurrió un Error: {}".format(e))





# fórmula sin usar, descartada.
"""
def update():
    dni = input("Ingrese el DNI: ")
    if verif_dni(dni) is True:
        name = str(input("Escriba el nombre: "))
        last_name = str(input("Escriba el apellido: "))
        email = str(input("Escriba el email: "))
        address = str(input("Escriba la dirección: "))
        location = str(input("Escriba la Localidad: "))
        if (len(name) > 0 and len(last_name) > 0 and len(email) > 0 and len(address) > 0 and len(location) > 0):
            sql = "UPDATE fichero SET NOMBRE=?, APELLIDO=?, EMAIL=?, DIRECCION=?, LOCALIDAD=? WHERE DNI=?"
            parametros = (name, last_name, email, address, location, dni)
            db.ejecutar_consulta(sql, parametros)
            print("Datos Actualizados correctamente!")
    else:
        print(f'El DNI {dni} NO es Válido')
"""
