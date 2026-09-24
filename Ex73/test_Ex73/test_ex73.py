import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from Ex73.UI.mymainwindowex import mymainwindowex

app=QApplication(sys.argv)

myui=mymainwindowex()
#MainWindow = QMainWindow()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()
