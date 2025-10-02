# pip install mediapipe opencv-python customtkinter
import cv2
import mediapipe as mp
import numpy as np
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

stop_event = None
capture_thread = None

def listar_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # CV backend on Windows
        if not cap.isOpened():
            cap.release()
            break
        ret, _ = cap.read()
        if ret:
            arr.append(f"Câmera {index}")
        cap.release()
        index += 1
    return arr

def iniciar_camera_thread():
    global capture_thread, stop_event
    if capture_thread and capture_thread.is_alive():
        messagebox.showinfo("Info", "A câmera já está rodando.")
        return

    cam = camera_var.get()
    if not cam:
        messagebox.showwarning("Aviso", "Selecione uma câmera antes de iniciar.")
        return

    try:
        camera_index = int(cam.split()[-1])
    except Exception:
        messagebox.showerror("Erro", "Índice da câmera inválido.")
        return

    # pega o valor do range
    try:
        max_diff = int(range_entry.get())
        if max_diff <= 0:
            max_diff = 30
    except Exception:
        max_diff = 30

    stop_event = threading.Event()
    capture_thread = threading.Thread(target=camera_loop, args=(camera_index, max_diff, stop_event), daemon=True)
    capture_thread.start()
    start_button.configure(state="disabled")
    stop_button.configure(state="normal")

def stop_camera():
    global stop_event
    if stop_event:
        stop_event.set()

def camera_loop(camera_index, max_diff, stop_event_local):
    cap = None
    try:
        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        if not cap.isOpened():
            tk.messagebox.showerror("Erro", "Não foi possível abrir a câmera selecionada.")
            return

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=False) as pose:
            while cap.isOpened() and not stop_event_local.is_set():
                ret, frame = cap.read()
                if not ret:
                    # pequeno sleep para evitar loop 100% CPU se frame falhar
                    time.sleep(0.01)
                    continue

                frame_width = frame.shape[1]
                frame_height = frame.shape[0]

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = pose.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.pose_landmarks:
                    try:
                        landmarks = results.pose_landmarks.landmark
                        leftShoulder_x = int(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].x * frame_width)
                        leftHip_x = int(landmarks[mp_pose.PoseLandmark.LEFT_HIP].x * frame_width)
                        rightShoulder_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * frame_width)
                        rightHip_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x * frame_width)

                        if abs(leftShoulder_x - leftHip_x) <= max_diff and abs(rightShoulder_x - rightHip_x) <= max_diff:
                            spec = mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
                            conn_spec = mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
                        else:
                            spec = mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
                            conn_spec = mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

                        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                  landmark_drawing_spec=spec,
                                                  connection_drawing_spec=conn_spec)
                    except Exception as e:
                        # só loga no console pra não travar a thread
                        print("Erro durante processamento de landmarks:", e)

                cv2.imshow(f'Câmera Selecionada: {camera_index}', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

    except Exception as exc:
        # mostra erro pro usuário se deu merda
        print("Erro na thread de captura:", exc)
        try:
            tk.messagebox.showerror("Erro", f"Ocorreu um erro na captura: {exc}")
        except:
            pass
    finally:
        if cap:
            cap.release()
        cv2.destroyAllWindows()
        # reabilita botões na GUI principal (tem que usar .after pra tocar na thread do Tk)
        try:
            app.after(0, lambda: start_button.configure(state="normal"))
            app.after(0, lambda: stop_button.configure(state="disabled"))
        except:
            pass

def on_closing():
    # pede para a thread parar e depois fecha
    stop_camera()
    # espera um tiquinho pra liberar recursos
    time.sleep(0.2)
    try:
        app.destroy()
    except:
        pass

# GUI
app = ctk.CTk()
app.geometry("500x420")
app.title("Seleção de Câmera")

camera_var = tk.StringVar()

cameras_disponiveis = listar_cameras()
camera_label = ctk.CTkLabel(app, text="Selecione a câmera:")
camera_label.pack(pady=10)

camera_dropdown = ctk.CTkOptionMenu(app, variable=camera_var, values=cameras_disponiveis)
camera_dropdown.pack(pady=10)

range_label = ctk.CTkLabel(app, text="Calibrador do intervalo de margem de erro da AI:")
range_label.pack(pady=10)

range_entry = ctk.CTkEntry(app, placeholder_text="Insira um número entre 25 e 50", width=250)
range_entry.pack(pady=10)

explanation_text = ("Se nenhum valor for inserido, por padrão será 30. "
                    "A utilização de um valor não calibrado pode resultar num software ineficaz e causar lesões.")
explanation_label = ctk.CTkLabel(app, text=explanation_text, wraplength=350, justify='center', text_color="gray")
explanation_label.pack(pady=10)

start_button = ctk.CTkButton(app, text="Iniciar Câmera", command=iniciar_camera_thread)
start_button.pack(pady=(6,4))

stop_button = ctk.CTkButton(app, text="Parar Câmera", command=stop_camera, state="disabled")
stop_button.pack(pady=(0,10))

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
