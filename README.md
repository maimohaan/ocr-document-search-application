# OCR and Document Search Application

## Description
This web application enables users to upload images containing printed or handwritten text, extract text using Optical Character Recognition (OCR), and perform various search operations on the extracted text. The application supports exact matches, fuzzy search, and Boolean search, making it a versatile tool for analyzing and searching text within images.

## Features
- **OCR for Text Extraction**: Upload images in .jpg, .png, or .jpeg format to extract text using OCR powered by Tesseract.
- **Handwritten Text Recognition**: Recognize and extract handwritten text from images.
- **Search Functionality**: Exact match, fuzzy search, and Boolean search capabilities for analyzing the extracted text.

## Prerequisites
- Python 3.x installed.
- Virtual environment.
- Libraries like Streamlit, Pytesseract, Pillow, Transformers, and others as listed in `requirements.txt`.

## Installation

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate  # On Windows

2. **Install the required dependencies**:Ensure you have a requirements.txt file with the following content
   streamlit==1.38.0
   pytesseract==0.3.13
   Pillow==10.4.0
   transformers==4.45.1
   fuzzywuzzy==0.18.0
   python-Levenshtein==0.25.1
   
   Then run:
   ```bash
   pip install -r requirements.txt

3. Download and install Tesseract OCR:
   For Windows: https://github.com/UB-Mannheim/tesseract/wiki
   For Linux/Mac, use a package manager like apt or brew.

4. Configure Tesseract Path (for Windows users): Update the path to the Tesseract executable in model.py:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Running the Application Locally
   Run the Streamlit app:
   ```bash
   Copy code
   streamlit run app/app.py
   Open your web browser and go to http://localhost:8501 to access the app.  

5. **Usage**: 
   Upload an image (e.g., a .jpg, .png, or .jpeg file) containing printed or handwritten text.
   The application will extract the text from the image.
   You can perform searches within the extracted text using Exact, Fuzzy, or Boolean search options.

4. Deployment Instructions
   Deploying on Streamlit Cloud
   1. Push your code to a GitHub repository:
      git init
      git add .
      git commit -m "Initial commit"
      git remote add origin https://github.com/maimohaan/ocr-document-search-application.git
      git push -u origin main
    2. Go to Streamlit Cloud and sign in with your GitHub account.
    3. Create a new app, link it to your GitHub repository, and select the branch (usually main or master).
    4. Streamlit will deploy your application and provide you with a public URL where users can access it.

Example Usage
Uploaded Image:

The uploaded image contains the text "The quick brown fox jumps over the lazy dog."
Extracted Text:

"The quick brown fox jumps over the lazy dog."
Search Query:

"fox"
Search Result:

Exact match found: "fox"
Extracted Text and Search Output
When you upload an image and extract the text, you will get an output similar to the following:

{
  "extracted_text": "The quick brown fox jumps over the lazy dog.",
  "search_query": "fox",
  "search_result": "Exact match found: fox"
}

5. Dependencies
   Streamlit==1.38.0
   Pytesseract==0.3.13
   Pillow==10.4.0
   Transformers==4.45.1
   Fuzzywuzzy==0.18.0
   Python-Levenshtein==0.25.1

6. Acknowledgments
   Streamlit for the web application framework.
   Tesseract OCR for text extraction.   

7. License
   This project is licensed under the MIT License.

   ## License
   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


 






