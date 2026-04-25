# Schema Reference — UK Veterinary Practices

Each JSON file in `practices/` contains an **array** of practice objects conforming to the
JSON Schema defined in `schema.json` (draft-07).

## Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | ✓ | Globally unique URL-safe slug |
| `practiceName` | string | ✓ | Official registered practice name |
| `tradingName` | string\|null | | Trading/DBA name if different |
| `parentGroup` | string\|null | | Corporate group owner (e.g. CVS, IVC Evidensia) |
| `practiceType` | string | ✓ | One of: Small Animal, Equine, Farm Animal, Mixed Practice, Exotic Animal, Referral Hospital, Emergency, Mobile Vet, Small Animal & Exotic, Companion Animal |
| `species` | string[] | ✓ | Species treated |
| `services` | string[] | ✓ | Services offered |
| `rcvsPracticeNumber` | string\|null | | RCVS-assigned practice number |
| `rcvsAccreditation` | string\|null | | RCVS Practice Standards Scheme tier |
| `addressLine1` | string\|null | | Street address |
| `addressLine2` | string\|null | | Suite/unit/building |
| `town` | string | ✓ | Town/city |
| `county` | string\|null | | County or unitary authority |
| `postcode` | string | ✓ | UK postcode |
| `country` | string | ✓ | England, Scotland, Wales, or Northern Ireland |
| `region` | string\|null | | ONS region or devolved nation |
| `latitude` | number\|null | | WGS84 decimal latitude |
| `longitude` | number\|null | | WGS84 decimal longitude |
| `phone` | string\|null | | Primary telephone |
| `alternatePhone` | string\|null | | Secondary telephone |
| `emergencyPhone` | string\|null | | Out-of-hours emergency line |
| `email` | string\|null | | Contact email |
| `website` | string\|null | | Website URL |
| `openingHours` | object\|null | | Keyed by lowercase day name, value "HH:MM-HH:MM" |
| `outOfHoursProvider` | string\|null | | Named out-of-hours cover provider |
| `socialMedia` | object\|null | | Keys: facebook, instagram, twitter |
| `companiesHouseNumber` | string\|null | | UK Companies House registration |
| `vatNumber` | string\|null | | GB VAT registration |
| `principalVet` | string\|null | | Named principal veterinary surgeon |
| `clinicalDirector` | string\|null | | Named clinical director |
| `numberOfVets` | number\|null | | Approximate vet headcount |
| `dateEstablished` | string\|null | | Year (YYYY) or full ISO date |
| `notes` | string\|null | | Free-text notes |
| `sources` | string[] | ✓ | Source identifiers or URLs |
| `lastVerified` | string (date) | ✓ | ISO-8601 date of last data verification |

## Validation

```bash
# Using ajv-cli (Node.js)
npx ajv validate -s schema.json -d "practices/A/Vets_A.json"
# Using Python jsonschema
python -m jsonschema -i practices/A/Vets_A.json schema.json
```
