import re

REQUIRED_SECTIONS = [
    "pendidikan",
    "pengalaman",
    "skill",
]

OPTIONAL_SECTIONS = [
    "profil",
    "tentang saya",
    "organisasi",
    "sertifikat",
    "proyek",
]

def validate_cv_template(cv_text: str):
    text = cv_text.lower()

    found_required = []
    missing_required = []

    for section in REQUIRED_SECTIONS:
        if section in text:
            found_required.append(section)
        else:
            missing_required.append(section)

    score = len(found_required) / len(REQUIRED_SECTIONS)

    return {
        "is_valid": score >= 0.7,
        "score": score,
        "missing": missing_required,
    }