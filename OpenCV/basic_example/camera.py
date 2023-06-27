# pip install opencv-python 

import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)
#video_cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#video_cap = cv2.VideoCapture('http://192.168.1.84:4747/video')

while True:
    success, frame = video_cap.read()
    if not success:
        print("YOU HAVE PROBLEM VITH CAMERA!!! (CODE DONT HAVE VIDEO)")
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows()