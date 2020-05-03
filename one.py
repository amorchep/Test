# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Gui\TestOne\one.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 119)
        Dialog.setStyleSheet("background-color: rgb(177, 177, 133);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 90, 161, 20))
        self.buttonBox.setStyleSheet("QPushButton{\n"
"background-color: rgb(103, 103, 77);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 238, 43);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 238, 43);\n"
"    background-color: rgb(204, 204, 153);\n"
"}\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 0);\n"
"}")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 50, 181, 31))
        self.label.setStyleSheet("color: rgb(255, 238, 43);\n"
"background-color: rgb(61, 61, 61);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 75, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(103, 103, 77);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(255, 238, 43);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(255, 238, 43);\n"
"    background-color: rgb(204, 204, 153);\n"
"}\n"
"QPushButton:pressed {\n"
"    color: rgb(255, 255, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.lineEdit.setStyleSheet("color: rgb(255, 238, 43);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"background-color: rgb(61, 61, 61);\n"
"border: none;\n"
"")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
