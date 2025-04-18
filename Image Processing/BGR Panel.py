import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.namedWindow("panel")

cv2.createTrackbar("R","panel",0,255,nothing)
cv2.createTrackbar("G","panel",0,255,nothing)
cv2.createTrackbar("B","panel",0,255,nothing)
cv2.createTrackbar("ON/OFF","panel",0,1,nothing)


while (True):
    cv2.imshow("panel",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
    else:
        red=cv2.getTrackbarPos("R","panel")
        green=cv2.getTrackbarPos("G","panel")
        blue=cv2.getTrackbarPos("B","panel")
        on_off=cv2.getTrackbarPos("ON/OFF","panel")

        if on_off==0:
            img[:]=0
        else:
            img[:]=[red,green,blue]# img[:] şeklinde yazmak gerek numpy dizisi olarak kalması için img yazarsın klasik diziye dönüşüyor ve çalışmıyor.
