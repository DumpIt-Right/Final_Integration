import serial.tools.list_ports 
import serial

def PortInit(port, baudrate):
    return serial.Serial(port, baudrate)

def Portlist():
    ports = list(serial.tools.list_ports.comports())
    port = None
    for p in ports: 
        print(str(p).split(' ')[0])

def inputSerial(port, baudrate, data):
    ser = serial.Serial(port, baudrate)
    ser.write(data.encode())
    print(data)

if __name__ == '__main__':
    Portlist()
    # port = input('Enter port = ')
    # baudrate = input('Enter baudrate = ')
    # ser = PortInit('COM4', '115200')
    # inputSerial('COM4', 115200, '1')  

    ser = serial.Serial('COM4', '115200')
    while True:
        data = input('Enter a number between 1 to 5 = ')
        if data == 'q':
            exit(0)
        print(data.encode())
        ser.write(data.encode())
        print(ser.readline())
        # print(data)
