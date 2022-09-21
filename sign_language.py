import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here   
            finger_fold_status = []
            for tip in fingerTips:
                x,y = int(im_list[tip].x*w),int(im_list[tip].y*h)
                cv2.circle(img, (x,y), 15, (255,0,0), cv2.FILLED)
                 
                if im_list[tip].x < im_list[tip - 3].x:
                    cv2.circle(img, (x,y), 15,(0,255,0, cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)

            if all(finger_fold_status):
                if im_list[thumb_tip].y < im_list[thumb_tip - 1].y < im_list[thumb_tip-2].y:
                    print("LIKE") 
                    cv2.putText(img, "LIKE", (20,30), cv2.FRONT_HERSHY_SIMPLEX, 1, (0,255,0), 3)  

                if im_list[thumb_tip].y > im_list[thumb_tip - 1].y > im_list[thumb_tip-2].y:
                    print("DISLIKE") 
                    cv2.putText(img, "DISLIKE", (20,30), cv2.FRONT_HERSHY_SIMPLEX, 1, (0,0,255), 3)   


            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)