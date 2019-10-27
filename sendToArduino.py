#script will connect through serial to the arduino sending com
import serial
from config import *
#setup arduino connection
import time

ser = serial.Serial(port_arduino)

def send_to_arduino(command):
    #import serial
      # open serial port COM4 FOR ERIC
            # check which port was really used
    #ser.baudrate(115200)
    #a = ser.write(command.encode())     # write a string
    #ser.write(170)
    #t = int(command)
    #ser.flush()
    #av = ser.availableForWrite()
    #print(av)
    ser.write(command)
    ser.flush()
    #print(l)
    time.sleep(6)
    #print("a", a)
    
    #ser.write(b"command")
    #print("command 1", t.encode())
    #print(command.encode())
    #ser.close()             # close port

#val=170
#send_to_arduino(val)
#val1 = 30
#send_to_arduino(val1)
