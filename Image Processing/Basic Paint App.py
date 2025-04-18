import numpy as np
import cv2


drawing = False  
mode = False     
ix, iy = -1, -1


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.circle(img, (x, y), 2, (50, 50, 50), -1)
            else:
                temp = img.copy()#Boyut ayarlayabildiğimizden orijinal arkaplanı bozmuyoruz kopyasını alıp, onda drawing yapıyoruz.
                cv2.rectangle(temp, (ix, iy), (x, y), (50, 50, 50), -1)
                cv2.imshow("Paint", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.circle(img, (x, y), 2, (50, 50, 50), -1)
        else:
            cv2.rectangle(img, (ix, iy), (x, y), (50, 50, 50), -1)


img = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", draw)#Sürekli  mouse aktivitelerini dinliyor ve event,x,y,flags ve param değerlerini dönüyor.

while True:
    cv2.imshow("Paint", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Processing stoped.")
        break
    elif key == ord('m'):
        mode = not mode
        print("Mod exchanged.")

cv2.destroyAllWindows()
