import serial
import time


arduino_pult = serial.Serial("COM3", 115200)
time.sleep(3)


def receive():
    data = arduino_pult.readline()
    data = data.decode(errors='replace')
    data = data.strip()
    list_ampl = [0, 0]
    try:
        if data[0] == 'l':
            data_str = data[1:]
            list_str = data_str.split(',')
            list_ampl[0] = int(list_str[0])
            list_ampl[1] = int(list_str[1])
            #print(list_ampl)
    except:
        print("Error")

while True:
    receive()
