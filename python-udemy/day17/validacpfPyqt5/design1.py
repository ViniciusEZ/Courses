# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 142)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.btnValidar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnValidar.setFont(font)
        self.btnValidar.setObjectName("btnValidar")
        self.gridLayout.addWidget(self.btnValidar, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.btnGerar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnGerar.setFont(font)
        self.btnGerar.setObjectName("btnGerar")
        self.gridLayout.addWidget(self.btnGerar, 1, 3, 1, 1)
        self.InputValidaCPF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputValidaCPF.setFont(font)
        self.InputValidaCPF.setObjectName("InputValidaCPF")
        self.gridLayout.addWidget(self.InputValidaCPF, 0, 1, 1, 2)
        self.lblReturn = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.lblReturn.setFont(font)
        self.lblReturn.setStyleSheet("color: cyan")
        self.lblReturn.setText("")
        self.lblReturn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblReturn.setObjectName("lblReturn")
        self.gridLayout.addWidget(self.lblReturn, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Valida ou Gera CPF"))
        self.label_2.setText(_translate("MainWindow", "VALIDA CPF:"))
        self.btnValidar.setText(_translate("MainWindow", "VALIDAR"))
        self.label.setText(_translate("MainWindow", "GERAR CPF:"))
        self.btnGerar.setText(_translate("MainWindow", "GERAR"))
