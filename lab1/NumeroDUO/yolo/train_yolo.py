from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='numero_duo.yolov8/data.yaml',
    epochs=100,
    imgsz=512,
    batch=8,
    device='cpu',
    name='yolo_aimbot'
)