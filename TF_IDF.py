from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def tfidf_summarizer(sentences, ratio=0.3):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(sentences)

    scores = np.array(
        tfidf_matrix.sum(axis=1)
    ).flatten()

    sentence_scores = {
        sentences[i]: scores[i]
        for i in range(len(sentences))
    }

    top_n = max(
        1,
        int(len(sentences) * ratio)
    )

    ranked = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    summary = " ".join(ranked[:top_n])

    return summary, sentence_scores