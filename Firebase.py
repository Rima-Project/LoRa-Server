import pyrebase
import time

Config = {
    "apiKey": "AIzaSyAl1eqO0UNJRekP7qNTXKbHiKRD7Cn-dFQ",
    "authDomain": "gateway-status.firebaseapp.com",
    "databaseURL": "https://gateway-status.firebaseio.com",
    "projectId": "gateway-status",
    "storageBucket": "gateway-status.appspot.com",
    "messagingSenderId": "781856594344",
    "appId": "1:781856594344:web:aaa6d9a2a9da9f2aaee59d",
    "measurementId": "G-Y5JK6K2N8D"
  }

firebase = pyrebase.initialize_app(Config)

Data = firebase.database()
for i in range(3):
	Data.child().push({"Var1":"10","Var2":"20","Var3":"30"})
	time.sleep(3)
