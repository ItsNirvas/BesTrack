import cv2
import mediapipe as mp
import numpy as np
import customtkinter as ctk
from tkinter import messagebox

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Função para listar câmeras disponíveis
def listar_cameras():
    index = 0
    arr = []
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
    if camera_index:
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
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                except:
                    pass

                # Atualizar o título da janela com o número da câmera
                cv2.imshow(f'Camera selecionada: {camera_index}', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
    else:
        messagebox.showwarning("Aviso", "Selecione uma câmera antes de iniciar.")

# Configurando a interface gráfica com customtkinter
app = ctk.CTk()
app.geometry("400x200")
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

# Botão para iniciar a câmera selecionada
start_button = ctk.CTkButton(app, text="Iniciar Câmera", command=iniciar_camera)
start_button.pack(pady=10)

# Iniciar a interface
app.mainloop()
