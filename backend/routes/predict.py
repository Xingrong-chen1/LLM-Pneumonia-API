from fastapi import APIRouter, UploadFile, File
import tensorflow as tf
import numpy as np
import io
from PIL import Image

router = APIRouter()

model = tf.keras.models.load_model("backend/model/cnn_pneumonia.keras")

def preprocess_image(image: Image.Image):
    """ Preprocessing uploaded X-rays """
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """ Process the uploaded X-rays and return the prediction results """
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    
    label = "PNEUMONIA" if prediction[0][0] > 0.5 else "NORMAL"
    confidence = float(prediction[0][0]) if label == "PNEUMONIA" else 1 - float(prediction[0][0])

    return {"diagnosis": label, "confidence": confidence}
