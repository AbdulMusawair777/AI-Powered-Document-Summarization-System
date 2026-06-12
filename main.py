from file_handler import *
from preprocessing import *
from summarizer import *
from analytics import *
from exporter import *

filepath = input("Enter file path: ")

if filepath.endswith(".txt"):
    text = load_text_file(filepath)

elif filepath.endswith(".pdf"):
    text = load_pdf_file(filepath)

else:
    text = input("Paste your text:\n")

filtered_words, sentences = preprocess_text(text)

summary, scores = tfidf_summarizer(
    sentences,
    ratio=0.3
)

print("\nORIGINAL TEXT")
print("=" * 50)
print(text)

print("\nSUMMARY")
print("=" * 50)
print(summary)

print("\nTOP KEYWORDS")
print(extract_keywords(filtered_words))

export_txt(summary)
export_pdf(summary)

print("\nSummary exported successfully.")