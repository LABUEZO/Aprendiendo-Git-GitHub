import time
import sys
from PyQt5.QtWidgets import QTableWidgetItem
from conexionBD import *
from vista import *


class MiApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # Defino objeto con la Clase de vista que es Ui_Form
        self.ui = Ui_Form()
        self.ui.setupUi(self)   # método de la clase Ui_Form
        # Defino objeto con la Clase de conexionBD que es Registro_datos
        self.datosTotal = Registro_datos()

        # botones con los métodos asignados
        self.ui.btn_actualizar.clicked.connect(self.m_productos)
        self.ui.btn_agregar.clicked.connect(self.insertar_productos)
        self.ui.btn_buscar.clicked.connect(self.buscar_producto)
        self.ui.btn_delete.clicked.connect(self.eliminar_producto)
        self.ui.btn_agregar_2.clicked.connect(self.modificar_producto)

        # Dimensión de tabla del menú PRODUCTO
        self.ui.tabla_producto.setColumnWidth(0, 98)
        self.ui.tabla_producto.setColumnWidth(1, 100)
        self.ui.tabla_producto.setColumnWidth(2, 98)
        self.ui.tabla_producto.setColumnWidth(3, 98)
        self.ui.tabla_producto.setColumnWidth(4, 98)
        # Dimensión de tabla del menú BORRAR PRODUCTO
        self.ui.tabla_delete.setColumnWidth(0, 98)
        self.ui.tabla_delete.setColumnWidth(1, 100)
        self.ui.tabla_delete.setColumnWidth(2, 98)
        self.ui.tabla_delete.setColumnWidth(3, 98)
        self.ui.tabla_delete.setColumnWidth(4, 98)
        # Dimensión de tabla del menú BUSCAR PRODUCTO
        self.ui.tabla_buscar.setColumnWidth(0, 98)
        self.ui.tabla_buscar.setColumnWidth(1, 100)
        self.ui.tabla_buscar.setColumnWidth(2, 98)
        self.ui.tabla_buscar.setColumnWidth(3, 98)
        self.ui.tabla_buscar.setColumnWidth(4, 98)

    # Método para btn_actualizar del Menú PRODUCTOS
    def m_productos(self):
        # Defino una variable que traiga una query SELECT del método buscar_productos()
        datos = self.datosTotal.buscar_productos()
        filas = len(datos)  # len trae la cantidad de filas

        self.ui.tabla_producto.setRowCount(filas)
        tablerow = 0
        for row in datos:   # ubicamos los datos en cada columna de la tabla_producto
            self.ui.tabla_producto.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_producto.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_producto.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_producto.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_producto.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    # Método para btn_agregar del Menú AGREGAR PRODUCTO
    def insertar_productos(self):
        codigo = self.ui.line_codigo.text()
        nombre = self.ui.line_nombre.text()
        modelo = self.ui.line_modelo.text()
        precio = self.ui.line_precio.text()
        cantidad = self.ui.line_cantidad.text()
        # Pasar estas variables como atributos al método inserta_producto de conexionBD
        self.datosTotal.inserta_producto(codigo, nombre, modelo, precio, cantidad) # datos insertados en base de datos
        # Limpiar los QLineEdit de la vista
        self.ui.line_codigo.clear()
        self.ui.line_nombre.clear()
        self.ui.line_modelo.clear()
        self.ui.line_precio.clear()
        self.ui.line_cantidad.clear()

    # Método para btn_agregar_2 del Menú ACTUALIZAR PRODUCTO
    def modificar_producto(self):
        # Capturo en una variable los datos del QLineEdit line_busqueda
        id_producto = self.ui.line_busqueda.text()  # QLineEdit del Menú ACTUALIZAR PRODUCTO
        id_producto = str("'" + id_producto + "'")
        # traer de la base de datos el id_producto
        nombre_prod = self.datosTotal.buscar_productos(id_producto)

        if nombre_prod != None:
            self.ui.btn_busqueda.setText("ACTUALIZAR")
            # capturar los datos de los QLineEdit
            codigoM = self.ui.line_codigo_2.text()
            nombreM = self.ui.line_nombre_2.text()
            modeloM = self.ui.line_modelo_2.text()
            precioM = self.ui.line_precio_2.text()
            cantidadM = self.ui.line_cantidad_2.text()
            # Actualizar en la base de datos
            act_bd = self.datosTotal.actualizar_productos(codigoM,nombreM,modeloM,precioM,cantidadM)
            if act_bd == 1:     # actualizar_productos devuelve un datos = cursor.rowcout
                self.ui.btn_busqueda.setText("ACTUALIZADO")
                # vaciar todos los QLineEdit
                self.ui.line_codigo_2.clear()
                self.ui.line_nombre_2.clear()
                self.ui.line_modelo_2.clear()
                self.ui.line_precio_2.clear()
                self.ui.line_cantidad_2.clear()
                self.ui.line_busqueda.clear()
                time.sleep(10)
                self.ui.btn_busqueda.text("BUSQUEDA")

            elif act_bd == 0:
                self.ui.btn_busqueda.setText("ERROR")
            else:
                self.ui.btn_busqueda.setText("INCORRECTO")
        else:
            self.ui.btn_busqueda.setText("NO EXISTE")

    # Método para btn_buscar del Menú BUSCAR PRODUCTO
    def buscar_producto(self):
        # capturar text del QLineEdit en Menú BUSCAR PRODUCTO
        nombre_producto = self.ui.lineEdit.text()
        nombre_producto = str("'" + nombre_producto + "'")
        # buscar en la base de datos el texto capturado
        datosB = self.datosTotal.buscar_productos(nombre_producto)
        fila = len(datosB)  # cantidad de filas que devuelve
        self.ui.tabla_buscar.setRowCount(fila)
        tablerow = 0
        for row in datosB:      # ubicamos los datos en cada columna de la tabla_buscar
            self.ui.tabla_buscar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_buscar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_buscar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_buscar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_buscar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    # Método para btn_delete del Menú BORRAR PRODUCTO
    def eliminar_producto(self):
        # capturar text del QLineEdit en Menú BORRAR PRODUCTO
        eliminar = self.ui.line_delete.text()
        eliminar = str("'" + eliminar + "'")
        # buscar en la base de datos el texto capturado y lo borra
        datosD = self.datosTotal.elimina_productos(eliminar)
        # buscamos los datos nuevamente de la BD
        datosB = self.datosTotal.buscar_productos()
        fila = len(datosB)
        self.ui.tabla_delete.setRowCount(fila)
        tablerow = 0
        for row in datosB:      # ubicamos los datos en cada columna de la tabla_delete
            self.ui.tabla_delete.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tabla_delete.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tabla_delete.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tabla_delete.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tabla_delete.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

        if datosD == None:
            self.ui.btn_borrado.setText("NO EXISTE")
        elif datosD == 0:
            self.ui.btn_borrado.setText("NO EXISTE")
        else:
            self.ui.btn_borrado.setText("SE ELIMINÓ")



