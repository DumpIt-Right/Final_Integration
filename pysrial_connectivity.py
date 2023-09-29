import serial.tools.list_ports 
import silence_tensorflow.auto 
import local_img_classifier as lic
import serial
import time

# Connect to the serial port
ports = list(serial.tools.list_ports.comports())

port = None
for p in ports: 
    port = str(p).split(' ')[0]


#time.sleep(0)

user = serial.Serial(port,"115200") 

output = lic.get_value()

match output:
    case "cardboard":
        user.write("1".encode())
    case "glass":
        user.write("2".encode())
    case "metal":
        user.write("3".encode())
    case "paper":
        user.write("4".encode())
    case "plastic":
        user.write("5".encode())


#time.sleep(0)
