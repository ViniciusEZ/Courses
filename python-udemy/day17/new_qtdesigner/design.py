# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desing.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.InputHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.InputHeight.setObjectName("InputHeight")
        self.gridLayout.addWidget(self.InputHeight, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.InputWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.InputWidth.setObjectName("InputWidth")
        self.gridLayout.addWidget(self.InputWidth, 2, 1, 1, 1)
        self.BtnRezise = QtWidgets.QPushButton(self.centralwidget)
        self.BtnRezise.setObjectName("BtnRezise")
        self.gridLayout.addWidget(self.BtnRezise, 2, 4, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 3, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 404))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LabelImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LabelImg.setText("")
        self.LabelImg.setObjectName("LabelImg")
        self.gridLayout_2.addWidget(self.LabelImg, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btnChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.gridLayout.addWidget(self.btnChooseFile, 1, 4, 1, 1)
        self.Input_OpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_OpenFile.setObjectName("Input_OpenFile")
        self.gridLayout.addWidget(self.Input_OpenFile, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rezige Image"))
        self.label_2.setText(_translate("MainWindow", "Height"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.BtnRezise.setText(_translate("MainWindow", "Rezise"))
        self.BtnSave.setText(_translate("MainWindow", "Save"))
        self.btnChooseFile.setText(_translate("MainWindow", "Choose File"))