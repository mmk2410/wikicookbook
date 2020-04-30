#!/usr/bin/python

"""
WikiCookBook

Easily enter recipes and export them to beautiful wiki pages.

2020 © Marcel Kapfer <opensource@mmk2410.org>
MIT License
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Connect close actions
        self.b_cancel.clicked.connect(self.close)
        self.ma_close.triggered.connect(self.close)

        # Conncect recipe name typing
        self.e_recipe_name.textChanged.connect(self.updateTitle)

        # Handle category buttons
        self.b_category_add.clicked.connect(self.category_add)
        self.e_category.returnPressed.connect(self.category_add)
        self.b_category_remove.clicked.connect(self.category_remove)

        self.show()

    def updateTitle(self):
        """
        Update the window title so it contains the name of the current recipe.
        """
        current_recipe_name = self.e_recipe_name.text()
        if current_recipe_name:
            self.setWindowTitle(f"{current_recipe_name} - WikiCookBook")
        else:
            self.setWindowTitle("WikiCookBook")

    def category_add(self):
        if self.e_category.text():
            self.v_categories.addItem(f"Kategorie{self.e_category.text()}")

    def category_remove(self):
        self.v_categories.takeItem(self.v_categories.currentRow())

    def close(self):
        """
        Close the application. A warning is shown before.
        """
        reply = QMessageBox.question(self, "Sicher?",
            "Möchten Sie wirklich schließen?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(0)

if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("WikiCookBook")
    window = MainWindow()
    app.exec_()
