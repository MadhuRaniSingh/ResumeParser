import re

def extract_contact_info(text, field=None):
    # Example pattern for extracting contact details
    email = re.search(r'\S+@\S+', text)
    phone = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

    contact_info = {
        "email": email.group(0) if email else "",
        "phone": phone.group(0) if phone else "",
    }

    if field:
        return contact_info.get(field, "")
    return contact_info

def extract_education(text):
    # Extract education details (degree, institution, dates)
    education_section = re.search(r"Education(.+?)(Experience|$)", text, re.DOTALL)
    # Process the education text here and return as structured data
    return []

def extract_experience(text):
    # Extract job titles, company names, dates from the experience section
    experience_section = re.search(r"Experience(.+?)(Skills|$)", text, re.DOTALL)
    # Process the experience text here and return as structured data
    return []

def extract_skills(text):
    # Extract skills from the skills section
    skills_section = re.search(r"Skills(.+?)(Experience|$)", text, re.DOTALL)
    # Process the skills text here and return as structured data
    return []
