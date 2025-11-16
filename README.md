📌 Deskripsi Dataset & Proyek Customer Churn Analysis
Dataset churn.csv merupakan kumpulan data pelanggan dari sebuah perusahaan telekomunikasi yang berisi informasi lengkap terkait profil pelanggan, layanan yang digunakan, biaya langganan, serta status apakah pelanggan berhenti berlangganan (Churn = Yes) atau tetap aktif (Churn = No). Variabel-variabel di dalam dataset mencakup aspek demografi, jenis layanan (internet, phone service), kontrak berlangganan, hingga besar pembayaran bulanan dan total tagihan.

Dataset ini digunakan untuk melakukan analisis menyeluruh terhadap pola perilaku pelanggan. Proyek ini mencakup beberapa proses utama:

🔍 1. Exploratory Data Analysis (EDA)
Meliputi pemeriksaan struktur data, statistik deskriptif, visualisasi distribusi fitur seperti tenure, Monthly Charges, Internet Service, dan perbandingan antara pelanggan churn dan non-churn.

📊 2. Visualisasi Churn
Menyajikan grafik perbandingan pelanggan churn vs non-churn, termasuk bar chart dan pie chart yang menggambarkan persentase churn secara keseluruhan.

🤖 3. Modeling
Menggunakan algoritma Logistic Regression untuk membangun model prediksi churn. Model dilatih menggunakan beberapa fitur numerik seperti tenure, MonthlyCharges, dan TotalCharges. Evaluasi dilakukan melalui akurasi, confusion matrix, dan classification report.

🧮 4. Prediction
Aplikasi Streamlit memungkinkan pengguna memasukkan data pelanggan baru (tenure, biaya bulanan, total tagihan) untuk memprediksi apakah pelanggan tersebut berpotensi churn atau tidak.

💼 5. Business Insights
Hasil analisis menghasilkan beberapa temuan penting:
Pelanggan dengan kontrak month-to-month memiliki risiko churn tertinggi.
Biaya bulanan yang lebih tinggi cenderung meningkatkan peluang churn.
Pengguna Internet Fiber Optic tercatat memiliki tingkat churn lebih besar.
Pelanggan dengan tenure rendah lebih rentan meninggalkan layanan.
Strategi retensi sebaiknya difokuskan pada pelanggan baru dan pengguna layanan berisiko tinggi.
