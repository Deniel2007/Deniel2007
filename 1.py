import cv2
from pprint import pprint

cap = cv2.VideoCapture(0)

while True:
    # ret - получилось ли достать кадр return code
    # frame - сам кадр
    ret, frame = cap.read()
    print(ret)
    print(list(frame))
    for el in frame:
        for i in el:
            print(i,end='')
    # название окна, сам кадр
    cv2.imshow('camera', frame)
    # ожидать нажатия клавиши
    cv2.waitKey(1)
    break