# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Gui\three\q.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("QPushBotton{\n"
"    background-color: rgb(138, 138, 103);\n"
"    color: rgb(243, 255, 1);\n"
"    border: none;\n"
"    font: 12pt \"Impact\";\n"
"}\n"
"QPushBotton:hover{\n"
"    color: rgb(255, 249, 51);\n"
"    background-color: rgb(150, 150, 112);\n"
"}\n"
"QPushBotton:presed{\n"
"    color: rgb(255, 227, 14);\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setStyleSheet("QPushButton{\n"
"    background-color: rgb(138, 138, 103);\n"
"    color: rgb(243, 255, 1);\n"
"    border: none;\n"
"    font: 10pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 249, 51);\n"
"    background-color: rgb(150, 150, 112);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 227, 14);\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 171, 201))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 181, 41))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(138, 138, 103);\n"
"    color: rgb(243, 255, 1);\n"
"    border: none;\n"
"    font: 10pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 249, 51);\n"
"    background-color: rgb(150, 150, 112);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 227, 14);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Scan"))



