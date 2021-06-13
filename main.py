import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import design
import Db
import os
import hashlib
import re

data = Db.Db(host='localhost', database='cswl1', user='root', password='Danilka210300')
strnumber = 1


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.Choise)
        self.SearchButton.clicked.connect(self.Search)
        self.UpdateButton.clicked.connect(self.Save)
        self.RightButton.clicked.connect(self.Right)
        self.LeftButton.clicked.connect(self.Left)
        self.DelButton.clicked.connect(self.Delete)
        self.SyncButton.clicked.connect(self.SyncDB)

    def Right(self):
        global strnumber
        strnumber += 1
        self.Label.setText(str(strnumber))
        try:
            self.Show(subres=data.Select(main_query=data.last_query, strnumber=strnumber))
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()

    def Left(self):
        global strnumber
        if strnumber == 1:
            return
        strnumber -= 1
        self.Label.setText(str(strnumber))
        try:
            self.Show(subres=data.Select(main_query=data.last_query, strnumber=strnumber))
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()

    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def exec_sql_file(self, cursor, sql_file):
        statement = ""
        for line in open(sql_file, encoding='utf-8'):
            if re.match(r'--', line):
                continue
            if not re.search(r';$', line):
                statement = statement + line
            else:
                statement = statement + line
                try:
                    cursor.execute(statement)
                except:
                    cursor.close()
                statement = ""

    def CreateDb(self):
        directory = os.getcwd()
        files = os.listdir(directory)
        arr = []
        for i in files:
            if i[-4:] == '.sql':
                if len(re.sub('[^0-9]+', '', i)) != 4:
                    QMessageBox.about(self, "Error", "Invalid .sql file name")
                    return
                arr.append(i)
        for i in arr:
            cursor = data.conn.cursor()
            f = open(i)
            cursor.execute(f.read())
            cursor.close()

    def SyncDB(self):
        directory = os.getcwd()
        files = os.listdir(directory)
        arr = []
        for i in files:
            if i[-4:] == '.sql':
                if len(re.sub('[^0-9]+', '', i)) != 4:
                    QMessageBox.about(self, "Error", "Invalid .sql file name")
                    return
                arr.append(i)
        for i in arr:
            cursor = data.conn.cursor()
            try:
                cursor.execute("SELECT * FROM cswl1.files WHERE filename = '%s'" % i)
            except:
                cursor.close()
                self.CreateDb()
                return
            res = cursor.fetchall()
            cursor.close()
            if len(res) == 0:
                cursor = data.conn.cursor()
                try:
                    self.exec_sql_file(cursor, i)
                except:
                    QMessageBox.about(self, "Error!", "Invalid SqlFile %s" % i)
                cursor.close()
                cursor = data.conn.cursor()
                cursor.execute("INSERT INTO cswl1.files(FileName, FileHash)VALUES('%s', '%s')" % (i, self.md5(i)))
                cursor.execute("COMMIT")
                cursor.close()
            else:
                if self.md5(i) == res[0][1]:
                    QMessageBox.about(self, "Message", "You are using the current version of the database")
                    return
                else:
                    QMessageBox.about(self, "Error!", "The content of the file has been changed %s" % i)
                    return
        QMessageBox.about(self, "Message!", "Sync of Database ended")

    def Search(self):
        usl = self.SearchText.text()
        usl = usl.lower()
        self.Show(subres=data.Search(self.comboBox.currentText(), usl))

    def Show(self, subres=None):
        if self.comboBox.currentText() == 'Повар':
            if subres is not None:
                self.ShowCook(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowCook(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Заведение':
            if subres is not None:
                self.ShowCafe(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowCafe(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Готовка':
            if subres is not None:
                self.ShowCreate(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowCreate(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Блюдо':
            if subres is not None:
                self.ShowDish(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowDish(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Ингридиент':
            if subres is not None:
                self.ShowIngridient(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowIngridient(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Владелец':
            if subres is not None:
                self.ShowOwner(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowOwner(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Продукт':
            if subres is not None:
                self.ShowProduct(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowProduct(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Поставщик':
            if subres is not None:
                self.ShowProvider(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowProvider(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Рецепт':
            if subres is not None:
                self.ShowRecipe(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowRecipe(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Столик':
            if subres is not None:
                self.ShowTable(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowTable(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Гость':
            if subres is not None:
                self.ShowVisitor(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowVisitor(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        if self.comboBox.currentText() == 'Официант':
            if subres is not None:
                self.ShowWaiter(subres)
                self.tableWidget.resizeColumnsToContents()
                return
            try:
                self.ShowWaiter(data.Select(table=self.comboBox.currentText(), strnumber=strnumber))
            except:
                QMessageBox.about(self, "Error", "Query Error!")
                data.Close()
        self.tableWidget.resizeColumnsToContents()

    def ShowWaiter(self, result):
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))

    def ShowVisitor(self, result):
        try:
            subres = data.Select(main_query="SELECT idtable FROM cswl1.table")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][0]) == str(result[i][2]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setCellWidget(i, 1, combobox)
        self.tableWidget.setItem(count - 1, 1, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count - 1, 1, combobox)

    def ShowTable(self, result):
        try:
            subres = data.Select(main_query="SELECT idwaiter, waitername FROM cswl1.waiter")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]) + " " + str(subres[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][1]) == str(result[i][2]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setCellWidget(i, 2, combobox)
        self.tableWidget.setItem(count - 1, 2, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count - 1, 2, combobox)

    def ShowRecipe(self, result):
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))

    def ShowProvider(self, result):
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))

    def ShowProduct(self, result):
        try:
            subres = data.Select(main_query="SELECT idprovider, providername FROM cswl1.provider")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]) + " " + str(subres[i][1]))
        try:
            subres1 = data.Select(main_query="SELECT idcafe, cafename FROM cswl1.cafe")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf1 = []
        for i in range(len(subres)):
            buf1.append(str(subres1[i][0]) + " " + str(subres1[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][1]) == str(result[i][2]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            combobox1 = QtWidgets.QComboBox()
            combobox1.addItems(buf1)
            k = 0
            for j in range(len(subres1)):
                if str(subres1[j][1]) == str(result[i][4]):
                    k = j
                    break
            combobox1.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setCellWidget(i, 2, combobox)
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setCellWidget(i, 4, combobox1)
        self.tableWidget.setItem(count - 1, 2, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count - 1, 2, combobox)
        self.tableWidget.setItem(count - 1, 4, QtWidgets.QTableWidgetItem(str(5)))
        combobox1 = QtWidgets.QComboBox()
        combobox1.addItems(buf1)
        self.tableWidget.setCellWidget(count - 1, 4, combobox1)

    def ShowOwner(self, result):
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))

    def ShowIngridient(self, result):
        try:
            recipes = data.Select(main_query="SELECT idrecipe, recipename FROM cswl1.recipe")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        bufrec = []
        for i in range(len(recipes)):
            bufrec.append(str(recipes[i][0]) + " " + str(recipes[i][1]))
        try:
            products = data.Select(main_query="SELECT idproduct, productname FROM cswl1.product")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        bufprod = []
        for i in range(len(products)):
            bufprod.append(str(products[i][0]) + " " + str(products[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            comboboxrec = QtWidgets.QComboBox()
            comboboxrec.addItems(bufrec)
            k = 0
            for j in range(len(recipes)):
                if str(recipes[j][1]) == str(result[i][2]):
                    k = j
                    break
            comboboxrec.setCurrentIndex(k)
            comboboxprod = QtWidgets.QComboBox()
            comboboxprod.addItems(bufprod)
            k = 0
            for j in range(len(products)):
                if str(products[j][1]) == str(result[i][3]):
                    k = j
                    break
            comboboxprod.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setCellWidget(i, 2, comboboxrec)
            self.tableWidget.setCellWidget(i, 3, comboboxprod)
        comboboxrec = QtWidgets.QComboBox()
        comboboxrec.addItems(bufrec)
        self.tableWidget.setCellWidget(count - 1, 2, comboboxrec)
        comboboxprod = QtWidgets.QComboBox()
        comboboxprod.addItems(bufprod)
        self.tableWidget.setCellWidget(count - 1, 3, comboboxprod)

    def ShowDish(self, result):
        try:
            recipes = data.Select(main_query="SELECT idrecipe, recipename FROM cswl1.recipe")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        bufrec = []
        for i in range(len(recipes)):
            bufrec.append(str(recipes[i][0]) + " " + str(recipes[i][1]))
        try:
            visitors = data.Select(main_query="SELECT idvisitor, visitorname FROM cswl1.visitor")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        bufvis = []
        for i in range(len(visitors)):
            bufvis.append(str(visitors[i][0]) + " " + str(visitors[i][1]))
        try:
            crets = data.Select(main_query="SELECT idcreating, creatingtime FROM cswl1.creating")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        bufcr = []
        for i in range(len(crets)):
            bufcr.append(str(crets[i][0]) + " " + str(crets[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            comboboxrec = QtWidgets.QComboBox()
            comboboxrec.addItems(bufrec)
            k = 0
            for j in range(len(recipes)):
                if str(recipes[j][1]) == str(result[i][2]):
                    k = j
                    break
            comboboxrec.setCurrentIndex(k)
            comboboxvis = QtWidgets.QComboBox()
            comboboxvis.addItems(bufvis)
            k = 0
            for j in range(len(visitors)):
                if str(visitors[j][1]) == str(result[i][4]):
                    k = j
                    break
            comboboxvis.setCurrentIndex(k)
            comboboxcr = QtWidgets.QComboBox()
            comboboxcr.addItems(bufcr)
            k = 0
            for j in range(len(crets)):
                if str(crets[j][1]) == str(result[i][3]):
                    k = j
                    break
            comboboxcr.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setCellWidget(i, 2, comboboxrec)
            self.tableWidget.setCellWidget(i, 3, comboboxcr)
            self.tableWidget.setCellWidget(i, 4, comboboxvis)
        comboboxrec = QtWidgets.QComboBox()
        comboboxrec.addItems(bufrec)
        self.tableWidget.setCellWidget(count - 1, 2, comboboxrec)
        comboboxcr = QtWidgets.QComboBox()
        comboboxcr.addItems(bufcr)
        self.tableWidget.setCellWidget(count - 1, 3, comboboxcr)
        comboboxvis = QtWidgets.QComboBox()
        comboboxvis.addItems(bufvis)
        self.tableWidget.setCellWidget(count - 1, 4, comboboxvis)

    def ShowCreate(self, result):
        try:
            subres = data.Select(main_query="SELECT idcook, cookaname FROM cswl1.cook")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]) + " " + str(subres[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][1]) == str(result[i][2]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setCellWidget(i, 1, combobox)
        self.tableWidget.setItem(count - 1, 1, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count - 1, 1, combobox)

    def ShowCafe(self, result):
        try:
            subres = data.Select(main_query="SELECT idowner, ownername FROM cswl1.owner")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]) + " " + str(subres[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][1]) == str(result[i][3]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setCellWidget(i, 3, combobox)
        self.tableWidget.setItem(count - 1, 3, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count - 1, 3, combobox)

    def ShowCook(self, result):
        try:
            subres = data.Select(main_query="SELECT idcafe, cafename FROM cswl1.cafe")
        except:
            QMessageBox.about(self, "Error", "Query Error!")
            data.Close()
            return
        buf = []
        for i in range(len(subres)):
            buf.append(str(subres[i][0]) + " " + str(subres[i][1]))
        self.tableWidget.setRowCount(0)
        count = 1
        for row in result:
            count += 1
        self.tableWidget.setRowCount(count)
        for i in range(len(result)):
            combobox = QtWidgets.QComboBox()
            combobox.addItems(buf)
            k = 0
            for j in range(len(subres)):
                if str(subres[j][1]) == str(result[i][3]):
                    k = j
                    break
            combobox.setCurrentIndex(k)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][3])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][2])))
            self.tableWidget.setCellWidget(i, 2, combobox)
        self.tableWidget.setItem(count-1, 2, QtWidgets.QTableWidgetItem(str(5)))
        combobox = QtWidgets.QComboBox()
        combobox.addItems(buf)
        self.tableWidget.setCellWidget(count-1, 2, combobox)

    def Choise(self, text):
        self.SearchText.setText("")
        global strnumber
        strnumber = 1
        self.Label.setText(str(strnumber))
        if text == 'Поставщик':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Наименование  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Номер телефона  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Продукт':
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Наименование  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Поставщик  "))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(
                "  Количество  "))
            self.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem(
                "  Заведение  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Владелец':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  ФИО  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Номер телефона  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Заведение':
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Название  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Рейтинг  "))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(
                "  Владелец  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Повар':
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  ФИО  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Место работы  "))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(
                "  Разряд  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()

        if text == 'Готовка':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Повар  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Дата и время  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Блюдо':
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Название  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Рецепт  "))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(
                "  Время приготовления  "))
            self.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem(
                "  Гость  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Рецепт':
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("  Номер(Id)  "))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Название  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Ингридиент':
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Номер(Id)"))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Количество  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Рецепт                                                   "))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem(
                "  Продукт                                                  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Гость':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Номер(Id)"))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Номер столика  "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  ФИО                                                                 "
                "                                                         "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Столик':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Номер(Id)"))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  Уровень   "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Официант                                                        "
                "                                                                  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        if text == 'Официант':
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Номер(Id)"))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem(
                "  ФИО                                                                    "
                "                                                                         "))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem(
                "  Стаж  "))
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
        self.Show()

    def Save(self):
        if self.comboBox.currentText() == 'Повар':
            for i in range(self.tableWidget.rowCount()):
                cafe = str(self.tableWidget.cellWidget(i, 2).currentText())
                cafe = cafe[0:cafe.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j != 2:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                    else:
                        atr.append(cafe)
                try:
                    data.Merge('Повар', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()

        if self.comboBox.currentText() == 'Заведение':
            for i in range(self.tableWidget.rowCount()):
                owner = str(self.tableWidget.cellWidget(i, 3).currentText())
                owner = owner[0:owner.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j != 3:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                    else:
                        atr.append(owner)
                try:
                    data.Merge('Заведение', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()

        if self.comboBox.currentText() == 'Готовка':
            for i in range(self.tableWidget.rowCount()):
                cook = str(self.tableWidget.cellWidget(i, 1).currentText())
                cook = cook[0:cook.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j != 1:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                if j != 2:
                                    atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                    else:
                        atr.append(cook)
                try:
                    data.Merge('Готовка', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()

        if self.comboBox.currentText() == 'Блюдо':
            for i in range(self.tableWidget.rowCount()):
                recipe = str(self.tableWidget.cellWidget(i, 2).currentText())
                recipe = recipe[0:recipe.index(" ")]
                creating = str(self.tableWidget.cellWidget(i, 3).currentText())
                creating = creating[0:creating.index(" ")]
                visitor = str(self.tableWidget.cellWidget(i, 4).currentText())
                visitor = visitor[0:visitor.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 2:
                        atr.append(recipe)
                    elif j == 3:
                        atr.append(creating)
                    elif j == 4:
                        atr.append(visitor)
                    else:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                try:
                    data.Merge('Блюдо', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()

        if self.comboBox.currentText() == 'Ингридиент':
            for i in range(self.tableWidget.rowCount()):
                recipe = str(self.tableWidget.cellWidget(i, 2).currentText())
                recipe = recipe[0:recipe.index(" ")]
                product = str(self.tableWidget.cellWidget(i, 3).currentText())
                product = product[0:product.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 2:
                        atr.append(recipe)
                    elif j == 3:
                        atr.append(product)
                    else:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                try:
                    data.Merge('Ингридиент', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Владелец':
            for i in range(self.tableWidget.rowCount()):
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 0 and self.tableWidget.item(i, j) is None:
                        atr.append(0)
                    else:
                        try:
                            atr.append(self.tableWidget.item(i, j).text())
                        except:
                            self.Show()
                            return
                try:
                    data.Merge('Владелец', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Продукт':
            for i in range(self.tableWidget.rowCount()):
                provider = str(self.tableWidget.cellWidget(i, 2).currentText())
                provider = provider[0:provider.index(" ")]
                cafe = str(self.tableWidget.cellWidget(i, 4).currentText())
                cafe = cafe[0:cafe.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 2:
                        atr.append(provider)
                    elif j == 4:
                        atr.append(cafe)
                    else:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                try:
                    data.Merge('Продукт', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Поставщик':
            for i in range(self.tableWidget.rowCount()):
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 0 and self.tableWidget.item(i, j) is None:
                        atr.append(0)
                    else:
                        try:
                            atr.append(self.tableWidget.item(i, j).text())
                        except:
                            self.Show()
                            return
                try:
                    data.Merge('Поставщик', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Рецепт':
            for i in range(self.tableWidget.rowCount()):
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 0 and self.tableWidget.item(i, j) is None:
                        atr.append(0)
                    else:
                        try:
                            atr.append(self.tableWidget.item(i, j).text())
                        except:
                            self.Show()
                            return
                try:
                    data.Merge('Рецепт', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Столик':
            for i in range(self.tableWidget.rowCount()):
                waiter = str(self.tableWidget.cellWidget(i, 2).currentText())
                waiter = waiter[0:waiter.index(" ")]
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j != 2:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                    else:
                        atr.append(waiter)
                try:
                    data.Merge('Столик', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()

        if self.comboBox.currentText() == 'Гость':
            for i in range(self.tableWidget.rowCount()):
                table = str(self.tableWidget.cellWidget(i, 1).currentText())
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 1:
                        atr.append(table)
                    else:
                        if j == 0 and self.tableWidget.item(i, j) is None:
                            atr.append(0)
                        else:
                            try:
                                atr.append(self.tableWidget.item(i, j).text())
                            except:
                                self.Show()
                                return
                try:
                    data.Merge('Гость', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        if self.comboBox.currentText() == 'Официант':
            for i in range(self.tableWidget.rowCount()):
                atr = []
                for j in range(self.tableWidget.columnCount()):
                    if j == 0 and self.tableWidget.item(i, j) is None:
                        atr.append(0)
                    else:
                        try:
                            atr.append(self.tableWidget.item(i, j).text())
                        except:
                            self.Show()
                            return
                try:
                    data.Merge('Официант', atr)
                except:
                    QMessageBox.about(self, "Error!!!", "Invalid Value!")
                    data.Close()
        self.Show()

    def Delete(self):
        string = int(self.tableWidget.currentRow())
        id = str(self.tableWidget.item(string, 0).text())
        try:
            data.Delete(self.comboBox.currentText(), id)
        except:
            QMessageBox.about(self, "Error!!!", "Deleting error")
            data.Close()
        self.Show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':

    main()
