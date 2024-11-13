import json
from resume_parser import ResumeParser

# Load the provided JSON schema
with open('schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

def main(pdf_path):
    parser = ResumeParser(pdf_path, schema)
    extracted_data = parser.extract_data()
    output_path = f"output/resume_{extracted_data['name']}.json"

    # Save extracted data to JSON
    with open(output_path, 'w') as outfile:
        json.dump(extracted_data, outfile, indent=4)
    print(f"Resume data saved to {output_path}")

if __name__ == "__main__":
    pdf_path = "path/to/resume.pdf"
    main(pdf_path)
