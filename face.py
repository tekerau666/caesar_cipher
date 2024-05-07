import re
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication

from caesar import Decrypt, Encrypt
from interface import Ui_MainWindow


def keyErrorMessage(msgText):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(msgText)
    msg.setWindowTitle("Key Error")
    msg.exec_()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.encryptButton.clicked.connect(self.EncryptHandler())
        self.decryptButton.clicked.connect(self.DecryptHandler())

    def EncryptHandler(self):
        plainText = self.enterText.toPlainText()
        key = self.keyLineEdit.text()

        if re.match('^[0-9]+$', key):
            cipherText = Encrypt(plainText, key)
        else:
            cipherText = ''
            keyErrorMessage("The key must be an integer value in Caesar cipher")
        self.encryptText.setPlainText(cipherText)

    def DecryptHandler(self):
        cipherText = self.encryptText.toPlainText()
        key = self.keyLineEdit.text()

        if re.match('^[0-9]+$', key):
            plainText = Decrypt(cipherText, key)
        else:
            plainText = ''
            keyErrorMessage("The key must be an integer value in Caesar cipher")
        self.encryptText.setPlainText(plainText)

    def resetHandler(self):
        self.keyLineEdit.clear()
        self.encryptText.clear()
        self.keyLineEdit.clear()


app = QApplication(sys.argv)
client = MainWindow()
client.show()
sys.exit(app.exec())


