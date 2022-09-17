import cv2 as cv
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def get_landmark(frame):
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        model_complexity=1) as hands:

        results = hands.process(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)
        
            return frame
        
        else:
            return frame

def get_landmark_2():
    cap = cv.VideoCapture(0)

    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        model_complexity=1) as hands:

        while cap.isOpened():
            success, frame = cap.read()

            results = hands.process(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS)
            
            cv.imshow("mp hands", frame)
            
            if cv.waitKey(1) == 27:
                cv.destroyAllWindows()
                cap.release()
                break

if __name__ == "__main__":
    get_landmark_2()