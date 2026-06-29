import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from engine.text_processing import (
    clean_text,
    remove_stopwords,
    extract_keywords_set,
)

from engine.recommender import get_job_recommendations
from engine.cv_validator import validate_cv_template
from engine.synonym import expand_indonesian_synonyms
from engine.ats_score import ats_score
from engine.domain_detector import detect_domain


# Action verbs Bahasa Indonesia
ACTION_VERBS = [
    "mengembangkan",
    "membangun",
    "mendesain",
    "membuat",
    "mengelola",
    "meningkatkan",
    "mengimplementasikan",
    "mengoptimalkan",
    "menganalisis",
    "meneliti",
    "memimpin",
    "mengotomatisasi",
    "merancang",
    "mengkoordinasikan",
    "menginisiasi",
    "menyelesaikan",
]


def _count_action_verbs(text: str) -> int:
    return sum(1 for verb in ACTION_VERBS if verb in text)


def _has_metrics(text: str) -> bool:
    return len(re.findall(r"\d+", text)) >= 3


def _semantic_bonus(verb_count: int, has_metrics_flag: bool) -> float:
    if verb_count >= 4 and has_metrics_flag:
        return 0.15
    elif verb_count >= 2:
        return 0.10
    else:
        return 0.05


def _tfidf_score(resume_clean: str, job_clean: str) -> float:
    try:
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            min_df=1,
        )

        tfidf = vectorizer.fit_transform(
            [resume_clean, job_clean]
        )

        return float(
            cosine_similarity(
                tfidf[0:1],
                tfidf[1:2]
            )[0][0]
        )

    except Exception:
        return 0.0


def run_analysis(
    resume_text: str,
    job_text: str,
) -> dict:

    resume_clean = remove_stopwords(
        clean_text(resume_text)
    )

    job_clean = remove_stopwords(
        clean_text(job_text)
    )

    #################################################
    # CV tidak terbaca
    #################################################

    if not resume_clean or len(resume_clean.split()) < 10:
        return {
            "score": 0,
            "verdict": "CV Tidak Terbaca",
            "verdict_class": "low",
            "feedback": [
                {
                    "title": "CV Tidak Bisa Diproses",
                    "desc": (
                        "Pastikan file PDF berisi teks "
                        "dan bukan hasil scan gambar."
                    ),
                }
            ],
            "recommendations": [],
            "matched_keywords": [],
            "missing_keywords": [],
            "job_recommendations": [],
        }

    #################################################
    # Validasi Template CV
    #################################################

    template_result = validate_cv_template(
        resume_text
    )

    if not template_result["is_valid"]:
        return {
            "score": 0,
            "verdict": "Template CV Tidak Didukung",
            "verdict_class": "low",
            "feedback": [
                {
                    "title": "Format CV Tidak Sesuai",
                    "desc": (
                        "Gunakan template CV ATS Bahasa Indonesia "
                        "yang memiliki bagian Pendidikan, "
                        "Pengalaman, dan Skill."
                    ),
                }
            ],
            "recommendations": [
                {
                    "title": "Lengkapi Bagian CV",
                    "desc":
                        "Bagian yang belum ditemukan: "
                        + ", ".join(
                            template_result["missing"]
                        ),
                    "success": False,
                }
            ],
            "matched_keywords": [],
            "missing_keywords": [],
            "job_recommendations": [],
        }

    #################################################
    # Keyword Extraction
    #################################################

    job_kws = extract_keywords_set(
        job_clean,
        25
    )

    resume_kws = extract_keywords_set(
        resume_clean,
        40
    )

    resume_domain = detect_domain(resume_kws)
    job_domain = detect_domain(job_kws)

    resume_kws_expanded = set(resume_kws)

    for kw in resume_kws:
        resume_kws_expanded.update(
            expand_indonesian_synonyms(
                {kw}
            )
        )

    matched = list(
        job_kws &
        resume_kws_expanded
    )

    intersection = len(
    job_kws &
    resume_kws_expanded
    )

    union = len(
        job_kws |
        resume_kws_expanded
    )

    jaccard = (
        intersection /
        max(union, 1)
    )

    missing = list(
        job_kws -
        resume_kws_expanded
    )

    keyword_coverage = (
        len(matched)
        / max(len(job_kws), 1)
    )

    #################################################
    # Scoring
    #################################################

    verb_count = _count_action_verbs(
        resume_clean
    )

    has_metrics = _has_metrics(
        resume_text
    )

    tfidf = _tfidf_score(
        resume_clean,
        job_clean
    )

    tfidf = min(
        tfidf * 3,
        1.0
    )

    semantic_bonus = _semantic_bonus(
        verb_count,
        has_metrics
    )

    ats = ats_score(
        resume_text
    )

    raw_score = (
    tfidf * 0.45
    + keyword_coverage * 0.35
    + semantic_bonus * 0.10
    + ats * 0.10
    )

    if (
    resume_domain
    and job_domain
    and resume_domain != job_domain
    ):
        raw_score *= 0.30

    if jaccard < 0.05:
        raw_score *= 0.20

    elif jaccard < 0.10:
         raw_score *= 0.50

    score = round(
        min(raw_score * 100, 100),
        1,
    )

    #################################################
    # Verdict
    #################################################

    if score >= 70:
        verdict = "Sangat Cocok"
        verdict_class = "good"

    elif score >= 45:
        verdict = "Cukup Cocok"
        verdict_class = "mid"

    else:
        verdict = "Kurang Cocok"
        verdict_class = "low"

    #################################################
    # Feedback
    #################################################

    feedback = [
        {
            "title":
                f"Keyword Match {round(keyword_coverage*100)}%",
            "desc":
                f"Ditemukan {len(matched)} keyword "
                "yang sesuai dengan Job Description.",
        },
        {
            "title":
                f"Kesesuaian Konten {round(tfidf*100)}%",
            "desc":
                "Mengukur kemiripan isi CV "
                "dengan Job Description.",
        },
        {
            "title":
                f"Skor ATS {round(ats*100)}%",
            "desc":
                "Mengukur apakah format CV "
                "mudah dibaca oleh ATS.",
        },
    ]

    if resume_domain:
        feedback.append({
            "title": "Bidang CV Terdeteksi",
            "desc":
                f"CV kamu terdeteksi berada pada bidang "
                f"{resume_domain.replace('_', ' ').title()}."
        })


    #################################################
    # Recommendations
    #################################################

    recommendations = []

    if missing:
        recommendations.append(
            {
                "title":
                    "Tambahkan Keyword",
                "desc":
                    "Keyword yang belum ada: "
                    + ", ".join(missing[:6]),
                "success": False,
            }
        )

    if not has_metrics:
        recommendations.append(
            {
                "title":
                    "Tambahkan Angka dan Pencapaian",
                "desc":
                    "Contoh: meningkatkan "
                    "efisiensi sebesar 25%.",
                "success": False,
            }
        )

    if verb_count < 3:
        recommendations.append(
            {
                "title":
                    "Perbaiki Deskripsi Pengalaman",
                "desc":
                    "Gunakan kata kerja aktif "
                    "seperti mengembangkan, "
                    "membangun, dan "
                    "mengimplementasikan.",
                "success": False,
            }
        )

    if len(resume_text.split()) > 1200:
        recommendations.append(
            {
                "title":
                    "Ringkaskan CV",
                "desc":
                    "CV terlalu panjang. "
                    "Idealnya 1-2 halaman.",
                "success": False,
            }
        )

    if not recommendations:
        recommendations.append(
            {
                "title":
                    "CV Sudah Sangat Baik",
                "desc":
                    "Tidak ada rekomendasi "
                    "perbaikan utama.",
                "success": True,
            }
        )

    #################################################
    # Job Recommendation
    #################################################

    job_recommendations = []

    if score < 70:
        job_recommendations = get_job_recommendations(
        resume_kws,
        num_recs=3
    )


    #################################################
    # Return
    #################################################

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