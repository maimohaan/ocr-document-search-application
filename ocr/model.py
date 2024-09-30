import pytesseract
from PIL import Image
import io
import os

# You can check if the Tesseract executable is set up correctly.
# Streamlit Cloud should have it available in the PATH without needing a hardcoded path.
try:
    pytesseract.pytesseract.tesseract_cmd = os.environ.get("TESSERACT_PATH", "tesseract")
except Exception as e:
    print(f"Error setting Tesseract path: {e}")

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using Pytesseract OCR.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        # Convert the uploaded file to a PIL image
        img = Image.open(io.BytesIO(uploaded_file.read()))  # Handling the uploaded file from Gradio
        
        # Perform OCR using Pytesseract
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')
        
        # Return the extracted text
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
