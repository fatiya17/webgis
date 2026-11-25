# Kumpulan Praktikum WebGIS

Repositori ini berisi kumpulan tugas dan modul **Praktikum Sistem Informasi Geografis berbasis Web (WebGIS)** yang dikembangkan menggunakan **Python**, framework **Django**, dan pustaka pemetaan **Leaflet.js**.

---

## Isi Proyek Ini

Semua kode utama proyek berada di dalam folder **`webumkm/`**, yang terbagi menjadi dua modul utama:

1. **`petaindonesia/`** : Modul visualisasi geospasial wilayah Indonesia:
   * **Peta Tematik Petani Jawa (`/petaindonesia/petani_jawa/`)** — Peta tematik data Sensus Pertanian BPS (ST2023) untuk 6 provinsi di Pulau Jawa. Warnanya otomatis berubah sesuai indikator yang dipilih (kepadatan, jumlah petani, luas panen, populasi).
   * **Peta 34 Provinsi Indonesia (`/petaindonesia/provinsi/`)** — Menampilkan batas poligon seluruh provinsi di Indonesia dengan fitur *auto-center* (wilayah langsung bergeser ke tengah saat diklik dari daftar) dan pencarian instan.
   * **Latihan Objek Leaflet (`/petakampus/`)** — Pengenalan objek dasar Leaflet: Marker titik, Lingkaran (*Circle*), Poligon bidang, dan Popup.
   * **Peta Jabodetabek (`/petadua/`)** & **Peta Dasar (`/petasatu/`)**.

2. **`gempabumi/`** : Modul pemantauan bencana gempa bumi yang mengambil data langsung secara otomatis dari API BMKG untuk gempa berkekuatan magnitudo 5.0 ke atas.

---

## Cara Menjalankan Aplikasi

1. **Masuk ke folder `webumkm` di terminal:**
   ```bash
   cd webumkm
   ```

2. **Buat dan aktifkan virtual environment:**
   * **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * **Mac / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan server Django:**
   ```bash
   python manage.py runserver
   ```

5. Buka browser di: **`http://127.0.0.1:8000/`**

---

## Ringkasan Link Halaman

| URL Halaman | Nama Fitur | Keterangan Singkat |
|---|---|---|
| `http://127.0.0.1:8000/` | Beranda WebGIS | Halaman pembuka aplikasi |
| `http://127.0.0.1:8000/petaindonesia/petani_jawa/` | Peta Petani Jawa | Peta tematik data BPS Sensus Pertanian 2023 |
| `http://127.0.0.1:8000/petaindonesia/provinsi/` | Peta Provinsi | Batas wilayah 34 provinsi + auto-center |
| `http://127.0.0.1:8000/petakampus/` | Objek Leaflet | Latihan marker, circle, polygon, popup |
| `http://127.0.0.1:8000/gempabumi/` | Gempa Bumi BMKG | Pantauan gempa bumi M 5.0+ live dari BMKG |
| `http://127.0.0.1:8000/petadua/` | Peta Jabodetabek | Poligon wilayah Jabodetabek |
| `http://127.0.0.1:8000/petasatu/` | Peta Dasar | Peta navigasi dasar Indonesia |
