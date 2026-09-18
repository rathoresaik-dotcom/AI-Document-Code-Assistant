import streamlit as st

from modules.summarizer import summarize_text
from modules.qa_assistant import answer_question
from modules.code_analyzer import analyze_code
from utils.document_loader import load_document


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Document & Code Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("🤖 AI Document & Code Assistant")

st.markdown(
    """
    ### 🚀 Your AI-powered workspace for documents and code

    Upload documents, generate summaries, ask questions,
    or analyze your programming code using AI.
    """
)

st.info("💡 Supported documents: PDF and DOCX")


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("🤖 AI Assistant")

    st.markdown("---")

    st.subheader("✨ Features")

    st.write("📄 Document Summarizer")
    st.write("💬 Document Q&A")
    st.write("💻 Code Analyzer")

    st.markdown("---")

    st.subheader("📖 How to use")

    st.write(
        """
        1. Upload a PDF or DOCX file.
        2. Generate an AI summary.
        3. Ask questions about the document.
        4. Paste your code into Code Analyzer.
        5. Select the programming language.
        """
    )

    st.markdown("---")

    st.caption("Powered by OpenAI")


# ==================================================
# PROJECT STATUS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Documents", "PDF + DOCX")

with col2:
    st.metric("💬 Q&A", "AI Powered")

with col3:
    st.metric("💻 Code Analysis", "AI Powered")


st.divider()


# ==================================================
# CREATE TABS
# ==================================================

tab1, tab2, tab3 = st.tabs(
    [
        "📄 Document Summarizer",
        "💬 Document Q&A",
        "💻 Code Analyzer"
    ]
)


# ==================================================
# DOCUMENT SUMMARIZER
# ==================================================

with tab1:

    st.header("📄 Document Summarizer")

    st.write(
        "Upload a PDF or DOCX document and let AI "
        "extract, understand, and summarize it."
    )

    with st.container(border=True):

        uploaded_file = st.file_uploader(
            "📤 Upload your document",
            type=["pdf", "docx"],
            help="Choose a PDF or DOCX file to analyze."
        )

    if uploaded_file:

        st.caption(
            f"📎 Uploaded file: {uploaded_file.name}"
        )

        try:

            text = load_document(uploaded_file)

            if not text.strip():

                st.warning(
                    "⚠️ No readable text was found in this document."
                )

            else:

                with st.expander("📃 View Extracted Document Text"):

                    st.text_area(
                        "Document content",
                        text,
                        height=300
                    )

                st.divider()

                if st.button(
                    "✨ Generate AI Summary",
                    type="primary",
                    use_container_width=True
                ):

                    with st.spinner(
                        "🤖 AI is analyzing your document..."
                    ):

                        summary = summarize_text(text)

                    st.success(
                        "✅ Summary generated successfully!"
                    )

                    with st.container(border=True):

                        st.subheader("📝 AI Summary")

                        st.write(summary)

        except Exception as e:

            st.error(
                f"❌ Error processing document: {e}"
            )


# ==================================================
# DOCUMENT Q&A
# ==================================================

with tab2:

    st.header("💬 Document Q&A")

    st.write(
        "Ask questions about the document you uploaded."
    )

    if uploaded_file:

        try:

            text = load_document(uploaded_file)

            if text.strip():

                question = st.text_input(
                    "❓ Ask a question about your document",
                    placeholder=(
                        "Example: What is the main topic "
                        "of this document?"
                    )
                )

                if st.button(
                    "🔍 Ask AI",
                    type="primary",
                    use_container_width=True
                ):

                    if not question.strip():

                        st.warning(
                            "⚠️ Please enter a question."
                        )

                    else:

                        with st.spinner(
                            "🤖 Searching the document..."
                        ):

                            answer = answer_question(
                                text,
                                question
                            )

                        st.success(
                            "✅ Answer generated!"
                        )

                        with st.container(border=True):

                            st.subheader("💡 Answer")

                            st.write(answer)

            else:

                st.warning(
                    "⚠️ The uploaded document does not contain "
                    "readable text."
                )

        except Exception as e:

            st.error(
                f"❌ Error answering question: {e}"
            )

    else:

        st.info(
            "📤 Please upload a PDF or DOCX document "
            "in the Document Summarizer tab first."
        )


# ==================================================
# CODE ANALYZER
# ==================================================

with tab3:

    st.header("💻 AI Code Analyzer")

    st.write(
        "Upload a code file or paste your source code "
        "and let AI explain, debug, and improve it."
    )

    with st.container(border=True):

        code_file = st.file_uploader(
            "📤 Upload a code file",
            type=[
                "py",
                "java",
                "c",
                "cpp",
                "js",
                "html",
                "css",
                "sql"
            ],
            help="Upload a source-code file for AI analysis."
        )

        st.markdown("### 🌐 Programming Language")

        language_options = [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript",
            "HTML",
            "CSS",
            "SQL",
            "Other"
        ]

        language = st.selectbox(
            "Select language",
            language_options
        )

        # Automatically detect language from file extension
        if code_file:

            extension = code_file.name.lower().split(".")[-1]

            language_map = {
                "py": "Python",
                "java": "Java",
                "c": "C",
                "cpp": "C++",
                "js": "JavaScript",
                "html": "HTML",
                "css": "CSS",
                "sql": "SQL"
            }

            detected_language = language_map.get(
                extension,
                "Other"
            )

            st.success(
                f"🤖 Detected language: {detected_language}"
            )

            language = detected_language

            code = code_file.read().decode(
                "utf-8",
                errors="ignore"
            )

            st.caption(
                f"📎 Uploaded file: {code_file.name}"
            )

        else:

            code = st.text_area(
                "🧑‍💻 Paste your code here",
                height=350,
                placeholder="""Example:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)
"""
            )

    if st.button(
        "🔎 Analyze Code",
        type="primary",
        use_container_width=True
    ):

        if not code.strip():

            st.warning(
                "⚠️ Please upload a code file "
                "or paste some code first."
            )

        else:

            with st.spinner(
                "🤖 AI is analyzing your code..."
            ):

                try:

                    analysis = analyze_code(
                        code,
                        language
                    )

                    st.success(
                        "✅ Code analysis completed!"
                    )

                    with st.container(border=True):

                        st.subheader(
                            "📊 AI Code Analysis"
                        )

                        st.markdown(
                            analysis
                        )

                except Exception as e:

                    st.error(
                        f"❌ Error analyzing code: {e}"
                    )

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "🤖 AI Document & Code Assistant • "
    "Built with Python, Streamlit and OpenAI"
)