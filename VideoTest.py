import time
import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Path to video files and capture of it
path = '../romanian deadlift_1.mov'
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print('Deu merda na captura do video, linha 15')
    exit()

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=False) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Deu merda na leitura do frame, linha 23")
            exit()

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
            # Give to vars the body coordinates
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
            leftShoulder_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * frame_width)
            leftShoulder_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * frame_height)
            rightShoulder_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * frame_width)
            rightShoulder_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * frame_height)
            leftElbow_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * frame_width)
            leftElbow_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * frame_height)
            rightElbow_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * frame_width)
            rightElbow_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * frame_height)
            leftWrist_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_Wrist].x * frame_width)
            leftWrist_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_Wrist].y * frame_height)
            rightWrist_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * frame_width)
            rightWrist_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * frame_height)
            leftPinky_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY].x * frame_width)
            leftPinky_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY].y * frame_height)
            rightPinky_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x * frame_width)
            rightPinky_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y * frame_height)
            leftIndex_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x * frame_width)
            leftIndex_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y * frame_height)
            rightIndex_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x * frame_width)
            rightIndex_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y * frame_height)
            leftThumb_x = int(results.pose_landmarks.landmark[mp_pose.PodeLandmark.LEFT_THUMB].x * frame_width)
            leftThumb_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB].y * frame_height)
            rightThumb_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB].x * frame_width)
            rightThumb_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB].y * frame_height)
            leftHip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * frame_width)
            leftHip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * frame_height)
            rightHip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * frame_width)
            rightHip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * frame_height)
            leftKnee_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x * frame_width)
            leftKnee_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y * frame_height)
            rightKnee_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * frame_width)
            rightKnee_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * frame_height)
            leftAnkle_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x * frame_width)
            leftAnkle_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y * frame_height)
            rightAnkle_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x * frame_width)
            rightAnkle_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y * frame_height)
            leftHeel_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL].x * frame_width)
            leftHeel_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL].y * frame_height)
            rightHeel_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x * frame_width)
            rightHeel_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y * frame_height)
            leftFootIndex_x = int(results.pose_landmarks.landmark[mp_pose.Landmark.LEFT_FOOT_INDEX].x * frame_width)
            leftFootIndex_y = int(results.pose_landmarks.landmark[mp_pose.Landmark.LEFT_FOOT_INDEX].y * frame_height)
            rightFootIndex_x = int(results.pose_landmarks.landmark[mp_pose.Landmark.RIGHT_FOOT_INDEX].x * frame_width)
            rightFootIndex_y = int(results.pose_landmarks.landmark[mp_pose.Landmark.RIGHT_FOOT_INDEX].y * frame_height)

            # Print coordinates to terminal
            print("---------- COORDS ----------")
            print("Nose Coords: ", nose_x, ",", nose_y)
            print("Right Eye Coords: ", rightEye_x, ",", rightEye_y)
            print("Left Eye Coords: ", leftEye_x, ",", leftEye_y)
            print("Mouth Right Coords: ", mouthRight_x, ",", mouthRight_x)
            print("Mouth Left Coords: ", mouthLeft_x, ",", mouthLeft_y)
            print("Left Shoulder", leftShoulder_x, ",", leftShoulder_y)
            print("Right Shoulder", rightShoulder_x, ",", rightShoulder_y)
            print("Left Elbow", leftElbow_x, ",", leftElbow_y)
            print("Right Elbow", rightElbow_x, ",", rightElbow_y)
            print("Left Wrist", leftWrist_x, ",", leftWrist_y)
            print("Right Wrist", rightWrist_x, ",", rightWrist_y)
            print("Left Pinky", leftPinky_x, ",", leftPinky_y)
            print("Right Pinky", rightPinky_x, ",", rightPinky_y)
            print("Left Index", leftIndex_x, ",", leftIndex_y)
            print("Right Index", rightIndex_x, ",", rightIndex_y)
            print("Left Thumb", leftThumb_x, ",", leftThumb_y)
            print("Right Thumb", rightThumb_x, ",", rightThumb_y)
            print("Left Hip", leftHip_x, ",", leftHip_y)
            print("Right Hip", rightHip_x, ",", rightHip_y)
            print("Left Knee", leftKnee_x, ",", leftKnee_y)
            print("Right Knee", rightKnee_x, ",", rightKnee_y)
            print("Left Ankle", leftAnkle_x, ",", leftAnkle_y)
            print("Right Ankle", rightAnkle_x, ",", rightAnkle_y)
            print("Left Heel", leftHeel_x, ",", leftHeel_y)
            print("Right Heel", rightHeel_x, ",", rightHeel_y)
            print("Left Foot Index", leftFootIndex_x, ",", leftFootIndex_y)
            print("Right Foot Index", rightFootIndex_x, ",", rightFootIndex_y)
            print("---------- END ----------")
            print(" ")
            
            # Definitions for dots and lines (correct and wrong)
            nose_spec1 = mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2)
            nose_spec2 = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
            nose_spec3 = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            
            # Verify nose position and set to draw color lines
            if nose_x >= 325:
                nose_specs = (nose_spec1, nose_spec2)
            else:
                nose_specs = (nose_spec1, nose_spec3)

            # Render detections and define styles of landmarks
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      landmark_drawing_spec=nose_specs[0],
                                      connection_drawing_spec=nose_specs[1])
        except:
            pass
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()