import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_code(code, language="Python"):
    """
    Analyze source code using AI.
    """

    response = client.responses.create(
        model="gpt-5.6-luna",

        instructions=(
            "You are an expert programming code analyzer. "
            "Analyze the user's code carefully and explain it "
            "in a beginner-friendly way. "
            "Do not invent errors that are not present. "
            "If the code appears correct, clearly say so. "
            "Give practical suggestions for improvement."
        ),

        input=f"""
Programming Language:
{language}


SOURCE CODE:
{code}


Analyze the code and provide the following sections:

1. 📖 Code Explanation
Explain what the program does and how it works.

2. 🐛 Errors and Bugs
Identify syntax errors, logical errors, runtime problems,
or possible bugs.
If there are no obvious problems, say so.

3. ⚡ Improvements
Suggest ways to make the code cleaner, safer,
more readable, or more efficient.

4. ⏱️ Time Complexity
Explain the approximate time complexity where applicable.

5. 💾 Space Complexity
Explain the approximate space complexity where applicable.

6. 🎓 Beginner Tips
Give a few useful programming concepts the user
can learn from this code.

7. ✅ Overall Analysis
Give a short summary of the code quality and behavior.
"""
    )

    return response.output_text