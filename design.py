# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Danil\Desktop\design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(610, 10, 181, 31))
        self.comboBox.addItems(['Поставщик', 'Продукт', 'Заведение', 'Владелец', 'Повар', 'Готовка',
                                'Блюдо', 'Рецепт', 'Ингридиент', 'Гость', 'Столик', 'Официант'])
        self.comboBox.setCurrentIndex(12)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")
        self.DelButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelButton.setGeometry(QtCore.QRect(610, 300, 181, 51))
        self.DelButton.setFont(font)
        self.DelButton.setObjectName("DelButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(610, 140, 181, 51))
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateButton.setGeometry(QtCore.QRect(610, 220, 181, 51))
        self.UpdateButton.setFont(font)
        self.UpdateButton.setObjectName("UpdateButton")
        self.SearchText = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchText.setGeometry(QtCore.QRect(610, 60, 181, 51))
        self.SearchText.setFont(font)
        self.SearchText.setObjectName("SearchText")
        self.LeftButton = QtWidgets.QPushButton(self.centralwidget)
        self.LeftButton.setGeometry(QtCore.QRect(610, 570, 50, 30))
        self.LeftButton.setFont(font)
        self.LeftButton.setObjectName("LeftButton")
        self.RightButton = QtWidgets.QPushButton(self.centralwidget)
        self.RightButton.setGeometry(QtCore.QRect(660, 570, 50, 30))
        self.RightButton.setFont(font)
        self.RightButton.setObjectName("RightButton")
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(655, 545, 30, 30))
        self.Label.setFont(font)
        self.Label.setObjectName("StrLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "База Данных"))
        self.DelButton.setText(_translate("MainWindow", "Удалить"))
        self.SearchButton.setText(_translate("MainWindow", "Поиск"))
        self.UpdateButton.setText(_translate("MainWindow", "Сохранить"))
        self.RightButton.setText(_translate("MainWindow", ">"))
        self.LeftButton.setText(_translate("MainWindow", "<"))
        self.Label.setText(_translate("MainWindow", "1"))

