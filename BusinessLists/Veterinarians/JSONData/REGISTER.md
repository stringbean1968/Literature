# Obtaining Veterinary Membership Registers (UK)

This document describes how to obtain registers of veterinary surgeons and
veterinary nurses from formal membership and statutory organisations in the
United Kingdom.

---

## 1. Royal College of Veterinary Surgeons (RCVS)

The RCVS is the statutory regulator for veterinary surgeons and veterinary
nurses in the UK under the Veterinary Surgeons Act 1966.

### 1.1 Register of Veterinary Surgeons

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.rcvs.org.uk/registration/find-a-vet-surgeon/ |
| **What is available** | Searchable register of all fully-registered veterinary surgeons. Fields: name, registration number, qualification(s), year of graduation, employer (voluntary). |
| **Bulk export** | Not publicly available for bulk download. Individual lookups via the search form only. |
| **API** | No public REST API documented. Unofficial scraping is prohibited by RCVS ToS. |
| **Data request / FOI** | A formal data request (not FOI — RCVS is not a public authority under FOIA 2000 for this purpose) can be submitted to registrations@rcvs.org.uk for research use. Commercial use requires a data licence agreement. |
| **Licence note** | RCVS register data is © Royal College of Veterinary Surgeons. Bulk use requires written permission. |

### 1.2 Register of Veterinary Nurses

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.rcvs.org.uk/registration/find-a-veterinary-nurse/ |
| **What is available** | Searchable register of all registered veterinary nurses. Fields: name, registration number, qualification(s), employer (voluntary). |
| **Bulk export** | Not publicly available. |
| **API** | No public API. |
| **Data request** | Same route as veterinary surgeons register (registrations@rcvs.org.uk). |

### 1.3 RCVS Practice Standards Scheme (PSS) Directory

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.rcvs.org.uk/setting-standards/practice-standards-scheme/find-a-pss-accredited-practice/ |
| **What is available** | Directory of RCVS-accredited practices. Tier information (Core, Silver, Gold, Platinum for different categories). Practice name, address, accreditation tier. |
| **Bulk export** | Not directly available. The directory is searchable but no CSV/JSON export is offered. |
| **Feasibility** | Moderate — a paginated scrape of the search results could enumerate accredited practices, but check ToS first. |

### 1.4 RCVS Find-a-Vet Practice Search

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.rcvs.org.uk/find-a-vet/ |
| **What is available** | Postcode-radius search returning practice name, address, phone, services, out-of-hours provision. The richest authoritative source. |
| **Bulk export** | None offered. Underlying data is the RCVS-maintained practice register. |
| **API** | An unofficial JSON endpoint is used internally; it is not documented or supported for third-party use. |
| **Data licence** | An RCVS data licence for commercial or research bulk use can be requested via info@rcvs.org.uk. |

---

## 2. British Veterinary Association (BVA)

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.bva.co.uk/ |
| **Register** | BVA publishes a member directory but it is not publicly searchable in bulk. Members opt in to listings. |
| **Bulk access** | Members-only via the BVA member portal. |
| **Contact** | bva@bva.co.uk |

---

## 3. Veterinary Council of Ireland (VCI) — Cross-Border Context

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.vci.ie/ |
| **Register** | Statutory register of veterinary practitioners in the Republic of Ireland. Relevant for Northern Ireland cross-border practices. |
| **Bulk export** | The VCI publishes an annual report with aggregate figures. The searchable register (https://www.vci.ie/registration/register-search/) does not offer bulk download. |
| **FOI** | Under the Irish FOI Act 2014, requests can be submitted to foi@agriculture.gov.ie (Dept of Agriculture, which sponsors the VCI). |

---

## 4. Veterinary Medicines Directorate (VMD)

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.vmd.defra.gov.uk/ |
| **Register** | VMD maintains a register of premises authorised to store and dispense veterinary medicines (Veterinary Written Directions). |
| **Bulk export** | The VMD Product Information Database is publicly searchable. A data extract can be requested via vmd@vmd.gov.uk. |
| **Open data** | Some VMD datasets are published on data.gov.uk. |

---

## 5. APHA / DEFRA Approved Establishments

| Attribute | Detail |
|-----------|--------|
| **URL** | https://www.gov.uk/government/collections/approved-laboratories-and-premises |
| **Register** | APHA-approved establishments for official veterinary activities (OVs, export health, TB testing). |
| **Bulk export** | Lists are published as downloadable documents (PDF/ODS) on GOV.UK. |
| **Licence** | Open Government Licence v3.0 where Crown copyright applies. |

---

## 6. OpenStreetMap

| Attribute | Detail |
|-----------|--------|
| **URL** | https://overpass-api.de/ / https://www.openstreetmap.org/ |
| **Register** | OSM tag `amenity=veterinary` covers community-mapped veterinary practices across the UK. |
| **Bulk export** | Full planet dump or UK extract available from Geofabrik (https://download.geofabrik.de/europe/great-britain.html). Overpass API for filtered queries. |
| **Licence** | ODbL — Open Database Licence. Attribution required. |
| **Overpass query** | `[out:json]; area["name"="United Kingdom"]->.uk; node[amenity=veterinary](area.uk); out body;` |

---

## 7. Companies House

| Attribute | Detail |
|-----------|--------|
| **URL** | https://find-and-update.company-information.service.gov.uk/ |
| **Register** | SIC code 75000 (Veterinary activities) filters ~6,000–8,000 registered companies. |
| **Bulk export** | Free bulk data download available at https://download.companieshouse.gov.uk/. Filter by SIC code 75000. |
| **API** | REST API available (https://developer.company-information.service.gov.uk/) — free for open data use. |
| **Licence** | Open Government Licence v3.0. |

---

## Summary: Recommended Acquisition Route

For building the most complete authoritative list:

1. **Companies House bulk CSV** filtered to SIC 75000 — gives all registered companies (not necessarily active practices, but broadest coverage).
2. **RCVS Find-a-Vet** — data licence request gives practice-level verified data with accreditation status.
3. **OSM Overpass** — free, open-licensed community data with location coordinates.
4. **VMD bulk extract** — adds regulated-premises angle.
5. Cross-reference and deduplicate on postcode + normalised name.
