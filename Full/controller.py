import time

import serial

import movement as mv

# порт машинки
# rec = serial.Serial('COM3', 9600)

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
            print(list_ampl)

            ampl_data = list_ampl

            if (ampl_data[0] > 15 and ampl_data[1] < 5):
                mv.rotate_left()

            if (ampl_data[1] > 50 and ampl_data[0] < 3):
                mv.rotate_right()

            if ((ampl_data[0] > 10 and ampl_data[1] > 30) and (ampl_data[0] < 50 and ampl_data[1] < 100)):
                #cam.makeShot()
                print('shot')

    except:
        print("Error")

while True:
    receive()