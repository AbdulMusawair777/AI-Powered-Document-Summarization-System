from collections import Counter

def word_frequency(words):

    return Counter(words).most_common(10)


def extract_keywords(words):

    return Counter(words).most_common(10)


def top_sentences(sentence_scores):

    return sorted(
        sentence_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]