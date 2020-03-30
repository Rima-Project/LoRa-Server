
import ttn
import time


app_id = "feathertest2019"
access_key = "ttn-account-v2.k3U7mcw7YH2sHQENaerNp8gKmk_56uF_8dA_l1rv8kI"


#def uplink_callback(msg, client):
  #print("Received uplink from ", msg.dev_id)
  #print(msg.counter)

def downlink_callback(mid, client):
  print("Received downlink")


handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
#mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.set_downlink_callback(downlink_callback)
mqtt_client.connect()
#mqtt_client.send(dev_id="test1_utb", pay="AQ==", port=1, conf=False, sched="replace")
time.sleep(60)
mqtt_client.close()










