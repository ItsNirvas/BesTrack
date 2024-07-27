# teste Isa
 
import cv2
import mediapipe as mp

# Inicializa MediaPipe Pose.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Inicializa MediaPipe Drawing.
mp_drawing = mp.solutions.drawing_utils

# Especifique o caminho completo do seu vídeo - todas as "\" trocar pelas "/" para dar certo
video_path = 'C:/Users/isabe/Downloads/WhatsApp Video 2024-07-23 at 15.56.11.mp4'

# Abre o vídeo.
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente.
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Verifica as dimensões do vídeo.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'Largura do vídeo: {frame_width}, Altura do vídeo: {frame_height}')

# Cria uma janela redimensionável, no meu precisou disso pra abrir certinho o video na janela e nao cortar
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', frame_width, frame_height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Verifica as dimensões do frame.
    h, w, _ = frame.shape
    print(f'Largura do frame: {w}, Altura do frame: {h}')

    # Converte a imagem BGR para RGB.
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Faz a detecção da pose.
    results = pose.process(image_rgb)


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
        leftWrist_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * frame_width)
        leftWrist_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * frame_height)
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
        leftThumb_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB].x * frame_width)
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
        leftFootIndex_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x * frame_width)
        leftFootIndex_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y * frame_height)
        rightFootIndex_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x * frame_width)
        rightFootIndex_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y * frame_height)

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

        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)


    except:
        pass       

    # Mostra o frame com as landmarks desenhadas.
    cv2.imshow('Video', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera os recursos.
cap.release()
cv2.destroyAllWindows()
