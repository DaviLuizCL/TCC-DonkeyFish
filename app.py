import cv2
from ultralytics import YOLO

# Carrega o modelo (pré-treinado com COCO, detecta pessoas entre outras coisas)
model = YOLO("yolov8n.pt")  # Pode usar yolov8s.pt ou yolov8m.pt pra mais precisão

# Define a "linha d'água"
WATER_LINE_Y = 300  # ajustar conforme necessário

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]  # Pega a primeira imagem (frame)
    
    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:  # 0 é a classe "person" no COCO
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            person_height = y2 - y1
            submersion = y2 - WATER_LINE_Y

            # Calcula fração do corpo abaixo da linha
            ratio = max(submersion / person_height, 0) if person_height > 0 else 0

            # Desenha a bounding box
            color = (0, 0, 255) if ratio > 0.5 else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Se mais da metade estiver submersa, avisa
            if ratio > 0.5:
                cv2.putText(
                    frame, "QUEDA DETECTADA", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2
                )

    # Desenha a linha d'água
    cv2.line(frame, (0, WATER_LINE_Y), (frame.shape[1], WATER_LINE_Y), (255, 0, 0), 2)

    cv2.imshow("Queda com YOLO", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
