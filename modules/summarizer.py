import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text):
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions="Summarize the provided document clearly and concisely. Include the main ideas, important points, and a short conclusion.",
        input=text
    )

    return response.output_text