import re

from nltk.corpus import wordnet
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from engine.text_processing import clean_text, remove_stopwords, extract_keywords_tfidf
from engine.recommender import get_job_recommendations

# Action verbs used to gauge description quality
ACTION_VERBS = [
    'managed', 'developed', 'designed', 'built', 'increased', 'optimized',
    'led', 'created', 'implemented', 'executed', 'engineered', 'collaborated',
    'delivered', 'reduced', 'launched', 'automated', 'architected', 'coordinated',
    'mentored', 'spearheaded', 'streamlined', 'analyzed', 'researched',
]


def _count_action_verbs(text: str) -> int:
    return sum(1 for v in ACTION_VERBS if v in text)


def _has_metrics(text: str) -> bool:
    return len(re.findall(r'\d+', text)) > 3


def _semantic_bonus(verb_count: int, has_metrics_flag: bool) -> float:
    if verb_count >= 4 and has_metrics_flag:
        return 0.15
    if verb_count >= 3 or has_metrics_flag:
        return 0.10
    if verb_count >= 1:
        return 0.06
    return 0.02


def _tfidf_score(resume_clean: str, job_clean: str) -> float:
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=1)
    try:
        tfidf = vectorizer.fit_transform([resume_clean, job_clean])
        return float(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0])
    except Exception:
        return 0.0


def _expand_with_synonyms(keywords: set) -> set:
    synonyms = set()
    for word in keywords:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace("_", " ").lower())
    return synonyms


def run_analysis(resume_text: str, job_text: str) -> dict:
    resume_clean = remove_stopwords(clean_text(resume_text))
    job_clean    = remove_stopwords(clean_text(job_text))

    # Guard: unreadable CV
    if not resume_clean or len(resume_clean.split()) < 10:
        return {
            "score": 0,
            "verdict": "Gagal Dianalisiss",
            "verdict_class": "low",
            "feedback": [{"title": "CV Tidak Terbaca", "desc": "CV tidak bisa diproses. Pastikan file PDF berisi teks yang bisa di-copy, bukan hasil scan gambar."}],
            "recommendations": [{"title": "Export Ulang CV", "desc": "Coba export CV dari Word ke PDF dengan format teks, bukan gambar.", "success": False}],
            "matched_keywords": [],
            "missing_keywords": [],
            "job_recommendations": [],
        }

    verb_count    = _count_action_verbs(resume_clean)
    has_metrics_f = _has_metrics(resume_text)

    # Keywords
    job_kws    = extract_keywords_tfidf(job_clean, resume_clean, 25)
    resume_kws = extract_keywords_tfidf(resume_clean, job_clean, 40)
    resume_kws_expanded = resume_kws | _expand_with_synonyms(resume_kws)

    matched = list(job_kws & resume_kws_expanded)
    missing = list(job_kws - resume_kws_expanded)
    keyword_coverage = len(matched) / max(len(job_kws), 1)

    # Scoring
    tfidf_raw        = _tfidf_score(resume_clean, job_clean)
    tfidf_normalized = min(tfidf_raw * 0.35, 1.0)
    semantic_bonus   = _semantic_bonus(verb_count, has_metrics_f)

    quality_score = min(semantic_bonus / 0.15, 1.0)  # normalize ke 0-1

    # formula lebih defensible dan transpara
    raw_score = (
        (keyword_coverage* 0.40) + (tfidf_normalized* 0.40) + (quality_score* 0.20)
    )

    score = round(min(raw_score * 100, 100), 1)

    # Verdict
    if score >= 70:
        verdict, verdict_class = "Strong Match", "good"
    elif score >= 45:
        verdict, verdict_class = "Partial Match", "mid"
    else:
        verdict, verdict_class = "Low Match", "low"

    # Feedback
    feedback = [
        {
            "title": f"Keyword Match: {len(matched)}/{len(job_kws)}",
            "desc": (
                f"CV kamu cocok dengan {round(keyword_coverage*100)}% keyword dari Job Description. "
                + ("Ini sudah baik!" if keyword_coverage >= 0.5 else "Perlu ditingkatkan lagi.")
            ),
        },
        {
            "title": f"Kesesuaian Konten: {round(tfidf_normalized*100)}%",
            "desc": "Mengukur seberapa mirip konteks dan frasa di CV dengan Job Description menggunakan analisis TF-IDF.",
        },
    ]

    if verb_count >= 4 and has_metrics_f:
        feedback.append({"title": "Kualitas Deskripsi: Sangat Baik", "desc": "CV kamu sudah menggunakan action verbs yang kuat dan data kuantitatif untuk menunjukkan pencapaian."})
    elif verb_count >= 2:
        feedback.append({"title": "Kualitas Deskripsi: Cukup", "desc": "CV sudah ada deskripsi pengalaman, tapi bisa diperkuat dengan lebih banyak angka dan hasil konkret."})
    else:
        feedback.append({"title": "Kualitas Deskripsi: Perlu Diperbaiki", "desc": "CV terlihat seperti daftar skill tanpa penjelasan pencapaian. Tambahkan deskripsi pengalaman kerja."})

    # Recommendations
    recommendations = []

    if missing:
        missing_list = ", ".join(missing[:6])
        recommendations.append({
            "title": "Tambahkan Keyword yang Kurang",
            "desc": f"Keyword berikut ada di Job Description tapi belum ada di CV: {missing_list}. Masukkan secara natural di bagian Skills atau pengalaman.",
            "success": False,
        })

    if not has_metrics_f:
        recommendations.append({
            "title": "Tambahkan Angka & Metrik",
            "desc": "Ganti 'meningkatkan performa' dengan 'meningkatkan performa sistem sebesar 35%'. Rekruter lebih tertarik pada pencapaian yang terukur.",
            "success": False,
        })

    if verb_count < 3:
        recommendations.append({
            "title": "Gunakan Action Verbs",
            "desc": "Mulai setiap bullet dengan kata kerja aktif seperti: Developed, Built, Led, Optimized, Delivered, Implemented.",
            "success": False,
        })

    if len(resume_text.split()) > 1200:
        recommendations.append({
            "title": "Ringkaskan CV",
            "desc": "CV terlalu panjang. Ideal 1-2 halaman untuk fresh graduate atau 2-3 halaman untuk yang berpengalaman.",
            "success": False,
        })

    if not recommendations:
        recommendations.append({
            "title": "CV Sudah Baik!",
            "desc": "Tidak ada perbaikan major yang diperlukan. Pastikan format PDF bersih dan mudah dibaca ATS.",
            "success": True,
        })

    # Job recommendations (only for non-strong matches)
    job_recommendations = []
    if score < 70:
        job_recommendations = get_job_recommendations(resume_kws, job_kws, num_recs=3)

    return {
        "score": score,
        "verdict": verdict,
        "verdict_class": verdict_class,
        "feedback": feedback,
        "recommendations": recommendations,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "job_recommendations": job_recommendations,
    }
