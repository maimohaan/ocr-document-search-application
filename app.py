import gradio as gr
from ocr.model import GOTModel
from search.search import search_keywords

# Load the GOT OCR model
got_model = GOTModel()

def ocr_and_search(image, keywords):
    """Performs OCR on the uploaded image and searches for keywords."""
    extracted_text = got_model.extract_text(image)

    # Search for keywords (if provided)
    if keywords:
        search_results = search_keywords(extracted_text, keywords)
    else:
        search_results = None

    return extracted_text, search_results

# Create the Gradio interface
demo = gr.Interface(
    fn=ocr_and_search,
    inputs=[
        gr.Image(label="Upload Image", type="pil", image_mode="RGB"), 
        gr.Textbox(label="Keywords (optional)", lines=1)
    ],
    outputs=[
        gr.Textbox(label="Extracted Text", lines=10),
        gr.Textbox(label="Search Results (if any)", lines=10)
    ],
    title="Hindi-English OCR with Search",
    description="Upload an image containing text (Hindi and English) and search for keywords.",
    css="""
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
    """
)

# Launch the Gradio app
demo.launch()

