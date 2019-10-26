#script will connect through serial to the arduino sending com
import serial
#setup arduino connection

def send_to_arduino(command="No Val"):
    import serial
    ser = serial.Serial('COM4')  # open serial port
    print(ser.name)         # check which port was really used
    ser.write(b"command")     # write a string
    ser.close()             # close port

val="Y"
send_to_arduino(val)
