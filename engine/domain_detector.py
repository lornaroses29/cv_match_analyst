from engine.skill_database import SKILL_CATEGORIES

def detect_domain(keywords):
    best_domain = None
    best_score = 0

    for domain, skills in SKILL_CATEGORIES.items():
        score = len(keywords & skills)

        if score > best_score:
            best_score = score
            best_domain = domain

    return best_domain