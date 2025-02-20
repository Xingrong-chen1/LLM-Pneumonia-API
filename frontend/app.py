import os
import streamlit as st
import requests
import io
from PIL import Image


API_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/predict")


st.title("Pneumonia Detection App")
st.write("Upload an X-ray image to predict pneumonia.")


uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded X-ray", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Processing..."):
            
            img_bytes = io.BytesIO()
            image = Image.open(uploaded_file)
            image.save(img_bytes, format="PNG")
            img_bytes = img_bytes.getvalue()

            response = requests.post(
                API_URL,
                files={"file": ("xray.png", img_bytes, "image/png")}
            )

            if response.status_code == 200:
                result = response.json()
                st.success(f"Diagnosis: {result['diagnosis']}")
                st.write(f"Confidence: {result['confidence']:.2f}")
            else:
                st.error("Error: Failed to get prediction.")
