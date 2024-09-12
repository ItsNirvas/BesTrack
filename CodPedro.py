import cv2
from typing import NoReturn
import tkinter as tk
import customtkinter
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

    
def main() -> NoReturn:
    
    def AbrirCamera():
        cap = cv2.VideoCapture(int(camera.get()))
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
                
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                        )               
                
                cv2.imshow('Retorno camera '+camera.get(), image)

                #

            cap.release()
            cv2.destroyAllWindows()
            
    
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    
    app = customtkinter.CTk()
    app.geometry("480x250")
    app.title("Reconhecimento da câmera")
    
    lbl_camera = customtkinter.CTkLabel(app, text="Escolha um dispositivo de captura:", font=customtkinter.CTkFont(size=15, weight="bold"))
    lbl_camera.place(x=125, y=30)
    
    camera = customtkinter.CTkEntry(app, placeholder_text="0, 1, 2...", width=100)
    camera.pack(pady=75, padx=5)                 
    
    ButtonAbrir = customtkinter.CTkButton(app, text="Abrir Camera", command=AbrirCamera)
    ButtonAbrir.pack(pady=10, padx=10)
    
    # ButtonFechar = customtkinter.CTkButton(app, text="Fechar Camera")
    # ButtonFechar.pack(pady=10, padx=10)
    
    app.mainloop()
    
if __name__ == '__main__':
    main()
    
    