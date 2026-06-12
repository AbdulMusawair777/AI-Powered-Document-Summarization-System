import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower()

    words = word_tokenize(text)

    filtered_words = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]

    sentences = sent_tokenize(text)

    return filtered_words, sentences