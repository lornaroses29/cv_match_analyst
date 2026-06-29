# ──────────────────────────────────────────────────────────────────────
# Job database & recommendation logic
# ──────────────────────────────────────────────────────────────────────

JOB_DATABASE = [

    # =========================
    # DATA & AI
    # =========================
    {
        "title": "Data Analyst",
        "description": "Mengolah dan menganalisis data untuk membantu pengambilan keputusan bisnis.",
        "skills": [
            "python", "sql", "excel", "power bi",
            "tableau", "analisis data", "statistics",
            "pandas"
        ]
    },
    {
        "title": "Data Scientist",
        "description": "Mengembangkan model machine learning dan analisis prediktif.",
        "skills": [
            "python", "machine learning", "deep learning",
            "data science", "statistics", "sql",
            "tensorflow", "pytorch", "pandas"
        ]
    },
    {
        "title": "Business Intelligence Analyst",
        "description": "Membangun dashboard dan insight bisnis berbasis data.",
        "skills": [
            "sql", "power bi", "tableau",
            "excel", "analisis data"
        ]
    },
    {
        "title": "Data Engineer",
        "description": "Membangun dan mengelola pipeline data.",
        "skills": [
            "python", "sql", "etl", "database",
            "postgresql", "aws", "docker"
        ]
    },

    # =========================
    # SOFTWARE ENGINEERING
    # =========================
    {
        "title": "Backend Developer",
        "description": "Mengembangkan API dan sistem backend.",
        "skills": [
            "python", "php", "laravel",
            "node", "sql", "database",
            "api", "git"
        ]
    },
    {
        "title": "Frontend Developer",
        "description": "Mengembangkan tampilan website dan aplikasi.",
        "skills": [
            "html", "css", "javascript",
            "react", "vue", "ui", "git"
        ]
    },
    {
        "title": "Full Stack Developer",
        "description": "Mengembangkan aplikasi dari frontend hingga backend.",
        "skills": [
            "html", "css", "javascript",
            "react", "node", "php",
            "laravel", "sql", "git"
        ]
    },
    {
        "title": "Software Engineer",
        "description": "Mengembangkan dan memelihara perangkat lunak.",
        "skills": [
            "java", "python", "c++",
            "git", "database", "algorithms",
            "oop"
        ]
    },

    # =========================
    # MOBILE
    # =========================
    {
        "title": "Android Developer",
        "description": "Mengembangkan aplikasi Android.",
        "skills": [
            "kotlin", "java",
            "android", "firebase",
            "git"
        ]
    },
    {
        "title": "iOS Developer",
        "description": "Mengembangkan aplikasi iOS.",
        "skills": [
            "swift", "ios",
            "firebase", "git"
        ]
    },
    {
        "title": "Flutter Developer",
        "description": "Mengembangkan aplikasi cross-platform menggunakan Flutter.",
        "skills": [
            "flutter", "dart",
            "firebase", "git"
        ]
    },

    # =========================
    # CYBER SECURITY
    # =========================
    {
        "title": "Cyber Security Analyst",
        "description": "Melindungi sistem dari ancaman keamanan siber.",
        "skills": [
            "network security",
            "penetration testing",
            "linux",
            "owasp",
            "cryptography"
        ]
    },
    {
        "title": "Network Engineer",
        "description": "Mengelola dan mengonfigurasi jaringan komputer.",
        "skills": [
            "tcp/ip",
            "mikrotik",
            "cisco",
            "ccna",
            "network security"
        ]
    },

    # =========================
    # CLOUD & DEVOPS
    # =========================
    {
        "title": "DevOps Engineer",
        "description": "Mengotomatisasi deployment dan infrastruktur.",
        "skills": [
            "docker",
            "kubernetes",
            "aws",
            "linux",
            "git",
            "ci/cd"
        ]
    },
    {
        "title": "Cloud Engineer",
        "description": "Mengelola layanan cloud dan infrastruktur.",
        "skills": [
            "aws",
            "azure",
            "gcp",
            "docker",
            "linux"
        ]
    },

    # =========================
    # DESIGN
    # =========================
    {
        "title": "UI/UX Designer",
        "description": "Merancang antarmuka dan pengalaman pengguna.",
        "skills": [
            "figma",
            "ui",
            "ux",
            "wireframe",
            "prototype"
        ]
    },
    {
        "title": "Graphic Designer",
        "description": "Membuat desain visual dan branding.",
        "skills": [
            "photoshop",
            "illustrator",
            "canva",
            "branding"
        ]
    },

    # =========================
    # BUSINESS
    # =========================
    {
        "title": "Business Analyst",
        "description": "Menganalisis kebutuhan bisnis dan memberikan solusi.",
        "skills": [
            "excel",
            "sql",
            "business analysis",
            "communication",
            "project management"
        ]
    },
    {
        "title": "Project Manager",
        "description": "Mengelola proyek dan tim.",
        "skills": [
            "project management",
            "agile",
            "scrum",
            "jira",
            "leadership"
        ]
    },
    {
        "title": "Product Manager",
        "description": "Mengelola pengembangan produk digital.",
        "skills": [
            "agile",
            "scrum",
            "leadership",
            "communication",
            "business analysis"
        ]
    },

    # =========================
    # MARKETING
    # =========================
    {
        "title": "Digital Marketing Specialist",
        "description": "Mengembangkan strategi pemasaran digital.",
        "skills": [
            "seo",
            "sem",
            "google analytics",
            "social media marketing",
            "content marketing"
        ]
    },
    {
        "title": "Content Creator",
        "description": "Membuat dan mengelola konten digital.",
        "skills": [
            "copywriting",
            "content marketing",
            "canva",
            "social media marketing"
        ]
    },

    # =========================
    # FINANCE
    # =========================
    {
        "title": "Accountant",
        "description": "Mengelola laporan keuangan dan akuntansi.",
        "skills": [
            "accounting",
            "financial analysis",
            "excel",
            "auditing",
            "tax"
        ]
    },
    {
        "title": "Financial Analyst",
        "description": "Menganalisis data keuangan dan investasi.",
        "skills": [
            "financial analysis",
            "excel",
            "statistics",
            "accounting"
        ]
    },

    # =========================
    # HR
    # =========================
    {
        "title": "HR Specialist",
        "description": "Mengelola proses rekrutmen dan SDM.",
        "skills": [
            "recruitment",
            "talent acquisition",
            "communication",
            "employee relations"
        ]
    },

    # =========================
    # OFFICE
    # =========================
    {
        "title": "Administrative Staff",
        "description": "Mengelola administrasi dan dokumentasi.",
        "skills": [
            "microsoft office",
            "word",
            "excel",
            "powerpoint",
            "communication"
        ]
    }
]

def get_job_recommendations(
        resume_skills,
        num_recs=3
):
    recommendations = []

    resume_skills = {
        skill.lower()
        for skill in resume_skills
    }

    for job in JOB_DATABASE:

        job_skills = set(
            skill.lower()
            for skill in job.get("skills", [])
        )

        matched = (
            job_skills &
            resume_skills
        )

        if not matched:
            continue

        score = round(
            (
                len(matched)
                /
                len(job_skills)
            ) * 100
        )

        recommendations.append({
            "title": job["title"],
            "description": job["description"],
            "match_score": score,
            "matched_skills": sorted(
                list(matched)
            )
        })

    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations[:num_recs]