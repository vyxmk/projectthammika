from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox

import sqlite3

from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
import pickle
import os
from pprint import pprint

import datetime
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
        self.clearbut.setGeometry(QtCore.QRect(240, 380, 120, 40))
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
        self.tableWidget.setGeometry(QtCore.QRect(90, 160, 430, 190))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0,120)
        self.tableWidget.setColumnWidth(1,270)
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
        
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(330, 90, 100, 30))
        self.dateEdit.setStyleSheet("font: 9pt \"Century Gothic\";")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(datetime.now().date())
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        
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
        self.delbut.clicked.connect(self.remove_task)
        self.ggbut.clicked.connect(self.create)
        self.connect_database()
        
        
        
    def connect_database(self):
        global db, db_cursor
        
        #create a database or connect
        db = sqlite3.connect("task.db")
        
        # cursor create
        db_cursor = db.cursor()
        
        #create table
        try:
            db_cursor.execute("CREATE TABLE to_do (task text,date text)")
        except:
            pass

        db_cursor.execute("SELECT * FROM to_do order by date desc")

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        data = db_cursor.fetchall()
        #add tasks from database to the table
        for r1 in range(len(data)):
            item = data[r1]
            item = list(item)
            self.tableWidget.insertRow(r1)
            self.tableWidget.setItem(r1, 0, QtWidgets.QTableWidgetItem(item[1]))
            self.tableWidget.setItem(r1, 1, QtWidgets.QTableWidgetItem(item[0]))
        

    
    def add_task(self):
        new_task = self.lineEdit.text()
        new_date = self.dateEdit.date()
        new_date = new_date.toPyDate()
        
        
        if len(new_task) == 0 == 0:
            self.infolabel.setText("Please type in a task")
            return None
        
        self.infolabel.setText("")
        db_cursor.execute("INSERT INTO to_do(task,date) VALUES (:task,:date)",{'task':new_task,'date':new_date})
        db.commit()
        
        self.lineEdit.setText("")
        self.dateEdit.setDate(datetime.now().date())
        
        self.connect_database()
        
        
    def remove_task(self):
        selected = self.tableWidget.selectedItems()
        # delete row from data
        for index in selected:
            name = self.tableWidget.item(index.row(),1)
            date = self.tableWidget.item(index.row(),0)
            db_cursor.execute(f"DELETE FROM to_do WHERE task = '{name.text()}' AND date = '{date.text()}'")
            db.commit()
            
            self.tableWidget.removeRow(index.row())
          
            
        
    def clear_task(self):
            # clear from database
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            
            db_cursor.execute("DELETE FROM to_do")
            db.commit()
            
    
     
     
    #start  ggcalenndar  
    def create(self):
        selected = self.tableWidget.selectedItems()
        
        
        def Create_Service(client_secret_file, api_name, api_version, *scopes, prefix=''):
            CLIENT_SECRET_FILE = client_secret_file
            API_SERVICE_NAME = api_name
            API_VERSION = api_version
            SCOPES = [scope for scope in scopes[0]]
        
            cred = None
            working_dir = os.getcwd()
            token_dir = 'token files'
            pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.pickle'

            ### Check if token dir exists first, if not, create the folder
            if not os.path.exists(os.path.join(working_dir, token_dir)):
                os.mkdir(os.path.join(working_dir, token_dir))

            if os.path.exists(os.path.join(working_dir, token_dir, pickle_file)):
                with open(os.path.join(working_dir, token_dir, pickle_file), 'rb') as token:
                    cred = pickle.load(token)

            if not cred or not cred.valid:
                if cred and cred.expired and cred.refresh_token:
                    cred.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                    cred = flow.run_local_server()

                with open(os.path.join(working_dir, token_dir, pickle_file), 'wb') as token:
                    pickle.dump(cred, token)

            try:
                service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
                print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
                return service
            except Exception as e:
                print(e)
                print(f'Failed to create service instance for {API_SERVICE_NAME}')
                os.remove(os.path.join(working_dir, token_dir, pickle_file))
                return None

            
        CLIENT_SECRET_FILE = "client_secret.json"
        API_SERVICE_NAME = "calendar"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/calendar"]

        service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


        #create new task/event
            
        def create_event(start_time, summary):
            
            start_time = start_time
            end_time = start_time
            summary = summary
 
            tasks = {
            'summary': summary,
            'start': {
            'date': start_time.strftime("%Y-%m-%d"),
            'timeZone': 'Asia/Bangkok',
            },
            'end': {
            'date': end_time.strftime("%Y-%m-%d"),
            'timeZone': 'Asia/Bangkok',
            },
            
        }

            return service.events().insert(calendarId = 'primary', body=tasks).execute()
        

        # add to calendar
        selected = self.tableWidget.selectedItems()
        for index in selected:
            name = self.tableWidget.item(index.row(),1)
            date = self.tableWidget.item(index.row(),0)
            print(f"{name.text()}  : {date.text()}")
            create_event(datetime(int(date.text().split("-")[0]), int(date.text().split("-")[1]),int(date.text().split("-")[2])), f"{name.text()}")
            
    
            #popupbox
            box = QMessageBox()
            box.setWindowTitle("Created Task !!")
            box.setText("Your Task Has Been Created !")
            x = box.exec_()
   


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do-List"))
        self.delbut.setText(_translate("MainWindow", "DELETE"))
        self.clearbut.setText(_translate("MainWindow", "CLEAR"))
        self.ggbut.setText(_translate("MainWindow", "GOOGLE \n"
"CALENDAR"))
        self.addbut.setText(_translate("MainWindow", "ADD"))
        self.datelabel.setText(_translate("MainWindow", "DATE :"))
        self.tasklabel.setText(_translate("MainWindow", "TASK :"))
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
