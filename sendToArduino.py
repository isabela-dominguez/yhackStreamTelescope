#script will connect through serial to the arduino sending com
import serial
from config import *
#setup arduino connection

def send_to_arduino(command):
    #import serial
    ser = serial.Serial(port_arduino, baudrate = 115200)  # open serial port COM4 FOR ERIC
    print(ser.name)         # check which port was really used
    #ser.baudrate(115200)
    a = ser.write(command.encode())     # write a string
    print("a", a)
    
    #ser.write(b"command")
    print("command 1", command)
    print(command.encode())
    ser.close()             # close port

#val="Y"
#send_to_arduino(val)
