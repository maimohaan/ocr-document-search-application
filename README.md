# OCR and Document Search Application

## Description
This web application enables users to upload images containing printed or handwritten text, extract text using Optical Character Recognition (OCR), and perform various search operations on the extracted text. The application supports exact matches, fuzzy search, and Boolean search, making it a versatile tool for analyzing and searching text within images.

## Features
- **OCR for Text Extraction**: Upload images in .jpg, .png, or .jpeg format to extract text using OCR powered by Tesseract.
- **Multi-Language Support**: Recognizes and extracts text in both Hindi and English.
- **Search Functionality**: Exact match, fuzzy search, and Boolean search capabilities for analyzing the extracted text.

## Prerequisites
- Python 3.8.10 installed.
- Virtual environment.
- Libraries like Streamlit, Pytesseract, Pillow, Transformers, and others as listed in `requirements.txt`.

## Installation

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate  # On Windows

2. **Install the required dependencies**:Ensure you have a requirements.txt file with the following content

    # Core Libraries
      streamlit==1.38.0
      gradio==4.44.0
      numpy==1.24.0  # Updated for compatibility
      pandas==1.5.3
      opencv-python==4.10.0.84
      pytesseract==0.3.13

    # Machine Learning 
      torch==2.4.1
      torchvision==0.19.1
      torchaudio==2.4.1
      transformers==4.45.1
      scipy==1.9.3  # Updated

    # Data Visualization
      altair==5.4.1
      matplotlib==3.7.5
      pydeck==0.9.1

    # OCR and PDF Libraries
      pdfminer.six==20231228
      pdfplumber==0.11.4
      pdf2image==1.17.0

    # Web and API Libraries
      fastapi==0.115.0
      httpx==0.27.2
      uvicorn==0.31.0

    # Utility Libraries
      fuzzywuzzy==0.18.0
      python-Levenshtein==0.25.1
      python-multipart==0.0.12
      pydantic==2.9.2
      pydantic_core==2.23.4

# Additional Libraries
attrs==24.2.0
blinker==1.8.2
cachetools==5.5.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
cryptography==43.0.1
gitdb==4.0.11
GitPython==3.1.43
iopath==0.1.10
Jinja2==3.1.4
jsonschema==4.23.0
kiwisolver==1.4.7
layoutparser==0.3.4
markdown-it-py==2.2.0
MarkupSafe==2.1.5
orjson==3.10.7
packaging==24.1
pycryptodome==3.20.0
python-dateutil==2.9.0.post0
requests==2.32.3
rich==13.8.1
tornado==6.4.1
watchdog==4.0.2
zipp==3.20.2


   
   Then run:
   ```bash
   pip install -r requirements.txt

3. Download and install Tesseract OCR:
   For Windows: https://github.com/UB-Mannheim/tesseract/wiki
   For Linux/Mac, use a package manager like apt or brew.

4.You should keep only the code that sets the Tesseract path based on the environment variable, which is more suitable for deployment in 
  a cloud environment like Streamlit Cloud. Here’s how to handle it:
  1. Keep the following line in your model.py:
      ```python
      os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"
      This is appropriate for the deployment environment.
  2. Remove any hardcoded paths specific to your local environment (like the Windows path):
     # Remove this line
     # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     In your README, you can note that the application is configured to automatically detect Tesseract's installation based on the 
     environment variable, making it easier for deployment in different environments.
    
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
    5. In Advanced settings, *CLICK ON Python 3.8* make sure. It will run on *Python 3.8 ONLY*

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
   
   ### Notes
   - Adjust any sections as necessary based on your specific project structure or additional features.
   - Make sure to test the instructions and paths provided to ensure they work for users who will set up the application.



 






