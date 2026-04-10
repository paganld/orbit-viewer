# 🛰️ Orbit Viewer

**Real-time satellite & aircraft tracking platform with KDE/DBSCAN analytics**

Built by [Dwight Pagán](https://github.com/paganld) · AI-Powered GEOINT

---

## Overview

Orbit Viewer is a full-stack geospatial intelligence (GEOINT) platform that visualizes real-time satellite trajectories and live aircraft positions. It combines data ingestion from OpenSky Network and Celestrak TLE feeds with interactive Leaflet maps and ML-based clustering (DBSCAN, KDE) to provide actionable situational awareness.

## Features

- 🌍 **Interactive map** — Real-time aircraft and satellite positions on Leaflet
- 📡 **Live ADS-B data** — Pulled from OpenSky Network API
- 🛰️ **Satellite TLE tracking** — Two-Line Element propagation via Celestrak
- 🔥 **KDE hotspot analysis** — Kernel Density Estimation for traffic concentration
- 🎯 **DBSCAN clustering** — Automatic pattern-of-life detection
- 🔌 **REST API** — Flask backend with structured JSON endpoints
- ⚡ **Lightweight stack** — SQLite, no heavy infrastructure required

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, JavaScript, Leaflet.js |
| Backend | Python, Flask, Flask-CORS |
| Data | OpenSky Network API, Celestrak TLE |
| Analytics | Scikit-learn (DBSCAN), SciPy (KDE) |
| Storage | SQLite |

## Architecture

```
orbitviewer/
├── frontend/
│   └── index.html          # Interactive map dashboard
├── backend/
│   ├── app.py              # Flask REST API
│   └── fetch_data.py       # Data ingestion pipeline
└── data/
    └── flights.db          # SQLite flight history
```

## Quick Start

```bash
# Clone
git clone https://github.com/paganld/orbit-viewer.git
cd orbit-viewer

# Install dependencies
pip install flask flask-cors requests

# Fetch data
cd backend
python fetch_data.py

# Start API
python app.py

# Open frontend/index.html in your browser
```

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/flights` | GET | Latest 100 flight states |

```json
{
  "icao24": "a3f5c2",
  "callsign": "UAL123",
  "latitude": 38.9072,
  "longitude": -77.0369,
  "altitude": 10000,
  "velocity": 250
}
```

## Use Cases

- **Airspace monitoring** — Track aircraft over regions of interest
- **Research** — Apply ML clustering to real-world movement data
- **Education** — Learn GEOINT concepts with hands-on code
- **Portfolio** — Full-stack geospatial data platform

## Data Sources

- [OpenSky Network](https://opensky-network.org/) — Open ADS-B flight data
- [Celestrak](https://celestrak.org/) — Satellite TLE data

## Author

**Dwight Pagán** — Data Scientist & AI Engineer
- GitHub: [@paganld](https://github.com/paganld)
- LinkedIn: [dwightjosefpagan](https://linkedin.com/in/dwightjosefpagan)

---

*Part of the OrbitData platform family.*
