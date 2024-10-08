import sys
import os
import streamlit as st
import pytesseract
from PIL import Image
import io

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from ocr.model import process_image  # Importing the OCR function
from search.search import fuzzy_search, boolean_search  # Import your search functions

# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Light background color */
        color: #333;  /* Text color */
        font-family: 'Arial', sans-serif;  /* Font style */
    }

    .header {
        text-align: center;
        padding: 20px;
        color: #2c3e50;  /* Header color */
    }

    .button {
        background-color: #3498db;  /* Button color */
        color: white;  /* Button text color */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .button:hover {
        background-color: #2980b9;  /* Button hover color */
    }

    .stTextArea {
        background-color: #ffffff;  /* Text area background */
        border: 1px solid #ccc;  /* Border color */
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit interface
st.title("OCR and Document Search Application")

# Upload an image for OCR processing
uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])

# Input for search query
search_query = st.text_input("Search within extracted text")

# Search type options
search_type = st.radio("Select Search Type", options=["Exact", "Fuzzy", "Boolean"], index=0)

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
        img = Image.open(io.BytesIO(uploaded_file.read()))
        
        # Perform OCR using Pytesseract for both Hindi and English
        extracted_text = pytesseract.image_to_string(img, lang='hin+eng')
        
        return extracted_text
    except Exception as e:
        return f"Error in OCR processing: {str(e)}"

if st.button("Process Image and Search"):
    if uploaded_file is not None:
        # Perform OCR on the uploaded image
        extracted_text = process_image(uploaded_file)

        # Display the extracted text
        st.text_area("Extracted Text", value=extracted_text, height=300)

        # Perform search if query is provided
        if search_query:
            search_result = ""
            # Normalize the extracted text and search query
            extracted_text_normalized = extracted_text.strip()
            search_query_normalized = search_query.strip()

            # Tokenizing the extracted text and search query
            extracted_words = set(extracted_text_normalized.split())
            query_words = set(search_query_normalized.split())

            # Perform the exact search
            if search_type == "Exact":
                # Check if all words in the query are present in the extracted text
                if query_words.issubset(extracted_words):
                    search_result = f"Exact match found: {search_query_normalized}"
                else:
                    search_result = "No exact match found."
                    
            # Perform fuzzy search
            elif search_type == "Fuzzy":
                if fuzzy_search(search_query_normalized, extracted_text_normalized):
                    search_result = f"Fuzzy match found: {search_query_normalized}"
                else:
                    search_result = "No fuzzy match found."
                    
            # Perform boolean search
            elif search_type == "Boolean":
                if boolean_search(search_query_normalized, extracted_text_normalized):
                    search_result = f"Boolean search match found: {search_query_normalized}"
                else:
                    search_result = "No Boolean match found."
            
            # Display the search result
            st.write(search_result)
    else:
        st.warning("Please upload an image file to process.")
