from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        # Ventana principal QWidget
        Form.setObjectName("Form")
        Form.resize(717, 389)
        # TABs de ventana Form
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 391))

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

        ### MENÚ PRODUCTO
        self.prod = QtWidgets.QWidget()
        self.prod.setObjectName("prod")   # QWidget prod
        self.tabla_producto = QtWidgets.QTableWidget(self.prod)
        # tabla_producto del menú PRODUCTOS
        self.tabla_producto.setGeometry(QtCore.QRect(100, 40, 501, 261))
        self.tabla_producto.setObjectName("tabla_producto")
        self.tabla_producto.setColumnCount(5)
        self.tabla_producto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        # Fuente de la tabla_producto
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        # Columnas de la tabla_producto
        self.tabla_producto.setHorizontalHeaderItem(0, item)    # Código
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(1, item)    # Nombre
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(2, item)    # Modelo
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(3, item)    # Precio
        item = QtWidgets.QTableWidgetItem()
        self.tabla_producto.setHorizontalHeaderItem(4, item)    # Cantidad
        # QPushButton ACTUALIZAR de la tabla_producto
        self.btn_actualizar = QtWidgets.QPushButton(self.prod)  # Botón actualizar
        self.btn_actualizar.setGeometry(QtCore.QRect(100, 310, 101, 21))
        # Fuente del botón ACTUALIZAR
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_actualizar.setFont(font)
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.tabWidget.addTab(self.prod, "")

        ### MENÚ BUSCAR PRODUCTO
        self.find = QtWidgets.QWidget()
        self.find.setObjectName("find")     # QWidget find
        self.codigoB = QtWidgets.QLabel(self.find)
        self.codigoB.setGeometry(QtCore.QRect(110, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codigoB.setFont(font)
        self.codigoB.setObjectName("codigoB")   # Etiqueta QLabel CÓDIGO
        # QLineEdit de CÓDIGO
        self.lineEdit = QtWidgets.QLineEdit(self.find)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        # tabla_buscar del Menú BUSCAR PRODUCTO
        self.tabla_buscar = QtWidgets.QTableWidget(self.find)
        self.tabla_buscar.setGeometry(QtCore.QRect(110, 80, 501, 261))
        # Fuente de tabla_buscar
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabla_buscar.setFont(font)
        self.tabla_buscar.setObjectName("tabla_buscar")
        self.tabla_buscar.setColumnCount(5)
        self.tabla_buscar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        # Fuente de tabla_buscar
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        # Columnas de tabla_buscar
        self.tabla_buscar.setHorizontalHeaderItem(0, item)      # Código
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(1, item)      # Nombre
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(2, item)      # Modelo
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(3, item)      # Precio
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(4, item)      # Contidad
        self.btn_buscar = QtWidgets.QPushButton(self.find)
        self.btn_buscar.setGeometry(QtCore.QRect(510, 50, 101, 21))
        # Fuente de btn_buscar
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setObjectName("btn_buscar")     # Botón BUSCAR
        self.tabWidget.addTab(self.find, "")

        # MENÚ AGREGAR PRODUCTO
        self.add = QtWidgets.QWidget()
        self.add.setObjectName("add")
        self.btn_agregar = QtWidgets.QPushButton(self.add)      # btn_agregar
        self.btn_agregar.setGeometry(QtCore.QRect(440, 270, 101, 21))
        # Fuente de botón AGREGAR
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setObjectName("btn_agregar")
        # Etiqueta QLabel label_2
        self.label_2 = QtWidgets.QLabel(self.add)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 351, 18))
        # Fuente de etqueta label_2
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # GRID QGridLayout de ventana AGREGAR PRODUCTO
        self.widget = QtWidgets.QWidget(self.add)
        self.widget.setGeometry(QtCore.QRect(160, 60, 381, 191))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # QLabel codigoAdd etiqueta CÓDIGO
        self.codigoAdd = QtWidgets.QLabel(self.widget)
        self.codigoAdd.setObjectName("codigoAdd")
        self.gridLayout.addWidget(self.codigoAdd, 0, 0, 1, 1)
        # QLineEdit  line_codigo de etiqueta CÓDIGO
        self.line_codigo = QtWidgets.QLineEdit(self.widget)
        self.line_codigo.setObjectName("line_codigo")
        self.gridLayout.addWidget(self.line_codigo, 0, 1, 1, 1)
        # QLabel nombreAdd etiqueta NOMBRE
        self.nombreAdd = QtWidgets.QLabel(self.widget)
        self.nombreAdd.setObjectName("nombreAdd")
        self.gridLayout.addWidget(self.nombreAdd, 1, 0, 1, 1)
        # QLineEdit line_nombre de etiqueta NOMBRE
        self.line_nombre = QtWidgets.QLineEdit(self.widget)
        self.line_nombre.setObjectName("line_nombre")
        self.gridLayout.addWidget(self.line_nombre, 1, 1, 1, 1)
        # QLabel modeloAdd etiqueta MODELO
        self.modeloAdd = QtWidgets.QLabel(self.widget)
        self.modeloAdd.setObjectName("modeloAdd")
        self.gridLayout.addWidget(self.modeloAdd, 2, 0, 1, 1)
        # QLineEdit line_modelo de etiqueta MODELO
        self.line_modelo = QtWidgets.QLineEdit(self.widget)
        self.line_modelo.setObjectName("line_modelo")
        self.gridLayout.addWidget(self.line_modelo, 2, 1, 1, 1)
        # QLabel precioAdd etiqueta PRECIO
        self.precioAdd = QtWidgets.QLabel(self.widget)
        self.precioAdd.setObjectName("precioAdd")
        self.gridLayout.addWidget(self.precioAdd, 3, 0, 1, 1)
        # QLineEdit line_precio etiqueta PRECIO
        self.line_precio = QtWidgets.QLineEdit(self.widget)
        self.line_precio.setObjectName("line_precio")
        self.gridLayout.addWidget(self.line_precio, 3, 1, 1, 1)
        # QLabel cantidadAdd etiqueta CANTIDAD
        self.cantidadAdd = QtWidgets.QLabel(self.widget)
        self.cantidadAdd.setObjectName("cantidadAdd")
        self.gridLayout.addWidget(self.cantidadAdd, 4, 0, 1, 1)
        # QLineEdit line_cantidad etiqueta CANTIDAD
        self.line_cantidad = QtWidgets.QLineEdit(self.widget)
        self.line_cantidad.setObjectName("line_cantidad")
        self.gridLayout.addWidget(self.line_cantidad, 4, 1, 1, 1)
        self.tabWidget.addTab(self.add, "")

        # MENÚ ACTUALIZAR PRODUCTO
        self.refresh = QtWidgets.QWidget()
        self.refresh.setObjectName("refresh")
        self.layoutWidget = QtWidgets.QWidget(self.refresh)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 120, 381, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        # GRID gridLayout_2 de ventana ACTUALIZAR PRODUCTO
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # QLabel codigoAdd_2 etiqueta CÓDIGO
        self.codigoAdd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.codigoAdd_2.setObjectName("codigoAdd_2")
        self.gridLayout_2.addWidget(self.codigoAdd_2, 0, 0, 1, 1)
        # QLineEdit line_codigo_2 etiqueta CÓDIGO
        self.line_codigo_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_codigo_2.setObjectName("line_codigo_2")
        self.gridLayout_2.addWidget(self.line_codigo_2, 0, 1, 1, 1)
        # QLabel nombreAdd_2 etiqueta NOMBRE
        self.nombreAdd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.nombreAdd_2.setObjectName("nombreAdd_2")
        self.gridLayout_2.addWidget(self.nombreAdd_2, 1, 0, 1, 1)
        # QLineEdit line_nombre_2 etiqueta NOMBRE
        self.line_nombre_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_nombre_2.setObjectName("line_nombre_2")
        self.gridLayout_2.addWidget(self.line_nombre_2, 1, 1, 1, 1)
        # QLabel modeloAdd_2 etiqueta MODELO
        self.modeloAdd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.modeloAdd_2.setObjectName("modeloAdd_2")
        self.gridLayout_2.addWidget(self.modeloAdd_2, 2, 0, 1, 1)
        # QLineEdit line_modelo_2 etiqueta MODELO
        self.line_modelo_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_modelo_2.setObjectName("line_modelo_2")
        self.gridLayout_2.addWidget(self.line_modelo_2, 2, 1, 1, 1)
        # QLabel precioAdd_2 etiqueta PRECIO
        self.precioAdd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.precioAdd_2.setObjectName("precioAdd_2")
        self.gridLayout_2.addWidget(self.precioAdd_2, 3, 0, 1, 1)
        # QLineEdit line_precio_2 etiqueta PRECIO
        self.line_precio_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_precio_2.setObjectName("line_precio_2")
        self.gridLayout_2.addWidget(self.line_precio_2, 3, 1, 1, 1)
        # QLabel cantidadAdd_2 etiqueta CANTIDAD
        self.cantidadAdd_2 = QtWidgets.QLabel(self.layoutWidget)
        self.cantidadAdd_2.setObjectName("cantidadAdd_2")
        self.gridLayout_2.addWidget(self.cantidadAdd_2, 4, 0, 1, 1)
        # QLineEdit line_cantidad_2 etiqueta CANTIDAD
        self.line_cantidad_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_cantidad_2.setObjectName("line_cantidad_2")
        self.gridLayout_2.addWidget(self.line_cantidad_2, 4, 1, 1, 1)
        # QPushButton btn_agregar_2 botón ACTUALIZAR
        self.btn_agregar_2 = QtWidgets.QPushButton(self.refresh)
        self.btn_agregar_2.setGeometry(QtCore.QRect(450, 330, 101, 21))
        # Fuente de botón btn_agregar_2
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_agregar_2.setFont(font)
        self.btn_agregar_2.setObjectName("btn_agregar_2")
        # QSplitter splitter ventana ACTUALIZAR PRODUCTO
        self.splitter = QtWidgets.QSplitter(self.refresh)
        self.splitter.setGeometry(QtCore.QRect(220, 30, 285, 71))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        # Fuente de etiqueta INGRESE EL NOMBRE DEL PRODUCTO
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # QLineEDit line_busqueda del Splitter
        self.line_busqueda = QtWidgets.QLineEdit(self.splitter)
        self.line_busqueda.setObjectName("line_busqueda")
        # QPushButton btn_busqueda del Splitter
        self.btn_busqueda = QtWidgets.QPushButton(self.splitter)
        # Fuente de btn_busqueda
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_busqueda.setFont(font)
        self.btn_busqueda.setObjectName("btn_busqueda")
        self.tabWidget.addTab(self.refresh, "")

        # MENÚ BORRAR PRODUCTO
        self.delete = QtWidgets.QWidget()
        self.delete.setObjectName("delete")
        # QPushButton btn_delete botón BORRAR
        self.btn_delete = QtWidgets.QPushButton(self.delete)
        self.btn_delete.setGeometry(QtCore.QRect(510, 50, 101, 21))
        # Fuente de btn_delete
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        # QLabel codigo_delete etiqueta CÓDIGO
        self.codigo_delete = QtWidgets.QLabel(self.delete)
        self.codigo_delete.setGeometry(QtCore.QRect(110, 20, 61, 21))
        # Fuente de etiqueta CÓDIGO
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codigo_delete.setFont(font)
        self.codigo_delete.setObjectName("codigo_delete")
        # QTableWidget tabla_delete del MENÚ BORRAR PRODUCTO
        self.tabla_delete = QtWidgets.QTableWidget(self.delete)
        self.tabla_delete.setGeometry(QtCore.QRect(110, 80, 501, 261))
        # Fuente de tabla_delete
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabla_delete.setFont(font)
        self.tabla_delete.setObjectName("tabla_delete")
        self.tabla_delete.setColumnCount(5)
        self.tabla_delete.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tabla_delete.setHorizontalHeaderItem(0, item)      # columna Código
        item = QtWidgets.QTableWidgetItem()
        self.tabla_delete.setHorizontalHeaderItem(1, item)      # columna Nombre
        item = QtWidgets.QTableWidgetItem()
        self.tabla_delete.setHorizontalHeaderItem(2, item)      # columna Modelo
        item = QtWidgets.QTableWidgetItem()
        self.tabla_delete.setHorizontalHeaderItem(3, item)      # columna Precio
        item = QtWidgets.QTableWidgetItem()
        self.tabla_delete.setHorizontalHeaderItem(4, item)      # columna Cantidad
        # QLineEdit line_delete etiqueta CÓDIGO
        self.line_delete = QtWidgets.QLineEdit(self.delete)
        self.line_delete.setGeometry(QtCore.QRect(170, 20, 161, 20))
        self.line_delete.setObjectName("line_delete")
        # QPushButton btn_borrado botón ESTADO
        self.btn_borrado = QtWidgets.QPushButton(self.delete)
        self.btn_borrado.setGeometry(QtCore.QRect(170, 50, 161, 23))
        # Fuente de botón ESTADO
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_borrado.setFont(font)
        self.btn_borrado.setObjectName("btn_borrado")
        self.tabWidget.addTab(self.delete, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # QTableWidget tabla_producto de ventana PRODUCTOS
        item = self.tabla_producto.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabla_producto.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_producto.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Modelo"))
        item = self.tabla_producto.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Precio"))
        item = self.tabla_producto.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cantidad"))
        # btn_actualizar de ventana PRODUCTOS
        self.btn_actualizar.setText(_translate("Form", "ACTUALIZAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prod), _translate("Form", "PRODUCTOS"))
        self.codigoB.setText(_translate("Form", "CÓDIGO:"))
        # QTableWidget tabla_buscar de ventana BUSCAR PRODUCTO
        item = self.tabla_buscar.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabla_buscar.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_buscar.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Modelo"))
        item = self.tabla_buscar.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Precio"))
        item = self.tabla_buscar.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cantidad"))
        # btn_buscar de ventana BUSCAR PRODUCTO
        self.btn_buscar.setText(_translate("Form", "BUSCAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.find), _translate("Form", "BUSCAR PRODUCTO"))
        # btn_agregar de ventana AGREGAR PRODUCTO
        self.btn_agregar.setText(_translate("Form", "AGREGAR"))
        self.label_2.setText(_translate("Form", "ESCRIBA EL PRODUCTO QUE DESEA AGREGAR"))
        # Form de AGREGAR PRODUCTO
        self.codigoAdd.setText(_translate("Form", "CÓDIGO:"))
        self.nombreAdd.setText(_translate("Form", "NOMBRE:"))
        self.modeloAdd.setText(_translate("Form", "MODELO:"))
        self.precioAdd.setText(_translate("Form", "PRECIO:"))
        self.cantidadAdd.setText(_translate("Form", "CANTIDAD:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("Form", "AGREGAR PRODUCTO"))
        # Form de ventana ACTUALIZAR PRODUCTO
        self.codigoAdd_2.setText(_translate("Form", "CÓDIGO:"))
        self.nombreAdd_2.setText(_translate("Form", "NOMBRE:"))
        self.modeloAdd_2.setText(_translate("Form", "MODELO:"))
        self.precioAdd_2.setText(_translate("Form", "PRECIO:"))
        self.cantidadAdd_2.setText(_translate("Form", "CANTIDAD:"))
        self.btn_agregar_2.setText(_translate("Form", "ACTUALIZAR"))
        self.label.setText(_translate("Form", "INGRESE EL NOMBRE DEL PRODUCTO"))
        self.btn_busqueda.setText(_translate("Form", "BUSQUEDA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.refresh), _translate("Form", "ACTUALIZAR PRODUCTO"))
        # btn_delete botón BORRAR de la ventana BORRAR PRODUCTO
        self.btn_delete.setText(_translate("Form", "BORRAR"))
        self.codigo_delete.setText(_translate("Form", "CÓDIGO:"))
        # tabla_delete de ventana BORRAR PRODUCTO
        item = self.tabla_delete.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tabla_delete.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tabla_delete.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Modelo"))
        item = self.tabla_delete.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Precio"))
        item = self.tabla_delete.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cantidad"))
        # btn_borrado ESTADO de ventana BORRAR PRODUCTO
        self.btn_borrado.setText(_translate("Form", "ESTADO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.delete), _translate("Form", "BORRAR PRODUCTO"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""