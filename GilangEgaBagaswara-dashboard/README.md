# Dashboard Analisis Mahasiswa - Jaya Jaya Institut

Dashboard business intelligence untuk memantau dan menganalisis performa mahasiswa di Jaya Jaya Institut.

## 🔐 Kredensial Login Metabase

**Akses Dashboard:**

- URL: http://localhost:3000
- **Username**: root@mail.com
- **Password**: root123

**Catatan**: Pastikan Metabase sudah running sebelum mengakses dashboard.

## 🗃️ Database Setup

Database yang digunakan: `Jaya Jaya Institut Database_GilangEgaBagaswara_Dicoding`

- **Jumlah Data:** 4,424 record mahasiswa
- **Tabel:** `data`
- **Lokasi:** Database SQLite yang terhubung ke Metabase
- **Format:** SQLite Database
- **Status:** Connected and verified

## 📊 Komponen Dashboard

Dashboard ini terdiri dari 6 visualisasi utama yang memberikan gambaran lengkap performa mahasiswa:

### 1. Overview Status Mahasiswa (Pie Chart)

- Proporsi mahasiswa berdasarkan status akhir
- Persentase dropout, graduate, dan yang masih aktif

### 2. Analisis Berdasarkan Gender (Bar Chart)

- Distribusi status mahasiswa per gender
- Komparasi performa antara mahasiswa pria dan wanita

### 3. Program Studi Terpopuler (Horizontal Bar)

- Ranking program studi berdasarkan peminat
- Total mahasiswa per program studi

### 4. Tingkat Dropout per Program (Horizontal Bar)

- Identifikasi program dengan tingkat dropout tinggi
- Data untuk evaluasi kurikulum dan metode pembelajaran

### 5. Tingkat Kelulusan per Program (Horizontal Bar)

- Success rate setiap program studi
- Benchmark performa akademik

### 6. Statistik Institusi (Tabel)

- Key Performance Indicators (KPI) utama
- Ringkasan metrik penting untuk manajemen

### 7. Program yang Memerlukan Perhatian (Tabel)

- Daftar program dengan dropout rate di atas rata-rata
- Prioritas untuk program perbaikan

## � Cara Menggunakan

### Setup Metabase:

1. Install Docker (jika belum ada)
2. Jalankan perintah: `docker run -d -p 3000:3000 metabase/metabase`
3. Buka browser ke `http://localhost:3000`
4. Setup akun administrator baru

### Koneksi Database:

1. Pilih "Add a database"
2. Pilih SQLite sebagai database type
3. Masukkan path ke file `data.db`
4. Test koneksi dan simpan
5. Nama database: "Jaya Jaya Institut Database_GilangEgaBagaswara_Dicoding"

### Mengakses Dashboard:

1. **Login ke Metabase** dengan kredensial yang tersedia
2. **Pilih database** "Jaya Jaya Institut Database_GilangEgaBagaswara_Dicoding"
3. **Akses dashboard** untuk melihat semua visualisasi

## 📈 Temuan Analisis Dashboard

Berdasarkan visualisasi dashboard yang telah dibuat, berikut hasil analisis performa mahasiswa Jaya Jaya Institut:

### 📊 **Ringkasan Institusi:**

Dari chart "Distribusi Status Mahasiswa" dan "Ringkasan Statistik Jaya Jaya Institut":

- **Total Mahasiswa**: 4,424 mahasiswa terdaftar
- **Jumlah Program Studi**: 17 program aktif
- **Tingkat Dropout**: 32.1% (perlu perhatian khusus)
- **Tingkat Kelulusan**: 49.9% (target perbaikan)
- **Mahasiswa Aktif**: 17.9% (masih belajar)

### 👥 **Analisis Berdasarkan Gender:**

Chart "Gender Analysis" menunjukkan:

- **Female**: 2,868 mahasiswa (64.8% dari total)
- **Male**: 1,556 mahasiswa (35.2% dari total)
- **Distribusi status relatif seimbang** antara pria dan wanita
- **Tidak teridentifikasi bias gender** dalam tingkat keberhasilan

### � **Program Studi Terpopuler:**

Dari chart "10 Program Studi Terpopuler":

1. **Program 9,500**: 766 mahasiswa (program paling diminati)
2. **Program 9,147**: 380 mahasiswa
3. **Program 9,238**: 355 mahasiswa
4. **Program 9,085**: 337 mahasiswa
5. **Program 9,773**: 291 mahasiswa

### ⚠️ **Program dengan Tingkat Dropout Tertinggi:**

Chart "Top 10 Program dengan Tingkat Dropout Tertinggi (%)" mengidentifikasi:

1. **Program 9,130**: 55.3% dropout rate (sangat tinggi)
2. **Program 9,119**: 54.1% dropout rate (sangat tinggi)
3. **Program 9,991**: 50.7% dropout rate (tinggi)
4. **Program 9,853**: 44.3% dropout rate (tinggi)
5. **Program 9,003**: 41% dropout rate (perlu perhatian)

### 📈 **Tingkat Kelulusan per Program:**

Dari chart "Tingkat Kelulusan per Program Studi":

- **Program 9500_00%**: Tingkat kelulusan tertinggi (71.5%)
- **Program 9238_00%**: 69.9% tingkat kelulusan
- **Program 9773_00%**: 59.2% tingkat kelulusan
- **Variasi signifikan** antar program (perlu evaluasi kurikulum)

### 🔍 **Program Prioritas Perhatian:**

Tabel "Program Studi dengan Tingkat Dropout Tinggi (>30%)" menunjukkan:

- **4 program** memerlukan intervensi segera
- **Program 9,130 dan 9,119** menjadi prioritas tertinggi
- **Total 141-268 mahasiswa** per program berisiko tinggi

## 🎯 Rekomendasi Aksi Berdasarkan Temuan

### 🚨 **Intervensi Segera (Priority 1):**

1. **Program 9,130 & 9,119** - Tingkat dropout >50%

   - Evaluasi komprehensif kurikulum dan metode pembelajaran
   - Survei kepuasan mahasiswa dan identifikasi kendala utama
   - Program mentoring intensif semester awal

2. **Sistem Early Warning**
   - Monitor performa akademik minggu ke-4 dan ke-8
   - Identifikasi mahasiswa berisiko berdasarkan pola absensi
   - Konseling akademik proaktif

### 💡 **Optimisasi Jangka Menengah (Priority 2):**

1. **Best Practice Sharing**

   - Adopsi strategi sukses dari Program 9,500 (tingkat kelulusan 71.5%)
   - Cross-program learning dan knowledge transfer
   - Standardisasi metode pembelajaran efektif

2. **Program Retensi Mahasiswa**
   - Peer tutoring system antar mahasiswa
   - Industry partnership untuk praktik kerja
   - Scholarship program untuk mahasiswa berprestasi

### 📊 **Monitoring & Evaluasi:**

1. **Dashboard KPI Tracking**

   - Monthly review tingkat dropout per program
   - Semester comparison untuk trend analysis
   - Student satisfaction index monitoring

2. **Predictive Analytics Development**
   - Model prediksi risiko dropout mahasiswa baru
   - Segmentasi mahasiswa berdasarkan karakteristik sukses
   - Automated alert system untuk academic advisor

## 🔧 Strategi Implementasi Dashboard

### 📋 **Action Items untuk Institusi:**

**Immediate Actions (0-3 bulan):**

1. **Crisis Management** - Program 9,130 & 9,119

   - Task force pembentukan untuk evaluasi menyeluruh
   - Student survey untuk identifikasi root cause dropout
   - Emergency support program untuk mahasiswa berisiko

2. **Data-Driven Decision Making**
   - Weekly monitoring dashboard usage oleh management
   - Monthly report generation dari metrics yang tersedia
   - Quarterly review dengan stakeholder program studi

**Medium-term Strategy (3-12 bulan):**

1. **Perbaikan Program Studi**

   - Curriculum revision berdasarkan best practice Program 9,500
   - Faculty development program untuk metode pembelajaran
   - Student support service expansion

2. **Predictive Analytics**
   - Early warning system development
   - Student success pattern analysis
   - Resource allocation optimization

### 📊 **Dashboard Utilization Guide:**

**For Management:**

- Focus pada overview charts untuk strategic planning
- Monitor trend changes semester-to-semester
- Utilize comparative analysis antar program studi

**For Academic Advisors:**

- Gunakan data performa program individual untuk planning
- Monitor pola perkembangan mahasiswa
- Identifikasi peluang intervensi yang tepat

**For Program Coordinators:**

- Bandingkan performa dengan program berprestasi tinggi
- Analisis tantangan dan peluang spesifik program
- Rencanakan inisiatif perbaikan yang terarah

### Panduan Akses Dashboard:

**Login Credentials:**

- Portal: http://localhost:3000
- User: root@mail.com
- Pass: root123

**Database Connection:**

- Source: Jaya Jaya Institut Database_GilangEgaBagaswara_Dicoding
- Format: SQLite
- Records: 4,424 student data points

**Navigation Tips:**

- Dashboard tersedia dalam 6 komponen visualisasi utama
- Setiap chart dapat di-filter sesuai kebutuhan analisis
- Data dapat diekspor untuk keperluan reporting

## 📋 Dokumentasi Teknis

### 📸 **Visual Assets:**

- `GilangEgaBagaswara_Dashboard.jpg` - Screenshot dashboard utama
- Menampilkan 6 komponen visualisasi utama
- Layout responsive dan user-friendly interface

### 🗂️ **File Structure:**

```
GilangEgaBagaswara-dashboard/
├── README.md                    # Dokumentasi dashboard
└── GilangEgaBagaswara_Dashboard.jpg  # Screenshot dashboard
```

### 📈 **Key Performance Indicators:**

| Metrik                      | Nilai Saat Ini | Target    | Status               |
| --------------------------- | -------------- | --------- | -------------------- |
| Overall Dropout Rate        | 32.1%          | <25%      | ⚠️ Perlu Perbaikan   |
| Overall Graduation Rate     | 49.9%          | >60%      | ⚠️ Perlu Perbaikan   |
| Program dengan Dropout >50% | 2 Program      | 0 Program | 🚨 Critical          |
| Student Satisfaction        | -              | >80%      | 📊 Perlu Measurement |

---

### 🎯 **Summary & Next Steps:**

Dashboard ini memberikan foundation yang solid untuk data-driven decision making di Jaya Jaya Institut. Dengan visualisasi yang lengkap dan insights yang actionable, institusi dapat mengambil langkah strategis untuk meningkatkan student success rate dan menurunkan tingkat dropout.

**Rekomendasi lanjutan:** Implementasi automated reporting dan integration dengan student information system untuk real-time monitoring.

---

**Dikembangkan untuk mendukung transformasi digital Jaya Jaya Institut dalam student analytics dan institutional effectiveness.**
