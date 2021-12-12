


from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import os
import datetime
from pprint import pprint
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from datetime import datetime, timedelta


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(120, 90, 151, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
         

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(self.create)
        
        
    
        
    
    def create(self):
        
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

        if __name__ == '__main__':
            API_NAME = 'calendar'
            API_VERSION = 'v3'
            SCOPES = ['https://www.googleapis.com/auth/calendar']
            CLIENT_FILE = 'client_secret.json'
            service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES, 'x')
            
        CLIENT_SECRET_FILE = "client_secret.json"
        API_SERVICE_NAME = "calendar"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/calendar"]

        service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)


        #create new events

        def create_event(start_time, summary):
            
            start_time = self.lineEdit.text()
            end_time = start_time
            
            summary = self.lineEdit2.text()
 
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
        
    
        create_event(datetime(start_time), summary)
        

        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
