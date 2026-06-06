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


def extract_keywords_set(text: str, num: int = 20) -> set:
    """Return the top-N most frequent words (min 3 chars, non-numeric)."""
    words = word_tokenize(text)
    filtered = [w for w in words if len(w) >= 3 and not w.isdigit()]
    return set(w for w, _ in Counter(filtered).most_common(num))
