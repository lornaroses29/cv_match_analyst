# ──────────────────────────────────────────────────────────────────────
# Job database & recommendation logic
# ──────────────────────────────────────────────────────────────────────

JOB_DATABASE = [
    # ── Teknologi & IT ──────────────────────────────────────────────
    {"title": "Frontend Developer", "keywords": {"react", "javascript", "typescript", "css", "html", "vue", "angular", "nextjs", "tailwind", "frontend", "ui", "web"}, "description": "Membangun antarmuka pengguna yang interaktif dan responsif menggunakan teknologi web modern."},
    {"title": "Backend Developer", "keywords": {"python", "java", "node", "golang", "api", "database", "sql", "rest", "microservices", "backend", "server", "express", "django", "flask", "spring"}, "description": "Mengembangkan server-side logic, API, dan integrasi database untuk aplikasi."},
    {"title": "Full Stack Developer", "keywords": {"react", "node", "javascript", "typescript", "python", "database", "api", "fullstack", "mongodb", "postgresql", "aws"}, "description": "Menangani pengembangan end-to-end dari frontend hingga backend aplikasi web."},
    {"title": "Mobile Developer", "keywords": {"android", "ios", "kotlin", "swift", "flutter", "mobile", "app", "java", "dart", "react"}, "description": "Mengembangkan aplikasi mobile untuk platform Android dan/atau iOS."},
    {"title": "DevOps Engineer", "keywords": {"docker", "kubernetes", "aws", "azure", "gcp", "ci", "cd", "jenkins", "terraform", "linux", "cloud", "infrastructure", "devops"}, "description": "Mengelola infrastruktur cloud, CI/CD pipeline, dan otomatisasi deployment."},
    {"title": "Data Engineer", "keywords": {"python", "sql", "spark", "airflow", "etl", "data", "pipeline", "warehouse", "hadoop", "kafka", "bigquery"}, "description": "Membangun dan mengelola infrastruktur data dan ETL pipeline."},
    {"title": "Data Scientist", "keywords": {"python", "machine", "learning", "tensorflow", "pytorch", "pandas", "numpy", "statistics", "ai", "model", "deep", "scikit"}, "description": "Membangun model machine learning dan mengekstrak insight dari data kompleks."},
    {"title": "Data Analyst", "keywords": {"sql", "python", "excel", "tableau", "powerbi", "analytics", "data", "visualization", "statistics", "reporting", "dashboard"}, "description": "Menganalisis data bisnis dan membuat visualisasi untuk mendukung pengambilan keputusan."},
    {"title": "Business Intelligence Analyst", "keywords": {"sql", "tableau", "powerbi", "looker", "analytics", "reporting", "dashboard", "kpi", "metrics", "business"}, "description": "Membuat dashboard dan laporan untuk mendukung keputusan bisnis berbasis data."},
    {"title": "Machine Learning Engineer", "keywords": {"python", "tensorflow", "pytorch", "mlops", "model", "deployment", "ai", "deep", "learning", "aws", "gcp"}, "description": "Mengembangkan dan men-deploy model machine learning ke production."},
    {"title": "AI Engineer", "keywords": {"ai", "llm", "gpt", "langchain", "python", "nlp", "chatbot", "openai", "prompt", "embeddings", "rag"}, "description": "Membangun aplikasi berbasis AI dan Large Language Models."},
    {"title": "Cloud Architect", "keywords": {"aws", "azure", "gcp", "cloud", "architecture", "serverless", "microservices", "terraform", "security", "scalability"}, "description": "Merancang arsitektur cloud yang scalable dan secure."},
    {"title": "System Administrator", "keywords": {"linux", "windows", "server", "network", "security", "admin", "system", "infrastructure", "monitoring", "backup"}, "description": "Mengelola dan memelihara sistem server dan infrastruktur IT."},
    {"title": "Network Engineer", "keywords": {"network", "cisco", "routing", "switching", "firewall", "vpn", "tcp", "ip", "wan", "lan", "security"}, "description": "Merancang dan mengelola infrastruktur jaringan perusahaan."},
    {"title": "Cybersecurity Analyst", "keywords": {"security", "penetration", "firewall", "network", "vulnerability", "cyber", "encryption", "audit", "compliance", "siem"}, "description": "Melindungi sistem dan data dari ancaman keamanan siber."},
    {"title": "Security Engineer", "keywords": {"security", "devsecops", "vulnerability", "penetration", "encryption", "compliance", "soc", "incident", "forensics"}, "description": "Mengimplementasikan keamanan dalam sistem dan infrastruktur IT."},
    {"title": "QA Engineer", "keywords": {"testing", "automation", "selenium", "cypress", "qa", "quality", "test", "manual", "bug", "jira", "postman"}, "description": "Memastikan kualitas software melalui pengujian manual dan otomatis."},
    {"title": "Software Architect", "keywords": {"architecture", "design", "patterns", "microservices", "scalability", "system", "technical", "leadership"}, "description": "Merancang arsitektur software yang scalable dan maintainable."},
    {"title": "Technical Lead", "keywords": {"leadership", "technical", "team", "architecture", "code", "review", "mentoring", "agile", "development"}, "description": "Memimpin tim teknis dan memberikan arahan arsitektur."},
    {"title": "IT Support Specialist", "keywords": {"support", "helpdesk", "troubleshooting", "hardware", "software", "windows", "network", "ticket", "customer"}, "description": "Memberikan dukungan teknis untuk pengguna dan sistem IT."},
    {"title": "Database Administrator", "keywords": {"database", "sql", "mysql", "postgresql", "oracle", "mongodb", "backup", "performance", "tuning", "replication"}, "description": "Mengelola dan mengoptimalkan database perusahaan."},
    {"title": "Game Developer", "keywords": {"unity", "unreal", "game", "3d", "c", "csharp", "gamedev", "graphics", "physics", "animation"}, "description": "Mengembangkan video game untuk berbagai platform."},
    {"title": "Embedded Systems Engineer", "keywords": {"embedded", "firmware", "c", "microcontroller", "iot", "rtos", "hardware", "arduino", "raspberry"}, "description": "Mengembangkan software untuk perangkat embedded dan IoT."},
    {"title": "Blockchain Developer", "keywords": {"blockchain", "solidity", "ethereum", "smart", "contract", "web3", "crypto", "defi", "nft"}, "description": "Membangun aplikasi berbasis blockchain dan smart contract."},

    # ── Desain & Kreatif ────────────────────────────────────────────
    {"title": "UI/UX Designer", "keywords": {"figma", "sketch", "adobe", "design", "prototype", "wireframe", "user", "experience", "interface", "ux", "ui", "research"}, "description": "Merancang pengalaman pengguna dan antarmuka visual yang intuitif."},
    {"title": "Graphic Designer", "keywords": {"photoshop", "illustrator", "design", "branding", "visual", "logo", "creative", "typography", "layout", "adobe"}, "description": "Membuat desain visual untuk branding, marketing, dan media."},
    {"title": "Product Designer", "keywords": {"figma", "design", "product", "ux", "ui", "prototype", "research", "systems", "interaction"}, "description": "Merancang produk digital dari konsep hingga implementasi."},
    {"title": "Motion Graphics Designer", "keywords": {"aftereffects", "animation", "motion", "video", "premiere", "2d", "3d", "visual", "effects"}, "description": "Membuat animasi dan motion graphics untuk video dan media digital."},
    {"title": "Video Editor", "keywords": {"premiere", "finalcut", "davinci", "video", "editing", "color", "grading", "audio", "storytelling"}, "description": "Mengedit dan memproduksi konten video."},
    {"title": "3D Artist", "keywords": {"blender", "maya", "3ds", "max", "3d", "modeling", "texturing", "rendering", "animation", "zbrush"}, "description": "Membuat model dan animasi 3D untuk berbagai media."},
    {"title": "Illustrator", "keywords": {"illustration", "drawing", "digital", "art", "procreate", "photoshop", "character", "concept", "creative"}, "description": "Membuat ilustrasi digital dan tradisional."},
    {"title": "Creative Director", "keywords": {"creative", "direction", "branding", "strategy", "team", "leadership", "campaign", "visual", "concept"}, "description": "Memimpin tim kreatif dan mengarahkan visi visual brand."},
    {"title": "Brand Designer", "keywords": {"branding", "identity", "logo", "design", "guidelines", "visual", "strategy", "creative"}, "description": "Mengembangkan identitas visual dan brand guidelines."},
    {"title": "Interior Designer", "keywords": {"interior", "design", "autocad", "sketchup", "3d", "furniture", "space", "planning", "rendering"}, "description": "Merancang ruang interior yang fungsional dan estetis."},
    {"title": "Architect", "keywords": {"architecture", "autocad", "revit", "design", "building", "construction", "3d", "planning", "structural"}, "description": "Merancang bangunan dan struktur arsitektur."},
    {"title": "Fashion Designer", "keywords": {"fashion", "design", "textile", "pattern", "sewing", "collection", "trend", "apparel", "clothing"}, "description": "Merancang pakaian dan koleksi fashion."},
    {"title": "Photographer", "keywords": {"photography", "lightroom", "photoshop", "camera", "lighting", "editing", "portrait", "commercial", "product"}, "description": "Mengambil dan mengedit foto profesional."},
    {"title": "Videographer", "keywords": {"video", "filming", "camera", "drone", "editing", "production", "documentary", "commercial", "storytelling"}, "description": "Memproduksi konten video dari shooting hingga editing."},

    # ── Marketing & Komunikasi ──────────────────────────────────────
    {"title": "Digital Marketing Specialist", "keywords": {"digital", "marketing", "seo", "sem", "google", "ads", "facebook", "analytics", "campaign", "social"}, "description": "Mengelola kampanye pemasaran digital dan optimasi online presence."},
    {"title": "Social Media Manager", "keywords": {"social", "media", "instagram", "tiktok", "facebook", "content", "engagement", "community", "scheduling"}, "description": "Mengelola akun media sosial dan strategi konten."},
    {"title": "Content Writer", "keywords": {"writing", "content", "copywriting", "blog", "article", "seo", "editing", "creative", "storytelling"}, "description": "Menulis konten untuk website, blog, dan media digital."},
    {"title": "Copywriter", "keywords": {"copywriting", "advertising", "creative", "writing", "campaign", "headline", "tagline", "brand", "messaging"}, "description": "Menulis copy persuasif untuk iklan dan marketing."},
    {"title": "SEO Specialist", "keywords": {"seo", "google", "analytics", "keyword", "backlink", "ranking", "search", "optimization", "content"}, "description": "Mengoptimalkan website untuk mesin pencari."},
    {"title": "Marketing Manager", "keywords": {"marketing", "strategy", "campaign", "budget", "team", "brand", "growth", "analytics", "leadership"}, "description": "Memimpin strategi dan tim marketing perusahaan."},
    {"title": "Brand Manager", "keywords": {"brand", "marketing", "strategy", "positioning", "campaign", "consumer", "research", "growth"}, "description": "Mengelola dan mengembangkan brand perusahaan."},
    {"title": "Public Relations Specialist", "keywords": {"pr", "media", "press", "communication", "crisis", "reputation", "stakeholder", "release"}, "description": "Mengelola hubungan dengan media dan reputasi perusahaan."},
    {"title": "Content Strategist", "keywords": {"content", "strategy", "planning", "editorial", "calendar", "seo", "audience", "engagement"}, "description": "Merancang strategi konten yang efektif."},
    {"title": "Email Marketing Specialist", "keywords": {"email", "marketing", "campaign", "automation", "mailchimp", "newsletter", "conversion", "crm"}, "description": "Mengelola kampanye email marketing dan automation."},
    {"title": "Growth Hacker", "keywords": {"growth", "marketing", "acquisition", "retention", "analytics", "experiment", "funnel", "viral"}, "description": "Mengembangkan strategi pertumbuhan yang inovatif."},
    {"title": "Market Research Analyst", "keywords": {"research", "market", "survey", "analysis", "consumer", "data", "insights", "trends", "competitive"}, "description": "Melakukan riset pasar dan analisis kompetitor."},
    {"title": "Event Coordinator", "keywords": {"event", "planning", "coordination", "venue", "vendor", "budget", "logistics", "conference"}, "description": "Merencanakan dan mengkoordinasi acara perusahaan."},
    {"title": "Communications Specialist", "keywords": {"communication", "internal", "corporate", "messaging", "newsletter", "stakeholder", "content"}, "description": "Mengelola komunikasi internal dan eksternal perusahaan."},

    # ── Bisnis & Manajemen ──────────────────────────────────────────
    {"title": "Product Manager", "keywords": {"product", "management", "agile", "scrum", "roadmap", "stakeholder", "strategy", "backlog", "sprint", "jira", "analytics"}, "description": "Mengelola lifecycle produk dari ideasi hingga launch."},
    {"title": "Project Manager", "keywords": {"project", "management", "planning", "timeline", "budget", "stakeholder", "risk", "agile", "pmp", "team"}, "description": "Mengelola proyek dari perencanaan hingga eksekusi."},
    {"title": "Business Analyst", "keywords": {"business", "analysis", "requirements", "process", "stakeholder", "documentation", "sql", "agile"}, "description": "Menganalisis kebutuhan bisnis dan merancang solusi."},
    {"title": "Operations Manager", "keywords": {"operations", "management", "process", "efficiency", "team", "kpi", "logistics", "supply", "chain"}, "description": "Mengelola operasional harian dan efisiensi proses."},
    {"title": "Business Development Manager", "keywords": {"business", "development", "sales", "partnership", "strategy", "negotiation", "growth", "client"}, "description": "Mengembangkan peluang bisnis dan kemitraan baru."},
    {"title": "Strategy Consultant", "keywords": {"strategy", "consulting", "analysis", "business", "market", "recommendation", "presentation", "client"}, "description": "Memberikan rekomendasi strategis untuk klien."},
    {"title": "General Manager", "keywords": {"management", "leadership", "operations", "strategy", "budget", "team", "kpi", "business"}, "description": "Memimpin keseluruhan operasi unit bisnis."},
    {"title": "Entrepreneur", "keywords": {"startup", "business", "founder", "venture", "pitch", "investor", "growth", "innovation", "leadership"}, "description": "Membangun dan menjalankan bisnis sendiri."},
    {"title": "Management Trainee", "keywords": {"trainee", "management", "rotation", "leadership", "development", "graduate", "business"}, "description": "Program pengembangan untuk calon manajer."},
    {"title": "Scrum Master", "keywords": {"scrum", "agile", "sprint", "team", "facilitation", "kanban", "retrospective", "jira"}, "description": "Memfasilitasi tim agile dan proses scrum."},
    {"title": "Supply Chain Manager", "keywords": {"supply", "chain", "logistics", "inventory", "procurement", "vendor", "planning", "erp"}, "description": "Mengelola rantai pasokan dan logistik."},
    {"title": "Procurement Specialist", "keywords": {"procurement", "purchasing", "vendor", "negotiation", "contract", "sourcing", "cost"}, "description": "Mengelola pengadaan barang dan jasa."},

    # ── Keuangan & Akuntansi ────────────────────────────────────────
    {"title": "Accountant", "keywords": {"accounting", "finance", "bookkeeping", "journal", "ledger", "tax", "audit", "excel", "sap", "financial"}, "description": "Mengelola pencatatan keuangan dan laporan akuntansi."},
    {"title": "Financial Analyst", "keywords": {"finance", "analysis", "modeling", "excel", "valuation", "forecasting", "investment", "reporting"}, "description": "Menganalisis data keuangan dan membuat proyeksi."},
    {"title": "Tax Consultant", "keywords": {"tax", "accounting", "compliance", "planning", "regulation", "filing", "corporate", "advisory"}, "description": "Memberikan konsultasi dan perencanaan pajak."},
    {"title": "Auditor", "keywords": {"audit", "internal", "external", "compliance", "risk", "financial", "reporting", "control"}, "description": "Melakukan audit keuangan dan kepatuhan."},
    {"title": "Investment Analyst", "keywords": {"investment", "portfolio", "analysis", "stock", "bond", "market", "research", "valuation"}, "description": "Menganalisis peluang investasi dan portofolio."},
    {"title": "Risk Analyst", "keywords": {"risk", "analysis", "management", "compliance", "financial", "credit", "market", "operational"}, "description": "Mengidentifikasi dan mengelola risiko bisnis."},
    {"title": "Finance Manager", "keywords": {"finance", "management", "budget", "forecasting", "reporting", "team", "strategy", "treasury"}, "description": "Memimpin fungsi keuangan perusahaan."},
    {"title": "Controller", "keywords": {"controller", "accounting", "financial", "reporting", "budget", "compliance", "management", "audit"}, "description": "Mengawasi fungsi akuntansi dan pelaporan keuangan."},
    {"title": "Treasury Analyst", "keywords": {"treasury", "cash", "management", "liquidity", "banking", "forex", "investment", "risk"}, "description": "Mengelola kas dan likuiditas perusahaan."},
    {"title": "Credit Analyst", "keywords": {"credit", "analysis", "risk", "lending", "financial", "assessment", "loan", "banking"}, "description": "Menganalisis kelayakan kredit dan risiko pinjaman."},
    {"title": "Payroll Specialist", "keywords": {"payroll", "salary", "tax", "benefits", "hris", "compliance", "processing"}, "description": "Mengelola penggajian dan administrasi karyawan."},
    {"title": "Bookkeeper", "keywords": {"bookkeeping", "accounting", "invoice", "reconciliation", "accounts", "payable", "receivable", "excel"}, "description": "Mencatat transaksi keuangan harian."},

    # ── Sales & Customer Service ────────────────────────────────────
    {"title": "Sales Executive", "keywords": {"sales", "selling", "target", "client", "negotiation", "presentation", "crm", "b2b", "revenue"}, "description": "Menjual produk/jasa dan mencapai target penjualan."},
    {"title": "Account Manager", "keywords": {"account", "client", "relationship", "sales", "retention", "growth", "crm", "service"}, "description": "Mengelola hubungan dengan klien existing."},
    {"title": "Sales Manager", "keywords": {"sales", "management", "team", "target", "strategy", "coaching", "pipeline", "revenue"}, "description": "Memimpin tim sales dan strategi penjualan."},
    {"title": "Business Development Representative", "keywords": {"bdr", "sales", "prospecting", "lead", "outreach", "cold", "calling", "pipeline"}, "description": "Mencari dan mengkualifikasi prospek baru."},
    {"title": "Customer Success Manager", "keywords": {"customer", "success", "retention", "onboarding", "churn", "relationship", "saas", "support"}, "description": "Memastikan kepuasan dan retensi pelanggan."},
    {"title": "Customer Service Representative", "keywords": {"customer", "service", "support", "helpdesk", "complaint", "resolution", "communication"}, "description": "Menangani pertanyaan dan keluhan pelanggan."},
    {"title": "Call Center Agent", "keywords": {"call", "center", "phone", "customer", "service", "inbound", "outbound", "communication"}, "description": "Menangani panggilan telepon pelanggan."},
    {"title": "Technical Support Engineer", "keywords": {"technical", "support", "troubleshooting", "customer", "ticket", "escalation", "product"}, "description": "Memberikan dukungan teknis untuk produk."},
    {"title": "Key Account Manager", "keywords": {"key", "account", "enterprise", "client", "relationship", "strategic", "sales", "revenue"}, "description": "Mengelola akun-akun strategis perusahaan."},
    {"title": "Retail Sales Associate", "keywords": {"retail", "sales", "store", "customer", "product", "cashier", "inventory", "service"}, "description": "Melayani pelanggan di toko retail."},
    {"title": "Telesales", "keywords": {"telesales", "phone", "sales", "cold", "calling", "script", "target", "closing"}, "description": "Menjual produk melalui telepon."},

    # ── HR & People ─────────────────────────────────────────────────
    {"title": "HR Generalist", "keywords": {"hr", "human", "resources", "recruitment", "payroll", "employee", "relations", "compliance"}, "description": "Menangani berbagai fungsi HR secara umum."},
    {"title": "Recruiter", "keywords": {"recruitment", "hiring", "sourcing", "interview", "candidate", "talent", "linkedin", "ats"}, "description": "Mencari dan merekrut kandidat terbaik."},
    {"title": "Talent Acquisition Specialist", "keywords": {"talent", "acquisition", "recruitment", "employer", "branding", "sourcing", "hiring"}, "description": "Mengembangkan strategi akuisisi talent."},
    {"title": "HR Manager", "keywords": {"hr", "management", "team", "policy", "employee", "relations", "compliance", "strategy"}, "description": "Memimpin fungsi HR perusahaan."},
    {"title": "Learning & Development Specialist", "keywords": {"learning", "development", "training", "lms", "curriculum", "facilitation", "onboarding"}, "description": "Mengembangkan program pelatihan karyawan."},
    {"title": "Compensation & Benefits Analyst", "keywords": {"compensation", "benefits", "salary", "benchmark", "payroll", "reward", "analysis"}, "description": "Mengelola kompensasi dan benefit karyawan."},
    {"title": "HR Business Partner", "keywords": {"hrbp", "business", "partner", "strategic", "employee", "relations", "talent", "management"}, "description": "Menjadi mitra strategis HR untuk unit bisnis."},
    {"title": "People Operations Specialist", "keywords": {"people", "operations", "hris", "onboarding", "employee", "experience", "process"}, "description": "Mengelola operasional HR dan employee experience."},
    {"title": "Organizational Development Specialist", "keywords": {"organizational", "development", "change", "management", "culture", "performance", "assessment"}, "description": "Mengembangkan organisasi dan manajemen perubahan."},

    # ── Hukum & Legal ───────────────────────────────────────────────
    {"title": "Legal Counsel", "keywords": {"legal", "law", "contract", "compliance", "corporate", "litigation", "advisory", "regulation"}, "description": "Memberikan nasihat hukum untuk perusahaan."},
    {"title": "Paralegal", "keywords": {"paralegal", "legal", "research", "document", "contract", "filing", "administrative"}, "description": "Mendukung tim legal dengan riset dan administrasi."},
    {"title": "Contract Manager", "keywords": {"contract", "legal", "negotiation", "agreement", "vendor", "compliance", "review"}, "description": "Mengelola kontrak dan perjanjian bisnis."},
    {"title": "Compliance Officer", "keywords": {"compliance", "regulation", "policy", "audit", "risk", "legal", "governance"}, "description": "Memastikan kepatuhan terhadap regulasi."},
    {"title": "Intellectual Property Specialist", "keywords": {"ip", "patent", "trademark", "copyright", "legal", "protection", "licensing"}, "description": "Mengelola hak kekayaan intelektual."},
    {"title": "Corporate Secretary", "keywords": {"corporate", "secretary", "governance", "board", "compliance", "filing", "regulation"}, "description": "Mengelola tata kelola perusahaan."},

    # ── Kesehatan & Medis ───────────────────────────────────────────
    {"title": "Dokter Umum", "keywords": {"dokter", "medis", "pasien", "diagnosis", "resep", "konsultasi", "kesehatan", "klinik"}, "description": "Memberikan pelayanan kesehatan umum kepada pasien."},
    {"title": "Perawat", "keywords": {"perawat", "nursing", "pasien", "medis", "obat", "perawatan", "rumah", "sakit"}, "description": "Memberikan asuhan keperawatan kepada pasien."},
    {"title": "Apoteker", "keywords": {"apoteker", "farmasi", "obat", "resep", "dispensing", "konsultasi", "pharmacy"}, "description": "Mengelola dan memberikan obat-obatan."},
    {"title": "Radiografer", "keywords": {"radiografi", "rontgen", "ct", "mri", "imaging", "medis", "diagnostik"}, "description": "Melakukan pemeriksaan radiologi diagnostik."},
    {"title": "Lab Technician", "keywords": {"laboratorium", "lab", "sample", "test", "analysis", "medis", "diagnostik"}, "description": "Melakukan pemeriksaan laboratorium medis."},
    {"title": "Nutritionist", "keywords": {"nutrisi", "diet", "gizi", "konsultasi", "meal", "plan", "kesehatan", "food"}, "description": "Memberikan konsultasi gizi dan nutrisi."},
    {"title": "Physiotherapist", "keywords": {"fisioterapi", "rehabilitation", "exercise", "therapy", "patient", "movement", "injury"}, "description": "Memberikan terapi fisik untuk pemulihan pasien."},
    {"title": "Psychologist", "keywords": {"psikologi", "counseling", "therapy", "mental", "health", "assessment", "patient"}, "description": "Memberikan layanan psikologi dan konseling."},
    {"title": "Health Administrator", "keywords": {"health", "administration", "hospital", "management", "operations", "compliance", "medical"}, "description": "Mengelola administrasi fasilitas kesehatan."},

    # ── Pendidikan ──────────────────────────────────────────────────
    {"title": "Guru/Teacher", "keywords": {"guru", "teacher", "mengajar", "kurikulum", "siswa", "pendidikan", "kelas", "lesson", "plan"}, "description": "Mengajar dan mendidik siswa di sekolah."},
    {"title": "Dosen/Lecturer", "keywords": {"dosen", "lecturer", "universitas", "research", "publikasi", "mahasiswa", "akademik"}, "description": "Mengajar dan melakukan penelitian di perguruan tinggi."},
    {"title": "Tutor", "keywords": {"tutor", "private", "teaching", "student", "subject", "exam", "preparation"}, "description": "Memberikan bimbingan belajar privat."},
    {"title": "Curriculum Developer", "keywords": {"curriculum", "education", "learning", "design", "content", "assessment", "pedagogy"}, "description": "Mengembangkan kurikulum dan materi pembelajaran."},
    {"title": "Academic Counselor", "keywords": {"counselor", "student", "guidance", "academic", "career", "admission", "university"}, "description": "Memberikan bimbingan akademik dan karir."},
    {"title": "Education Consultant", "keywords": {"education", "consultant", "school", "admission", "overseas", "study", "planning"}, "description": "Memberikan konsultasi pendidikan dan studi."},
    {"title": "Instructional Designer", "keywords": {"instructional", "design", "elearning", "course", "lms", "content", "learning"}, "description": "Merancang materi pembelajaran online."},
    {"title": "School Administrator", "keywords": {"school", "administration", "management", "operations", "staff", "student", "education"}, "description": "Mengelola administrasi sekolah."},

    # ── Teknik & Engineering ────────────────────────────────────────
    {"title": "Mechanical Engineer", "keywords": {"mechanical", "engineering", "cad", "autocad", "solidworks", "design", "manufacturing", "machine"}, "description": "Merancang dan mengembangkan sistem mekanik."},
    {"title": "Electrical Engineer", "keywords": {"electrical", "engineering", "circuit", "plc", "power", "electronics", "design", "system"}, "description": "Merancang sistem dan komponen elektrik."},
    {"title": "Civil Engineer", "keywords": {"civil", "engineering", "construction", "structural", "autocad", "building", "infrastructure"}, "description": "Merancang infrastruktur dan konstruksi."},
    {"title": "Chemical Engineer", "keywords": {"chemical", "engineering", "process", "plant", "production", "quality", "safety"}, "description": "Mengembangkan proses kimia industri."},
    {"title": "Industrial Engineer", "keywords": {"industrial", "engineering", "process", "efficiency", "lean", "manufacturing", "optimization"}, "description": "Mengoptimalkan proses dan sistem industri."},
    {"title": "Quality Engineer", "keywords": {"quality", "engineering", "qc", "inspection", "iso", "six", "sigma", "testing"}, "description": "Memastikan kualitas produk dan proses."},
    {"title": "Manufacturing Engineer", "keywords": {"manufacturing", "production", "process", "lean", "automation", "assembly", "engineering"}, "description": "Mengembangkan proses manufaktur."},
    {"title": "Environmental Engineer", "keywords": {"environmental", "engineering", "sustainability", "waste", "pollution", "compliance", "green"}, "description": "Mengembangkan solusi lingkungan."},
    {"title": "Petroleum Engineer", "keywords": {"petroleum", "oil", "gas", "drilling", "reservoir", "production", "engineering"}, "description": "Mengekstraksi minyak dan gas bumi."},
    {"title": "Automotive Engineer", "keywords": {"automotive", "vehicle", "car", "engine", "design", "testing", "manufacturing"}, "description": "Merancang dan mengembangkan kendaraan."},

    # ── Hospitality & F&B ───────────────────────────────────────────
    {"title": "Hotel Manager", "keywords": {"hotel", "management", "hospitality", "guest", "operations", "front", "office", "service"}, "description": "Mengelola operasional hotel."},
    {"title": "Front Office Staff", "keywords": {"front", "office", "reception", "check", "guest", "service", "hospitality", "hotel"}, "description": "Melayani tamu di front office hotel."},
    {"title": "Housekeeping Supervisor", "keywords": {"housekeeping", "cleaning", "room", "hotel", "supervisor", "hygiene", "laundry"}, "description": "Mengawasi kebersihan dan kerapian hotel."},
    {"title": "Chef", "keywords": {"chef", "cooking", "kitchen", "culinary", "menu", "food", "restaurant", "recipe"}, "description": "Memasak dan mengelola dapur."},
    {"title": "F&B Manager", "keywords": {"food", "beverage", "restaurant", "management", "operations", "service", "hospitality"}, "description": "Mengelola operasional F&B."},
    {"title": "Barista", "keywords": {"barista", "coffee", "espresso", "cafe", "beverage", "latte", "customer", "service"}, "description": "Membuat dan menyajikan minuman kopi."},
    {"title": "Restaurant Manager", "keywords": {"restaurant", "management", "staff", "operations", "customer", "service", "food"}, "description": "Mengelola operasional restoran."},
    {"title": "Tour Guide", "keywords": {"tour", "guide", "travel", "tourism", "destination", "customer", "language", "history"}, "description": "Memandu wisatawan di destinasi."},
    {"title": "Event Planner", "keywords": {"event", "wedding", "planning", "vendor", "venue", "decoration", "coordination"}, "description": "Merencanakan dan mengkoordinasi acara."},
    {"title": "Travel Agent", "keywords": {"travel", "agent", "booking", "flight", "hotel", "tour", "customer", "itinerary"}, "description": "Membantu pelanggan merencanakan perjalanan."},

    # ── Media & Jurnalistik ─────────────────────────────────────────
    {"title": "Journalist", "keywords": {"journalist", "news", "writing", "reporting", "interview", "media", "press", "investigation"}, "description": "Menulis dan meliput berita."},
    {"title": "Editor", "keywords": {"editor", "editing", "proofreading", "content", "publication", "writing", "quality"}, "description": "Mengedit dan menyunting konten."},
    {"title": "News Anchor", "keywords": {"anchor", "news", "broadcast", "television", "presenter", "speaking", "media"}, "description": "Membawakan berita di televisi."},
    {"title": "Podcast Producer", "keywords": {"podcast", "audio", "production", "editing", "content", "host", "interview"}, "description": "Memproduksi konten podcast."},
    {"title": "Social Media Influencer", "keywords": {"influencer", "content", "creator", "social", "media", "instagram", "youtube", "tiktok"}, "description": "Membuat konten dan mempengaruhi audiens."},
    {"title": "Content Creator", "keywords": {"content", "creator", "video", "social", "media", "youtube", "editing", "storytelling"}, "description": "Membuat konten digital untuk berbagai platform."},
    {"title": "Broadcaster", "keywords": {"broadcast", "radio", "television", "presenter", "voice", "media", "live"}, "description": "Menyiarkan konten di radio atau TV."},

    # ── Administrasi & Sekretaris ───────────────────────────────────
    {"title": "Administrative Assistant", "keywords": {"admin", "administrative", "office", "scheduling", "filing", "coordination", "excel", "correspondence"}, "description": "Mendukung operasional administratif kantor."},
    {"title": "Executive Assistant", "keywords": {"executive", "assistant", "secretary", "calendar", "travel", "meeting", "confidential"}, "description": "Mendukung eksekutif senior."},
    {"title": "Office Manager", "keywords": {"office", "management", "administration", "facilities", "supplies", "coordination", "staff"}, "description": "Mengelola operasional kantor."},
    {"title": "Receptionist", "keywords": {"receptionist", "front", "desk", "phone", "visitor", "greeting", "administrative"}, "description": "Menyambut tamu dan menangani telepon."},
    {"title": "Data Entry Clerk", "keywords": {"data", "entry", "typing", "database", "excel", "accuracy", "administrative"}, "description": "Memasukkan data ke sistem."},
    {"title": "Virtual Assistant", "keywords": {"virtual", "assistant", "remote", "administrative", "scheduling", "email", "support"}, "description": "Memberikan dukungan administratif secara remote."},

    # ── Logistik & Warehouse ────────────────────────────────────────
    {"title": "Logistics Coordinator", "keywords": {"logistics", "shipping", "transportation", "coordination", "delivery", "tracking", "supply"}, "description": "Mengkoordinasi pengiriman dan logistik."},
    {"title": "Warehouse Supervisor", "keywords": {"warehouse", "inventory", "storage", "shipping", "receiving", "forklift", "management"}, "description": "Mengawasi operasional gudang."},
    {"title": "Inventory Analyst", "keywords": {"inventory", "stock", "analysis", "forecasting", "demand", "planning", "supply"}, "description": "Menganalisis dan mengelola inventori."},
    {"title": "Delivery Driver", "keywords": {"driver", "delivery", "transportation", "logistics", "package", "route", "vehicle"}, "description": "Mengantarkan paket ke pelanggan."},
    {"title": "Import Export Specialist", "keywords": {"import", "export", "customs", "shipping", "documentation", "international", "trade"}, "description": "Mengelola kegiatan ekspor impor."},
    {"title": "Fleet Manager", "keywords": {"fleet", "vehicle", "management", "maintenance", "driver", "transportation", "logistics"}, "description": "Mengelola armada kendaraan perusahaan."},

    # ── Real Estate & Properti ──────────────────────────────────────
    {"title": "Real Estate Agent", "keywords": {"real", "estate", "property", "sales", "listing", "client", "negotiation", "marketing"}, "description": "Menjual dan menyewakan properti."},
    {"title": "Property Manager", "keywords": {"property", "management", "tenant", "maintenance", "lease", "real", "estate"}, "description": "Mengelola properti dan hubungan penyewa."},
    {"title": "Mortgage Specialist", "keywords": {"mortgage", "loan", "financing", "banking", "credit", "property", "application"}, "description": "Membantu proses pembiayaan properti."},
    {"title": "Building Inspector", "keywords": {"building", "inspection", "code", "compliance", "safety", "construction", "report"}, "description": "Memeriksa bangunan untuk kepatuhan kode."},

    # ── Pertanian & Lingkungan ──────────────────────────────────────
    {"title": "Agricultural Engineer", "keywords": {"agriculture", "farming", "crop", "irrigation", "soil", "machinery", "production"}, "description": "Mengembangkan teknologi pertanian."},
    {"title": "Agronomist", "keywords": {"agronomy", "crop", "soil", "plant", "farming", "research", "yield", "agriculture"}, "description": "Meneliti dan mengoptimalkan produksi tanaman."},
    {"title": "Environmental Scientist", "keywords": {"environmental", "science", "research", "sustainability", "pollution", "ecology", "conservation"}, "description": "Meneliti isu lingkungan dan keberlanjutan."},
    {"title": "Sustainability Specialist", "keywords": {"sustainability", "green", "environmental", "csr", "carbon", "renewable", "compliance"}, "description": "Mengembangkan inisiatif keberlanjutan."},
    {"title": "Forestry Manager", "keywords": {"forestry", "forest", "timber", "conservation", "management", "logging", "environment"}, "description": "Mengelola sumber daya hutan."},

    # ── Olahraga & Fitness ──────────────────────────────────────────
    {"title": "Personal Trainer", "keywords": {"trainer", "fitness", "exercise", "gym", "workout", "nutrition", "coaching", "health"}, "description": "Melatih klien untuk mencapai tujuan fitness."},
    {"title": "Sports Coach", "keywords": {"coach", "sports", "training", "team", "athlete", "performance", "strategy"}, "description": "Melatih atlet dan tim olahraga."},
    {"title": "Sports Manager", "keywords": {"sports", "management", "athlete", "contract", "sponsorship", "event", "marketing"}, "description": "Mengelola karir atlet dan acara olahraga."},
    {"title": "Fitness Instructor", "keywords": {"fitness", "instructor", "class", "aerobic", "yoga", "gym", "group", "exercise"}, "description": "Mengajar kelas fitness grup."},
    {"title": "Physical Education Teacher", "keywords": {"pe", "physical", "education", "teacher", "sports", "school", "student"}, "description": "Mengajar pendidikan jasmani di sekolah."},

    # ── Keamanan ────────────────────────────────────────────────────
    {"title": "Security Officer", "keywords": {"security", "guard", "patrol", "surveillance", "safety", "protection", "access"}, "description": "Menjaga keamanan fasilitas."},
    {"title": "Security Manager", "keywords": {"security", "management", "team", "risk", "protocol", "emergency", "safety"}, "description": "Mengelola tim dan protokol keamanan."},
    {"title": "Loss Prevention Specialist", "keywords": {"loss", "prevention", "retail", "theft", "surveillance", "investigation", "security"}, "description": "Mencegah kerugian di retail."},

    # ── Research & Science ──────────────────────────────────────────
    {"title": "Research Scientist", "keywords": {"research", "scientist", "laboratory", "experiment", "publication", "analysis", "methodology"}, "description": "Melakukan penelitian ilmiah."},
    {"title": "Research Assistant", "keywords": {"research", "assistant", "data", "collection", "laboratory", "literature", "review"}, "description": "Mendukung proyek penelitian."},
    {"title": "Biostatistician", "keywords": {"biostatistics", "statistics", "clinical", "trial", "analysis", "sas", "research"}, "description": "Menganalisis data penelitian kesehatan."},
    {"title": "Clinical Research Coordinator", "keywords": {"clinical", "research", "trial", "patient", "protocol", "regulatory", "data"}, "description": "Mengkoordinasi uji klinis."},
    {"title": "Lab Manager", "keywords": {"laboratory", "management", "equipment", "safety", "inventory", "research", "staff"}, "description": "Mengelola operasional laboratorium."},

    # ── Non-Profit & Social ─────────────────────────────────────────
    {"title": "Program Coordinator", "keywords": {"program", "coordination", "nonprofit", "community", "event", "volunteer", "grant"}, "description": "Mengkoordinasi program sosial."},
    {"title": "Fundraiser", "keywords": {"fundraising", "donation", "nonprofit", "campaign", "donor", "grant", "development"}, "description": "Menggalang dana untuk organisasi."},
    {"title": "Social Worker", "keywords": {"social", "work", "case", "management", "counseling", "community", "welfare", "support"}, "description": "Membantu individu dan keluarga yang membutuhkan."},
    {"title": "Community Manager", "keywords": {"community", "engagement", "social", "media", "forum", "members", "events", "moderation"}, "description": "Mengelola dan membangun komunitas."},
    {"title": "Volunteer Coordinator", "keywords": {"volunteer", "coordination", "recruitment", "training", "nonprofit", "community"}, "description": "Mengkoordinasi program relawan."},
    {"title": "NGO Project Manager", "keywords": {"ngo", "project", "management", "development", "humanitarian", "grant", "donor"}, "description": "Mengelola proyek organisasi non-profit."},
]


def get_job_recommendations(
    resume_keywords: set,
    current_job_keywords: set,
    num_recs: int = 3,
) -> list[dict]:
    """Return jobs that match the CV but differ from the target JD."""
    recommendations = []

    for job in JOB_DATABASE:
        matched_skills = resume_keywords & job["keywords"]
        match_score = len(matched_skills) / max(len(job["keywords"]), 1)


        current_overlap = len(job["keywords"] & current_job_keywords) / max(len(job["keywords"]), 1)
        if current_overlap > 0.5:
            continue

        if len(matched_skills) >= 2:
            recommendations.append({
                "title": job["title"],
                "description": job["description"],
                "matched_skills": list(matched_skills)[:5],
                "match_score": round(match_score * 100),
            })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations[:num_recs]
