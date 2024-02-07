from ultralytics import YOLO

# Create a new YOLO model from scratch
# model = YOLO('yolov8m.yaml')

# Load a pretrained YOLO model (recommended for training)
model = YOLO('./runs/detect/train/weights/best.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
# results = model.train(data='data.yaml', epochs=300, batch=4)

# Evaluate the model's performance on the validation set
# results = model.val()

# Perform object detection on an image using the model
results = model.predict(source='0',show=True)

# Export the model to ONNX format
# success = model.export(format='onnx')