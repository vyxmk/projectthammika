
from PyQt5 import QtCore, QtGui, QtWidgets 
import sqlite3
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(QtCore.QSize(610, 450))
        MainWindow.resize(610, 450)
        MainWindow.setStyleSheet("background-color: rgb(252, 255, 217);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delbut = QtWidgets.QPushButton(self.centralwidget)
        self.delbut.setGeometry(QtCore.QRect(75, 380, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.delbut.setFont(font)
        self.delbut.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.delbut.setObjectName("delbut")
        self.clearbut = QtWidgets.QPushButton(self.centralwidget)
        self.clearbut.setGeometry(QtCore.QRect(245, 380, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.clearbut.setFont(font)
        self.clearbut.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.clearbut.setObjectName("clearbut")
        self.ggbut = QtWidgets.QPushButton(self.centralwidget)
        self.ggbut.setGeometry(QtCore.QRect(410, 380, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.ggbut.setFont(font)
        self.ggbut.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.ggbut.setObjectName("ggbut")
        self.addbut = QtWidgets.QPushButton(self.centralwidget)
        self.addbut.setGeometry(QtCore.QRect(450, 85, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.addbut.setFont(font)
        self.addbut.setStyleSheet("background-color: rgb(234, 227, 174);")
        self.addbut.setObjectName("addbut")
        self.datelabel = QtWidgets.QLabel(self.centralwidget)
        self.datelabel.setGeometry(QtCore.QRect(270, 100, 50, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.datelabel.setFont(font)
        self.datelabel.setStyleSheet("\n"
"color: rgb(144, 112, 37);")
        self.datelabel.setObjectName("datelabel")
        self.tasklabel = QtWidgets.QLabel(self.centralwidget)
        self.tasklabel.setGeometry(QtCore.QRect(60, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tasklabel.setFont(font)
        self.tasklabel.setStyleSheet("\n"
"color: rgb(144, 112, 37);")
        self.tasklabel.setObjectName("tasklabel")
        self.todolistlabel = QtWidgets.QLabel(self.centralwidget)
        self.todolistlabel.setGeometry(QtCore.QRect(0, 0, 600, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.todolistlabel.setFont(font)
        self.todolistlabel.setStyleSheet("\n"
"color: rgb(144, 112, 37);\n"
"font: 75 48pt \"Century Gothic\";")
        self.todolistlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.todolistlabel.setObjectName("todolistlabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 90, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 155, 430, 185))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0,120)
        self.tableWidget.setColumnWidth(1,260)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.infolabel = QtWidgets.QLabel(self.centralwidget)
        self.infolabel.setGeometry(QtCore.QRect(0, 130, 611, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.infolabel.setFont(font)
        self.infolabel.setText("")
        self.infolabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infolabel.setObjectName("infolabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 90, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.addbut.clicked.connect(self.add_task)
        self.clearbut.clicked.connect(self.clear_task)
        self.connect_database()


    def connect_database(self):
        global db, db_cursor, tasks, dates, x , rows
        db = sqlite3.connect("alltask.db")
        db_cursor = db.cursor()
        try:
            db_cursor.execute("CREATE TABLE to_do (id INTEGER PRIMARY KEY AUTOINCREMENT,task text,date text)")
        except:
            pass

        db_cursor.execute("SELECT * FROM to_do")

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        data = db_cursor.fetchall()
        #add tasks from database to the table
        for r1 in range(len(data)):
            item = data[r1]
            item = list(item)
            self.tableWidget.insertRow(r1)
            self.tableWidget.setItem(r1, 0, QtWidgets.QTableWidgetItem(item[2]))
            self.tableWidget.setItem(r1, 1, QtWidgets.QTableWidgetItem(item[1]))



        
    def add_task(self):
        new_task = self.lineEdit.text()
        new_date = self.lineEdit_2.text()
        if len(new_task) == 0 or len(new_date) == 0:
            self.infolabel.setText("Please enter a task and a date")
            return None
    
        self.infolabel.setText("")
        db_cursor.execute("INSERT INTO to_do(task,date) VALUES (:task,:date)",{'task':new_task,'date':new_date})
        db.commit()
        
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

        self.connect_database()
        
    def clear_task(self):
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.delbut.setText(_translate("MainWindow", "DELETE"))
        self.clearbut.setText(_translate("MainWindow", "CLEAR"))
        self.ggbut.setText(_translate("MainWindow", "GOOGLE \n"
"CALENDAR"))
        self.addbut.setText(_translate("MainWindow", "ADD"))
        self.datelabel.setText(_translate("MainWindow", "DATE :"))
        self.tasklabel.setText(_translate("MainWindow", "TASK :"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "xx/xx/xxxx"))
        self.todolistlabel.setText(_translate("MainWindow", "TO DO LIST"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TASK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
