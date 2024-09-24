# NECESSARY COMMAND BELOW TO HANDLE THE IMPORTS
# pip install mediapipe opencv-python

import cv2
import mediapipe as mp
import numpy as np
import customtkinter as ctk
from tkinter import messagebox

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

arr = []

# Função para listar câmeras disponíveis
def listar_cameras():
    index = 0
    
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        ret, _ = cap.read()
        if ret:
            arr.append(f"Câmera {index}")
        cap.release()
        index += 1
    return arr

# Função para iniciar a captura de vídeo com a câmera selecionada
def iniciar_camera():
    camera_index = camera_var.get()
    max_diff = 30  # Valor padrão

    # Tentar obter o valor da textbox
    try:
        input_value = int(range_entry.get())
        if input_value > 0:
            max_diff = input_value
    except ValueError:
        pass  # Se não for um número válido, mantém o padrão
    
    if arr.size <= 0:
        messagebox.showwarning("Erro", "Nenhuma camera foi encontrada")
    elif camera_index:
        camera_index = int(camera_index.split()[-1])
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            messagebox.showerror("Erro", "Não foi possível abrir a câmera selecionada.")
            return

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=False) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    continue

                # Obtém o tamanho do frame
                frame_width = frame.shape[1]
                frame_height = frame.shape[0]

                # Recolorir a imagem para RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Fazer a detecção
                results = pose.process(image)

                # Recolorir de volta para BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extrair landmarks e desenhar na imagem
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Pegando coordenadas corporais para cálculo
                    leftShoulder_x = int(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x * frame_width)
                    leftHip_x = int(landmarks[mp_pose.PoseLandmark.LEFT_HIP].x * frame_width)
                    rightShoulder_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * frame_width)
                    rightHip_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x * frame_width)

                    # Definindo estilos de pontos e linhas para correção
                    if abs(leftShoulder_x - leftHip_x) <= max_diff and abs(rightShoulder_x - rightHip_x) <= max_diff:
                        specs = (mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                 mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
                    else:
                        specs = (mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                                 mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))

                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                              landmark_drawing_spec=specs[0],
                                              connection_drawing_spec=specs[1])

                except:
                    pass

                # Atualizar o título da janela com o número da câmera
                cv2.imshow(f'Câmera Selecionada: {camera_index}', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Aviso", "Selecione uma câmera antes de iniciar.")

# Configurando a interface gráfica com customtkinter
app = ctk.CTk()
app.geometry("500x500")
app.title("Seleção de Câmera")

# Variável para armazenar a câmera selecionada
camera_var = ctk.StringVar()

# Listando câmeras disponíveis
cameras_disponiveis = listar_cameras()

# Dropdown para seleção de câmeras
camera_label = ctk.CTkLabel(app, text="Selecione a câmera:")
camera_label.pack(pady=10)

camera_dropdown = ctk.CTkOptionMenu(app, variable=camera_var, values=cameras_disponiveis)
camera_dropdown.pack(pady=10)

# Label e TextBox para calibrador de range
range_label = ctk.CTkLabel(app, text="Calibrador de Range da AI:")
range_label.pack(pady=10)

range_entry = ctk.CTkEntry(app, placeholder_text="Insira o range (25 a 50)", width=200)
range_entry.pack(pady=10)

# Texto explicativo
explanation_text = ("O range costuma ser entre 25 e 50. "
                    "Este valor é para definir a margem de erro levada em consideração pela IA. "
                    "Caso nenhum valor seja inserido, a margem será por padrão 30. "
                    "Esteja ciente de que uma margem fora da recomendada, não testada ou não calibrada anteriormente pode gerar lesões.")
explanation_label = ctk.CTkLabel(app, text=explanation_text, wraplength=350, justify='center', text_color="gray")
explanation_label.pack(pady=10)

# Botão para iniciar a câmera selecionada
start_button = ctk.CTkButton(app, text="Iniciar Câmera", command=iniciar_camera)
start_button.pack(pady=10)

# Iniciar a interface
app.mainloop()
