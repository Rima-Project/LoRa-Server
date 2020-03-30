
import ttn
import pyrebase
import time

Time = ""
Gateway_id = ""
Timestamp = ""
RSSI = ""
SNR = ""
Lat = ""
Lon = "" 
Data_rate = ""
Coding_rate = ""

app_id = "feathertest2019"
access_key = "ttn-account-v2.k3U7mcw7YH2sHQENaerNp8gKmk_56uF_8dA_l1rv8kI"

Config = {
    "apiKey": "AIzaSyCtZ-lMaF5WG85duK4u4ohDudELNDIGDpk",
    "authDomain": "ttn-metadata.firebaseapp.com",
    "databaseURL": "https://ttn-metadata.firebaseio.com",
    "projectId": "ttn-metadata",
    "storageBucket": "ttn-metadata.appspot.com",
    "messagingSenderId": "727803110990",
    "appId": "1:727803110990:web:086b2e0d81c0ab0fb2451f",
    "measurementId": "G-9QQVKH10CL"
    }

firebase = pyrebase.initialize_app(Config)


def uplink_callback(msg, client):
    print("Received uplink from ", msg.dev_id)
    print(msg)
    #print(type(msg))
    print("\n")

    # Extracting Data from TTN msg
    Time = str(msg.metadata.time)
    Gateway_id = str(msg.metadata.gateways[0].gtw_id)
    Timestamp = str(msg.metadata.gateways[0].timestamp)
    RSSI = str(msg.metadata.gateways[0].rssi)
    SNR = str(msg.metadata.gateways[0].snr)
    Lat = str(msg.metadata.gateways[0].latitude)
    Lon = str(msg.metadata.gateways[0].longitude)
    Data_rate = str(msg.metadata.data_rate)
    Coding_rate = str(msg.metadata.coding_rate)
    Rpi_Timestamp = time.ctime()
   

    # Posting Data to Firebase  
    Data_dict = {
        "Time":Time,"Gateway_id":Gateway_id,"Timestamp":Timestamp,"RSSI":RSSI,"SNR":SNR,
	"Latitude":Lat,"Longitude":Lon,"Data_rate":Data_rate,
	"Coding_rate":Coding_rate,"Rpi Timestamp":Rpi_Timestamp}
    #print(Data_dict)	

    db = firebase.database()
    db.child().push(Data_dict)

    # Writing Data on .csv file
    File1 = open("/home/pi/Server_Scripts/Metadata_log.txt","a")
    File1.write("\n")
    File1.write(Time)
    File1.write(",")
    File1.write(Gateway_id)
    File1.write(",")
    File1.write(Timestamp)
    File1.write(",")
    File1.write(RSSI)
    File1.write(",")
    File1.write(SNR)
    File1.write(",")
    File1.write(Lat)
    File1.write(",")
    File1.write(Lon)
    File1.write(",")
    File1.write(Data_rate)
    File1.write(",")
    File1.write(Coding_rate)
    File1.write(",")
    File1.write(Rpi_Timestamp)
    File1.close()    
    

handler = ttn.HandlerClient(app_id, access_key)

while(True):

    # Using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)
    mqtt_client.connect()
    time.sleep(10)
    mqtt_client.close()


