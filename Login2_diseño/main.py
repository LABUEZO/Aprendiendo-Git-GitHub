import sys

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5.uic import loadUi
from conexion_sqlite import Comunicacion
#from GUI_login2 import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.signal_actualizar = None
        self.act_codigo = None
        self.base_datos_login2 = None
        self.tabla_borrar = None
        self.signal_eliminar = None
        self.line_eliminar_buscar = None
        loadUi('GUI_login2.ui', self)
        print("main:VentanaPrincipal: la GUI es ejecutada correctamente")


        # boton de menú lateral
        self.btn_menu.clicked.connect(self.mover_menu)
        self.base_datos = Comunicacion()

        # ocultar botones
        self.btn_restaurar.hide()
        # botones
        self.btn_refrescar.clicked.connect(self.mostrar_productos)
        self.btn_registrar.clicked.connect(self.registrar_productos)
        self.btn_buscar_actualizar.clicked.connect(self.buscar_por_nombre_actualiza)
        self.btn_actualizar.clicked.connect(self.modificar_productos)
        self.btn_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)
        self.btn_eliminar.clicked.connect(self.eliminar_producto)

        # control barra de titulos
        self.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.btn_restaurar.clicked.connect(self.control_btn_normal)
        self.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.btn_cerrar.clicked.connect(lambda: self.close())

        # eliminar barra de titulos - opacidad, ocultar menu lateral
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # SizeGrip: redimensiona ventana
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # conexion de botones
        self.btn_base_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.btn_nuevo_registro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.btn_actualizar_reg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.btn_eliminar_reg.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))

        # ancho de columna adaptable
        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # Métodos de la barra de títulos
    def control_btn_minimizar(self):
        self.showMinimized()

    def control_btn_normal(self):
        self.showNormal()
        self.btn_restaurar.hide()
        self.btn_maximizar.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.btn_maximizar.hide()
        self.btn_restaurar.show()

    # Método de SizeGrip para redimensionar
    def resizeEvent(self, event):   # event: argumento para redimensionar
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    # Método para mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.btn_restaurar.hide()
            self.btn_maximizar.show()
        else:
            self.showNormal()
            self.btn_restaurar.hide()
            self.btn_maximizar.show()

    # Metodo para mover el menu lateral izquierdo
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    # Configuración Página Base de datos
    def mostrar_productos(self):
        datos = self.base_datos.mostrar_productos()
        i = len(datos)
        self.tabla_productos.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.id = row[0]
            self.tabla_productos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_productos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_productos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_productos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_productos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1
            self.signal_actualizar.setText("")
            self.signal_registrar.setText("")
            self.signal_eliminar.setText("")

    # Metodo del btn_registrar
    def registrar_productos(self):
        codigo = self.reg_codigo.text().upper()  #QLineEdit
        nombre = self.reg_nombre.text().upper()
        modelo = self.reg_modelo.text().upper()
        precio = self.reg_precio.text().upper()
        cantidad = self.reg_cantidad.text().upper()
        # Condicional: si los QLabel indicadores no están vacíos, agregamos los datos a la BD
        if codigo != '' and nombre != '' and modelo != '' and precio != '' and cantidad != '':
            try:
                self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)
            except Exception as e:
                print(e)
            self.reg_codigo.clear()
            self.reg_nombre.clear()
            self.reg_modelo.clear()
            self.reg_precio.clear()
            self.reg_cantidad.clear()
            print("registros agregados y celdas vacias")
        else:
            self.signal_registrar.setText('Hay Espacios Vacíos.')

    # Metodo del btn_buscar_actualizar
    def buscar_por_nombre_actualiza(self):
        id_producto = self.line_actualizar_buscar.text().upper()
        id_producto = str("'" + id_producto + "'")
        print(id_producto)
        self.producto = self.base_datos.busca_productos(id_producto) # busca datos de la BD
        # condicional: si la BD retorna datos a self.producto, insertamos en los QLineEdit de Actualizar.
        if len(self.producto) != 0:
            self.id = self.producto[0][0]   # no se muestra este dato en la app
            self.act_codigo.setText(self.producto[0][1])
            self.act_nombre.setText(self.producto[0][2])
            self.act_modelo.setText(self.producto[0][3])
            self.act_precio.setText(self.producto[0][4])
            self.act_cantidad.setText(self.producto[0][5])
        else:
            self.signal_actualizar.setText("NO EXISTE")

    # Metodo del btn_actualizar
    def modificar_productos(self):
        if self.producto != '':
            codigo = self.act_codigo.text().upper()
            nombre = self.act_nombre.text().upper()
            modelo = self.act_modelo.text().upper()
            precio = self.act_precio.text().upper()
            cantidad = self.act_cantidad.text().upper()
            act = self.base_datos.actualiza_productos(self.id, codigo, nombre, modelo, precio, cantidad)
            # actualiza_productos() devuelve a, que puede ser 0 o 1 (a=cursor.rowcount)si actualiza los datos.
            if act == 1:
                self.signal_actualizar.setText("DATOS ACTUALIZADOS")
                self.act_codigo.clear()
                self.act_nombre.clear()
                self.act_modelo.clear()
                self.act_precio.clear()
                self.act_cantidad.clear()
                self.line_actualizar_buscar.setText('')
            elif act == 0:
                self.signal_actualizar.setText("ERROR")
            else:
                self.signal_actualizar.setText("INCORRECTO")

    # Metodo del btn_buscar_borrar
    def buscar_por_nombre_eliminar(self):
        nombre_producto = self.line_eliminar_buscar.text().upper()
        print("main:buscar_por_nombre_eliminar: se captura el texto del line_edit en variable nombre_producto.")
        nombre_producto = str("'" + nombre_producto + "'")
        print(nombre_producto)
        print("main:buscar_por_nombre_eliminar: se va a buscar los datos, llama a método busca_productos, de conexion_sqlite")
        producto = self.base_datos.busca_productos(nombre_producto)  # buscamos datos en la BD
        print("main:buscar_por_nombre_eliminar: retorna de la BD {}".format(producto))
        self.tabla_borrar.setRowCount(len(producto))    # indicamos cantidad de filas de la tabla segun datos retornados
        filas = len(producto)
        print("Cantidad de filas: {}".format(filas))
        if len(producto) == 0:
            self.signal_eliminar.setText('NO EXISTE')
        else:
            self.signal_eliminar.setText('Producto Seleccionado')
        print("Salió del if del signal_eliminar")
        tablerow = 0
        # bucle for para insertar en la tabla los datos buscados
        for row in producto:
            self.elemento = row[2]
            print("Dentro del bucle For, producto a borrar: {}".format(self.elemento))
            self.tabla_borrar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_borrar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_borrar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_borrar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_borrar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1
        print("datos insertados en la tabla_borrar")

    # Metodo del btn_eliminar_reg
    def eliminar_producto(self):
        self.row_flag = self.tabla_borrar.currentRow() # obtener el valor de una fila al selecionarla
        print("main:eliminar_producto: fila seleccionada, ingresar al if para eliminar")
        nombre = str("'" + self.elemento + "'")
        print(nombre)
        if self.row_flag == 0:
            print("main:eliminar_producto:if: fila == 0")
            self.tabla_borrar.removeRow(0)
            print("datos borrados de tabla_borrar")
            self.base_datos.elimina_productos(nombre)
            print("datos borrados de la BD")
            self.signal_eliminar.setText('Producto Eliminado')
            self.line_eliminar_buscar.setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())



