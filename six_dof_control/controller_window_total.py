#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 130))
        Form.setMaximumSize(QtCore.QSize(346, 158))
        self.classification_pushButton = QtWidgets.QPushButton(Form)
        self.classification_pushButton.setGeometry(QtCore.QRect(10, 10, 171, 25))
        self.classification_pushButton.setObjectName("classification_pushButton")

        self.retranslateUi(Form)
        self.classification_pushButton.clicked.connect(Form.Classification_move)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "controller"))
        self.classification_pushButton.setText(_translate("Form", "Clasificar objeto"))
