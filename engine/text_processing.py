import re
from collections import Counter

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def clean_text(text: str) -> str:
    """Lowercase, normalize common tech aliases, strip special characters."""
    text = text.lower()
    text = re.sub(r'\b(react|react\.js|reactjs)\b', 'react', text)
    text = re.sub(r'\b(node|node\.js|nodejs)\b', 'node', text)
    text = re.sub(r'\b(nest|nest\.js|nestjs)\b', 'nest', text)
    text = re.sub(r'[^a-zA-Z0-9\s\/]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def remove_stopwords(text: str) -> str:
    """Remove English and common Indonesian stopwords."""
    en_stops = set(stopwords.words('english'))
    id_stops = {
        'yang', 'dengan', 'dan', 'untuk', 'saya', 'pada', 'dalam', 'bisa',
        'dari', 'di', 'ia', 'ini', 'itu', 'adalah', 'ke', 'oleh', 'juga',
        'sudah', 'telah', 'kami', 'kamu', 'anda', 'mereka', 'kita',
    }
    combined = en_stops | id_stops
    words = word_tokenize(text)
    return " ".join(w for w in words if w not in combined)

# engine/text_processing.py — ganti Counter biasa dengan TF-IDF proper
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords_tfidf(text: str, reference_corpus: str, num: int = 20) -> set:
    """Keyword extraction yang benar-benar context-aware."""
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    tfidf = vectorizer.fit_transform([text, reference_corpus])
    scores = zip(vectorizer.get_feature_names_out(), np.asarray(tfidf[0].todense()).ravel())
    sorted_kws = sorted(scores, key=lambda x: x[1], reverse=True)
    return set(kw for kw, score in sorted_kws[:num] if score > 0)