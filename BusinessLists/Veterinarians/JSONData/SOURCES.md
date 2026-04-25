# Data Sources — UK Veterinary Practices

## Statutory & Professional Registers

| Source | URL | Notes |
|--------|-----|-------|
| RCVS Find-a-Vet | https://www.rcvs.org.uk/find-a-vet/ | Statutory register of RCVS-listed premises |
| RCVS Practice Standards Scheme (PSS) | https://www.rcvs.org.uk/setting-standards/practice-standards-scheme/ | Voluntary accreditation; tiers Core → Advanced → Specialist/Referral |
| VMD Registered Premises | https://www.vmd.defra.gov.uk/ProductInformationDatabase/ | Premises registered for veterinary medicinal product use |
| DEFRA/APHA Approved Establishments | https://www.gov.uk/guidance/approved-laboratories-and-veterinary-practices | APHA-approved for official veterinary activities |

## Trade & Membership Bodies

| Source | URL |
|--------|-----|
| British Veterinary Association (BVA) | https://www.bva.co.uk/ |
| British Small Animal Veterinary Association (BSAVA) | https://www.bsava.com/ |
| British Equine Veterinary Association (BEVA) | https://www.beva.org.uk/ |
| British Cattle Veterinary Association (BCVA) | https://www.bcva.org.uk/ |
| Society of Practising Veterinary Surgeons (SPVS) | https://www.spvs.org.uk/ |
| British Veterinary Nursing Association (BVNA) | https://www.bvna.org.uk/ |
| Veterinary Management Group (VMG) | https://vmg.org.uk/ |
| XLVets | https://xlvets.co.uk/ |
| VetPartners | https://www.vetpartners.co.uk/ |
| MiVetClub | https://www.mivetclub.co.uk/ |
| VetSure | https://www.vetsure.com/ |

## Corporate Group Practice Locators

| Group | Locator URL |
|-------|-------------|
| CVS Group | https://www.cvsvets.com/find-a-vet/ |
| IVC Evidensia | https://www.ivcevidensia.co.uk/find-a-vet/ |
| Medivet | https://www.medivet.co.uk/find-a-vet/ |
| Vets4Pets / Companion Care | https://www.vets4pets.com/find-a-vet/ |
| VetPartners | https://www.vetpartners.co.uk/find-a-vet/ |
| Linnaeus Group | https://www.linnaeusgroup.co.uk/ |
| White Cross Vets | https://www.whitecrossvets.co.uk/find-a-vet/ |
| Goddard Veterinary Group | https://www.goddardvetgroup.co.uk/ |
| My Family Vets | https://myfamilyvets.co.uk/find-a-vet/ |
| Independent Vets | https://www.independentvets.co.uk/ |

## Referral & Emergency Networks

| Source | URL |
|--------|-----|
| Vets Now | https://www.vets-now.com/find-an-emergency-vet/ |
| Medivet 24/7 | https://www.medivet.co.uk/emergency-vets/ |
| AniCura | https://www.anicura.co.uk/ |
| University of Edinburgh R(D)SVS | https://www.ed.ac.uk/vet/hospital |
| University of Bristol Vet School | https://www.bris.ac.uk/vetscience/services/ |
| Royal Veterinary College (RVC) | https://www.rvc.ac.uk/small-animal-referrals |
| University of Liverpool SATH | https://www.liverpool.ac.uk/veterinary-science/teaching-hospital/ |
| University of Nottingham SVMS | https://www.nottingham.ac.uk/vetschool/ |
| University of Surrey VSH | https://www.surrey.ac.uk/veterinary-school/clinical-services |
| University of Glasgow SVMS | https://www.gla.ac.uk/schools/vet/ |

## General Business Directories

| Source | Notes |
|--------|-------|
| Companies House | https://find-and-update.company-information.service.gov.uk/ |
| Yell | https://www.yell.com/s/veterinary+surgeons.html |
| Google Places | Via Places API — amenity=veterinary |
| OpenStreetMap (OSM) | https://www.openstreetmap.org/ — tag amenity=veterinary |
| Bing Places | https://www.bingplaces.com/ |
| Foursquare | https://foursquare.com/ |
| Yelp UK | https://www.yelp.co.uk/ |

## Open Data

| Source | Notes |
|--------|-------|
| OSM Overpass API | https://overpass-api.de/ — query: `node[amenity=veterinary]` |
| data.gov.uk | https://data.gov.uk/ — search "veterinary" |

## Animal Charity Clinics

| Organisation | URL |
|--------------|-----|
| PDSA | https://www.pdsa.org.uk/find-a-vet |
| Blue Cross | https://www.bluecross.org.uk/ |
| RSPCA | https://www.rspca.org.uk/local/animal-clinics |
| Dogs Trust | https://www.dogstrust.org.uk/ |
| Cats Protection | https://www.cats.org.uk/ |

---

**Source identifier key** (used in each record's `sources` array):

| ID | Description |
|----|-------------|
| `RCVS-FindAVet` | RCVS online register |
| `RCVS-PSS` | RCVS Practice Standards Scheme |
| `OSM-amenity=veterinary` | OpenStreetMap node/way with amenity=veterinary |
| `VMD-RegisteredPremises` | VMD registered premises database |
| `Companies-House` | Companies House registration data |
| `Google-Places` | Google Places / Maps listing |
| `BVA-MemberDirectory` | BVA member directory listing |
