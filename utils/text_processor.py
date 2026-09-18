import re


def clean_text(text):
    """
    Clean unnecessary spaces and blank lines from document text.
    """

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def split_text(text, chunk_size=3000, overlap=400):
    """
    Split a document into overlapping chunks.
    """

    text = clean_text(text)

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


def find_relevant_chunks(chunks, question, max_chunks=5):
    """
    Find the document chunks most related to the user's question.
    """

    question_words = set(
        re.findall(
            r"\b[a-zA-Z]{3,}\b",
            question.lower()
        )
    )

    scored_chunks = []

    for chunk in chunks:

        chunk_words = set(
            re.findall(
                r"\b[a-zA-Z]{3,}\b",
                chunk.lower()
            )
        )

        score = len(question_words & chunk_words)

        scored_chunks.append(
            (score, chunk)
        )

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True
    )

    relevant_chunks = [
        chunk
        for score, chunk in scored_chunks[:max_chunks]
        if score > 0
    ]

    if not relevant_chunks:
        relevant_chunks = chunks[:max_chunks]

    return relevant_chunks