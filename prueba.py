import time

File1 = open("/home/pi/Gateway_scripts/prueba_log.txt","a")
File1.write("\n")
File1.write(time.ctime())


