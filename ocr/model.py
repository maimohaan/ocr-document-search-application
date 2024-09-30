from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PIL import Image
import torch
import numpy as np

class GOTModel:
    """Represents the General OCR Theory (GOT) model for text extraction."""

    def __init__(self):
        self.model_name = "microsoft/m2m100-418M"  # Replace with the actual GOT model name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = 512  # Maximum sequence length for the model

    def extract_text(self, image):
        """Extracts text from an image using the GOT model."""
        # Preprocess the image (resize, convert to tensor)
        image = image.convert("RGB")  # Ensure RGB format
        image = image.resize((512, 512))  # Resize to a suitable size (adjust if needed)
        image = np.array(image) / 255.0  # Normalize pixel values
        image = torch.from_numpy(image).permute(2, 0, 1).float().unsqueeze(0).to(self.model.device) 

        # Perform OCR with the model
        with torch.no_grad():
            outputs = self.model(image)
        predicted_ids = outputs.logits.argmax(-1)[0]  # Get the most likely predicted tokens

        # Decode predicted tokens into text
        extracted_text = self.tokenizer.decode(predicted_ids, skip_special_tokens=True)

        return extracted_text
