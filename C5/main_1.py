import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

# Ensure QApplication is created one
#app = QApplication([])
app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

Form, Window = uic.loadUiType("MainWindow.ui" )

w=Window()
f=Form()
f.setupUi(w)

w.show()
sys.exit(app.exec())

