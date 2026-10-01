"""Build the plates: download public-domain images and edition pages, resize, draw the schematic map.

Writes assets/plates/<id>.jpg (max 1600 px) and <id>_t.jpg (360 px wide). Sources are named in data/plates.json.
"""
import io
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "HussiteFieldArmiesSite/1.0 (research site; plates build)"}

SOURCES = {
    # Wikimedia Commons originals (public domain)
    "jena": ("https://upload.wikimedia.org/wikipedia/commons/a/a7/Jensky_kodex_Zizka.jpg", None),
    "wagenburg": ("https://upload.wikimedia.org/wikipedia/commons/0/0d/344Wagenburg_der_Hussiten.jpg", None),
    "kratzau": ("https://upload.wikimedia.org/wikipedia/commons/9/9d/Buch-kaiser-sigismund-L09740-26-lr-8.png", None),
    "ruben": ("https://upload.wikimedia.org/wikipedia/commons/d/d0/Christoph_Christian_Ruben_-_Die_Schlacht_bei_Lipan_1434_-_3728_-_Kunsthistorisches_Museum.jpg", None),
    # edition pages (internet archive / FONTES)
    "toman392": ("https://archive.org/download/husitske_valecnictvi-toman/page/n408_w1800.jpg", (0.08, 0.05, 0.94, 0.97)),
    "song545": ("https://sources.cms.flu.cas.cz/src/online/1103/591.jpg", (0.12, 0.2, 0.92, 0.95)),
    "bartosek614": ("https://sources.cms.flu.cas.cz/src/online/1103/660.jpg", (0.04, 0.03, 0.97, 0.97)),
    "leidinger483": ("https://archive.org/download/bub_gb_bWsrAQAAIAAJ/page/n605_w1800.jpg", (0.0, 0.03, 1.0, 0.6)),
}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def save(im, pid):
    full = im.copy(); full.thumbnail((1600, 1600)); full.save(OUT / f"{pid}.jpg", quality=86)
    w = 360; t = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS); t.save(OUT / f"{pid}_t.jpg", quality=82)


PLACES = [  # (name, lat, lon, kind) kind: b battle, t town, x other
    ("Prague", 50.08, 14.42, "t"), ("Vítkov 1420", 50.09, 14.47, "b"), ("Vyšehrad 1420", 50.06, 14.42, "b"),
    ("Tábor", 49.41, 14.68, "t"), ("Klokoty 1421", 49.43, 14.62, "x"), ("Vodňany 1420", 49.15, 14.18, "x"),
    ("Plzeň", 49.75, 13.38, "t"), ("Domažlice 1431", 49.44, 12.93, "b"), ("Tachov 1427", 49.80, 12.63, "b"),
    ("Ústí 1426", 50.66, 14.03, "b"), ("Chomutov 1421", 50.46, 13.42, "x"), ("Beroun 1421", 49.96, 14.07, "x"),
    ("Kutná Hora", 49.95, 15.27, "t"), ("Malešov 1424", 49.91, 15.22, "b"), ("Čáslav", 49.91, 15.39, "t"),
    ("Lipany 1434", 50.01, 14.97, "b"), ("Kolín", 50.03, 15.20, "t"), ("Hradec Králové", 50.21, 15.83, "t"),
    ("Německý Brod 1422", 49.61, 15.58, "b"), ("Přibyslav (Žižka †1424)", 49.58, 15.74, "x"), ("Jihlava 1436", 49.40, 15.59, "x"),
    ("Rabí 1421", 49.28, 13.62, "x"), ("Hiltersried 1433", 49.42, 12.57, "b"), ("Nittenau 1428", 49.20, 12.27, "x"),
    ("Regensburg", 49.02, 12.10, "t"),
]


OFFS = {"Prague": (-90, -30), "Vítkov": (12, -30), "Vyšehrad": (-60, 10), "Lipany": (-60, -40), "Kolín": (12, -30), "Beroun": (-140, -12),
        "Kutná": (14, -12), "Čáslav": (12, -2), "Malešov": (-150, 2), "Německý": (-200, -32), "Přibyslav": (-40, 10),
        "Tábor": (12, -24), "Klokoty": (-140, 4), "Hiltersried": (-150, 10), "Domažlice": (12, -26), "Jihlava": (12, -6)}


def draw_map():
    W, H = 1400, 900
    lat0, lat1, lon0, lon1 = 48.85, 50.85, 11.8, 16.3
    im = Image.new("RGB", (W, H), (244, 239, 230)); d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 22); fb = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 30); fs = ImageFont.truetype("C:/Windows/Fonts/georgiai.ttf", 18)
    except OSError:
        f = fb = fs = ImageFont.load_default()
    X = lambda lon: 60 + (lon - lon0) / (lon1 - lon0) * (W - 120)
    Y = lambda lat: 80 + (lat1 - lat) / (lat1 - lat0) * (H - 160)
    d.rectangle([20, 20, W - 20, H - 20], outline=(107, 63, 29), width=3)
    d.text((40, 32), "The Hussite field armies, 1420–1436: places in the texts", font=fb, fill=(107, 63, 29))
    ly = H - 48
    d.text((40, ly), "Schematic: positions from modern coordinates; no borders or rivers.", font=fs, fill=(98, 88, 95))
    lx = 640
    d.ellipse([lx, ly + 4, lx + 14, ly + 18], fill=(140, 28, 43)); d.text((lx + 22, ly), "battle", font=fs, fill=(98, 88, 95))
    d.ellipse([lx + 110, ly + 4, lx + 124, ly + 18], outline=(35, 28, 34), width=3); d.text((lx + 132, ly), "town", font=fs, fill=(98, 88, 95))
    d.ellipse([lx + 210, ly + 7, lx + 218, ly + 15], fill=(35, 28, 34)); d.text((lx + 226, ly), "other event in the texts", font=fs, fill=(98, 88, 95))
    for name, la, lo, k in PLACES:
        x, y = X(lo), Y(la)
        if k == "b":
            d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(140, 28, 43))
        elif k == "t":
            d.ellipse([x - 7, y - 7, x + 7, y + 7], outline=(35, 28, 34), width=3)
        else:
            d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(35, 28, 34))
        dx, dy = OFFS.get(name.split(" ")[0], (12, -14))
        d.text((x + dx, y + dy), name, font=f, fill=(35, 28, 34))
    d.text((X(12.0), Y(49.25)), "BAVARIA", font=fs, fill=(98, 88, 95))
    d.text((X(14.2), Y(50.55)), "BOHEMIA", font=fs, fill=(98, 88, 95))
    d.text((X(16.0), Y(49.25)), "MORAVIA", font=fs, fill=(98, 88, 95))
    return im


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for pid, (url, crop) in SOURCES.items():
        im = fetch(url)
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        save(im, pid); print(pid, im.size)
    save(draw_map(), "map"); print("map")


if __name__ == "__main__":
    main()
