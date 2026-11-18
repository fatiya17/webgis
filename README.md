# Praktikum WebGIS

Repository ini berisi kumpulan modul dan proyek Praktikum WebGIS berbasis Python & Django.

## Struktur Direktori
- `webumkm/` : Proyek WebGIS UMKM & Pemantauan Gempa Bumi BMKG (Leaflet.js + Django)
<!-- Praktikum berikutnya bisa ditambahkan di folder terpisah di dalam repository ini -->

---

## Cara Menjalankan Proyek `webumkm`

Bagi yang mendownload atau clone repository ini:

### 1. Masuk ke Folder Proyek
```bash
cd webumkm
```

### 2. Buat & Aktifkan Virtual Environment
- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Migrasi Database
```bash
python manage.py migrate
```

### 5. Jalankan Server
```bash
python manage.py runserver
```

Buka browser di: `http://127.0.0.1:8000/`

---

## Halaman yang Tersedia di `webumkm`
- `/` atau `/welcome/` : Halaman Beranda
- `/petasatu/` : Peta Leaflet Indonesia
- `/petadua/` : Peta Wilayah Jabodetabek (GeoJSON Layer)
- `/gempabumi/` : Peta Sebaran Gempa Bumi BMKG (Real-time M 5.0+)
