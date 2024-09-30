import os
import io
from PIL import Image
import pytesseract
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
import streamlit as st

# Set the Tesseract path
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"

# Load the tokenizer and model for the General OCR Theory (GOT) model
tokenizer = AutoTokenizer.from_pretrained("your-got-model-name")  # Update with the actual model name
model = AutoModelForTokenClassification.from_pretrained("your-got-model-name")  # Update with the actual model name

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using the General OCR Theory model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))
        
        # Here, we will use the GOT model to extract text
        # Convert the image into a format suitable for the model
        img = img.convert("RGB")  # Ensure image is in RGB format

        # Tokenize the image input
        inputs = tokenizer(img, return_tensors="pt")

        # Perform inference
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the predicted class labels
        logits = outputs.logits
        predicted_classes = logits.argmax(-1).numpy()

        # Convert predicted classes to text (you may need a mapping here based on your model)
        extracted_text = ' '.join(map(str, predicted_classes))  # This may need adjustments based on how you want to format the output

        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
