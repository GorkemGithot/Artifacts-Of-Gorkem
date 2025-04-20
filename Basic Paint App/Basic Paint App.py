import numpy as np
import cv2


drawing = False  
mode = False     
ix, iy = -1, -1



def nothing(x):
    pass

img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.namedWindow("panel")

cv2.createTrackbar("R","panel",0,255,nothing)
cv2.createTrackbar("G","panel",0,255,nothing)
cv2.createTrackbar("B","panel",0,255,nothing)
cv2.createTrackbar("ON/OFF","panel",0,1,nothing)


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
            else:
                temp = img.copy()#Boyut ayarlayabildiğimizden orijinal arkaplanı bozmuyoruz kopyasını alıp, onda drawing yapıyoruz.
                cv2.rectangle(temp, (ix, iy), (x, y), (255, 255, 255), -1)
                cv2.imshow("panel", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.circle(img, (x, y), 2, (255, 255,255), -1)
        else:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 255), -1)



cv2.setMouseCallback("panel", draw)#Sürekli  mouse aktivitelerini dinliyor ve event,x,y,flags ve param değerlerini dönüyor.

while True:
    cv2.imshow("panel", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Processing stoped.")
        break
    elif key == ord('m'):
        mode = not mode
        print("Mod exchanged.")
    else:
        red=cv2.getTrackbarPos("R","panel")
        green=cv2.getTrackbarPos("G","panel")
        blue=cv2.getTrackbarPos("B","panel")
        on_off=cv2.getTrackbarPos("ON/OFF","panel")

        if on_off==0:
            pass
        else:
            temp=img
            img[:]=[red,green,blue]# img[:] şeklinde yazmak gerek numpy dizisi olarak kalması için img yazarsın klasik diziye dönüşüyor ve çalışmıyor.
            img=img+temp
cv2.destroyAllWindows()
