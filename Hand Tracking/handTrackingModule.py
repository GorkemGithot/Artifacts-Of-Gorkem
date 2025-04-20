import numpy as np
import cv2
import mediapipe as mp
import time




class HandDetector():
    def __init__(self,mode=False,maxNumberOfHands=2,detectionConfidence=0.5,trackConfidence=0.5):
        self.mode=mode
        self.maxNumberOfHands=maxNumberOfHands
        self.detectionConfidence=detectionConfidence
        self.trackConfidence=trackConfidence
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxNumberOfHands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackConfidence
        )
        self.mp_draw = mp.solutions.drawing_utils  
        self.lmList=[]


    def findHands(self,frame,draw=True):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgb_frame)
        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                if(draw):
                    self.mp_draw.draw_landmarks(frame, hand_landmarks,self.mp_hands.HAND_CONNECTIONS)
        return frame
    
    def findPosition(self,frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgb_frame)
        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                for id,lm in enumerate(hand_landmarks.landmark):
                    h,w,d=rgb_frame.shape
                    cx,cy=int(lm.x*w),int(lm.y*h),
                    self.lmList.append([id,cx,cy])
        return self.lmList
        

def main():
    pTime = 0
    cTime = 0
    myHandDetector = HandDetector()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret:
            frame = myHandDetector.findHands(frame)
            list1=myHandDetector.findPosition(frame)
            if len(list1)!=0:
                for a in list1:
                    if a[0]==4:
                        print(a)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 4)
            cv2.imshow("Hand Recognize", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()