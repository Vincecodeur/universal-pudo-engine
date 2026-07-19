# Provider Mapping Strategy

Status: Draft

Last Updated: 2026-07-19

==================================================
PURPOSE
==================================================

The purpose of this document is to define a
standard mapping strategy for all pickup point
providers supported by Universal PUDO Engine.

The objective is to allow any carrier-specific
payload to be transformed into a common
PickupPointModel.

Examples:

- Colissimo
- Mondial Relay
- InPost
- DPD
- GLS
- UPS

All providers must follow the same strategy.

==================================================
CORE PRINCIPLE
==================================================

Carrier payloads are never exposed outside the
provider.

The rest of the application must only work with:

PickupPointModel

Architecture:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
API

==================================================
MAPPING RESPONSIBILITY
==================================================

Provider Responsibilities

- Read provider payload
- Validate provider payload
- Transform provider fields
- Normalize provider values
- Return PickupPointModel

---

Forbidden Responsibilities

- Business rules
- FastAPI logic
- SQL queries
- Repository logic
- PostgreSQL persistence

==================================================
UNIVERSAL TARGET MODEL
==================================================

Current target:

PickupPointModel

Fields:

id

carrier_id

carrier_pickup_id

name

pickup_type

street_line_1

street_line_2

postal_code

city

state_or_region

country_code

latitude

longitude

opening_hours

active

==================================================
STANDARD FIELD MAPPING
==================================================

Universal Field

carrier_pickup_id

Purpose:

Provider identifier.

Examples:

Colissimo:
identifiant

Mondial Relay:
Num

InPost:
name

---

name

Purpose:

Human-readable pickup point name.

Examples:

Colissimo:
nom

Mondial Relay:
LgNom

InPost:
name

---

street_line_1

Purpose:

Primary address line.

Examples:

Colissimo:
adresse1

Mondial Relay:
LgAdr1

InPost:
address.line1

---

street_line_2

Purpose:

Complementary address line.

Examples:

Colissimo:
adresse2

Mondial Relay:
LgAdr2

InPost:
address.line2

---

postal_code

Purpose:

Postal code.

Examples:

Colissimo:
codePostal

Mondial Relay:
CP

InPost:
address.post_code

---

city

Purpose:

City name.

Examples:

Colissimo:
localite

Mondial Relay:
Ville

InPost:
address.city

---

country_code

Purpose:

Country ISO code.

Examples:

Colissimo:
codePays

Mondial Relay:
Pays

InPost:
address.country_code

---

latitude

Purpose:

Latitude.

Examples:

Colissimo:
coordGeolocalisationLatitude

Mondial Relay:
Latitude

InPost:
location.latitude

---

longitude

Purpose:

Longitude.

Examples:

Colissimo:
coordGeolocalisationLongitude

Mondial Relay:
Longitude

InPost:
location.longitude

==================================================
PROVIDER-SPECIFIC FIELDS
==================================================

Some carrier fields do not currently exist
inside PickupPointModel.

Examples:

distanceEnMetre

accesPersonneMobiliteReduite

parking

loanOfHandlingTool

indiceDeLocalisation

reseau

---

Rule

Ignore unsupported fields.

Do not expand PickupPointModel until business
requirements justify it.

==================================================
OPENING HOURS STRATEGY
==================================================

Different carriers expose opening hours in
different formats.

Examples:

Colissimo

horairesOuvertureLundi

horairesOuvertureMardi

...

---

Universal PUDO V1

opening_hours

Type:

string

---

Normalization Rule

All provider schedules are converted into
a single normalized string.

Example:

Mon-Fri 09:00-18:00

Future versions may introduce a structured
OpeningHours model.

==================================================
ACTIVE STATUS STRATEGY
==================================================

Universal Field

active

---

If provider indicates:

closed

holiday

disabled

inactive

unavailable

Then:

active = False

---

Otherwise:

active = True

==================================================
NORMALIZATION RULES
==================================================

Rule 1

Trim leading and trailing spaces.

---

Rule 2

Normalize country codes to ISO-3166.

Example:

FR

NL

BE

DE

---

Rule 3

Convert latitude to float.

---

Rule 4

Convert longitude to float.

---

Rule 5

Preserve provider identifier exactly as
received.

==================================================
MAPPER STRUCTURE
==================================================

Recommended structure:

providers/

├── colissimo/
│ ├── colissimo_pickup_provider.py
│ └── mapper.py
│
├── mondial_relay/
│ └── mapper.py
│
├── inpost/
│ └── mapper.py

==================================================
EXAMPLE
==================================================

Colissimo Payload

{
"identifiant": "923560",
"nom": "BUREAU DE POSTE",
"adresse1": "60 RUE CAMILLE DESMOULINS",
"codePostal": "92130",
"localite": "ISSY LES MOULINEAUX",
"codePays": "FR"
}

↓

PickupPointModel

carrier_pickup_id="923560"

name="BUREAU DE POSTE"

street_line_1="60 RUE CAMILLE DESMOULINS"

postal_code="92130"

city="ISSY LES MOULINEAUX"

country_code="FR"

==================================================
NON-GOALS
==================================================

Do not create:

ProviderRegistry

ProviderFactory

ProviderSelector

ProviderManager

---

Reason

These abstractions are not yet required.

==================================================
SUCCESS CRITERIA
==================================================

The strategy is successful when:

1. Colissimo payload maps successfully.

2. Mondial Relay payload maps successfully.

3. InPost payload maps successfully.

4. PickupProvider contract remains unchanged.

5. API Layer remains unchanged.

6. Use Cases remain unchanged.

7. Repository Layer remains unchanged.

==================================================
ARCHITECT DECISION
==================================================

The Universal PUDO Engine shall standardize
all carrier pickup point payloads through
provider-specific mappers.

The canonical internal representation shall
remain:

PickupPointModel

Carrier-specific payloads shall never be
exposed outside provider implementations.

This strategy enables future carrier additions
without architecture redesign.
