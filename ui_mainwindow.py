# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        MainWindow.setMinimumSize(QtCore.QSize(800, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.y_buttons = QtWidgets.QHBoxLayout()
        self.y_buttons.setObjectName("y_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.y_buttons.addItem(spacerItem)
        self.b_create = QtWidgets.QPushButton(self.centralwidget)
        self.b_create.setObjectName("b_create")
        self.y_buttons.addWidget(self.b_create)
        self.b_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.b_cancel.setObjectName("b_cancel")
        self.y_buttons.addWidget(self.b_cancel)
        self.gridLayout.addLayout(self.y_buttons, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.t_basics = QtWidgets.QWidget()
        self.t_basics.setObjectName("t_basics")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.t_basics)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.y_basics = QtWidgets.QGridLayout()
        self.y_basics.setObjectName("y_basics")
        self.l_rating = QtWidgets.QLabel(self.t_basics)
        self.l_rating.setObjectName("l_rating")
        self.y_basics.addWidget(self.l_rating, 2, 0, 1, 1)
        self.l_url = QtWidgets.QLabel(self.t_basics)
        self.l_url.setObjectName("l_url")
        self.y_basics.addWidget(self.l_url, 2, 2, 1, 1)
        self.e_servings = QtWidgets.QLineEdit(self.t_basics)
        self.e_servings.setObjectName("e_servings")
        self.y_basics.addWidget(self.e_servings, 1, 1, 1, 1)
        self.e_url = QtWidgets.QLineEdit(self.t_basics)
        self.e_url.setObjectName("e_url")
        self.y_basics.addWidget(self.e_url, 2, 3, 1, 1)
        self.l_recipe_name = QtWidgets.QLabel(self.t_basics)
        self.l_recipe_name.setObjectName("l_recipe_name")
        self.y_basics.addWidget(self.l_recipe_name, 0, 0, 1, 1)
        self.e_time = QtWidgets.QLineEdit(self.t_basics)
        self.e_time.setObjectName("e_time")
        self.y_basics.addWidget(self.e_time, 1, 3, 1, 1)
        self.e_recipe_name = QtWidgets.QLineEdit(self.t_basics)
        self.e_recipe_name.setObjectName("e_recipe_name")
        self.y_basics.addWidget(self.e_recipe_name, 0, 1, 1, 3)
        self.l_servings = QtWidgets.QLabel(self.t_basics)
        self.l_servings.setObjectName("l_servings")
        self.y_basics.addWidget(self.l_servings, 1, 0, 1, 1)
        self.l_zeit = QtWidgets.QLabel(self.t_basics)
        self.l_zeit.setObjectName("l_zeit")
        self.y_basics.addWidget(self.l_zeit, 1, 2, 1, 1)
        self.e_rating_overall = QtWidgets.QSpinBox(self.t_basics)
        self.e_rating_overall.setMaximum(5)
        self.e_rating_overall.setProperty("value", 3)
        self.e_rating_overall.setObjectName("e_rating_overall")
        self.y_basics.addWidget(self.e_rating_overall, 2, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.y_basics)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.v_categories = QtWidgets.QListWidget(self.t_basics)
        self.v_categories.setObjectName("v_categories")
        self.horizontalLayout_16.addWidget(self.v_categories)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.y_category = QtWidgets.QGridLayout()
        self.y_category.setObjectName("y_category")
        self.l_category = QtWidgets.QLabel(self.t_basics)
        self.l_category.setObjectName("l_category")
        self.y_category.addWidget(self.l_category, 0, 0, 1, 1)
        self.e_category = QtWidgets.QLineEdit(self.t_basics)
        self.e_category.setObjectName("e_category")
        self.y_category.addWidget(self.e_category, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.y_category)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.b_category_remove = QtWidgets.QPushButton(self.t_basics)
        self.b_category_remove.setObjectName("b_category_remove")
        self.horizontalLayout_15.addWidget(self.b_category_remove)
        self.b_category_add = QtWidgets.QPushButton(self.t_basics)
        self.b_category_add.setObjectName("b_category_add")
        self.horizontalLayout_15.addWidget(self.b_category_add)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.tabWidget.addTab(self.t_basics, "")
        self.t_ingredients = QtWidgets.QWidget()
        self.t_ingredients.setObjectName("t_ingredients")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.t_ingredients)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.v_ingredients = QtWidgets.QTableWidget(self.t_ingredients)
        self.v_ingredients.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.v_ingredients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.v_ingredients.setObjectName("v_ingredients")
        self.v_ingredients.setColumnCount(2)
        self.v_ingredients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.v_ingredients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.v_ingredients.setHorizontalHeaderItem(1, item)
        self.v_ingredients.horizontalHeader().setStretchLastSection(True)
        self.v_ingredients.verticalHeader().setVisible(False)
        self.horizontalLayout_14.addWidget(self.v_ingredients)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.y_ingredient = QtWidgets.QGridLayout()
        self.y_ingredient.setObjectName("y_ingredient")
        self.e_amount = QtWidgets.QLineEdit(self.t_ingredients)
        self.e_amount.setObjectName("e_amount")
        self.y_ingredient.addWidget(self.e_amount, 3, 1, 1, 1)
        self.l_ingredient = QtWidgets.QLabel(self.t_ingredients)
        self.l_ingredient.setObjectName("l_ingredient")
        self.y_ingredient.addWidget(self.l_ingredient, 0, 0, 1, 1)
        self.l_amount = QtWidgets.QLabel(self.t_ingredients)
        self.l_amount.setObjectName("l_amount")
        self.y_ingredient.addWidget(self.l_amount, 3, 0, 1, 1)
        self.c_heading = QtWidgets.QCheckBox(self.t_ingredients)
        self.c_heading.setObjectName("c_heading")
        self.y_ingredient.addWidget(self.c_heading, 1, 1, 1, 1)
        self.e_ingredient = QtWidgets.QLineEdit(self.t_ingredients)
        self.e_ingredient.setObjectName("e_ingredient")
        self.y_ingredient.addWidget(self.e_ingredient, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.y_ingredient)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.b_ingredient_remove = QtWidgets.QPushButton(self.t_ingredients)
        self.b_ingredient_remove.setObjectName("b_ingredient_remove")
        self.horizontalLayout_13.addWidget(self.b_ingredient_remove)
        self.b_ingredient_add = QtWidgets.QPushButton(self.t_ingredients)
        self.b_ingredient_add.setObjectName("b_ingredient_add")
        self.horizontalLayout_13.addWidget(self.b_ingredient_add)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.horizontalLayout_14.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.t_ingredients, "")
        self.t_utensils = QtWidgets.QWidget()
        self.t_utensils.setObjectName("t_utensils")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.t_utensils)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.v_utensils = QtWidgets.QListWidget(self.t_utensils)
        self.v_utensils.setObjectName("v_utensils")
        self.horizontalLayout_11.addWidget(self.v_utensils)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.y_utensils = QtWidgets.QGridLayout()
        self.y_utensils.setObjectName("y_utensils")
        self.l_utensil = QtWidgets.QLabel(self.t_utensils)
        self.l_utensil.setObjectName("l_utensil")
        self.y_utensils.addWidget(self.l_utensil, 0, 0, 1, 1)
        self.e_utensil = QtWidgets.QLineEdit(self.t_utensils)
        self.e_utensil.setObjectName("e_utensil")
        self.y_utensils.addWidget(self.e_utensil, 0, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.y_utensils)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.b_utensil_remove = QtWidgets.QPushButton(self.t_utensils)
        self.b_utensil_remove.setObjectName("b_utensil_remove")
        self.horizontalLayout_12.addWidget(self.b_utensil_remove)
        self.b_utensil_add = QtWidgets.QPushButton(self.t_utensils)
        self.b_utensil_add.setObjectName("b_utensil_add")
        self.horizontalLayout_12.addWidget(self.b_utensil_add)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.t_utensils, "")
        self.t_steps = QtWidgets.QWidget()
        self.t_steps.setObjectName("t_steps")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.t_steps)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.e_step = QtWidgets.QTextEdit(self.t_steps)
        self.e_step.setObjectName("e_step")
        self.verticalLayout_5.addWidget(self.e_step)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.b_step_add = QtWidgets.QPushButton(self.t_steps)
        self.b_step_add.setObjectName("b_step_add")
        self.horizontalLayout_9.addWidget(self.b_step_add)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.v_steps = QtWidgets.QListWidget(self.t_steps)
        self.v_steps.setObjectName("v_steps")
        self.verticalLayout_5.addWidget(self.v_steps)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.b_step_edit = QtWidgets.QPushButton(self.t_steps)
        self.b_step_edit.setObjectName("b_step_edit")
        self.horizontalLayout_10.addWidget(self.b_step_edit)
        self.b_step_replace = QtWidgets.QPushButton(self.t_steps)
        self.b_step_replace.setObjectName("b_step_replace")
        self.horizontalLayout_10.addWidget(self.b_step_replace)
        self.b_step_remove = QtWidgets.QPushButton(self.t_steps)
        self.b_step_remove.setObjectName("b_step_remove")
        self.horizontalLayout_10.addWidget(self.b_step_remove)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.t_steps, "")
        self.t_notes = QtWidgets.QWidget()
        self.t_notes.setObjectName("t_notes")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.t_notes)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.e_note = QtWidgets.QTextEdit(self.t_notes)
        self.e_note.setObjectName("e_note")
        self.verticalLayout_4.addWidget(self.e_note)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.b_note_add = QtWidgets.QPushButton(self.t_notes)
        self.b_note_add.setObjectName("b_note_add")
        self.horizontalLayout_7.addWidget(self.b_note_add)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.v_notes = QtWidgets.QListWidget(self.t_notes)
        self.v_notes.setObjectName("v_notes")
        self.verticalLayout_4.addWidget(self.v_notes)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.b_note_edit = QtWidgets.QPushButton(self.t_notes)
        self.b_note_edit.setObjectName("b_note_edit")
        self.horizontalLayout_8.addWidget(self.b_note_edit)
        self.b_note_replace = QtWidgets.QPushButton(self.t_notes)
        self.b_note_replace.setObjectName("b_note_replace")
        self.horizontalLayout_8.addWidget(self.b_note_replace)
        self.b_note_remove = QtWidgets.QPushButton(self.t_notes)
        self.b_note_remove.setObjectName("b_note_remove")
        self.horizontalLayout_8.addWidget(self.b_note_remove)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.t_notes, "")
        self.t_tips = QtWidgets.QWidget()
        self.t_tips.setObjectName("t_tips")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.t_tips)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.e_tip = QtWidgets.QTextEdit(self.t_tips)
        self.e_tip.setObjectName("e_tip")
        self.verticalLayout_2.addWidget(self.e_tip)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.b_tip_add = QtWidgets.QPushButton(self.t_tips)
        self.b_tip_add.setObjectName("b_tip_add")
        self.horizontalLayout_5.addWidget(self.b_tip_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.v_tips = QtWidgets.QListWidget(self.t_tips)
        self.v_tips.setObjectName("v_tips")
        self.verticalLayout_2.addWidget(self.v_tips)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.b_tip_edit = QtWidgets.QPushButton(self.t_tips)
        self.b_tip_edit.setObjectName("b_tip_edit")
        self.horizontalLayout_6.addWidget(self.b_tip_edit)
        self.b_tip_replace = QtWidgets.QPushButton(self.t_tips)
        self.b_tip_replace.setObjectName("b_tip_replace")
        self.horizontalLayout_6.addWidget(self.b_tip_replace)
        self.b_tip_remove = QtWidgets.QPushButton(self.t_tips)
        self.b_tip_remove.setObjectName("b_tip_remove")
        self.horizontalLayout_6.addWidget(self.b_tip_remove)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.t_tips, "")
        self.t_variations = QtWidgets.QWidget()
        self.t_variations.setObjectName("t_variations")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.t_variations)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.e_variation = QtWidgets.QTextEdit(self.t_variations)
        self.e_variation.setObjectName("e_variation")
        self.verticalLayout_3.addWidget(self.e_variation)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.b_variation_add = QtWidgets.QPushButton(self.t_variations)
        self.b_variation_add.setObjectName("b_variation_add")
        self.horizontalLayout_3.addWidget(self.b_variation_add)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.v_variations = QtWidgets.QListWidget(self.t_variations)
        self.v_variations.setObjectName("v_variations")
        self.verticalLayout_3.addWidget(self.v_variations)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.b_variation_edit = QtWidgets.QPushButton(self.t_variations)
        self.b_variation_edit.setObjectName("b_variation_edit")
        self.horizontalLayout_4.addWidget(self.b_variation_edit)
        self.b_variation_replace = QtWidgets.QPushButton(self.t_variations)
        self.b_variation_replace.setObjectName("b_variation_replace")
        self.horizontalLayout_4.addWidget(self.b_variation_replace)
        self.b_variation_remove = QtWidgets.QPushButton(self.t_variations)
        self.b_variation_remove.setObjectName("b_variation_remove")
        self.horizontalLayout_4.addWidget(self.b_variation_remove)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.t_variations, "")
        self.t_rating = QtWidgets.QWidget()
        self.t_rating.setObjectName("t_rating")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.t_rating)
        self.verticalLayout.setObjectName("verticalLayout")
        self.e_rating = QtWidgets.QTextEdit(self.t_rating)
        self.e_rating.setObjectName("e_rating")
        self.verticalLayout.addWidget(self.e_rating)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.b_rating_add = QtWidgets.QPushButton(self.t_rating)
        self.b_rating_add.setObjectName("b_rating_add")
        self.horizontalLayout_2.addWidget(self.b_rating_add)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.v_ratings = QtWidgets.QListWidget(self.t_rating)
        self.v_ratings.setObjectName("v_ratings")
        self.verticalLayout.addWidget(self.v_ratings)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.b_rating_edit = QtWidgets.QPushButton(self.t_rating)
        self.b_rating_edit.setObjectName("b_rating_edit")
        self.horizontalLayout.addWidget(self.b_rating_edit)
        self.b_rating_replace = QtWidgets.QPushButton(self.t_rating)
        self.b_rating_replace.setObjectName("b_rating_replace")
        self.horizontalLayout.addWidget(self.b_rating_replace)
        self.b_rating_remove = QtWidgets.QPushButton(self.t_rating)
        self.b_rating_remove.setObjectName("b_rating_remove")
        self.horizontalLayout.addWidget(self.b_rating_remove)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.t_rating, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuMen = QtWidgets.QMenu(self.menuBar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menuBar)
        self.ma_close = QtWidgets.QAction(MainWindow)
        self.ma_close.setObjectName("ma_close")
        self.ma_information = QtWidgets.QAction(MainWindow)
        self.ma_information.setObjectName("ma_information")
        self.menuMen.addAction(self.ma_information)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.ma_close)
        self.menuBar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.e_recipe_name, self.e_servings)
        MainWindow.setTabOrder(self.e_servings, self.e_time)
        MainWindow.setTabOrder(self.e_time, self.e_rating_overall)
        MainWindow.setTabOrder(self.e_rating_overall, self.e_url)
        MainWindow.setTabOrder(self.e_url, self.e_category)
        MainWindow.setTabOrder(self.e_category, self.e_ingredient)
        MainWindow.setTabOrder(self.e_ingredient, self.c_heading)
        MainWindow.setTabOrder(self.c_heading, self.e_amount)
        MainWindow.setTabOrder(self.e_amount, self.v_ingredients)
        MainWindow.setTabOrder(self.v_ingredients, self.e_utensil)
        MainWindow.setTabOrder(self.e_utensil, self.v_utensils)
        MainWindow.setTabOrder(self.v_utensils, self.e_step)
        MainWindow.setTabOrder(self.e_step, self.v_steps)
        MainWindow.setTabOrder(self.v_steps, self.e_note)
        MainWindow.setTabOrder(self.e_note, self.v_notes)
        MainWindow.setTabOrder(self.v_notes, self.e_tip)
        MainWindow.setTabOrder(self.e_tip, self.v_tips)
        MainWindow.setTabOrder(self.v_tips, self.e_variation)
        MainWindow.setTabOrder(self.e_variation, self.v_variations)
        MainWindow.setTabOrder(self.v_variations, self.e_rating)
        MainWindow.setTabOrder(self.e_rating, self.v_ratings)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WikiCookBook"))
        self.b_create.setText(_translate("MainWindow", "Rezept erstellen"))
        self.b_cancel.setText(_translate("MainWindow", "Abbrechen"))
        self.l_rating.setText(_translate("MainWindow", "Bewertung"))
        self.l_url.setText(_translate("MainWindow", "Link"))
        self.l_recipe_name.setText(_translate("MainWindow", "Rezeptname"))
        self.l_servings.setText(_translate("MainWindow", "Portionen"))
        self.l_zeit.setText(_translate("MainWindow", "Zeit"))
        self.l_category.setText(_translate("MainWindow", "Kategorie"))
        self.b_category_remove.setText(_translate("MainWindow", "Ausgewähltes entfernen"))
        self.b_category_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_basics), _translate("MainWindow", "Grundsätzliches"))
        item = self.v_ingredients.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Menge"))
        item = self.v_ingredients.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Zutat"))
        self.l_ingredient.setText(_translate("MainWindow", "Zutat"))
        self.l_amount.setText(_translate("MainWindow", "Menge"))
        self.c_heading.setText(_translate("MainWindow", "Zwischenüberschrift"))
        self.b_ingredient_remove.setText(_translate("MainWindow", "Ausgewähltes entfernen"))
        self.b_ingredient_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_ingredients), _translate("MainWindow", "Zutaten"))
        self.l_utensil.setText(_translate("MainWindow", "Utensil"))
        self.b_utensil_remove.setText(_translate("MainWindow", "Ausgewähltes entfernen"))
        self.b_utensil_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_utensils), _translate("MainWindow", "Küchenutensilien"))
        self.b_step_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.b_step_edit.setText(_translate("MainWindow", "Bearbeiten"))
        self.b_step_replace.setText(_translate("MainWindow", "Ersetzen"))
        self.b_step_remove.setText(_translate("MainWindow", "Entfernen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_steps), _translate("MainWindow", "Zubereitung"))
        self.b_note_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.b_note_edit.setText(_translate("MainWindow", "Bearbeiten"))
        self.b_note_replace.setText(_translate("MainWindow", "Ersetzen"))
        self.b_note_remove.setText(_translate("MainWindow", "Entfernen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_notes), _translate("MainWindow", "Notizen"))
        self.b_tip_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.b_tip_edit.setText(_translate("MainWindow", "Bearbeiten"))
        self.b_tip_replace.setText(_translate("MainWindow", "Ersetzen"))
        self.b_tip_remove.setText(_translate("MainWindow", "Entfernen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_tips), _translate("MainWindow", "Tipps"))
        self.b_variation_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.b_variation_edit.setText(_translate("MainWindow", "Bearbeiten"))
        self.b_variation_replace.setText(_translate("MainWindow", "Ersetzen"))
        self.b_variation_remove.setText(_translate("MainWindow", "Entfernen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_variations), _translate("MainWindow", "Variantionen"))
        self.b_rating_add.setText(_translate("MainWindow", "Hinzufügen"))
        self.b_rating_edit.setText(_translate("MainWindow", "Bearbeiten"))
        self.b_rating_replace.setText(_translate("MainWindow", "Ersetzen"))
        self.b_rating_remove.setText(_translate("MainWindow", "Entfernen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.t_rating), _translate("MainWindow", "Bewertung"))
        self.menuMen.setTitle(_translate("MainWindow", "Me&nü"))
        self.ma_close.setText(_translate("MainWindow", "&Schließen"))
        self.ma_information.setText(_translate("MainWindow", "Informationen"))
