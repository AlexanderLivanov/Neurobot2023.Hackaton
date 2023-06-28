# pip install opencv-contrib-python

from time import time
import cv2
import cv2.aruco as aruco
import serial

# import controller as cntrl
import movement as mv

# установка адреса и порта для подключения к DroidCam


arduino_pult = serial.Serial("COM3", 115200)

address = 'http://192.168.205.31:4747/video'

# создание объекта VideoCapture для захвата видео с DroidCam
cap = cv2.VideoCapture(address)
# cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# проверка успешности подключения
if not cap.isOpened():
    print("Ошибка подключения к DroidCam")
    exit()

# задание параметров для определения аруко датчиков
aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
parameters = aruco.DetectorParameters_create()
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
# parameters = aruco.DetectorParameters()
names = []
# цикл для вывода видео с DroidCam и определения аруко датчиков
while True:

    ret, frame = cap.read()

    if not ret:
        print("Ошибка чтения кадра")
        break

    # определение аруко датчиков
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    # отрисовка найденных аруко датчиков
    frame = aruco.drawDetectedMarkers(frame, corners, ids)

    try:
        a = corners[0][0]
        x = (a[0][0] + a[1][0] + a[2][0] + a[3][0]) // 4
        y = (a[0][1] + a[1][1] + a[2][1] + a[3][1]) // 4
        # print(x, " | ", y)
        # print(str(ids))

        name = str(ids)[2:(len(ids) - 3)]
        if name not in names:
            names.append(name)
            if name:
                mv.stop()
                print('управление сдал')
                while True:
                    print('1')
                    data = arduino_pult.readline()
                    data = data.decode(errors='replace')
                    data = data.strip()
                    list_ampl = [0, 0]
                    print('2')
                    try:
                        print('3')
                        if data[0] == 'l':
                            print('4')
                            data_str = data[1:]
                            list_str = data_str.split(',')
                            list_ampl[0] = int(list_str[0])
                            list_ampl[1] = int(list_str[1])
                            print(list_ampl)
                            print('5')

                            ampl_data = list_ampl

                            if (ampl_data[0] > 15 and ampl_data[1] < 5):
                                mv.rotate_left()

                            if (ampl_data[1] > 50 and ampl_data[0] < 3):
                                mv.rotate_right()

                            if ((ampl_data[0] > 10 and ampl_data[1] > 30) and (ampl_data[0] < 50 and ampl_data[1] < 100)):
                                break
                    except IndexError:
                        print("Error")


    except IndexError:
        print('Not found')

    # вывод кадра
    cv2.imshow('DroidCam', frame)

    if cv2.waitKey(1) == ord('w'):
        makeShot()


    def makeShot():
        cv2.imwrite(str(int(time())) + ".jpg", frame)
        print('Shot')


    # выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) == 27:
        break

# освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
