import numpy as np
import cv2
import mediapipe as mp
import time

pTime=0
cTime=0



cap = cv2.VideoCapture(0)  


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
#hands objesi sadece rgb kanalda çalışıyor
#static_image_mode false ise hem detect hem track yapıyor, true ise sadece detect yapılıyor
mp_draw = mp.solutions.drawing_utils  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    result = hands.process(rgb_frame)
    #result.multi_hand_landmarks kordinat dönüyor.
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            for id,lm in enumerate(hand_landmarks.landmark):
                
                h,w,d=rgb_frame.shape
                cx,cy=int(lm.x*w),int(lm.y*h),
                print(f"\nID:{id}\nCx:{cx} Cy:{cy}")#idlerin penceredeki pixel değerleri
                if(id==4):
                    cv2.circle(frame,(cx,cy),15,(255,0,0),-1)
                #cv2.circle(frame,(cx,cy),15,(255,0,0),-1)
            #mp_draw.draw_landmarks(frame, hand_landmarks) bu elimizi işaretliyor 0,1,3,4 başparmak.... devam edecek şekilde
            mp_draw.draw_landmarks(frame, hand_landmarks,mp_hands.HAND_CONNECTIONS)
            #mp_hands.HAND_CONNECTIONS el üzerindeki o işaretleri bağlıyor

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),4)
    cv2.imshow("Hand Recognize", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
