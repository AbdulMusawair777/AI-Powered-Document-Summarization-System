# AI-Powered Document Summarization System

## Project Overview

The AI-Powered Document Summarization System is a Natural Language Processing (NLP) application developed in Python that automatically generates concise and meaningful summaries from lengthy documents. The system helps users quickly extract key insights from large volumes of text while preserving the most important information.

This project addresses the challenge of manual document summarization by implementing extractive summarization techniques based on NLP preprocessing, word frequency analysis, TF-IDF scoring, and sentence ranking algorithms.

---

## Problem Statement

Organizations and individuals often deal with large amounts of textual information such as reports, articles, emails, research papers, and business documents. Reading and summarizing these documents manually is time-consuming and inefficient.

The objective of this project is to develop an intelligent system capable of automatically analyzing documents and generating high-quality summaries that retain essential information.

---

## Features

### Document Input

* Text file (.txt) support
* PDF document support
* Direct text input through user interface

### NLP Preprocessing

* Text normalization
* Lowercase conversion
* Tokenization
* Stopword removal
* Sentence segmentation

### Summarization Techniques

* Frequency-based summarization
* TF-IDF based sentence scoring
* Sentence ranking and extraction
* Adjustable summary length

### Analytics Module

* Word frequency analysis
* Important keyword extraction
* Sentence importance scoring

### Output Features

* Original document display
* Generated summary display
* Summary export to TXT file
* Summary export to PDF file

### User Interface

* Interactive Streamlit dashboard
* Real-time document summarization
* Adjustable summary percentage

---

## Technology Stack

| Category             | Technology    |
| -------------------- | ------------- |
| Programming Language | Python        |
| NLP Library          | NLTK          |
| Machine Learning     | Scikit-Learn  |
| Data Processing      | Pandas, NumPy |
| PDF Processing       | PyPDF2        |
| PDF Export           | FPDF2         |
| Web Interface        | Streamlit     |

---

## Project Structure

```text
AI-Powered-Document-Summarization-System/
│
├── data/
│   ├── sample1.txt
│   └── sample2.txt
│
├── output/
│   ├── summary.txt
│   └── summary.pdf
│
├── screenshots/
│
├── src/
│   ├── app.py
│   ├── main.py
│   ├── file_handler.py
│   ├── preprocessing.py
│   ├── summarizer.py
│   ├── analytics.py
│   └── exporter.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Powered-Document-Summarization-System.git
cd AI-Powered-Document-Summarization-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download NLP Resources

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
```

---

## Running the Application

### Streamlit Web Interface

```bash
streamlit run src/app.py
```

### Command Line Version

```bash
python src/main.py
```

---

## Workflow

1. User uploads a document or enters text.
2. Text is preprocessed using NLP techniques.
3. Important words and sentences are identified.
4. TF-IDF and frequency-based scoring algorithms rank sentences.
5. Top-ranked sentences are selected.
6. A concise summary is generated.
7. Results are displayed and exported.

---

## Example Output

### Original Text

Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and increasing efficiency across healthcare, finance, education, transportation, and manufacturing sectors.

### Generated Summary

Artificial Intelligence improves efficiency and decision-making across multiple industries including healthcare, finance, education, transportation, and manufacturing.

---

## Evaluation Metrics

The project was developed according to the following assessment criteria:

| Criteria            | Weightage |
| ------------------- | --------- |
| NLP Preprocessing   | 25%       |
| Summarization Logic | 25%       |
| Code Structure      | 20%       |
| Output Quality      | 15%       |
| Error Handling      | 10%       |
| Documentation       | 5%        |

---

## Future Enhancements

* Transformer-based abstractive summarization
* Multi-document summarization
* Language detection support
* Keyword highlighting
* Summary quality evaluation metrics
* REST API integration
* Cloud deployment

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Natural Language Processing (NLP)
* Text Preprocessing
* Information Extraction
* TF-IDF Vectorization
* Extractive Text Summarization
* Python Modular Programming
* Streamlit Application Development

---

## Author

**Abdul Musawair**

Computer Vision Engineer | AI & Machine Learning Enthusiast

Specializations:

* Computer Vision
* Deep Learning
* Machine Learning
* Natural Language Processing
* Python Development

---

## License

This project is developed for educational and research purposes.
