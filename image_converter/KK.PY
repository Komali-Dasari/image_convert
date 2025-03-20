import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title of the Web App
st.title("Color to Binary Image Converter 🖼️")

# Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to an OpenCV image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Convert to binary
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Display Original and Binary Images
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(binary_image, caption="Binary Image", use_column_width=True, clamp=True)

    # Download Binary Image
    binary_pil = Image.fromarray(binary_image)
    st.download_button(label="Download Binary Image",
                       data=binary_pil.tobytes(),
                       file_name="binary_image.png",
                       mime="image/png")


