# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_close_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CloseDialog(object):
    def setupUi(self, CloseDialog):
        CloseDialog.setObjectName("CloseDialog")
        CloseDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        CloseDialog.resize(313, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CloseDialog.sizePolicy().hasHeightForWidth())
        CloseDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(CloseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.t_close = QtWidgets.QLabel(CloseDialog)
        self.t_close.setObjectName("t_close")
        self.verticalLayout.addWidget(self.t_close)
        self.l_buttons = QtWidgets.QHBoxLayout()
        self.l_buttons.setObjectName("l_buttons")
        self.b_yes = QtWidgets.QPushButton(CloseDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_yes.sizePolicy().hasHeightForWidth())
        self.b_yes.setSizePolicy(sizePolicy)
        self.b_yes.setObjectName("b_yes")
        self.l_buttons.addWidget(self.b_yes)
        self.b_no = QtWidgets.QPushButton(CloseDialog)
        self.b_no.setObjectName("b_no")
        self.l_buttons.addWidget(self.b_no)
        self.verticalLayout.addLayout(self.l_buttons)

        self.retranslateUi(CloseDialog)
        QtCore.QMetaObject.connectSlotsByName(CloseDialog)

    def retranslateUi(self, CloseDialog):
        _translate = QtCore.QCoreApplication.translate
        CloseDialog.setWindowTitle(_translate("CloseDialog", "Programm schließen"))
        self.t_close.setText(_translate("CloseDialog", "Soll das Programm wirklich geschlossen werden?"))
        self.b_yes.setText(_translate("CloseDialog", "Ja"))
        self.b_no.setText(_translate("CloseDialog", "Nein"))