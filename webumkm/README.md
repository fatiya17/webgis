# Proyek WebGIS UMKM & Pemetaan Geospasial

Aplikasi web pemetaan (WebGIS) ini dibangun menggunakan **Django** (Python) dan **Leaflet.js**. Tujuannya adalah memvisualisasikan data wilayah Indonesia, data statistik pertanian dari BPS, serta pemantauan bencana gempa bumi secara langsung dari BMKG.

---

## Halaman Peta yang Tersedia

Berikut rincian fitur peta yang sudah dibuat di proyek ini:

1. **Peta Tematik Petani Pulau Jawa (`/petaindonesia/petani_jawa/`)**  
   * **Maksud:** Membuat peta tematik bertingkat (*Choropleth map*) di 6 provinsi Pulau Jawa (DKI Jakarta, Jawa Barat, Jawa Tengah, DI Yogyakarta, Jawa Timur, dan Banten).
   * **Data yang dipakai:** Data spasial poligon GeoJSON Jawa digabung dengan data statistik **Badan Pusat Statistik (BPS) — Sensus Pertanian 2023 (ST2023)**.
   * **Cara pakai:** Kamu bisa mengganti warna peta lewat menu pilihan (Kepadatan Penduduk, Jumlah Petani, Luas Panen Padi, atau Populasi). Warna pada kartu informasi di kanan atas akan otomatis mengikuti warna wilayah yang sedang disorot.

2. **Peta Batas 34 Provinsi Indonesia (`/petaindonesia/provinsi/`)**  
   * **Maksud:** Menampilkan batas administrasi seluruh provinsi di Indonesia dengan cepat dan interaktif.
   * **Fitur:** Semua garis batas wilayah sudah muncul rapi dari awal. Kalau kamu klik salah satu nama provinsi di daftar samping kiri, petanya akan otomatis menggeser wilayah tersebut tepat ke tengah layar (*auto-center*).

3. **Peta Objek Dasar Leaflet (`/petakampus/`)**  
   * **Maksud:** Latihan mengenal komponen dasar Leaflet seperti titik koordinat (*Marker*), lingkaran (*Circle*), area segitiga (*Polygon*), dan kotak pesan info (*Popup*).

4. **Peta Sebaran Gempa Bumi BMKG (`/gempabumi/`)**  
   * **Maksud:** Memantau 15 titik gempa bumi terbaru berkekuatan 5.0 ke atas di Indonesia dengan data yang ditarik otomatis dari server BMKG.

5. **Peta Wilayah Jabodetabek (`/petadua/`)**  
   * Menampilkan poligon wilayah Jakarta, Bogor, Depok, Tangerang, Tangsel, dan Bekasi beserta data jumlah penduduk dan luas daerahnya.

6. **Peta Dasar Indonesia (`/petasatu/`)**  
   * Peta awal untuk navigasi nasional dengan fitur beralih antara peta jalan dan citra satelit.

---

## Tabel Alamat Halaman (URL)

| Alamat URL di Browser | Nama Peta | Keterangan |
|---|---|---|
| `http://127.0.0.1:8000/` | Beranda | Halaman pembuka / welcome |
| `http://127.0.0.1:8000/petaindonesia/petani_jawa/` | Petani Pulau Jawa | Peta tematik data BPS ST2023 |
| `http://127.0.0.1:8000/petaindonesia/provinsi/` | Provinsi Indonesia | Peta 34 provinsi dengan auto-center |
| `http://127.0.0.1:8000/petakampus/` | Objek Leaflet | Latihan marker, circle, polygon, popup |
| `http://127.0.0.1:8000/gempabumi/` | Gempa Bumi BMKG | Data langsung gempa terkini M 5.0+ |
| `http://127.0.0.1:8000/petadua/` | Wilayah Jabodetabek | Poligon wilayah Jabodetabek |
| `http://127.0.0.1:8000/petasatu/` | Peta Dasar | Peta navigasi nasional dasar |

---

## Cara Menjalankan Aplikasi di Komputer

Kalau kamu baru saja mengunduh (*download*) atau clone repositori ini:

1. **Buka terminal dan masuk ke folder `webumkm`:**
   ```bash
   cd webumkm
   ```

2. **Buat dan aktifkan virtual environment:**
   * Di Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * Di Mac / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install bahan/paket pendukung:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan database dan server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Buka di browser:**
   Buka link: **`http://127.0.0.1:8000/`**

---

## Sumber Data
* **Data Pertanian & Kependudukan:** Badan Pusat Statistik (BPS) Republik Indonesia — Sensus Pertanian 2023 (ST2023).
* **Data Gempa Bumi:** Katalog Data Terbuka BMKG (Badan Meteorologi, Klimatologi, dan Geofisika).
* **Peta Dasar & Wilayah:** OpenStreetMap, Esri World Imagery, dan poligon batas administrasi GeoJSON Indonesia.
