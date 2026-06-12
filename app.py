import streamlit as st
from PyPDF2 import PdfReader

from preprocessing import preprocess_text
from summarizer import tfidf_summarizer

st.set_page_config(
    page_title="AI-Powered Document Summarization System",
    layout="wide"
)

st.title("AI-Powered Document Summarization System")

# Input Method
input_type = st.radio(
    "Choose Input Method",
    ["Direct Text", "TXT File", "PDF File"]
)

text = ""

# Direct Text
if input_type == "Direct Text":
    text = st.text_area(
        "Enter or Paste Your Document",
        height=300
    )

# TXT Upload
elif input_type == "TXT File":

    uploaded_file = st.file_uploader(
        "Upload TXT File",
        type=["txt"]
    )

    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")
        st.success("TXT file loaded successfully!")

# PDF Upload
elif input_type == "PDF File":

    uploaded_file = st.file_uploader(
        "Upload PDF File",
        type=["pdf"]
    )

    if uploaded_file:

        try:
            pdf_reader = PdfReader(uploaded_file)

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            st.success("PDF loaded successfully!")

        except Exception as e:
            st.error(f"Error reading PDF: {e}")

# Summary Length Slider
ratio = st.slider(
    "Summary Length (%)",
    min_value=10,
    max_value=80,
    value=30
)

# Generate Summary Button
if st.button("Generate Summary"):

    if text.strip():

        try:

            filtered_words, sentences = preprocess_text(text)

            summary, sentence_scores = tfidf_summarizer(
                sentences,
                ratio / 100
            )

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Document")
                st.text_area(
                    "",
                    text,
                    height=400
                )

            with col2:
                st.subheader("Generated Summary")
                st.text_area(
                    "",
                    summary,
                    height=400
                )

            st.success("Summary generated successfully!")

        except Exception as e:
            st.error(f"Error generating summary: {e}")

    else:
        st.warning(
            "Please upload a document or enter text before generating a summary."
        )