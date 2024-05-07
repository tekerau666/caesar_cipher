# -*- coding: utf-8 -*-
import re

from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'cipher.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

from caesar import Encrypt, Decrypt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.keyLineEdit = QLineEdit(self.centralwidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setGeometry(QRect(300, 20, 113, 22))
        self.encryptButton = QPushButton(self.centralwidget)
        self.encryptButton.setObjectName(u"encryptButton")
        self.encryptButton.clicked.connect(self.EncryptHandler)
        self.encryptButton.setGeometry(QRect(80, 230, 251, 201))
        self.decryptButton = QPushButton(self.centralwidget)
        self.decryptButton.setObjectName(u"decryptButton")
        self.decryptButton.clicked.connect(self.DecryptHandler)
        self.decryptButton.setGeometry(QRect(430, 230, 251, 201))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 110, 191, 31))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 0, 49, 16))
        self.enterText = QTextEdit(self.centralwidget)
        self.enterText.setObjectName(u"enterText")
        self.enterText.setGeometry(QRect(80, 50, 571, 51))
        self.encryptText = QTextEdit(self.centralwidget)
        self.encryptText.setObjectName(u"encryptText")
        self.encryptText.setGeometry(QRect(80, 140, 571, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
    # retranslateUi

def keyErrorMessage(self, msgText):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText(msgText)
    msg.setWindowTitle("Key Error")
    msg.exec_()


def EncryptHandler(self):
    plainText = self.enterText.toPlainText()
    key = self.keyLineEdit.text()

    if re.match('^[0-9]+$', key):
        cipherText = Encrypt(plainText, key)
    else:
        cipherText = ''
        self.keyErrorMessage("The key must be an integer value in Caesar cipher")
    self.encryptText.setPlainText(cipherText)


def DecryptHandler(self):
    cipherText = self.encryptText.toPlainText()
    key = self.keyLineEdit.text()

    if re.match('^[0-9]+$', key):
        Decrypt(cipherText)
    else:
        self.keyErrorMessage("The key must be an integer value in Caesar cipher")


def resetHandler(self):
    self.keyLineEdit.clear()
    self.encryptText.clear()
    self.keyLineEdit.clear()