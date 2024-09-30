import os
import io
from PIL import Image
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the tokenizer and model for the selected OCR model
model_name = "gpt2"  # Replace with the actual model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Set Tesseract path for OCR
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using the selected OCR model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))
        
        # Here, we will use the selected model to extract text
        inputs = tokenizer(img, return_tensors="pt")
        outputs = model(**inputs)
        extracted_text = outputs.logits.argmax(-1).numpy()

        # Convert extracted text to a human-readable format
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"

