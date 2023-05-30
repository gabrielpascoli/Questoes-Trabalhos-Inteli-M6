from ultralytics import YOLO #importa o ulralytics
import cv2 as cv

video = cv.VideoCapture(0) # abre a camera 
modelo = YOLO('./best.pt') # abre o modelo que foi treinado "best.pt"

while True: # enquanto a camera esteja ligada ele usara do modelo para indentificar as rachaduras 
    ret, frame = video.read()
    result = modelo.predict(frame, conf=0.4) # aplica o modelo no frame e indentifica com confiança de 40%
    if ret:
        frame_resultados = result[0].plot() # identifica os resultados do modelo 
        cv.imshow("Resultados", frame_resultados) # mostra a rachadura 
        if cv.waitKey(1) == ord('f'): # apertando "f" voce fecha o modelo 
            break

video.release()
cv.destroyAllWindows() # parte que fecha o modelo 