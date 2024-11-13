import pdfplumber
import re
from utils import extract_contact_info, extract_education, extract_experience, extract_skills

class ResumeParser:
    def __init__(self, pdf_path, schema):
        self.pdf_path = pdf_path
        self.schema = schema

    def extract_data(self):
        # Extract text from PDF
        with pdfplumber.open(self.pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"

        # Initialize JSON data based on schema
        data = {
            "name": extract_contact_info(text, 'name'),
            "contact_info": extract_contact_info(text),
            "education": extract_education(text),
            "experience": extract_experience(text),
            "skills": extract_skills(text),
            # Additional fields can be added as needed
        }

        return data
