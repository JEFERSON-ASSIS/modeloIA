import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
import os

# Set the path to your service account JSON key file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Jeferson Silva\\Desktop\\modelo\\modelo_ia\\src\\api\\integration\\pivotal-essence-410920-c3a96195c1ac.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), 'integration', 'pivotal-essence-410920-c3a96195c1ac.json')

# Initialize Vertex AI with the project ID and location
google_project_id = os.getenv("PROJECT_ID")
vertexai.init(project=google_project_id, location="us-central1")

class LLM: 
    def __init__(self):
        # Initialize the Generative Models with specific system instructions
        self.modelFlash = GenerativeModel("gemini-1.5-flash-001", system_instruction="Você analisa notas fiscais")
        self.modelPro = GenerativeModel("gemini-1.5-pro-001", system_instruction="Você analisa notas fiscais")
        
        # Generation configurations
        self.generation_config = {
            "max_output_tokens": 1024,
            "temperature": 0.0,
            "top_p": 0.95,
            "response_mime_type": "application/json"
        }
        self.gen_config = {
            "max_output_tokens": 1200,
            "temperature": 0.0,
            "top_p": 0.95
        }
            
    def call_ai(self, prompt):
        # Call the AI with the flash model
        return self.modelFlash.generate_content([prompt], generation_config=self.generation_config)
    
    def call_ai_with_image(self, prompt, image):
        # Call the AI with an image using the pro model
        return self.modelPro.generate_content(
            [generative_models.Image.from_bytes(image), prompt], 
            generation_config=self.generation_config
        )
    
    def call_ai_with_imageOCR(self, prompt, image):
        # Call the AI with OCR processing using the flash model
        return self.modelFlash.generate_content(
            [generative_models.Image.from_bytes(image), prompt], 
            generation_config=self.gen_config
        )
