# 🪐 Cosmo: Astronomy Query Toolkit

> **Modular Python framework for querying online astronomical catalogs and surveys.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)  
[![Astroquery](https://img.shields.io/badge/Astroquery-✔︎-purple.svg)](https://astroquery.readthedocs.io/)



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




## ⚙️ Installation

Cosmo runs on `astroquery`, and `astropy`

Install dependencies:

```
> pip install astroquery astropy
```



## 🧱 Project Structure

```
    cosmo.py                  # Main library (all services)
    boogr.py                  # Error + ErrorDialog definitions
    Python Style Example.py   # Enforced documentation and formatting standard
```



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





## 🔍 Example Usage

```

    from cosmo import SimbadService, VizierService
    from astropy import units as u
    from astropy.coordinates import SkyCoord
    
    simbad = SimbadService()
    result = simbad.query_object("M31")
    
    vizier = VizierService()
    catalog = "I/345/gaia2"
    coord = SkyCoord.from_name("M31")
    vizier_result = vizier.query_region(catalog, coord, radius=5 * u.arcmin)
    
```

### 1. 🌟 Resolve Object Name (SIMBAD) and Query Dust Map (IRSA)

```

    from cosmo import SimbadService, IrsaService
    from astropy.coordinates import SkyCoord
    
    simbad = SimbadService()
    result = simbad.query_object("M31")
    coord = SkyCoord(result["RA"][0] + " " + result["DEC"][0], unit=("hourangle", "deg"))
    
    irsa = IrsaService()
    dust = irsa.ebv(coord)
    print(dust["ext SandF mean"].data[0])

```



### 2. 📡 Query VizieR Catalog Around M31

```

    python
    from cosmo import VizierService
    from astropy import units as u
    from astropy.coordinates import SkyCoord
    
    vizier = VizierService()
    center = SkyCoord.from_name("M31")
    table = vizier.query_region("I/345/gaia2", center, radius=10 * u.arcmin)
    print(table.colnames)

```



### 3. 💫 Crossmatch Two Star Tables (XMatch)

```

    python
    from cosmo import XMatchService
    from astropy.table import Table
    import astropy.units as u
    
    # Local mock tables or previously queried results
    table1 = Table.read("stars1.vot", format="votable")
    table2 = Table.read("stars2.vot", format="votable")
    
    xmatch = XMatchService()
    matched = xmatch.match(table1, table2, max_distance=5 * u.arcsec)
    print(matched[:5])

```



### 4. 🛰️ Query and Download Hubble Data (MAST)

```

    python
    from cosmo import MastService
    
    mast = MastService()
    obs = mast.query_object("M51")
    products = mast.download(obs, limit=3)
    print(products)

```

### 5. 🔭 Query Gaia Archive with ADQL

```

    from cosmo import GaiaService
    
    gaia = GaiaService()
    query = """
    SELECT TOP 5 source_id, ra, dec, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE CONTAINS(
        POINT('ICRS', ra, dec),
        CIRCLE('ICRS', 10.684, 41.269, 0.05)
    ) = 1
    """
    stars = gaia.query_adql(query)
    print(stars)

```



## 📚 Requirements

- `astroquery>=0.4`
- `astropy>=5.0`
- Python 3.10 or higher



## 📜 License

This project is licensed under the terms of the **MIT license**. See [LICENSE](https://github.com/is-leeroy-jenkins/Cosmo/blob/master/LICENSE.txt) for details.



## 🙌 Acknowledgments

- Built with ❤️ using [Astroquery](https://astroquery.readthedocs.io/)
- Inspired by modular service-oriented wrappers and astronomy data science workflows.