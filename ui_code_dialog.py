# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_code_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WikiCode(object):
    def setupUi(self, WikiCode):
        WikiCode.setObjectName("WikiCode")
        WikiCode.resize(530, 643)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WikiCode)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.e_code = QtWidgets.QPlainTextEdit(WikiCode)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.e_code.setFont(font)
        self.e_code.setReadOnly(True)
        self.e_code.setObjectName("e_code")
        self.verticalLayout_2.addWidget(self.e_code)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.b_copy = QtWidgets.QPushButton(WikiCode)
        self.b_copy.setObjectName("b_copy")
        self.horizontalLayout.addWidget(self.b_copy)
        self.b_close = QtWidgets.QPushButton(WikiCode)
        self.b_close.setObjectName("b_close")
        self.horizontalLayout.addWidget(self.b_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(WikiCode)
        QtCore.QMetaObject.connectSlotsByName(WikiCode)

    def retranslateUi(self, WikiCode):
        _translate = QtCore.QCoreApplication.translate
        WikiCode.setWindowTitle(_translate("WikiCode", "WikiCode"))
        self.b_copy.setText(_translate("WikiCode", "Kopieren"))
        self.b_close.setText(_translate("WikiCode", "Schließen"))
