# UK Veterinary Practices — BusinessLists Dataset

A synthetic-but-realistic dataset of **2,300 UK veterinary practices**,
structured for use in business-listing, mapping, and data-engineering projects.

## Quick Start

```bash
# Count total records
cat manifest.json | python3 -c "import json,sys; m=json.load(sys.stdin); print(m['totalRecords'])"

# List all files
cat manifest.json | python3 -c "import json,sys; [print(f['file']) for f in json.load(sys.stdin)['files']]"

# Validate a file against the schema
python3 -m jsonschema -i practices/A/Vets_A.json schema.json
```

## Directory Structure

```
JSONData/
  practices/
    A/Vets_A.json          ← All practices starting with A
    B/Vets_B.json
    ...
    Z/Vets_Z.json
    0-9/Vets_0-9.json      ← Practices starting with a digit
    _other/Vets_other.json ← Practices starting with other chars
  manifest.json            ← Index of all chunk files + record counts
  schema.json              ← JSON Schema draft-07
  SCHEMA.md                ← Human-readable schema docs
  SOURCES.md               ← Data source documentation
  REGISTER.md              ← Practice register summary
  README.md                ← This file
```

## Data Model

Each record is a JSON object with **35 fields**.
See [SCHEMA.md](SCHEMA.md) for full field-level documentation.

Key fields:
- `id` — globally unique URL-safe slug
- `practiceName` / `tradingName`
- `practiceType` — Small Animal, Equine, Farm Animal, Mixed, Exotic, Referral, etc.
- `rcvsPracticeNumber` — RCVS register reference
- `parentGroup` — corporate group (CVS, IVC Evidensia, Medivet, Vets4Pets, etc.)
- `postcode` / `latitude` / `longitude` — location data
- `sources` — provenance identifiers

## Sources

See [SOURCES.md](SOURCES.md) for a full list of statutory registers, trade bodies,
corporate locators, open data, and charity clinic sources.

## Licence & Disclaimer

This dataset is **synthetic** — generated algorithmically for development and
testing purposes. Practice names, addresses, phone numbers, and other details
are fictional. Do not use this data for clinical, commercial, or navigation purposes.

For authoritative data, consult the [RCVS Find-a-Vet register](https://www.rcvs.org.uk/find-a-vet/).
