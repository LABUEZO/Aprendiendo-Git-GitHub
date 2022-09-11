from PyQt5 import QtWidgets
from messagebox import msg_about, msg_error
import sqlite3 as sql
import form as forma
import ventana1 as login
import ventana2 as entrar

# iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar archivos .ui
#login= uic.loadUi("ventana1.ui")
#entrar= uic.loadUi("ventana2.ui")
#forma = uic.loadUi("form.ui")

try:
    con = sql.connect("base de datos.db")
    con.commit()
    con.close()
except:
    print("Error en la base de datos...")

def gui_login():
    name = login.lineEdit.text()
    password = login.lineEdit_2.text()

    if len(name)==0 or len(password)==0:
        login.label_5.setText("Ingrese todos los datos")
    else:
        con = sql.connect("base de datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT nombre, contraseña FROM usuarios WHERE nombre = ? AND contraseña = ?',(name, password))
        if cursor.fetchall():
            gui_entrar()
        else:
            msg_error("Error", "El usuario o la contraseña no son correctas")





def crear_tabla():
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS usuarios (
            nombre text,
            apellido_paterno text,
            apellido_materno text,
            edad integer,
            sexo text,
            celular integer,
            correo text, 
            contraseña text
            )"""
    )
    con.commit()
    con.close()


def registrar(nombre, ap, am, edad, sex, cel, mail, contrasenia):
    con = sql.connect("base de datos.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{nombre}', '{ap}', '{am}'," \
                  f"'{edad}', '{sex}', '{cel}', '{mail}', '{contrasenia}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombre = forma.line_nombre.text()
    apellido_p = forma.line_ap.text()
    apellido_m = forma.line_am.text()
    edad = int(forma.line_edad.text())
    box = str(forma.comboBox.currentText())
    celular = int(forma.line_cel.text())
    correo = forma.line_correo.text()
    contraseña = forma.line_contra.text()
    contraseña_2 = forma.line_contra_2.text()
    if contraseña != contraseña_2:
        msg_error("Error", "Las contraseñas no son iguales...")
    elif len(str(celular)) != 10:
        msg_error("Error", "El número de celular debe contener 10 dígitos")
    elif contraseña == contraseña_2:
        registrar(nombre, apellido_p, apellido_m, edad, box, celular, correo, contraseña)
        msg_about("Éxito!", "Se ha registrado exitosamente! \n Tu nombre es tu usuario")
        forma.line_nombre.setText("")
        forma.line_ap.setText("")
        forma.line_am.setText("")
        forma.line_edad.setText("")
        forma.line_cel.setText("")
        forma.line_correo.setText("")
        forma.line_contra.setText("")
        forma.line_contra_2.setText("")


def gui_entrar():
    login.hide()
    entrar.show()

def gui_registrar():
    login.hide()
    forma.show()
    crear_tabla()

def regresar_forma():
    forma.hide()
    login.show()

def regresar_entrar():
    entrar.hide()
    login.label_5.setText("")
    login.show()

def salir():
    app.exit()

# Botones de login
login.pushButton.clicked.connect(gui_login)
login.pushButton_3.clicked.connect(gui_registrar)
login.pushButton_2.clicked.connect(salir)

# Botones de entrar
entrar.pushButton.clicked.connect(regresar_entrar)
entrar.pushButton_2.clicked.connect(salir)

# Botones de form
forma.btn_regresar.clicked.connect(regresar_forma)
forma.btn_registrar.clicked.connect(datos)

# Ejecutable
login.show()
app.exec()