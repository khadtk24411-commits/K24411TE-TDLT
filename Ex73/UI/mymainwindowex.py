from Ex73.UI.mymainwindow import Ui_MainWindow
from Ex73.libs.my_module import PTbac2
from Ex73.UI.mymainwindow import Ui_MainWindow
class mymainwindowex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.Mainwindow = MainWindow # luu lai vi tri o nho tren thanh ram vi mainwindow dang o bien local thuong se tu giai phong khi ra khoi ham
        self.setupSignalAndSlot()
    def show_window(self):
        self.Mainwindow.show()
    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.giai)
    def giai(self):
        a=float(self.aLineEdit.text())
        b=float(self.bLineEdit.text())
        c=float(self.cLineEdit.text())
        ketqua=PTbac2(a,b,c)
        self.resultLineEdit.setText(ketqua)