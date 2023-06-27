import serial
import time


arduino_pult = serial.Serial("COM36", 115200)
time.sleep(3)


def receive():
    data = arduino_pult.readline()
    data = data.decode(errors='replace')
    data = data.strip()
    list_numbers = [0, 0]
    try:
        if data[0] == 's':
            data_str = data[1:]
            list_str = data_str.split(',')
            list_numbers[0] = int(list_str[0])
            list_numbers[1] = int(list_str[1])
            print(list_numbers)
    except:
        print("Error")

while True:
    receive()
