import cv2
import easyocr
from ultralytics import YOLO
import requests

# Charger YOLO pour détecter les plaques
model = YOLO("models/yolov8n.pt")  # Ton modèle entraîné

# OCR
reader = easyocr.Reader(['fr'])

cap = cv2.VideoCapture("C:/Users/HP/Desktop/master/backend_gestion_parking/detection/files/vv.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cropped = frame[y1:y2, x1:x2]
            result = reader.readtext(cropped)

            if result:
                plaque_text = result[0][1]
                print("🚗 Plaque détectée :", plaque_text)

                try:
                    # 1. Créer ou ignorer le véhicule (optionnel selon ton besoin réel)
                    payload_vehicule = {
                        "immatricule": plaque_text,
                        "marque": "Inconnue",         # à personnaliser ou auto-déduire
                        "couleur": "Inconnue",        # idem
                        "parking": 1,                 # à adapter si nécessaire
                        "user": 1                     # idem : un user dummy ou auto-détecté
                    }
                    r1 = requests.post("http://localhost:8000/api/vehicule/", json=payload_vehicule)
                    print("✅ Véhicule :", r1.json())

                    # 2. Déclencher entrée ou sortie
                    r2 = requests.post(
                        "http://localhost:8000/api/detecter-entree-sortie/",
                        json={"immatricule": plaque_text}
                    )
                    print("✅ Entrée/Sortie :", r2.json())

                except Exception as e:
                    print("❌ Erreur API :", e)

    try:
        cv2.imshow("Détection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except cv2.error as e:
        print("⚠️ Affichage désactivé (imshow non supporté)")

cap.release()
cv2.destroyAllWindows()
