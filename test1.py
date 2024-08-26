from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("C:/MaterialTreinoIA/ModeloTreinado/keras_Model.h5", compile=False)

# Load the labels
class_names = open("C:/MaterialTreinoIA/ModeloTreinado/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        image2 = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

        # Make the image a numpy array and reshape it to the models input shape.
        image2 = np.asarray(image2, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image2 = (image2 / 127.5) - 1
        
        prediction = model.predict(image2)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        
        # Render detections
        if index == 0:       
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(0,0,0), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2) 
                                    )  
        else:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(0,0,0), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2) 
                                    )                  

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()