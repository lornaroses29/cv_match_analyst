INDO_SYNONYM = {
    "pemrograman": [
        "programming",
        "coding",
        "pengkodean"
    ],

    "pengembangan web": [
        "web development",
        "website",
        "web"
    ],

    "basis data": [
        "database",
        "db",
        "sql"
    ],

    "kecerdasan buatan": [
        "artificial intelligence",
        "ai"
    ],

    "machine learning": [
        "ml",
        "pembelajaran mesin"
    ],

    "data science": [
        "ilmu data",
        "data scientist"
    ],

    "analisis data": [
        "data analysis",
        "analytics",
        "analitik"
    ],

    "frontend": [
        "front end",
        "ui"
    ],

    "backend": [
        "back end",
        "server"
    ],

    "fullstack": [
        "full stack",
        "full-stack"
    ],

    "javascript": [
        "js"
    ],

    "python": [
        "py"
    ],

    "manajemen proyek": [
        "project management"
    ],

    "pengujian": [
        "testing",
        "quality assurance",
        "qa"
    ],

    "visualisasi data": [
        "data visualization",
        "dashboard"
    ],

    "komunikasi": [
        "communication"
    ],

    "kepemimpinan": [
        "leadership"
    ],

    "kerja tim": [
        "teamwork",
        "collaboration"
    ]
}

SYNONYM_MAP = {
    "frontend": {
        "front end",
        "front-end"
    },
    "backend": {
        "back end",
        "back-end"
    },
    "javascript": {
        "js"
    },
    "machine learning": {
        "ml"
    },
    "artificial intelligence": {
        "ai"
    },
    "ui": {
        "user interface"
    },
    "ux": {
        "user experience"
    }
}


def expand_indonesian_synonyms(keywords: set):
    expanded = set(keywords)

    for word in keywords:

        if word in INDO_SYNONYM:
            expanded.update(
                INDO_SYNONYM[word]
            )

        for key, values in INDO_SYNONYM.items():
            if word in values:
                expanded.add(key)
                expanded.update(values)

    return expanded