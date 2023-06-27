# pip install pyserial
import serial
arduino = serial.Serial("COM11",9600)
print(arduino.in_waiting)
print(arduino.readline())
arduino.write(b'hello')
arduino.close()