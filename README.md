# 🛒 BDD AI GitHub Issues — E-Commerce Promo Test Cases

Repositori ini berisi implementasi **Behavior-Driven Development (BDD)** untuk pengujian fitur promo otomatis pada aplikasi e-commerce. Test case dibuat menggunakan **Python** dan dikelola melalui **GitHub Issues** sebagai medium dokumentasi skenario BDD berbasis AI.

---

## 📋 Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Fitur yang Diuji](#fitur-yang-diuji)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Direktori](#struktur-direktori)
- [Cara Menjalankan Test](#cara-menjalankan-test)
- [Skenario BDD (GitHub Issues)](#skenario-bdd-github-issues)
- [CI/CD dengan GitHub Actions](#cicd-dengan-github-actions)
- [Kontribusi](#kontribusi)

---

## Tentang Proyek

**bdd-ai-github-issues** adalah proyek praktikum yang mendemonstrasikan pendekatan BDD dalam pengujian fitur bisnis e-commerce. Skenario pengujian ditulis dalam format **Given-When-Then** dan didokumentasikan sebagai GitHub Issues, memudahkan kolaborasi antara tim pengembang, QA, dan pemangku kepentingan bisnis.

Proyek ini juga mengeksplorasi pemanfaatan **AI** dalam pembuatan dan pengelolaan test case secara otomatis.

---

## Fitur yang Diuji

### 🏷️ Promo Otomatis: Diskon 10% dengan ShopeePay

Sistem memberikan diskon **10%** apabila dua kondisi terpenuhi secara bersamaan:

| Kondisi | Nilai |
|---------|-------|
| Total belanja | ≥ Rp 500.000 |
| Metode pembayaran | ShopeePay |

**Contoh kalkulasi:**

```
Total belanja : Rp 500.000
Pembayaran    : ShopeePay
Harga setelah diskon : Rp 500.000 × 0.9 = Rp 450.000 ✅
```

---

## Teknologi yang Digunakan

| Teknologi | Keterangan |
|-----------|------------|
| Python | Bahasa pemrograman utama |
| GitHub Issues | Dokumentasi skenario BDD |
| GitHub Actions | Pipeline CI/CD otomatis |
| BDD (Behavior-Driven Development) | Metodologi pengujian |

---

## Struktur Direktori

```
bdd-ai-github-issues/
├── .github/
│   └── workflows/       # Konfigurasi GitHub Actions (CI/CD)
├── promo_test.py        # File pengujian utama (BDD test cases)
└── README.md            # Dokumentasi proyek
```

---

## Cara Menjalankan Test

Tidak diperlukan instalasi library eksternal. Cukup jalankan langsung dengan Python:

```bash
python promo_test.py
```

Output yang diharapkan:

```
Semua test case PASSED!
```

---

## Skenario BDD (GitHub Issues)

Setiap skenario pengujian didokumentasikan sebagai GitHub Issue dengan format BDD. Berikut ringkasan tiga skenario utama:

### ✅ Issue #1 — Diskon 10% Berhasil Diterapkan dengan ShopeePay

```gherkin
Given  pelanggan memiliki total belanja Rp 500.000
When   pelanggan membayar menggunakan ShopeePay
Then   sistem menerapkan diskon 10%
And    harga akhir menjadi Rp 450.000
```

### ❌ Issue #2 — Diskon Tidak Diterapkan Saat Belanja di Bawah Rp 500.000

```gherkin
Given  pelanggan memiliki total belanja Rp 499.999
When   pelanggan membayar menggunakan ShopeePay
Then   sistem tidak menerapkan diskon
And    harga akhir tetap Rp 499.999
```

### ❌ Issue #3 — Diskon Tidak Diterapkan Saat Pembayaran Bukan ShopeePay

```gherkin
Given  pelanggan memiliki total belanja Rp 550.000
When   pelanggan membayar menggunakan OVO
Then   sistem tidak menerapkan diskon
And    harga akhir tetap Rp 550.000
```

---

## CI/CD dengan GitHub Actions

Repositori ini dilengkapi pipeline **GitHub Actions** yang berjalan otomatis setiap kali ada perubahan kode. Workflow memastikan semua test case tetap lolos sebelum kode digabungkan ke branch utama.

Konfigurasi tersimpan di `.github/workflows/`.

---

## Kontribusi

Kontribusi sangat disambut! Untuk menambahkan skenario BDD baru:

1. Buat **GitHub Issue** baru dengan format BDD (Given-When-Then)
2. Fork repositori ini
3. Tambahkan test case di `promo_test.py`
4. Buat Pull Request dan referensikan Issue terkait
