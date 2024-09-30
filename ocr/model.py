import os
import io
from PIL import Image
import pytesseract
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use a suitable OCR model, such as microsoft/trocr-base-handwritten
tokenizer = AutoTokenizer.from_pretrained("microsoft/trocr-base-handwritten")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/trocr-base-handwritten")

# Set Tesseract path for OCR
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using the OCR model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))

        # Use Pytesseract to extract the initial text from the image
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')

        # Tokenize the extracted text
        inputs = tokenizer(extracted_text, return_tensors="pt")

        # Generate predictions with the model
        outputs = model.generate(inputs["input_ids"])

        # Decode the model's predictions
        decoded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return decoded_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"

