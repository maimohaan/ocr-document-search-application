import os
import io
from PIL import Image
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
import pytesseract

# Load the tokenizer and model for a publicly available OCR model
tokenizer = AutoTokenizer.from_pretrained("microsoft/beit-base-patch16-224")
model = AutoModelForTokenClassification.from_pretrained("microsoft/beit-base-patch16-224")

# Set Tesseract path for OCR
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using the model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))

        # Use Pytesseract to extract text from the image first
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')

        # Process the extracted text using the model
        inputs = tokenizer(extracted_text, return_tensors="pt", padding=True, truncation=True)

        with torch.no_grad():
            outputs = model(**inputs)

        # Extract logits and convert them to text (adjust based on your model's requirements)
        extracted_logits = outputs.logits.argmax(dim=-1)
        extracted_labels = [model.config.id2label[label.item()] for label in extracted_logits[0]]

        # Combine the labels into a single string (you can modify this as needed)
        final_extracted_text = ' '.join(extracted_labels)

        return final_extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
