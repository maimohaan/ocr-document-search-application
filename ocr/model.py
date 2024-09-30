import pytesseract
from PIL import Image
import io
import os

# Set the Tesseract command path, if needed, or rely on the default environment setup.
try:
    pytesseract.pytesseract.tesseract_cmd = os.environ.get("TESSERACT_PATH", "tesseract")
except Exception as e:
    print(f"Error setting Tesseract path: {e}")

def process_image(uploaded_file, languages='eng+hin'):
    """
    Process the uploaded image file and extract text using Pytesseract OCR.
    
    Args:
        uploaded_file (file-like object): The uploaded image file.
        languages (str): Languages to use for OCR (e.g., 'eng+hin' for English and Hindi).
    
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        # Convert the uploaded file to a PIL image
        img = Image.open(io.BytesIO(uploaded_file.read()))  # Handling the uploaded file
        
        # Perform OCR using Pytesseract with the specified languages
        extracted_text = pytesseract.image_to_string(img, lang='*')  # Use '*' to detect all available languages
        
        # Return the extracted text
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
