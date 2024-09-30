import pytesseract
from PIL import Image
import io

# Set the path to the Tesseract executable (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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

def handwritten_text(uploaded_file):
    """
    Perform handwritten text recognition using Pytesseract.

    Args:
        uploaded_file (file-like object): The uploaded image file.

    Returns:
        str: Extracted handwritten text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))  # Handling the uploaded file from Gradio
        
        # Perform handwritten text recognition using Pytesseract
        text = pytesseract.image_to_string(img, lang='hin+eng')
        return text
    except Exception as e:
        return f"Error in handwriting recognition: {str(e)}"
