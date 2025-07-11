from ultralytics import YOLO

# Cette commande télécharge et charge automatiquement le modèle
model = YOLO('yolov8n.pt')

print("✅ Modèle YOLOv8n téléchargé avec succès.")
