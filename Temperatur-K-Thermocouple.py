import os
import time
from datetime import datetime
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit
def loop(ds18b20):

     try: 
        tempWriter = open("/home/pi/Desktop/temperaturLog.txt", "a")
        while True:
         now = datetime.now()
         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
         currTemp = dt_string + "--Temperatur T1 : %0.3f C" % read(ds18b20)[0]
         tempWriter.write(currTemp)
         tempWriter.write("\n")
         print (currTemp)
         time.sleep(0.2)
     except IOError:
        print("Could not open file or directory. Please check USB Stick!")
def kill():
    quit()
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()