import io
import logging
import streamlit as st
import PyPDF2
import docx

@st.cache_data
def extract_text_from_pdf(file_bytes):
    try:
        reader = PyPDF2.PdfReader(file_bytes)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {e}")
        st.error("Error extracting text from PDF. Please check the file format or content.")
        return ""

@st.cache_data
def extract_text_from_docx(file_bytes):
    try:
        document = docx.Document(file_bytes)
        return "\n".join(paragraph.text for paragraph in document.paragraphs)
    except Exception as e:
        logging.error(f"Error extracting text from DOCX: {e}")
        st.error("Error extracting text from DOCX. Please check the file format or content.")
        return ""

@st.cache_data
def extract_text(uploaded_file):
    """Extracts text from the uploaded file"""
    file_type = uploaded_file.type
    file_bytes = uploaded_file.getvalue()
    file_name = uploaded_file.name
    logging.info(f"Processing file: {file_name}, Type: {file_type}")
    extract_text = ""
    if not file_bytes:
        logging.warning(f"Uploaded file {file_name} is empty.")
        st.warning("No file content found. Please upload a valid file.")
        return ""
    
    with io.BytesIO(file_bytes) as file_bytes_s:
        if file_type == "application/pdf":
            extracted_text = extract_text_from_pdf(file_bytes_s)
            
        elif file_type == "text/plain":
            extracted_text = uploaded_file.read().decode("utf-8")
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            extracted_text = extract_text_from_docx(file_bytes_s)
        
    if not extracted_text.strip():
        logging.warning(f"File {file_name} does not contain any extractable text.")
        st.warning("The file does not contain any extractable text. Please check the file content.")
        return ""
    else:
        logging.info(f"Extracted text from {file_name} successfully.")
    return extracted_text
    #elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
