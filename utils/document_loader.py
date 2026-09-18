from pypdf import PdfReader
from docx import Document


def load_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_docx(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():

            text += paragraph.text + "\n"

    return text


def load_document(file):

    file_name = file.name.lower()

    if file_name.endswith(".pdf"):

        return load_pdf(file)

    elif file_name.endswith(".docx"):

        return load_docx(file)

    else:

        raise ValueError(
            "Unsupported file type. "
            "Please upload a PDF or DOCX file."
        )