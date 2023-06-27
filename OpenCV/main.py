import cv2

video_cap = cv2.VideoCapture(0)

while True:
    success, frame = video_cap.read()
    if not success:
        print('Ошибка')
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

video_cap.release()
cv2.destroyAllWindows()
