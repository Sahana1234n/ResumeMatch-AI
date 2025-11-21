from pdfminer.high_level import extract_text
import re

def extract_text_from_pdf(uploaded_file):
    """Extract the text from the uploaded PDF file
    
    Args:
        uploaded_file: file-like object
    
    Returns:
        str: Cleaned text from the PDF
    """

    try:
        extracted_text = extract_text(uploaded_file)

        # Remove multiple new lines, tabs, and extra spaces
        cleaned_text = re.sub(r'\s+', ' ', extracted_text)
        cleaned_text = cleaned_text.strip()

        return cleaned_text

    except Exception as e:
        raise e
