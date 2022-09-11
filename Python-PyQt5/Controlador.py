import sys
from PyQt5 import QtWidgets
from modelo import MiApp


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())