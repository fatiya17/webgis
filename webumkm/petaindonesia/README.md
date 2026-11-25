# Modul Peta Indonesia (`petaindonesia`)

Folder ini adalah modul di dalam proyek Django `webumkm` yang khusus menangani latihan visualisasi peta interaktif menggunakan **Leaflet.js**, file data **GeoJSON**, dan data statistik resmi dari **Badan Pusat Statistik (BPS)**.

---

## Apa Saja yang Ada di Modul Ini?

Di modul ini, ada beberapa halaman peta yang dibuat bertahap dari materi dasar sampai peta tematik:

### 1. Peta Petani & Lahan Pertanian Pulau Jawa (`/petaindonesia/petani_jawa/`)
* **Tujuan Praktikum:** Latihan menggabungkan data batas wilayah (*spasial / GeoJSON*) dengan data angka statistik (*non-spasial / JSON*) untuk menghasilkan peta tematik (*Choropleth*) di 6 provinsi Pulau Jawa (DKI Jakarta, Jawa Barat, Jawa Tengah, DI Yogyakarta, Jawa Timur, dan Banten).
* **Sumber Data:** Data resmi **Badan Pusat Statistik (BPS) — Sensus Pertanian 2023 (ST2023)** dan data kependudukan tahun 2024.
* **Fitur Utama:**
  * **Warna Peta Otomatis Berubah:** Lewat menu pilihan di atas, warna wilayah langsung menyesuaikan indikator yang dipilih (Kepadatan Penduduk, Jumlah Petani, Luas Panen Padi, atau Populasi).
  * **Sinkronisasi Warna:** Warna kartu info di pojok kanan atas otomatis mengikuti warna wilayah yang sedang disorot kursor.
  * **Legenda Dinamis:** Skala angka di pojok kanan bawah otomatis berganti sesuai pilihan data.
  * **Tampilan Bersih (Flat):** Desain rapi tanpa bayangan berlebihan, responsif, dan tidak ada gerakan melompat saat wilayah diklik.

### 2. Peta 34 Provinsi Indonesia (`/petaindonesia/provinsi/`)
* **Tujuan Praktikum:** Latihan memuat data poligon batas wilayah seluruh provinsi di Indonesia menggunakan GeoJSON teroptimasi.
* **Sumber Data:** File `provinces.json` (materi dosen Dr. Sirojul Munir) dan poligon batas administrasi provinsi Indonesia.
* **Fitur Utama:**
  * **Langsung Tampil dari Awal:** Semua batas provinsi langsung tampak di peta begitu halaman dibuka, jadi tidak ada jeda *loading* atau peta yang bergerak-gerak mencari wilayah.
  * **Otomatis Menengahkan Layar (*Auto-Center*):** Saat kamu klik nama provinsi di daftar sebelah kiri, peta langsung menggeser wilayah tersebut tepat ke tengah layar.
  * **Pencarian Cepat:** Cukup ketik nama provinsi di kotak pencarian sidebar, daftarnya langsung terfilter.
  * **Pilihan Peta Dasar:** Bisa beralih antara peta jalan (OpenStreetMap) dan citra satelit (Esri Satellite).

### 3. Peta Objek Dasar Leaflet (`/petakampus/`)
* **Tujuan Praktikum:** Memahami objek-objek visual dasar yang ada di Leaflet.js.
* **Fitur:** Menampilkan titik penanda (*Marker*), lingkaran radius area (*Circle*), bidang datar segitiga (*Polygon*), dan kotak pesan info (*Popup*).

### 4. Peta Dasar Nasional (`/petasatu/`) & Peta Jabodetabek (`/petadua/`)
* `/petasatu/` : Peta navigasi dasar Indonesia dengan koordinat klik dan layer satelit.
* `/petadua/` : Menampilkan batas poligon wilayah Jakarta, Bogor, Depok, Tangerang, Tangsel, dan Bekasi beserta data luas dan jumlah penduduknya.

---

## File Data yang Dipakai di Folder `static/json/`

Supaya tidak membingungkan, berkas data di dalam `static/json/` sudah dirapikan hanya untuk file yang benar-benar dipakai:

```text
static/json/
├── jawa/                          # Berisi 6 file poligon provinsi se-Jawa (31.geojson s/d 36.geojson)
├── profil_petani_jawa.json        # Data angka BPS (jumlah petani, luas panen, kepadatan, dsb.)
├── indonesia_provinsi.geojson     # Satu file ringan berisi batas poligon 34 provinsi se-Indonesia
└── provinces.json                 # Data titik koordinat ibukota provinsi (referensi modul dosen)
```

---

## Struktur File Modul Ini

```text
petaindonesia/
├── templates/petaindonesia/       # File tampilan HTML tiap halaman peta
│   ├── petani_jawa.html           # Template peta tematik petani Jawa
│   ├── peta_provinsi.html         # Template peta 34 provinsi Indonesia
│   ├── petakampus.html            # Template latihan objek dasar Leaflet
│   ├── petasatu.html              # Template peta dasar
│   └── petadua.html               # Template peta Jabodetabek
├── view_peta.py                   # File Python fungsi pemanggil masing-masing template
└── urls.py                        # Pengaturan alamat URL untuk tiap halaman peta
```
