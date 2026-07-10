import pypdf
import io

def extract_text_from_pdf(file_buffer) -> str:
    """Extracts raw text from an uploaded PDF file byte stream."""
    try:
        pdf_reader = pypdf.PdfReader(io.BytesIO(file_buffer.read()))
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
        return extracted_text.strip()
    except Exception as e:
        raise RuntimeError(f"Error parsing PDF document: {str(e)}")