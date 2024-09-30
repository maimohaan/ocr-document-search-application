# OCR and Document Search Application

## Description
This web application enables users to upload images containing printed or handwritten text, extract text using Optical Character Recognition (OCR), and perform various search operations on the extracted text. The application supports exact matches, fuzzy search, and Boolean search, making it a versatile tool for analyzing and searching text within images.

## Features
- **OCR for Text Extraction**: Upload images in .jpg, .png, or .jpeg format to extract text using OCR powered by Tesseract.
- **Handwritten Text Recognition**: Recognize and extract handwritten text from images.
- **Search Functionality**: Exact match, fuzzy search, and Boolean search capabilities for analyzing the extracted text.

## Prerequisites
- Python 3.8 installed.
- Virtual environment.
- Libraries like Streamlit, Pytesseract, Pillow, Transformers, and others as listed in `requirements.txt`.

## Installation

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate  # On Windows


2. Install the required dependencies: Ensure you have a requirements.txt file with the appropriate content and run:

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
   List of dependencies as mentioned in requirements.txt.

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



 






