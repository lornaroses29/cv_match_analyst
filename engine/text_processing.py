import re
from collections import Counter

from nltk.corpus import stopwords


from engine.skills import TECH_SKILLS
from engine.skill_alias import SKILL_ALIAS

from nltk.tokenize import word_tokenize
from engine.skill_database import (
    TECH_SKILLS,
    SKILL_ALIAS
)



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



def extract_keywords_set(text, num=50):

    text = text.lower()

    found = set()

    for alias, actual in SKILL_ALIAS.items():
        if alias in text:
            found.add(actual)

    for skill in TECH_SKILLS:
        if skill in text:
            found.add(skill)

    return found