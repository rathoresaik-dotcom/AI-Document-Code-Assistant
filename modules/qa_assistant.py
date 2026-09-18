import os
from dotenv import load_dotenv
from openai import OpenAI

from utils.text_processor import split_text, find_relevant_chunks

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def answer_question(document_text, question):
    """
    Answer a question using the most relevant parts
    of the uploaded document.
    """

    # Split document into chunks
    chunks = split_text(
        document_text,
        chunk_size=3000,
        overlap=400
    )

    # Find relevant sections
    relevant_chunks = find_relevant_chunks(
        chunks,
        question,
        max_chunks=5
    )

    # Combine relevant sections
    context = "\n\n--- DOCUMENT SECTION ---\n\n".join(
        relevant_chunks
    )

    # Ask AI using only the selected document content
    response = client.responses.create(
        model="gpt-5.6-luna",

        instructions=(
            "You are a document question-answering assistant. "
            "Answer the user's question using ONLY the information "
            "contained in the provided document sections. "
            "Do not invent or assume information that is not present. "
            "If the answer cannot be found in the document, clearly "
            "say: 'This information is not available in the uploaded document.' "
            "Give a clear and beginner-friendly answer."
        ),

        input=f"""
DOCUMENT SECTIONS:

{context}


USER QUESTION:

{question}


Please answer the question based only on the document.
"""
    )

    return response.output_text