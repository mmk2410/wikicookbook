# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(About)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.l_title = QtWidgets.QLabel(About)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_title.setFont(font)
        self.l_title.setAlignment(QtCore.Qt.AlignCenter)
        self.l_title.setObjectName("l_title")
        self.verticalLayout_2.addWidget(self.l_title)
        self.l_description = QtWidgets.QLabel(About)
        self.l_description.setAlignment(QtCore.Qt.AlignCenter)
        self.l_description.setWordWrap(True)
        self.l_description.setObjectName("l_description")
        self.verticalLayout_2.addWidget(self.l_description)
        self.l_basedon = QtWidgets.QLabel(About)
        self.l_basedon.setAlignment(QtCore.Qt.AlignCenter)
        self.l_basedon.setObjectName("l_basedon")
        self.verticalLayout_2.addWidget(self.l_basedon)
        self.l_copyright = QtWidgets.QLabel(About)
        self.l_copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.l_copyright.setObjectName("l_copyright")
        self.verticalLayout_2.addWidget(self.l_copyright)
        self.l_sourcecode = QtWidgets.QLabel(About)
        self.l_sourcecode.setAlignment(QtCore.Qt.AlignCenter)
        self.l_sourcecode.setObjectName("l_sourcecode")
        self.verticalLayout_2.addWidget(self.l_sourcecode)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.b_close = QtWidgets.QPushButton(About)
        self.b_close.setObjectName("b_close")
        self.horizontalLayout.addWidget(self.b_close)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.l_title.setText(_translate("About", "WikiCookBook"))
        self.l_description.setText(_translate("About", "A graphical editor for creating cookbook entries using the MoinMoin wiki syntax"))
        self.l_basedon.setText(_translate("About", "<html><head/><body><p>Based on <a href=\"https://www.python.org/\"><span style=\" text-decoration: underline; color:#4c6b8a;\">Python</span></a> and <a href=\"https://www.riverbankcomputing.com/software/pyqt/intro\"><span style=\" text-decoration: underline; color:#4c6b8a;\">PyQt</span></a>.</p></body></html>"))
        self.l_copyright.setText(_translate("About", "<html><head/><body><p>2020 © Marcel Kapfer (opensource@mmk2410.org)<br/>Licensed under GPL v3</p></body></html>"))
        self.l_sourcecode.setText(_translate("About", "<html><head/><body><p>Sourcecode available at<br/><a href=\"https://git.mmk2410.org/mmk2410/wikicookbook\"><span style=\" text-decoration: underline; color:#4c6b8a;\">git.mmk2410.org/mmk2410/wikicookbook</span></a></p></body></html>"))
        self.b_close.setText(_translate("About", "Schließen"))
