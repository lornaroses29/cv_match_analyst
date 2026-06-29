import re


def ats_score(cv_text):

    text = cv_text.lower()

    score = 0

    # pendidikan
    if "pendidikan" in text:
        score += 15

    # pengalaman
    if (
        "pengalaman" in text
        or "pengalaman kerja" in text
    ):
        score += 20

    # skill
    if (
        "skill" in text
        or "keahlian" in text
        or "kemampuan" in text
    ):
        score += 20

    # proyek
    if "proyek" in text:
        score += 10

    # organisasi
    if "organisasi" in text:
        score += 5

    # kontak
    if (
        "email" in text
        or "@gmail" in text
        or "@outlook" in text
    ):
        score += 5

    # nomor telepon
    if re.search(r"08\d{8,12}", text):
        score += 5

    # angka pencapaian
    if len(re.findall(r"\d+", text)) >= 3:
        score += 10

    # panjang CV
    total_words = len(text.split())

    if 200 <= total_words <= 900:
        score += 10

    return min(score / 100, 1.0)