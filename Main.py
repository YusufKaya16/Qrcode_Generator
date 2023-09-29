import sys
from PyQt5.QtWidgets import *
from Generater import *
from pyqrcode import *


class Anapencere(QWidget):

    def __init__(self):
        super().__init__()
        window = QMainWindow(self)
        self.picture = QLabel(window)
        self.picture.resize(200, 200)
        self.ui_window = Ui_MainWindow()
        self.ui_window.setupUi(window)
        self.ui_window.pushButton.clicked.connect(self.click)
        self.message = QMessageBox(window)
        window.show()

    def message_set(self, content):
        self.message.setWindowTitle("QrCode Generator")
        self.message.setText(content)
        self.message.setIcon(self.message.Warning)
        self.message.show()

    def click(self):
        data = self.ui_window.lineEdit.text()
        if "" == data:
            self.message_set("Please enter the link!")

        else:
            link = QRCode(data, error='H', version=10, encoding='utf-8')
            link.png("code.png", scale=3, background=(0, 0, 0, 0))
            self.picture.setPixmap(QtGui.QPixmap("code.png"))
            self.picture.move(270, 255)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    deneme = Anapencere()
    sys.exit(app.exec())
