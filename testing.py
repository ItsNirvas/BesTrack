import cv2
import mediapipe as mp
import pandas as pd

# Inicializa MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Inicializa MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Especifique o caminho completo do seu vídeo
video_path = 'C:/Users/vinic/Desktop/TCC/Video Exercises to train AI/Lateral Raise/Videos/lateral raise_1.mov'

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Verifica as dimensões do vídeo
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define os nomes das colunas para cada landmark
columns = []
for landmark in mp_pose.PoseLandmark:
    columns.append(f'{landmark.name}_x')
    columns.append(f'{landmark.name}_y')

# Cria uma lista para armazenar os dados
data = []

# Itera sobre cada frame do vídeo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Converte a imagem BGR para RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Faz a detecção da pose
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        # Inicializa o dicionário para as coordenadas do frame atual
        frame_data = {}
        # Para cada landmark, obtém as coordenadas x e y e adiciona ao dicionário
        for landmark in mp_pose.PoseLandmark:
            x = results.pose_landmarks.landmark[landmark].x * frame_width
            y = results.pose_landmarks.landmark[landmark].y * frame_height
            frame_data[f'{landmark.name}_x'] = x
            frame_data[f'{landmark.name}_y'] = y
        # Adiciona as coordenadas do frame atual à lista de dados
        data.append(frame_data)

    # Desenha os landmarks no frame
    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Mostra o frame com os landmarks desenhados
    cv2.imshow('Video', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()

# Cria o DataFrame com os dados e colunas
df = pd.DataFrame(data, columns=columns)

# Salva o DataFrame como CSV 
# ---- NOME DO ARQUIVO EXCEL ----
df.to_csv('pose_landmarks_data.csv', index=False)
