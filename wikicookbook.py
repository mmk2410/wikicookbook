#!/usr/bin/python

"""
WikiCookBook

Easily enter recipes and export them to beautiful wiki pages.

2020 © Marcel Kapfer <opensource@mmk2410.org>
MIT License
"""

import sys
import recipe
from writer.MoinMoinWriter import MoinMoinWriter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDialog
from ui_mainwindow import Ui_MainWindow
from ui_code_dialog import Ui_WikiCode
from ui_about_dialog import Ui_About

class AboutDialog(QDialog, Ui_About):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.b_close.clicked.connect(self.close)

        self.show()

class WikiCodeDialog(QDialog, Ui_WikiCode):
    def __init__(self, code, *args, **kwargs):
        super(WikiCodeDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.e_code.setPlainText(code)

        self.b_close.clicked.connect(self.close)
        self.b_copy.clicked.connect(self.copy)

        self.show()

    def copy(self):
        self.e_code.selectAll()
        self.e_code.copy()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Connect close actions
        self.b_cancel.clicked.connect(self.close)
        self.ma_close.triggered.connect(self.close)

        # Connect about action
        self.ma_information.triggered.connect(self.about)

        # Conncect recipe name typing
        self.e_recipe_name.textChanged.connect(self.updateTitle)

        # Handle categories
        self.b_category_add.clicked.connect(self.category_add)
        self.e_category.returnPressed.connect(self.category_add)
        self.b_category_remove.clicked.connect(self.category_remove)

        # Handle ingredients
        self.b_ingredient_add.clicked.connect(self.ingredient_add)
        self.b_ingredient_remove.clicked.connect(self.ingredient_remove)

        # Handle utensils
        self.b_utensil_add.clicked.connect(self.utensil_add)
        self.e_utensil.returnPressed.connect(self.utensil_add)
        self.b_utensil_remove.clicked.connect(self.utensil_remove)

        # Handle steps
        self.b_step_add.clicked.connect(self.step_add)
        self.b_step_edit.clicked.connect(self.step_edit)
        self.b_step_replace.clicked.connect(self.step_replace)
        self.b_step_remove.clicked.connect(self.step_remove)

        # Handle notes
        self.b_note_add.clicked.connect(self.note_add)
        self.b_note_edit.clicked.connect(self.note_edit)
        self.b_note_replace.clicked.connect(self.note_replace)
        self.b_note_remove.clicked.connect(self.note_remove)

        # Handle tips
        self.b_tip_add.clicked.connect(self.tip_add)
        self.b_tip_edit.clicked.connect(self.tip_edit)
        self.b_tip_replace.clicked.connect(self.tip_replace)
        self.b_tip_remove.clicked.connect(self.tip_remove)

        # Handle variations
        self.b_variation_add.clicked.connect(self.variation_add)
        self.b_variation_edit.clicked.connect(self.variation_edit)
        self.b_variation_replace.clicked.connect(self.variation_replace)
        self.b_variation_remove.clicked.connect(self.variation_remove)

        # Handle ratings
        self.b_rating_add.clicked.connect(self.rating_add)
        self.b_rating_edit.clicked.connect(self.rating_edit)
        self.b_rating_replace.clicked.connect(self.rating_replace)
        self.b_rating_remove.clicked.connect(self.rating_remove)

        # Handle recipe creation
        self.b_create.clicked.connect(self.create_recipe)

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

    def ingredient_add(self):
        if self.c_heading.checkState() == 2 or self.e_amount.text():
            if self.e_ingredient.text():
                if self.c_heading.checkState() == 2:
                    current_amount = QTableWidgetItem("----------")
                else:
                    current_amount = QTableWidgetItem(self.e_amount.text())
                current_ingredient = QTableWidgetItem(self.e_ingredient.text())
                self.v_ingredients.setRowCount(self.v_ingredients.rowCount() + 1)
                self.v_ingredients.setItem(self.v_ingredients.rowCount() - 1, 0, current_amount)
                self.v_ingredients.setItem(self.v_ingredients.rowCount() - 1, 1, current_ingredient)

    def ingredient_remove(self):
       self.v_ingredients.removeRow(self.v_ingredients.currentRow())

    def utensil_add(self):
        if self.e_utensil.text():
            self.v_utensils.addItem(self.e_utensil.text())

    def utensil_remove(self):
        self.v_utensils.takeItem(self.v_utensils.currentRow())

    def step_add(self):
        if self.e_step.toPlainText():
            self.v_steps.addItem(self.e_step.toPlainText())

    def step_edit(self):
        if self.v_steps.count() > 0:
            self.e_step.setText(self.v_steps.currentItem().text())

    def step_replace(self):
        if self.e_step.toPlainText() and self.v_steps.count() > 0:
            self.v_steps.currentItem().setText(self.e_step.toPlainText())

    def step_remove(self):
        self.v_steps.takeItem(self.v_steps.currentRow())

    def note_add(self):
        if self.e_note.toPlainText():
            self.v_notes.addItem(self.e_note.toPlainText())

    def note_edit(self):
        if self.v_notes.count() > 0:
            self.e_note.setText(self.v_notes.currentItem().text())

    def note_replace(self):
        if self.e_note.toPlainText() and self.v_notes.count() > 0:
            self.v_notes.currentItem().setText(self.e_note.toPlainText())

    def note_remove(self):
        self.v_notes.takeItem(self.v_notes.currentRow())

    def tip_add(self):
        if self.e_tip.toPlainText():
            self.v_tips.addItem(self.e_tip.toPlainText())

    def tip_edit(self):
        if self.v_tips.count() > 0:
            self.e_tip.setText(self.v_tips.currentItem().text())

    def tip_replace(self):
        if self.e_tip.toPlainText() and self.v_tips.count() > 0:
            self.v_tips.currentItem().setText(self.e_tip.toPlainText())

    def tip_remove(self):
        self.v_tips.takeItem(self.v_tips.currentRow())

    def variation_add(self):
        if self.e_variation.toPlainText():
            self.v_variations.addItem(self.e_variation.toPlainText())

    def variation_edit(self):
        if self.v_variations.count() > 0:
            self.e_variation.setText(self.v_variations.currentItem().text())

    def variation_replace(self):
        if self.e_variation.toPlainText() and self.v_variations.count() > 0:
            self.v_variations.currentItem().setText(self.e_variation.toPlainText())

    def variation_remove(self):
        self.v_variations.takeItem(self.v_variations.currentRow())

    def rating_add(self):
        if self.e_rating.toPlainText():
            self.v_ratings.addItem(self.e_rating.toPlainText())

    def rating_edit(self):
        if self.v_ratings.count() > 0:
            self.e_rating.setText(self.v_ratings.currentItem().text())

    def rating_replace(self):
        if self.e_rating.toPlainText() and self.v_ratings.count() > 0:
            self.v_ratings.currentItem().setText(self.e_rating.toPlainText())

    def rating_remove(self):
        self.v_ratings.takeItem(self.v_ratings.currentRow())

    def create_recipe(self):
        current_recipe = recipe.Recipe(self.e_recipe_name.text(),
                                       self.e_servings.text(),
                                       self.e_time.text(),
                                       self.e_rating_overall.value(),
                                       self.e_url.text())

        # Categories
        for row in range(self.v_categories.count()):
            current_recipe.add_category(self.v_categories.item(row).text())

        # Ingredients
        for row in range(self.v_ingredients.rowCount()):
            current_recipe.add_ingredient(
                self.v_ingredients.item(row, 0).text(),
                self.v_ingredients.item(row, 1).text()
            )

        # Utensils
        for row in range(self.v_utensils.count()):
            current_recipe.add_utensil(self.v_utensils.item(row).text())

        # Steps
        for row in range(self.v_steps.count()):
            current_recipe.add_step(self.v_steps.item(row).text())

        # Notes
        for row in range(self.v_notes.count()):
            current_recipe.add_note(self.v_notes.item(row).text())

        # Tips
        for row in range(self.v_tips.count()):
            current_recipe.add_tip(self.v_tips.item(row).text())

        # Variations
        for row in range(self.v_variations.count()):
            current_recipe.add_variation(self.v_variations.item(row).text())

        # Ratings
        for row in range(self.v_ratings.count()):
            current_recipe.add_rating(self.v_ratings.item(row).text())

        writer = MoinMoinWriter()
        code = current_recipe.wikicode(writer)

        dialog = WikiCodeDialog(code)
        dialog.exec_()

    def about(self):
        """
        Show an about dialog.
        """
        dialog = AboutDialog()
        dialog.exec_()

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
