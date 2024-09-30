import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from PIL import Image
import pytesseract

# Load the model and tokenizer from Hugging Face
model_name = "ColPali/Qwen2-VL"  # Update this to the correct model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using Hugging Face OCR model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        # Convert the uploaded file to a PIL image
        img = Image.open(uploaded_file)
        
        # Use Tesseract for initial OCR extraction
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')
        
        # Here, you can add logic to process the extracted text with the Hugging Face model if needed
        
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
