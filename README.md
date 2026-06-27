# 📄 CV Match Analyst

Aplikasi web untuk menganalisis seberapa cocok CV kamu dengan Job Description secara otomatis. Cukup upload CV dan paste job description, aplikasi akan langsung memberikan skor kecocokan, feedback, dan rekomendasi perbaikan.

---

## ✨ Fitur

- **Match Score** — skor kecocokan CV vs Job Description (0–100%)
- **Analisis Keyword** — keyword apa yang sudah ada dan yang masih kurang
- **Feedback Otomatis** — penilaian kualitas deskripsi pengalaman di CV
- **Rekomendasi Perbaikan** — saran konkret untuk meningkatkan skor
- **Rekomendasi Posisi Lain** — posisi alternatif yang lebih cocok berdasarkan skill di CV
- Support upload file **PDF** dan **DOCX**, atau paste teks langsung

---

## 🛠️ Teknologi

- [Streamlit](https://streamlit.io/) — framework UI
- [scikit-learn](https://scikit-learn.org/) — TF-IDF & cosine similarity
- [NLTK](https://www.nltk.org/) — text processing & synonym expansion
- [pdfplumber](https://github.com/jsvine/pdfplumber) — ekstrak teks dari PDF
- [python-docx](https://python-docx.readthedocs.io/) — ekstrak teks dari DOCX

---

## 📁 Struktur Project

```
cv_match_analyst/
├── app.py                  # Entry point utama
├── config.py               # Konfigurasi halaman & session state
├── styles.py               # CSS styling
├── requirements.txt
├── engine/
│   ├── text_processing.py  # Fungsi pembersihan & ekstraksi teks
│   ├── analyzer.py         # Logika analisis utama
│   └── recommender.py      # Database posisi & rekomendasi pekerjaan
└── pages/
    ├── welcome.py           # Halaman awal
    ├── input.py             # Halaman input CV & JD
    └── result.py            # Halaman hasil analisis
```

---

## 🚀 Cara Menjalankan

### 1. Clone repository ini

```bash
git clone https://github.com/username/cv-match-analyst.git
cd cv-match-analyst
```

### 2. Buat virtual environment (opsional tapi disarankan)

```bash
python -m venv venv
```

Aktifkan virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi

```bash
streamlit run app.py
```

### 5. Buka di browser

Aplikasi akan otomatis terbuka di browser. Kalau tidak, buka manual:
```
http://localhost:8501
```

---

## 📖 Cara Pakai

1. Klik **Mulai Analisis**
2. Upload file CV (PDF/DOCX) atau paste teks CV langsung
3. Paste Job Description dari lowongan yang dituju
4. Klik **Analisis Sekarang**
5. Lihat hasil skor, feedback, dan rekomendasi perbaikan

---

## 📝 Catatan

- File CV maksimal **2MB**
- CV dalam format **scan gambar (bukan teks)** tidak dapat diproses — gunakan PDF yang bisa di-copy teksnya
- Data NLTK akan otomatis didownload saat pertama kali dijalankan, butuh koneksi internet

---

## 👩‍💻 Developer

Dibuat oleh **Nazkia** — Data Science Student @ Binus University
