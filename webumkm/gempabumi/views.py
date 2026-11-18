import json
import os
import urllib.request
from datetime import datetime
from django.conf import settings
from django.shortcuts import render

# api bmkg gempa terkini
BMKG_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"


def gempaterkini(request):
    raw_data = None
    sumber = "BMKG Online"

    # 1. fetch data bmkg online
    try:
        req = urllib.request.Request(
            BMKG_URL,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=4) as resp:
            if resp.status == 200:
                raw_data = json.loads(resp.read().decode('utf-8'))
    except Exception:
        raw_data = None

    # 2. fallback baca file json lokal
    if not raw_data:
        sumber = "File Lokal (gempaterkini.json)"
        local_candidates = [
            os.path.join(settings.BASE_DIR, 'gempabumi', 'gempaterkini.json'),
            os.path.join(settings.BASE_DIR, 'petaindonesia', 'gempaterkini.json'),
            os.path.join(settings.BASE_DIR, 'gempaterkini.json'),
        ]
        for path in local_candidates:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    raw_data = json.load(f)
                break

    # ekstrak list gempa
    gempa_raw = []
    if raw_data and 'Infogempa' in raw_data and 'gempa' in raw_data['Infogempa']:
        gempa_raw = raw_data['Infogempa']['gempa']

    # format 15 gempa terbaru
    gempa_list = []
    for idx, item in enumerate(gempa_raw[:15], start=1):
        coords = item.get('Coordinates', '0,0').split(',')
        try:
            lat = float(coords[0].strip())
            lon = float(coords[1].strip())
        except (ValueError, IndexError):
            lat, lon = 0.0, 0.0

        try:
            mag_float = float(item.get('Magnitude', 0))
        except ValueError:
            mag_float = 0.0

        # styling warna magnitudo
        if mag_float >= 7.0:
            color = "#dc2626"
            badge_class = "danger"
        elif mag_float >= 6.0:
            color = "#ea580c"
            badge_class = "warning"
        else:
            color = "#d97706"
            badge_class = "caution"

        gempa_list.append({
            'nomor': idx,
            'tanggal': item.get('Tanggal', ''),
            'jam': item.get('Jam', ''),
            'datetime': item.get('DateTime', ''),
            'coordinates': item.get('Coordinates', ''),
            'lat': lat,
            'lon': lon,
            'lintang': item.get('Lintang', ''),
            'bujur': item.get('Bujur', ''),
            'magnitude': item.get('Magnitude', ''),
            'mag_float': mag_float,
            'kedalaman': item.get('Kedalaman', ''),
            'wilayah': item.get('Wilayah', ''),
            'potensi': item.get('Potensi', ''),
            'color': color,
            'badge_class': badge_class,
        })

    waktu_sekarang = datetime.now().strftime("%H.%M.%S")

    # context render template
    context = {
        'gempa_list': gempa_list,
        'gempa_json': json.dumps(gempa_list),
        'waktu_update': waktu_sekarang,
        'sumber': sumber,
        'total_gempa': len(gempa_list),
    }
    return render(request, 'gempabumi/gempaterkini.html', context)
