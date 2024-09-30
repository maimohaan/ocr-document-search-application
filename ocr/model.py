import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the tokenizer and model for the ColPali OCR model
tokenizer = AutoTokenizer.from_pretrained("ColPali")
model = AutoModelForTokenClassification.from_pretrained("ColPali")

def process_image(uploaded_file):
    """
    Process the uploaded image file and extract text using the new OCR model.
    Args:
        uploaded_file (file-like object): The uploaded image file.
    Returns:
        str: Extracted text or error message if the processing fails.
    """
    try:
        img = Image.open(io.BytesIO(uploaded_file.read()))
        
        # Here, we will use the ColPali model to extract text
        # Convert the image into a format suitable for the model
        # Perform OCR using the model (example code structure)
        inputs = tokenizer(img, return_tensors="pt")
        outputs = model(**inputs)
        extracted_text = outputs.logits.argmax(-1).numpy()

        # Convert extracted text to a human-readable format
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"
