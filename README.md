# 🪐 Cosmo: Astronomy Query Toolkit

> **Modular Python framework for querying online astronomical catalogs and surveys.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)  
[![Astroquery](https://img.shields.io/badge/Astroquery-✔︎-purple.svg)](https://astroquery.readthedocs.io/)

---

## ✨ Overview

**Cosmo** is a unified interface to major astronomical data services such as:

- SIMBAD
- VizieR
- Gaia TAP+
- IRSA & Dust Maps
- SDSS
- NED
- MAST
- CDS XMatch


---

## ⚙️ Installation

Cosmo depends on `astroquery`, `astropy`, and your local `boogr.py`.

Install dependencies:

```bash
pip install astroquery astropy
```

> Place `boogr.py` in the same directory or make it importable via your `PYTHONPATH`.

---

## 🧱 Project Structure

```
cosmo.py                  # Main library (all services)
boogr.py                  # Error + ErrorDialog definitions
Python Style Example.py   # Enforced documentation and formatting standard
```

---

## 🧩 Included Services

| Class              | Description                                                   |
|-------------------|---------------------------------------------------------------|
| `SimbadService`    | Resolves star/galaxy names to coordinates and metadata        |
| `VizierService`    | Queries regional catalogs via VizieR                          |
| `GaiaService`      | Executes ADQL queries against the ESA Gaia archive            |
| `IrsaService`      | Accesses IRSA Dust maps and reddening (E(B–V)) values         |
| `SdssService`      | Retrieves SDSS photometry and spectra near a target           |
| `NedService`       | Queries NED for redshift and metadata on extragalactic objects|
| `MastService`      | Searches the MAST archive and downloads mission products      |
| `XMatchService`    | Crossmatches two sky catalogs using CDS XMatch                |



---

## 🔍 Example Usage

```
python
from cosmo import SimbadService, VizierService
from astropy import units as u
from astropy.coordinates import SkyCoord

simbad = SimbadService()
result = simbad.resolve("M31")

vizier = VizierService()
catalog = "I/345/gaia2"
coord = SkyCoord.from_name("M31")
vizier_result = vizier.query_region(catalog, coord, radius=5 * u.arcmin)
```




---

## 🧪 Testing

- Add unit tests for each service’s key method using `pytest` and `astropy`’s offline mode.
- Validate error handling via mocked service failures.
- Provide CLI tools or notebook demos using example coordinates like `"M31"`, `"NGC 253"`, etc.

---

## 📚 Requirements

- `astroquery>=0.4`
- `astropy>=5.0`
- Python 3.10 or higher

---

## 📜 License

This project is licensed under the terms of the **MIT license**. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgments

- Built with ❤️ using [Astroquery](https://astroquery.readthedocs.io/)
- Inspired by modular service-oriented wrappers and astronomy data science workflows.