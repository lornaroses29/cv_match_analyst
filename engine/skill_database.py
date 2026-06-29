# engine/skill_database.py

SKILL_CATEGORIES = {

    "information_technology": {
        "python", "java", "javascript", "typescript",
        "php", "c", "c++", "c#", "go", "kotlin",
        "swift", "dart",
        "react", "vue", "angular",
        "node", "express", "laravel",
        "django", "flask", "spring boot",
        "mysql", "postgresql", "mongodb",
        "firebase", "oracle", "sql", "nosql",
        "git", "github",
        "docker", "kubernetes",
        "linux", "aws", "azure", "gcp",
        "machine learning", "deep learning",
        "artificial intelligence",
        "data science",
        "data analysis",
        "power bi",
        "tableau",
        "excel",
        "api",
        "rest api",
        "web development",
        "frontend",
        "backend",
        "full stack",
        "software engineering",
        "oop",
        "algoritma",
        "struktur data",
        "computer vision",
        "nlp",
        "streamlit",
        "tensorflow",
        "pytorch",
        "scikit learn",
        "pandas",
        "numpy"
    },

    "data": {
        "python",
        "sql",
        "excel",
        "tableau",
        "power bi",
        "statistics",
        "machine learning",
        "data mining",
        "data visualization",
        "data cleaning",
        "data wrangling",
        "business intelligence",
        "forecasting",
        "predictive analytics",
        "r",
        "pandas",
        "numpy",
        "scikit learn"
    },

    "finance": {
        "accounting",
        "bookkeeping",
        "financial analysis",
        "financial reporting",
        "tax",
        "taxation",
        "auditing",
        "budgeting",
        "forecasting",
        "cash flow",
        "payroll",
        "invoice",
        "accounts payable",
        "accounts receivable",
        "quickbooks",
        "sap",
        "erp",
        "financial modeling",
        "general ledger"
    },

    "human_resources": {
        "recruitment",
        "talent acquisition",
        "interview",
        "training",
        "employee relations",
        "payroll",
        "human resources",
        "hris",
        "performance management",
        "onboarding",
        "offboarding",
        "people development"
    },

    "marketing": {
        "digital marketing",
        "seo",
        "sem",
        "social media",
        "content marketing",
        "copywriting",
        "email marketing",
        "branding",
        "market research",
        "campaign management",
        "google analytics",
        "google ads",
        "meta ads",
        "instagram marketing",
        "tiktok marketing",
        "content creation"
    },

    "design": {
        "figma",
        "adobe photoshop",
        "illustrator",
        "canva",
        "ui design",
        "ux design",
        "wireframing",
        "prototyping",
        "graphic design",
        "video editing",
        "adobe premiere",
        "after effects"
    },

    "healthcare": {
        "nursing",
        "patient care",
        "medical records",
        "hospital administration",
        "healthcare management",
        "clinical procedures",
        "first aid",
        "emergency response",
        "medication administration",
        "infection control",
        "phlebotomy",
        "electronic medical records"
    },

    "education": {
        "teaching",
        "curriculum development",
        "classroom management",
        "lesson planning",
        "assessment",
        "tutoring",
        "public speaking",
        "research",
        "mentoring"
    },

    "engineering": {
        "autocad",
        "solidworks",
        "civil engineering",
        "mechanical engineering",
        "electrical engineering",
        "project management",
        "quality control",
        "manufacturing",
        "construction management",
        "technical drawing"
    },

    "sales": {
        "sales",
        "negotiation",
        "customer relationship",
        "lead generation",
        "crm",
        "business development",
        "presentation",
        "customer service",
        "account management"
    },

    "operations": {
        "administration",
        "microsoft office",
        "excel",
        "project management",
        "documentation",
        "scheduling",
        "inventory management",
        "procurement",
        "coordination",
        "reporting"
    }
}


SOFT_SKILLS = {
    "communication",
    "teamwork",
    "leadership",
    "problem solving",
    "critical thinking",
    "adaptability",
    "time management",
    "creativity",
    "analytical thinking",
    "attention to detail",
    "collaboration",
    "presentation",
    "decision making"
}


SKILL_ALIAS = {
    "js": "javascript",
    "reactjs": "react",
    "react.js": "react",
    "nodejs": "node",
    "node.js": "node",
    "postgres": "postgresql",
    "machine-learning": "machine learning",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "ui/ux": "ui design",
    "ux/ui": "ui design",
    "hr": "human resources",
    "hrd": "human resources",
    "seo specialist": "seo",
    "social media marketing": "social media",
    "frontend developer": "frontend",
    "backend developer": "backend",
    "fullstack": "full stack",
    "data analyst": "data analysis",
    "data scientist": "data science",
    "software engineer": "software engineering",
    "software developer": "software engineering"
}


# ===========================
# Gabungkan semua skill
# ===========================

TECH_SKILLS = set()

for skills in SKILL_CATEGORIES.values():
    TECH_SKILLS.update(skills)

TECH_SKILLS.update(SOFT_SKILLS)