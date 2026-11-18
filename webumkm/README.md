# WebGIS UMKM & Kebencanaan Indonesia

Aplikasi WebGIS berbasis Django dan Leaflet.js untuk visualisasi data geospasial Indonesia dan pemantauan gempa bumi real-time dari BMKG.

## Fitur Utama
1. **Peta Indonesia Dasar (`/petasatu/`)** - Peta interaktif Leaflet dengan basemap Esri Satellite & OpenStreetMap serta penunjuk koordinat.
2. **Peta Wilayah Jabodetabek (`/petadua/`)** - Visualisasi poligon GeoJSON untuk Jakarta, Bogor, Depok, Tangerang, Tangsel, dan Bekasi lengkap dengan data populasi, luas wilayah, dan kontrol layer interaktif.
3. **Peta Gempa Bumi Terkini (`/gempabumi/`)** - Pemantauan 15 gempa bumi terkini (M 5.0+) dengan data live dari BMKG, visualisasi episentrum bergaya heatmap konsentris, sidebar interaktif, dan auto-zoom.

---

## Cara Menjalankan Proyek

Bagi yang mendownload atau melakukan clone repository ini, ikuti langkah berikut:

### 1. Clone Repository
```bash
git clone <URL_REPOSITORY_ANDA>
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

### 5. Jalankan Development Server
```bash
python manage.py runserver
```

Buka browser dan akses: `http://127.0.0.1:8000/`

---

## Rute / Halaman Tersedia
| Rute | Deskripsi |
|---|---|
| `/` atau `/welcome/` | Halaman utama / welcome |
| `/petasatu/` | Peta Leaflet Indonesia |
| `/petadua/` | Peta Wilayah Jabodetabek (GeoJSON) |
| `/gempabumi/` | Peta Sebaran Gempa Bumi BMKG |
| `/admin/` | Panel admin Django |

---

## Sumber Data & Kredit
- Data Gempabumi: **Data Gempabumi Terbuka BMKG**
- Basemap: **OpenStreetMap** & **Esri World Imagery**
- Library Peta: **Leaflet.js**
