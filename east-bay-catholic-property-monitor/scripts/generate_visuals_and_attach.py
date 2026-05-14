#!/usr/bin/env python3
"""Generate durable visual assets for the East Bay Catholic property monitor and
attach a small visual block to every markdown page in the sub-vault.

The images are deliberately marked as visual aids, not photographic evidence or
appraisals. Source claims remain in the dossier text; this script only gives the
wiki pages eyes. A note without eyes is a spreadsheet wearing a cassock.
"""
from __future__ import annotations

import html
import importlib
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.request
from dataclasses import dataclass
from datetime import date
from io import BytesIO
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "visuals"
MAP_ASSETS = ROOT / "assets" / "maps"
DATA = ROOT / "assets" / "data"
TILE_CACHE = DATA / "map-tile-cache"
MAPS_CLIENT = Path("/Users/ericfode/.hermes/skills/productivity/maps/scripts/maps_client.py")
TODAY = os.environ.get("VISUAL_UPDATE_DATE", date.today().isoformat())

ASSETS.mkdir(parents=True, exist_ok=True)
MAP_ASSETS.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)
TILE_CACHE.mkdir(parents=True, exist_ok=True)

CLOSURE_WORDS = ("closure announced", "court-listed", "sale signal", "disposition")


@dataclass
class Site:
    slug: str
    title: str
    address: str
    status: str
    estimate_text: str
    low: float
    high: float
    mid: float
    lat: float | None = None
    lon: float | None = None
    geocode_name: str | None = None

    @property
    def risk_class(self) -> str:
        s = self.status.lower()
        if "closure announced" in s and "court-listed" in s:
            return "closure/court watch"
        if any(w in s for w in CLOSURE_WORDS):
            return "watch"
        if "cathedral" in self.slug:
            return "estate-structure watch"
        return "active/low"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def esc(s: object) -> str:
    return html.escape(str(s), quote=True)


def money_to_float(token: str) -> float:
    token = token.strip().replace("$", "").replace(",", "")
    multiplier = 1.0
    if token.lower().endswith("m"):
        multiplier = 1_000_000.0
        token = token[:-1]
    elif token.lower().endswith("k"):
        multiplier = 1_000.0
        token = token[:-1]
    return float(token) * multiplier


def fmt_money(value: float) -> str:
    if value >= 1_000_000:
        rounded = value / 1_000_000
        return f"${rounded:.1f}M" if rounded < 10 else f"${rounded:.0f}M"
    if value >= 1000:
        return f"${value/1000:.0f}k"
    return f"${value:.0f}"


def parse_range(text: str) -> tuple[float, float]:
    # Captures forms like "$2M–$4.6M", "$438,838–$997,359", "$831.9k–$1.9M".
    m = re.search(r"\$[\d,.]+\s*[kKmM]?\s*[–-]\s*\$[\d,.]+\s*[kKmM]?", text)
    if not m:
        raise ValueError(f"No dollar range in {text!r}")
    a, b = re.split(r"[–-]", m.group(0), maxsplit=1)
    # If low bound omits suffix but high bound has one and low has no comma, inherit suffix.
    high_suffix = re.search(r"[kKmM]\s*$", b.strip())
    if high_suffix and not re.search(r"[kKmM]\s*$", a.strip()) and "," not in a:
        a = a.strip() + high_suffix.group(0)
    return money_to_float(a), money_to_float(b)


def extract_field(text: str, label: str) -> str | None:
    m = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def h1_title(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Untitled"


def extract_sites() -> list[Site]:
    sites: list[Site] = []
    for path in sorted((ROOT / "entities").glob("*.md")):
        text = read(path)
        address = extract_field(text, "Address/source address")
        estimate = extract_field(text, "Core acquisition/redevelopment screen")
        status = extract_field(text, "Current status") or "unknown"
        if not address or not estimate:
            continue
        low, high = parse_range(estimate)
        sites.append(
            Site(
                slug=path.stem,
                title=h1_title(text),
                address=address,
                status=status,
                estimate_text=estimate.rstrip("."),
                low=low,
                high=high,
                mid=(low + high) / 2,
            )
        )
    return sites


def geocode_sites(sites: list[Site]) -> None:
    cache_path = DATA / "oakland-site-geocodes.json"
    cache = json.loads(read(cache_path)) if cache_path.exists() else {}
    changed = False
    for site in sites:
        cached = cache.get(site.slug)
        if cached and cached.get("lat") and cached.get("lon"):
            site.lat = float(cached["lat"])
            site.lon = float(cached["lon"])
            site.geocode_name = cached.get("display_name") or cached.get("name")
            continue
        query = f"{site.address}, Oakland, CA"
        if not MAPS_CLIENT.exists():
            raise SystemExit(f"maps client not found: {MAPS_CLIENT}")
        proc = subprocess.run(
            [sys.executable, str(MAPS_CLIENT), "search", query],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60,
            check=False,
        )
        if proc.returncode != 0:
            print(f"WARN: geocode failed for {site.slug}: {proc.stderr or proc.stdout}", file=sys.stderr)
            continue
        data = json.loads(proc.stdout)
        results = data.get("results") or []
        if not results:
            print(f"WARN: no geocode result for {site.slug}: {query}", file=sys.stderr)
            continue
        r = results[0]
        site.lat = float(r["lat"])
        site.lon = float(r["lon"])
        site.geocode_name = r.get("display_name") or r.get("name")
        cache[site.slug] = {
            "query": query,
            "lat": site.lat,
            "lon": site.lon,
            "display_name": site.geocode_name,
            "osm_type": r.get("osm_type"),
            "osm_id": r.get("osm_id"),
            "retrieved": TODAY,
            "source": "OpenStreetMap/Nominatim via Hermes maps skill",
        }
        changed = True
        time.sleep(1.05)
    if changed or not cache_path.exists():
        write(cache_path, json.dumps(cache, indent=2, sort_keys=True) + "\n")


class Projector:
    def __init__(self, sites: Iterable[Site], width: int, height: int, left=70, right=390, top=100, bottom=80):
        pts = [(s.lat, s.lon) for s in sites if s.lat is not None and s.lon is not None]
        if not pts:
            raise ValueError("No coordinates")
        lats = [p[0] for p in pts]
        lons = [p[1] for p in pts]
        self.min_lat, self.max_lat = min(lats), max(lats)
        self.min_lon, self.max_lon = min(lons), max(lons)
        lat_pad = max((self.max_lat - self.min_lat) * 0.12, 0.005)
        lon_pad = max((self.max_lon - self.min_lon) * 0.12, 0.005)
        self.min_lat -= lat_pad
        self.max_lat += lat_pad
        self.min_lon -= lon_pad
        self.max_lon += lon_pad
        self.width = width
        self.height = height
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def xy(self, site: Site) -> tuple[float, float]:
        assert site.lat is not None and site.lon is not None
        x0, x1 = self.left, self.width - self.right
        y0, y1 = self.top, self.height - self.bottom
        x = x0 + (site.lon - self.min_lon) / (self.max_lon - self.min_lon) * (x1 - x0)
        y = y0 + (self.max_lat - site.lat) / (self.max_lat - self.min_lat) * (y1 - y0)
        return x, y


def color_for(site: Site) -> str:
    rc = site.risk_class
    if rc.startswith("closure"):
        return "#c2410c"
    if rc == "watch":
        return "#d97706"
    if rc.startswith("estate"):
        return "#2563eb"
    return "#0f766e"


def price_radius(site: Site, max_mid: float, base=7, scale=33) -> float:
    return base + math.sqrt(site.mid / max_mid) * scale


def mercator_world_pixel(lat: float, lon: float, zoom: int) -> tuple[float, float]:
    """Web-Mercator global pixel coordinate for slippy-map tiles."""
    sin_lat = math.sin(math.radians(max(min(lat, 85.05112878), -85.05112878)))
    scale = 256 * (2 ** zoom)
    x = (lon + 180.0) / 360.0 * scale
    y = (0.5 - math.log((1 + sin_lat) / (1 - sin_lat)) / (4 * math.pi)) * scale
    return x, y


def choose_tile_zoom(sites: list[Site], width: int, height: int, padding: int = 170) -> int:
    pts = [(s.lat, s.lon) for s in sites if s.lat is not None and s.lon is not None]
    lats = [p[0] for p in pts]
    lons = [p[1] for p in pts]
    for zoom in range(17, 8, -1):
        pix = [mercator_world_pixel(lat, lon, zoom) for lat, lon in pts]
        xs = [p[0] for p in pix]
        ys = [p[1] for p in pix]
        if max(xs) - min(xs) <= width - padding * 2 and max(ys) - min(ys) <= height - padding * 2:
            return zoom
    return 11


def tile_url(x: int, y: int, zoom: int) -> str:
    # CARTO's Positron tiles are OSM-derived, keyless, and readable under dense markers.
    shard = "abc"[(x + y + zoom) % 3]
    return f"https://{shard}.basemaps.cartocdn.com/light_all/{zoom}/{x}/{y}.png"


def fetch_tile(x: int, y: int, zoom: int) -> bytes:
    cache_path = TILE_CACHE / str(zoom) / str(x) / f"{y}.png"
    if cache_path.exists():
        return cache_path.read_bytes()
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        tile_url(x, y, zoom),
        headers={"User-Agent": "Hermes Oakland church price-bubble map / small static wiki render"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        data = response.read()
    cache_path.write_bytes(data)
    time.sleep(0.12)
    return data


def load_font(size: int, bold: bool = False):
    ImageFont = importlib.import_module("PIL.ImageFont")

    candidates = [
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            continue
    return ImageFont.load_default()


def static_map_canvas(sites: list[Site], width: int, height: int):
    Image = importlib.import_module("PIL.Image")

    zoom = choose_tile_zoom(sites, width, height)
    pts = [(s.lat, s.lon) for s in sites if s.lat is not None and s.lon is not None]
    center_lat = (min(p[0] for p in pts) + max(p[0] for p in pts)) / 2
    center_lon = (min(p[1] for p in pts) + max(p[1] for p in pts)) / 2
    center_x, center_y = mercator_world_pixel(center_lat, center_lon, zoom)
    left = center_x - width / 2
    top = center_y - height / 2
    first_tile_x = math.floor(left / 256)
    last_tile_x = math.floor((left + width) / 256)
    first_tile_y = math.floor(top / 256)
    last_tile_y = math.floor((top + height) / 256)

    canvas = Image.new("RGB", (width, height), "#eef2f7")
    for tx in range(first_tile_x, last_tile_x + 1):
        for ty in range(first_tile_y, last_tile_y + 1):
            try:
                tile = Image.open(BytesIO(fetch_tile(tx, ty, zoom))).convert("RGB")
            except Exception as exc:
                print(f"WARN: map tile failed z{zoom}/{tx}/{ty}: {exc}", file=sys.stderr)
                continue
            px = round(tx * 256 - left)
            py = round(ty * 256 - top)
            canvas.paste(tile, (px, py))
    return canvas, zoom, left, top


def draw_centered_text(draw, xy: tuple[float, float], text: str, font, fill: str) -> None:
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    except Exception:
        w, h = draw.textlength(text, font=font), 12
    draw.text((xy[0] - w / 2, xy[1] - h / 2 - 1), text, font=font, fill=fill)


def generate_static_tile_map(sites: list[Site]) -> None:
    """Generate a real basemap PNG with price-scaled bubbles.

    The previous SVG was intentionally schematic; the user was quite right that
    it made Oakland look as though it had been surveyed by a poet with a ruler.
    This one uses live OSM-derived map tiles, then commits the rendered result.
    """
    try:
        Image = importlib.import_module("PIL.Image")
        ImageDraw = importlib.import_module("PIL.ImageDraw")
    except Exception as exc:
        raise SystemExit("Pillow is required for tile-backed map rendering") from exc

    width, height = 1600, 1080
    canvas, zoom, left, top = static_map_canvas(sites, width, height)
    overlay = Image.new("RGBA", canvas.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    max_mid = max(s.mid for s in sites)
    ranked = sorted(sites, key=lambda s: s.mid, reverse=True)
    index = {s.slug: i + 1 for i, s in enumerate(ranked)}
    font_title = load_font(38, True)
    font_sub = load_font(20, False)
    font_label = load_font(18, True)
    font_small = load_font(15, False)
    font_tiny = load_font(13, False)

    # Header and attribution panels.
    draw.rounded_rectangle((34, 28, 1118, 122), radius=24, fill=(255, 255, 255, 232), outline=(203, 213, 225, 255), width=2)
    draw.text((60, 45), "Oakland Catholic church price-bubble map", font=font_title, fill="#0f172a")
    draw.text((62, 91), "Real OSM/CARTO basemap; bubble area follows midpoint of current core agent estimate.", font=font_sub, fill="#334155")

    # Draw largest bubbles first so smaller sites remain clickable/legible.
    for s in sorted(sites, key=lambda site: site.mid, reverse=True):
        assert s.lat is not None and s.lon is not None
        px, py = mercator_world_pixel(s.lat, s.lon, zoom)
        x, y = px - left, py - top
        r = price_radius(s, max_mid, base=10, scale=34)
        c = color_for(s)
        rgb = tuple(int(c[i:i+2], 16) for i in (1, 3, 5))
        draw.ellipse((x-r, y-r, x+r, y+r), fill=rgb + (142,), outline=(15, 23, 42, 230), width=3)
        draw.ellipse((x-13, y-13, x+13, y+13), fill=(15, 23, 42, 238))
        draw_centered_text(draw, (x, y), str(index[s.slug]), font_label, "#ffffff")

    # Right-side ranked legend.
    panel = (1136, 80, 1570, 1018)
    draw.rounded_rectangle(panel, radius=26, fill=(255, 255, 255, 238), outline=(148, 163, 184, 255), width=2)
    draw.text((1162, 110), "Ranked by midpoint", font=font_sub, fill="#0f172a")
    y = 150
    for i, s in enumerate(ranked, start=1):
        c = color_for(s)
        rgb = tuple(int(c[j:j+2], 16) for j in (1, 3, 5))
        title = s.title.replace("Catholic Church", "").replace("Parish", "").replace("Oakland", "").strip(" ,/")
        if len(title) > 37:
            title = title[:34] + "…"
        draw.ellipse((1165, y-11, 1187, y+11), fill=rgb + (210,), outline=(15, 23, 42, 255), width=2)
        draw.text((1198, y-15), f"{i}. {title}", font=font_label, fill="#0f172a")
        draw.text((1198, y+8), f"mid {fmt_money(s.mid)} · {s.risk_class}", font=font_tiny, fill="#475569")
        y += 43

    # Bubble scale and source note.
    draw.rounded_rectangle((46, 923, 782, 1040), radius=20, fill=(255, 255, 255, 224), outline=(203, 213, 225, 255), width=2)
    draw.text((70, 945), "Bubble scale", font=font_label, fill="#0f172a")
    for j, val in enumerate([250_000, 1_000_000, 3_000_000, max_mid]):
        r = 10 + math.sqrt(val / max_mid) * 34
        x = 205 + j * 150
        draw.ellipse((x-r, 982-r, x+r, 982+r), fill=(51, 65, 85, 42), outline=(51, 65, 85, 180), width=2)
        draw_centered_text(draw, (x, 1030), fmt_money(val), font_tiny, "#334155")
    draw.text((46, 1052), "© OpenStreetMap contributors © CARTO · price labels are agent estimates, not appraisals or asking prices", font=font_tiny, fill="#334155")

    out = Image.alpha_composite(canvas.convert("RGBA"), overlay)
    out.save(ASSETS / "oakland-catholic-price-bubble-map.png", "PNG", optimize=True)


def generate_leaflet_map(sites: list[Site]) -> None:
    rows = []
    for s in sorted(sites, key=lambda site: site.mid, reverse=True):
        rows.append({
            "slug": s.slug,
            "title": s.title,
            "address": s.address,
            "status": s.status,
            "riskClass": s.risk_class,
            "estimate": s.estimate_text,
            "midpoint": s.mid,
            "midpointLabel": fmt_money(s.mid),
            "lat": s.lat,
            "lon": s.lon,
            "color": color_for(s),
        })
    max_mid = max(s.mid for s in sites)
    payload = json.dumps({"updated": TODAY, "maxMidpoint": max_mid, "sites": rows}, ensure_ascii=False)
    html_text = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Oakland Catholic price-bubble map</title>
  <link rel=\"stylesheet\" href=\"https://unpkg.com/leaflet@1.9.4/dist/leaflet.css\" integrity=\"sha256-p4NxAoJBhIINfQ6xO4O3mddPfM/sB9MQZWZsS9j6F9w=\" crossorigin=\"\" />
  <style>
    .leaflet-container {{ overflow: hidden; position: relative; outline-offset: 1px; }}
    .leaflet-pane, .leaflet-tile, .leaflet-marker-icon, .leaflet-marker-shadow, .leaflet-tile-container, .leaflet-pane > svg, .leaflet-pane > canvas, .leaflet-zoom-box, .leaflet-image-layer, .leaflet-layer {{ position: absolute; left: 0; top: 0; }}
    .leaflet-tile, .leaflet-marker-icon, .leaflet-marker-shadow {{ user-select: none; -webkit-user-drag: none; }}
    .leaflet-container img.leaflet-tile {{ max-width: none !important; max-height: none !important; }}
    .leaflet-zoom-animated {{ transform-origin: 0 0; }}
    .leaflet-interactive {{ cursor: pointer; }}
    .leaflet-control-container .leaflet-top, .leaflet-control-container .leaflet-bottom {{ position: absolute; z-index: 1000; pointer-events: none; }}
    .leaflet-top {{ top: 0; }} .leaflet-right {{ right: 0; }} .leaflet-bottom {{ bottom: 0; }} .leaflet-left {{ left: 0; }}
    .leaflet-control {{ position: relative; z-index: 800; pointer-events: auto; float: left; clear: both; }}
    .leaflet-right .leaflet-control {{ float: right; }}
    .leaflet-top .leaflet-control {{ margin-top: 10px; }} .leaflet-bottom .leaflet-control {{ margin-bottom: 10px; }}
    .leaflet-left .leaflet-control {{ margin-left: 10px; }} .leaflet-right .leaflet-control {{ margin-right: 10px; }}
    .leaflet-bar a {{ display:block; width:26px; height:26px; line-height:26px; text-align:center; text-decoration:none; background:white; color:#0f172a; border-bottom:1px solid #cbd5e1; }}
    .leaflet-bar a:first-child {{ border-top-left-radius:4px; border-top-right-radius:4px; }} .leaflet-bar a:last-child {{ border-bottom-left-radius:4px; border-bottom-right-radius:4px; border-bottom:0; }}
    .leaflet-control-attribution {{ background:rgba(255,255,255,.82); color:#334155; font-size:11px; padding:2px 6px; }}
    .leaflet-popup-pane {{ z-index: 700; }} .leaflet-marker-pane {{ z-index: 600; }} .leaflet-overlay-pane {{ z-index: 400; }} .leaflet-tile-pane {{ z-index: 200; }}
    html, body, #map {{ margin: 0; width: 100%; height: 100%; min-height: 640px; background: #e2e8f0; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif; }}
    .title-card {{ position:absolute; z-index:500; top:18px; left:18px; max-width:640px; background:rgba(255,255,255,.94); border:1px solid #cbd5e1; border-radius:18px; padding:14px 18px; box-shadow:0 12px 30px rgba(15,23,42,.18); }}
    .title-card h1 {{ margin:0 0 4px; font:700 24px Georgia,serif; color:#0f172a; }}
    .title-card p {{ margin:0; color:#334155; font-size:14px; line-height:1.35; }}
    .legend {{ position:absolute; z-index:500; top:18px; right:18px; width:330px; max-height:calc(100% - 72px); overflow:auto; background:rgba(255,255,255,.94); border:1px solid #cbd5e1; border-radius:18px; padding:14px 16px; box-shadow:0 12px 30px rgba(15,23,42,.18); }}
    .legend h2 {{ margin:0 0 10px; font-size:17px; color:#0f172a; }}
    .site-row {{ display:grid; grid-template-columns:22px 1fr; gap:9px; padding:7px 0; border-top:1px solid #e2e8f0; }}
    .dot {{ width:16px; height:16px; margin-top:3px; border-radius:999px; border:2px solid #0f172a; }}
    .site-name {{ color:#0f172a; font-weight:700; font-size:13px; }}
    .site-meta {{ color:#475569; font-size:12px; line-height:1.3; }}
    .rank-label {{ background:#0f172a; color:white; border-radius:999px; border:2px solid white; box-shadow:0 2px 8px rgba(15,23,42,.35); font-weight:800; font-size:12px; text-align:center; line-height:22px; width:22px; height:22px; }}
    .leaflet-popup-content {{ min-width:240px; }}
    .popup-title {{ font-weight:800; color:#0f172a; margin-bottom:4px; }}
    .popup-meta {{ color:#334155; line-height:1.35; }}
    .popup-meta a {{ color:#2563eb; }}
    @media (max-width: 900px) {{ .legend {{ left:12px; right:12px; bottom:12px; top:auto; width:auto; max-height:170px; border-radius:14px; padding:10px 12px; }} .title-card {{ top:12px; left:12px; right:12px; max-width:none; border-radius:14px; padding:10px 12px; }} .title-card h1 {{ font-size:18px; }} .title-card p {{ font-size:12px; }} html, body, #map {{ min-height:680px; }} .site-row {{ padding:4px 0; }} }}
  </style>
</head>
<body>
  <div id=\"map\"></div>
  <section class=\"title-card\">
    <h1>Oakland Catholic price-bubble map</h1>
    <p>Leaflet/CARTO/OpenStreetMap basemap. Bubbles scale by midpoint of the current core <code>agent estimate</code>; no bubble is an asking price, appraisal, or sale confirmation.</p>
  </section>
  <aside class=\"legend\" id=\"legend\"><h2>Ranked by midpoint</h2></aside>
  <script src=\"https://unpkg.com/leaflet@1.9.4/dist/leaflet.js\" integrity=\"sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=\" crossorigin=\"\"></script>
  <script>
    const data = {payload};
    const map = L.map('map', {{ scrollWheelZoom: false, preferCanvas: true }});
    L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}.png', {{
      maxZoom: 19,
      attribution: '&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors &copy; <a href=\"https://carto.com/attributions\">CARTO</a>'
    }}).addTo(map);
    const bounds = [];
    const legend = document.getElementById('legend');
    const radiusFor = midpoint => 7 + Math.sqrt(midpoint / data.maxMidpoint) * 26;
    data.sites.forEach((site, index) => {{
      const latlng = [site.lat, site.lon];
      bounds.push(latlng);
      const marker = L.circleMarker(latlng, {{
        radius: radiusFor(site.midpoint),
        color: '#0f172a', weight: 2,
        fillColor: site.color, fillOpacity: .62
      }}).addTo(map);
      marker.bindPopup(`<div class=\"popup-title\">${{index+1}}. ${{site.title}}</div><div class=\"popup-meta\">${{site.address}}<br><strong>${{site.estimate}}</strong><br>${{site.riskClass}}<br><a target=\"_blank\" rel=\"noreferrer\" href=\"https://www.google.com/maps/search/?api=1&query=${{site.lat}},${{site.lon}}\">Open in Google Maps</a></div>`);
      L.marker(latlng, {{
        interactive: false,
        icon: L.divIcon({{ className: 'rank-label', html: String(index+1), iconSize: [22,22], iconAnchor: [11,11] }})
      }}).addTo(map);
      const row = document.createElement('div');
      row.className = 'site-row';
      row.innerHTML = `<span class=\"dot\" style=\"background:${{site.color}}\"></span><div><div class=\"site-name\">${{index+1}}. ${{site.title}}</div><div class=\"site-meta\">mid ${{site.midpointLabel}} · ${{site.riskClass}}</div></div>`;
      row.addEventListener('mouseenter', () => marker.openPopup());
      legend.appendChild(row);
    }});
    const fitOptions = window.innerWidth < 900
      ? {{ paddingTopLeft: [28, 112], paddingBottomRight: [28, 178], maxZoom: 13 }}
      : {{ paddingTopLeft: [44, 96], paddingBottomRight: [390, 44], maxZoom: 13 }};
    map.fitBounds(bounds, fitOptions);
  </script>
</body>
</html>
"""
    write(MAP_ASSETS / "oakland-catholic-price-bubble-map.htm", html_text)


def svg_wrap(width: int, height: int, body: str, title: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">
  <defs>
    <style>
      .title {{ font: 700 38px Georgia, serif; fill: #111827; }}
      .subtitle {{ font: 500 17px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #475569; }}
      .small {{ font: 500 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #475569; }}
      .tiny {{ font: 500 11px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #64748b; }}
      .label {{ font: 700 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #0f172a; }}
      .num {{ font: 800 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: white; }}
      .card-title {{ font: 700 33px Georgia, serif; fill: #111827; }}
      .card-subtitle {{ font: 600 19px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #334155; }}
      .card-body {{ font: 500 17px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #334155; }}
      .mono {{ font: 600 13px "SFMono-Regular", ui-monospace, Menlo, monospace; fill: #475569; }}
    </style>
    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fff7ed"/>
      <stop offset="1" stop-color="#eff6ff"/>
    </linearGradient>
    <linearGradient id="night" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f172a"/>
      <stop offset="1" stop-color="#164e63"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="7" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.16"/>
    </filter>
  </defs>
{body}
</svg>
'''



def generate_rank_chart(sites: list[Site]) -> None:
    width, height = 1400, 1020
    ranked = sorted(sites, key=lambda s: s.mid, reverse=True)
    max_mid = max(s.mid for s in sites)
    body = [
        '<rect width="1400" height="1020" fill="url(#paper)"/>',
        '<text x="58" y="66" class="title">Oakland Catholic core-site price screen</text>',
        '<text x="60" y="96" class="subtitle">Horizontal bars show midpoint of the current low-confidence core acquisition/redevelopment range.</text>',
    ]
    y = 145
    for i, s in enumerate(ranked, start=1):
        bar_w = 810 * (s.mid / max_mid)
        col = color_for(s)
        title = s.title.replace("Catholic Church", "").replace("Parish", "").strip()
        if len(title) > 44:
            title = title[:41] + "…"
        body.append(f'<text x="60" y="{y+18}" class="label">{i:02d}. {esc(title)}</text>')
        body.append(f'<rect x="430" y="{y}" width="820" height="24" rx="12" fill="#e2e8f0"/>')
        body.append(f'<rect x="430" y="{y}" width="{bar_w:.1f}" height="24" rx="12" fill="{col}" opacity="0.82"/>')
        body.append(f'<text x="1272" y="{y+18}" class="label">{esc(s.estimate_text)}</text>')
        y += 45
    body.append('<text x="60" y="980" class="tiny">Labels: `agent estimate`; no public asking price, confirmed buyer, broker listing, or sale price unless later dossier text says otherwise.</text>')
    write(ASSETS / "oakland-catholic-site-price-rank.svg", svg_wrap(width, height, "\n".join(body), "Oakland Catholic core-site price rank"))


def generate_project_index(sites: list[Site]) -> None:
    width, height = 1400, 920
    ranked = sorted(sites, key=lambda s: s.mid, reverse=True)
    max_mid = max(s.mid for s in sites)
    body = [
        '<rect width="1400" height="920" fill="#f8fafc"/>',
        '<text x="58" y="66" class="title">Project visual index</text>',
        '<text x="60" y="96" class="subtitle">Each tile is a dossier hook: site, price-range screen, and current watch class.</text>',
    ]
    cols = 4
    tile_w, tile_h = 305, 145
    start_x, start_y = 60, 130
    gap_x, gap_y = 25, 24
    for i, s in enumerate(ranked):
        col_i = i % cols
        row_i = i // cols
        x = start_x + col_i * (tile_w + gap_x)
        y = start_y + row_i * (tile_h + gap_y)
        c = color_for(s)
        r = price_radius(s, max_mid, base=8, scale=26)
        body.append(f'<rect x="{x}" y="{y}" width="{tile_w}" height="{tile_h}" rx="18" fill="white" stroke="#cbd5e1" filter="url(#shadow)"/>')
        body.append(f'<circle cx="{x+40}" cy="{y+47}" r="{r:.1f}" fill="{c}" fill-opacity="0.65" stroke="#0f172a"/>')
        title = s.title.replace("Catholic Church", "").replace("Parish", "").replace("Oakland", "").strip(" ,/")
        lines = [title[:30], title[30:60].strip()] if len(title) > 30 else [title]
        body.append(f'<text x="{x+86}" y="{y+38}" class="label">{esc(lines[0])}</text>')
        if len(lines) > 1 and lines[1]:
            body.append(f'<text x="{x+86}" y="{y+56}" class="label">{esc(lines[1])}</text>')
        body.append(f'<text x="{x+86}" y="{y+82}" class="small">{esc(s.estimate_text)}</text>')
        body.append(f'<text x="{x+86}" y="{y+106}" class="tiny">{esc(s.risk_class)}</text>')
        body.append(f'<text x="{x+18}" y="{y+128}" class="mono">{esc(s.slug)}</text>')
    write(ASSETS / "oakland-catholic-project-visual-index.svg", svg_wrap(width, height, "\n".join(body), "Project visual index"))


def mini_map_svg(sites: list[Site], highlight: Site, x0: int, y0: int, w: int, h: int) -> str:
    pr = Projector(sites, x0 + w, y0 + h, left=x0+22, right=22, top=y0+22, bottom=22)
    parts = [f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="24" fill="#eff6ff" stroke="#bfdbfe"/>']
    for s in sites:
        if s.lat is None or s.lon is None:
            continue
        x, y = pr.xy(s)
        r = 4 if s.slug != highlight.slug else 12
        color = color_for(s) if s.slug == highlight.slug else "#64748b"
        opacity = "0.95" if s.slug == highlight.slug else "0.38"
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="{opacity}"/>')
    parts.append(f'<text x="{x0+20}" y="{y0+h-18}" class="tiny">relative Oakland position</text>')
    return "\n".join(parts)


def generate_site_cards(sites: list[Site]) -> None:
    max_mid = max(s.mid for s in sites)
    for s in sites:
        width, height = 1200, 720
        c = color_for(s)
        body = [
            '<rect width="1200" height="720" rx="0" fill="url(#paper)"/>',
            '<rect x="48" y="48" width="1104" height="624" rx="34" fill="white" filter="url(#shadow)"/>',
            f'<circle cx="1030" cy="170" r="{price_radius(s, max_mid, base=30, scale=82):.1f}" fill="{c}" fill-opacity="0.18"/>',
            f'<circle cx="1030" cy="170" r="{price_radius(s, max_mid, base=16, scale=42):.1f}" fill="{c}" fill-opacity="0.70" stroke="#0f172a" stroke-width="2"/>',
            f'<text x="1030" y="176" text-anchor="middle" class="num">{fmt_money(s.mid)}</text>',
            f'<text x="84" y="122" class="card-title">{esc(s.title)}</text>',
            f'<text x="86" y="164" class="card-subtitle">{esc(s.address)}</text>',
            f'<text x="86" y="223" class="label">Core price screen</text>',
            f'<text x="86" y="260" class="card-title" font-size="46">{esc(s.estimate_text)}</text>',
            f'<text x="86" y="306" class="card-body">Label: agent estimate · midpoint {fmt_money(s.mid)} · not an asking price</text>',
            f'<rect x="86" y="344" width="610" height="92" rx="18" fill="#f8fafc" stroke="#e2e8f0"/>',
            f'<text x="112" y="379" class="label">Current watch class</text>',
            f'<text x="112" y="410" class="card-body">{esc(s.risk_class)}</text>',
            f'<rect x="86" y="462" width="610" height="94" rx="18" fill="#fff7ed" stroke="#fed7aa"/>',
            f'<text x="112" y="496" class="label">Status note</text>',
        ]
        status = s.status
        if len(status) > 85:
            status = status[:82] + "…"
        body.append(f'<text x="112" y="528" class="card-body">{esc(status)}</text>')
        body.append(mini_map_svg(sites, s, 760, 330, 330, 250))
        body.append('<text x="84" y="626" class="tiny">Generated visual aid from dossier fields and OpenStreetMap/Nominatim coordinates. Source claims remain in the dossier body.</text>')
        write(ASSETS / f"site-card-{s.slug}.svg", svg_wrap(width, height, "\n".join(body), f"Visual dossier card for {s.title}"))


def generate_signal_ladder() -> None:
    width, height = 1200, 680
    steps = [
        ("Closure / MAP mention", "Watch item only", "#64748b"),
        ("Court docket names parcel", "Disposition/collateralization signal", "#d97706"),
        ("Broker listing / asking price", "Market signal", "#c2410c"),
        ("Sale motion / confirmed buyer", "Transaction signal", "#7c2d12"),
        ("Recorded sale price", "Observed price", "#0f766e"),
    ]
    body = ['<rect width="1200" height="680" fill="url(#paper)"/>', '<text x="58" y="72" class="title">Property-sale signal ladder</text>', '<text x="60" y="102" class="subtitle">A visual reminder: closure is not sale; sale evidence has levels.</text>']
    x = 85
    for i, (a, b, c) in enumerate(steps, start=1):
        y = 160 + (i - 1) * 92
        body.append(f'<circle cx="{x}" cy="{y}" r="28" fill="{c}"/>')
        body.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" class="num">{i}</text>')
        body.append(f'<rect x="140" y="{y-33}" width="890" height="66" rx="20" fill="white" stroke="#cbd5e1" filter="url(#shadow)"/>')
        body.append(f'<text x="168" y="{y-7}" class="label">{esc(a)}</text>')
        body.append(f'<text x="168" y="{y+18}" class="small">{esc(b)}</text>')
        if i < len(steps):
            body.append(f'<path d="M{x},{y+32} V{y+58}" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>')
    body.append('<text x="60" y="640" class="tiny">Current project posture: several Oakland closure sites have court-docket disposition/collateralization signals; none has an observed asking or sale price in the current dossiers.</text>')
    write(ASSETS / "property-sale-signal-ladder.svg", svg_wrap(width, height, "\n".join(body), "Property sale signal ladder"))


def generate_valuation_flow() -> None:
    width, height = 1200, 620
    nodes = [
        ("Parcel envelope", "APNs, lot area, owner, use code"),
        ("Assessed values", "Land + improvements from parcel data"),
        ("Same-ZIP land screen", "Median land value / sq ft sample"),
        ("Core range", "Low-confidence acquisition screen"),
        ("Observed price override", "Asking / court value / sale price wins"),
    ]
    body = ['<rect width="1200" height="620" fill="#f8fafc"/>', '<text x="58" y="72" class="title">Valuation method flow</text>', '<text x="60" y="102" class="subtitle">The estimate is a maintenance screen until real market evidence arrives.</text>']
    x0, y0 = 72, 190
    for i, (a, b) in enumerate(nodes):
        x = x0 + i * 218
        body.append(f'<rect x="{x}" y="{y0}" width="180" height="185" rx="24" fill="white" stroke="#cbd5e1" filter="url(#shadow)"/>')
        body.append(f'<circle cx="{x+90}" cy="{y0+52}" r="28" fill="#0f766e"/>')
        body.append(f'<text x="{x+90}" y="{y0+58}" text-anchor="middle" class="num">{i+1}</text>')
        body.append(f'<text x="{x+18}" y="{y0+104}" class="label">{esc(a)}</text>')
        # split b into two lines if needed
        if len(b) > 28:
            cut = b.rfind(" ", 0, 28)
            if cut == -1: cut = 28
            b1, b2 = b[:cut], b[cut:].strip()
            body.append(f'<text x="{x+18}" y="{y0+134}" class="tiny">{esc(b1)}</text>')
            body.append(f'<text x="{x+18}" y="{y0+153}" class="tiny">{esc(b2)}</text>')
        else:
            body.append(f'<text x="{x+18}" y="{y0+140}" class="tiny">{esc(b)}</text>')
        if i < len(nodes) - 1:
            body.append(f'<path d="M{x+188},{y0+92} H{x+215}" stroke="#94a3b8" stroke-width="4" marker-end="url(#arrow)"/>')
    body.append('<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L6,3 z" fill="#94a3b8"/></marker></defs>')
    body.append('<text x="72" y="535" class="small">Rule: never promote an agent estimate to a listing price. The first grounded price source displaces the screen.</text>')
    write(ASSETS / "valuation-method-flow.svg", svg_wrap(width, height, "\n".join(body), "Valuation method flow"))


def generate_schema_map() -> None:
    width, height = 1200, 640
    nodes = [
        ("Raw articles / dockets", "captured evidence", "#2563eb"),
        ("Entities", "site dossiers", "#0f766e"),
        ("Concepts", "rules and methods", "#7c3aed"),
        ("Comparisons", "ranked screens", "#d97706"),
        ("Queries", "monitor instructions", "#c2410c"),
    ]
    body = ['<rect width="1200" height="640" fill="url(#paper)"/>', '<text x="58" y="72" class="title">Sub-vault structure</text>', '<text x="60" y="102" class="subtitle">Evidence stays separate from synthesis; the ontology earns its keep.</text>']
    y = 190
    for i, (a, b, c) in enumerate(nodes):
        x = 75 + i * 220
        body.append(f'<rect x="{x}" y="{y}" width="180" height="180" rx="28" fill="white" stroke="#cbd5e1" filter="url(#shadow)"/>')
        body.append(f'<rect x="{x+24}" y="{y+28}" width="132" height="46" rx="23" fill="{c}" opacity="0.85"/>')
        body.append(f'<text x="{x+90}" y="{y+58}" text-anchor="middle" class="num">{i+1}</text>')
        body.append(f'<text x="{x+20}" y="{y+115}" class="label">{esc(a)}</text>')
        body.append(f'<text x="{x+20}" y="{y+144}" class="small">{esc(b)}</text>')
        if i < len(nodes) - 1:
            body.append(f'<path d="M{x+184},{y+90} H{x+215}" stroke="#64748b" stroke-width="4"/>')
    body.append('<text x="72" y="535" class="small">Visual convention added 2026-05-14: rendered pages include at least one non-evidentiary image block.</text>')
    write(ASSETS / "schema-content-map.svg", svg_wrap(width, height, "\n".join(body), "Sub-vault structure"))


def generate_source_basis_card() -> None:
    width, height = 1200, 620
    body = [
        '<rect width="1200" height="620" fill="#0f172a"/>',
        '<text x="64" y="84" class="title" fill="#f8fafc">Raw source note wrapper</text>',
        '<text x="66" y="122" class="subtitle" fill="#cbd5e1">Images on raw pages are navigation aids; they do not alter the source evidence body.</text>',
        '<rect x="70" y="175" width="310" height="260" rx="28" fill="#1e293b" stroke="#475569"/>',
        '<text x="105" y="235" class="label" fill="#e2e8f0">Evidence capture</text>',
        '<text x="105" y="278" class="small" fill="#cbd5e1">quotes, URLs, docket notes</text>',
        '<rect x="445" y="175" width="310" height="260" rx="28" fill="#1e293b" stroke="#475569"/>',
        '<text x="480" y="235" class="label" fill="#e2e8f0">Synthesis pages</text>',
        '<text x="480" y="278" class="small" fill="#cbd5e1">entities, concepts, comparisons</text>',
        '<rect x="820" y="175" width="310" height="260" rx="28" fill="#1e293b" stroke="#475569"/>',
        '<text x="855" y="235" class="label" fill="#e2e8f0">Visual aids</text>',
        '<text x="855" y="278" class="small" fill="#cbd5e1">maps, cards, signal diagrams</text>',
        '<path d="M385,305 H435" stroke="#94a3b8" stroke-width="5"/>',
        '<path d="M760,305 H810" stroke="#94a3b8" stroke-width="5"/>',
        '<text x="66" y="535" class="tiny" fill="#cbd5e1">If a visual and a source conflict, the source text wins. The image is the handle, not the blade.</text>',
    ]
    write(ASSETS / "source-basis-visual-wrapper.svg", svg_wrap(width, height, "\n".join(body), "Raw source note wrapper"))


def generate_all_assets(sites: list[Site]) -> None:
    generate_static_tile_map(sites)
    generate_leaflet_map(sites)
    generate_rank_chart(sites)
    generate_project_index(sites)
    generate_site_cards(sites)
    generate_signal_ladder()
    generate_valuation_flow()
    generate_schema_map()
    generate_source_basis_card()


def rel_image(page: Path, asset_name: str) -> str:
    # Quartz's `shortest` link resolver treats resource URLs as vault-root-ish
    # slugs; the stable source form is therefore the content-root path for
    # Markdown images. Raw HTML embeds are not rewritten, so they use a real
    # page-relative path via rel_embed(). One resolver would be too merciful.
    return f"{ROOT.name}/assets/visuals/{asset_name}"


def rel_embed(page: Path, rel_asset: str) -> str:
    target = ROOT / rel_asset
    return os.path.relpath(target, page.parent).replace(os.sep, "/")


def image_line(page: Path, asset_name: str, alt: str) -> str:
    return f"![{alt}]({rel_image(page, asset_name)})"


def interactive_map_iframe(page: Path) -> str:
    # Quartz rewrites local .html src attributes just like Markdown links, so
    # the iframe targets a checked-in .htm twin; old-fashioned, but with a proper
    # text/html MIME type on static hosts. A small price for less occult routing.
    src = f"{ROOT.name}/assets/maps/oakland-catholic-price-bubble-map.htm"
    return (
        f'<iframe title="Interactive Oakland Catholic price-bubble map" src="{src}" '
        'loading="lazy" width="100%" height="680" '
        'style="border:1px solid #cbd5e1;border-radius:18px;max-width:100%;background:#e2e8f0;"></iframe>'
    )


def update_frontmatter_date(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end == -1:
        return text
    fm = text[: end + 4]
    rest = text[end + 4 :]
    if re.search(r"^updated:\s*.+$", fm, re.M):
        fm = re.sub(r"^updated:\s*.+$", f"updated: {TODAY}", fm, flags=re.M)
    return fm + rest


def visual_block_for(page: Path, site_by_slug: dict[str, Site]) -> str:
    rel = page.relative_to(ROOT).as_posix()
    slug = page.stem
    lines = ["<!-- oakland-visuals:start -->", "## Visuals", "", interactive_map_iframe(page), ""]
    if slug in site_by_slug:
        site = site_by_slug[slug]
        lines += [
            image_line(page, f"site-card-{slug}.svg", f"Visual dossier card for {site.title}"),
            "",
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
            "",
            "> Visuals are navigation aids generated from dossier fields and OpenStreetMap/Nominatim coordinates; price labels remain `agent estimate` unless the text says otherwise.",
        ]
    elif rel == "entities/diocese-of-oakland.md":
        lines += [
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "property-sale-signal-ladder.svg", "Property-sale signal ladder"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
            "",
            "> Diocese-level visuals summarize the monitored Oakland site set; they are not appraisals or sale confirmations.",
        ]
    elif rel.endswith("valuation-methodology.md"):
        lines += [
            image_line(page, "valuation-method-flow.svg", "Valuation method flow"),
            "",
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
        ]
    elif rel.endswith("property-sale-signals.md"):
        lines += [
            image_line(page, "property-sale-signal-ladder.svg", "Property-sale signal ladder"),
            "",
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
        ]
    elif rel.endswith("SCHEMA.md"):
        lines += [
            image_line(page, "schema-content-map.svg", "Sub-vault structure diagram"),
            "",
            image_line(page, "oakland-catholic-project-visual-index.svg", "Oakland Catholic project visual index"),
            "",
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
        ]
    elif rel.startswith("raw/articles/"):
        lines += [
            image_line(page, "source-basis-visual-wrapper.svg", "Raw source note visual wrapper"),
            "",
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
            "",
            "> Presentation wrapper added 2026-05-14. The source-capture body below remains the evidentiary surface; images are non-evidentiary navigation aids.",
        ]
    elif rel.startswith("comparisons/"):
        lines += [
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
            "",
            image_line(page, "oakland-catholic-project-visual-index.svg", "Oakland Catholic project visual index"),
        ]
    else:
        lines += [
            image_line(page, "oakland-catholic-price-bubble-map.png", "Oakland Catholic church price-bubble map"),
            "",
            image_line(page, "oakland-catholic-project-visual-index.svg", "Oakland Catholic project visual index"),
            "",
            image_line(page, "oakland-catholic-site-price-rank.svg", "Oakland Catholic core-site price rank"),
        ]
    lines += ["", "<!-- oakland-visuals:end -->"]
    return "\n".join(lines)


def insert_or_replace_visual_block(text: str, block: str) -> str:
    start = "<!-- oakland-visuals:start -->"
    end = "<!-- oakland-visuals:end -->"
    pattern = re.compile(rf"\n?{re.escape(start)}.*?{re.escape(end)}\n?", re.S)
    if start in text and end in text:
        return pattern.sub("\n" + block + "\n\n", text).rstrip() + "\n"
    m = re.search(r"^#\s+.+$", text, re.M)
    if not m:
        return block + "\n\n" + text.lstrip()
    insert_at = m.end()
    return text[:insert_at] + "\n\n" + block + text[insert_at:]


def update_index_header(text: str) -> str:
    return re.sub(r"^> Last updated: \d{4}-\d{2}-\d{2} \| Total pages: (\d+)$", f"> Last updated: {TODAY} | Total pages: \\1", text, flags=re.M)


def update_schema_visual_convention(path: Path) -> None:
    text = read(path)
    text = update_frontmatter_date(text)
    needle = "- Every content page must have YAML frontmatter with `title`, `created`, `updated`, `type`, `tags`, and `sources`."
    addition = "- Every rendered project page should include at least one non-evidentiary visual block (`<!-- oakland-visuals:start -->`) so the public surface is navigable by eye; raw evidence bodies remain authoritative over visual aids."
    if addition not in text and needle in text:
        text = text.replace(needle, needle + "\n" + addition)
    write(path, text)


def attach_visuals(sites: list[Site]) -> None:
    site_by_slug = {s.slug: s for s in sites}
    md_files = sorted(ROOT.rglob("*.md"))
    for page in md_files:
        if ".quartz-site" in page.parts:
            continue
        text = read(page)
        if page.name == "index.md" and page.parent == ROOT:
            text = update_index_header(text)
        if page.name == "SCHEMA.md" and page.parent == ROOT:
            # handled after insertion as well; preserve one write path.
            pass
        text = update_frontmatter_date(text)
        block = visual_block_for(page, site_by_slug)
        text = insert_or_replace_visual_block(text, block)
        write(page, text)
    update_schema_visual_convention(ROOT / "SCHEMA.md")
    append_log()


def append_log() -> None:
    path = ROOT / "log.md"
    text = read(path)
    entry = f"""
## [{TODAY}] update | visual coverage and price-bubble map
- Added generated visual blocks to every Markdown page in the Oakland church sub-vault: dossier cards for site pages, shared price-bubble map, rank chart, method diagrams, schema diagram, and raw-note visual wrappers.
- Added [[oakland-catholic-church-price-screen-2026-05-13]] map/rank visuals with bubbles scaled by midpoint of the current core `agent estimate`; no visual is an asking price, appraisal, or sale confirmation.
- Generated durable local SVG assets under the sub-vault asset tree and cached OpenStreetMap/Nominatim coordinates for the 19 Oakland site dossiers.
""".strip()
    if "visual coverage and price-bubble map" not in text:
        text = text.rstrip() + "\n\n" + entry + "\n"
    tile_entry = f"""
## [{TODAY}] update | real basemap price-bubble map
- Replaced the schematic Oakland price map with a real OpenStreetMap/CARTO tile-backed PNG and an embedded Leaflet interactive map on every Oakland project page.
- The map still uses the current dossier `agent estimate` midpoint for bubble area; it remains a navigational screen, not an appraisal or asking-price claim.
""".strip()
    if "real basemap price-bubble map" not in text:
        text = text.rstrip() + "\n\n" + tile_entry + "\n"
    write(path, text)


def write_site_data(sites: list[Site]) -> None:
    rows = []
    for s in sorted(sites, key=lambda s: s.slug):
        rows.append({
            "slug": s.slug,
            "title": s.title,
            "address": s.address,
            "status": s.status,
            "risk_class": s.risk_class,
            "estimate_text": s.estimate_text,
            "estimate_low": round(s.low, 2),
            "estimate_high": round(s.high, 2),
            "estimate_midpoint": round(s.mid, 2),
            "lat": s.lat,
            "lon": s.lon,
            "coordinate_source": "OpenStreetMap/Nominatim via Hermes maps skill",
        })
    write(DATA / "oakland-site-price-bubble-map-data.json", json.dumps({"updated": TODAY, "sites": rows}, indent=2, sort_keys=False) + "\n")


def verify(sites: list[Site]) -> None:
    missing = []
    too_few = []
    broken = []
    missing_interactive = []
    for page in sorted(ROOT.rglob("*.md")):
        if ".quartz-site" in page.parts:
            continue
        text = read(page)
        image_links = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
        iframe_links = re.findall(r"<iframe\b[^>]*\bsrc=\"([^\"]+)\"", text)
        if not image_links:
            missing.append(page.relative_to(ROOT).as_posix())
        if len(image_links) < 3:
            too_few.append(f"{page.relative_to(ROOT).as_posix()} ({len(image_links)})")
        if not any("oakland-catholic-price-bubble-map.htm" in link for link in iframe_links):
            missing_interactive.append(page.relative_to(ROOT).as_posix())
        for link in image_links + iframe_links:
            if re.match(r"^[a-z]+://", link):
                continue
            if link.startswith(f"{ROOT.name}/"):
                target = (ROOT.parent / link).resolve()
            else:
                target = (page.parent / link).resolve()
            if not target.exists():
                broken.append(f"{page.relative_to(ROOT).as_posix()} -> {link}")
    if missing:
        raise SystemExit("Pages still lacking images: " + ", ".join(missing))
    if too_few:
        raise SystemExit("Pages with fewer than three images: " + ", ".join(too_few))
    if missing_interactive:
        raise SystemExit("Pages lacking interactive map iframe: " + ", ".join(missing_interactive))
    if broken:
        raise SystemExit("Broken local image/embed links: " + ", ".join(broken))
    # XML sanity: parse all generated SVGs with stdlib.
    import xml.etree.ElementTree as ET
    for svg in sorted(ASSETS.glob("*.svg")):
        ET.parse(svg)
    print(json.dumps({
        "updated": TODAY,
        "site_count": len(sites),
        "markdown_pages_with_images": sum(1 for p in ROOT.rglob("*.md") if "![" in read(p)),
        "minimum_images_per_markdown_page": 3,
        "interactive_iframe_required": True,
        "svg_assets": len(list(ASSETS.glob("*.svg"))),
        "static_tile_map": str((ASSETS / "oakland-catholic-price-bubble-map.png").relative_to(ROOT)),
        "interactive_map": str((MAP_ASSETS / "oakland-catholic-price-bubble-map.htm").relative_to(ROOT)),
    }, indent=2))


def main() -> None:
    sites = extract_sites()
    if len(sites) < 10:
        raise SystemExit(f"Expected Oakland site dossiers; found only {len(sites)}")
    geocode_sites(sites)
    sites = [s for s in sites if s.lat is not None and s.lon is not None]
    if len(sites) < 10:
        raise SystemExit("Too few geocoded sites for map")
    write_site_data(sites)
    generate_all_assets(sites)
    attach_visuals(sites)
    verify(sites)


if __name__ == "__main__":
    main()
