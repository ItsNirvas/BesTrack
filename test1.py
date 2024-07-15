################################################################
##### THIS IS THE BEST PROGRAMMER'S BRANCH, QUIT IT BITCH ######
################################################################

# NECESSARY COMMAND BELOW TO HANDKE THE IMPORTS
# pip install mediapipe opencv-python

import time
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=False) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Obtains the frame size to further use
        frame_width = frame.shape[1]
        frame_height = frame.shape[0]
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks and print them on terminal
        try:
            landmarks = results.pose_landmarks.landmark
            # RIGHT HAND
            nose_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * frame_width)
            nose_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * frame_height)
            rightEye_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].x * frame_width)
            rightEye_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y * frame_height)
            leftEye_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].x * frame_width)
            leftEye_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].y * frame_height)
            mouthRight_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].x * frame_width)
            mouthRight_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].y * frame_height)
            mouthLeft_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT].x * frame_width)
            mouthLeft_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT].y * frame_height)
            print("Nose Coords: ", nose_x, ",", nose_y)
            print("Right Eye Coords: ", rightEye_x, ",", rightEye_y)
            print("Left Eye Coords: ", leftEye_x, ",", leftEye_y)
            print("Mouth Right Coords: ", mouthRight_x, ",", mouthRight_x)
            print("Mouth Left Coords: ", mouthLeft_x, ",", mouthLeft_y)
            print("---------- TIME ----------")
            print(" ")
        except:
            pass
        
        # Render detections and define styles of landmarks
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0,0,0), thickness=2, circle_radius=2), 
                                  mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2) 
                                 )
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()