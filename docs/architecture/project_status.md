# Universal PUDO Engine - Project Status

Last Updated: 2026-07-19

---

## PROJECT VISION

Universal Pickup Point Engine

Objectif :

Créer un moteur unifié capable de rechercher,
récupérer et gérer des points relais provenant
de plusieurs transporteurs à travers une
abstraction commune.

Transporteurs cibles futurs :

- Colissimo
- Mondial Relay
- InPost
- DPD
- DHL
- Transporteurs custom

---

## CURRENT STATE

Project Status:

[MVP TECHNIQUE V1 COMPLETED]

Tests:

78 passed
0 failed
1 warning

Swagger:

Validated

Git:

Repository synchronized

---

## ARCHITECTURE

Layers implemented:

[Domain]
[Application]
[API]
[Infrastructure]
[Providers]

Pattern used:

API
↓
Use Cases
↓
Repositories
↓
PostgreSQL

Provider Layer:

PickupProvider
↓
MockPickupProvider
↓
PickupPointRepository
↓
PostgreSQL

---

## DOMAIN LAYER

Status: COMPLETE (v1)

Models:

- Carrier
- CarrierAccount
- PickupPoint

Value Objects:

- Address
- Geolocation

Enums:

- CarrierLifecycle
- CarrierCapability
- PickupType

---

## INFRASTRUCTURE LAYER

Status: COMPLETE (v1)

Database:

- PostgreSQL
- SQLAlchemy

Repositories:

- CarrierRepository
- CarrierAccountRepository
- PickupPointRepository

Features:

- CRUD carriers
- CRUD carrier accounts
- CRUD pickup points

---

## APPLICATION LAYER

Status: COMPLETE (v1)

Use Cases:

- GetCarrier
- ListCarriers
- GetPickupPoint
- ListPickupPoints
- SearchPickupPoints
- SearchPickupPointsByRadius

---

## API LAYER

Status: COMPLETE (v1)

Validated Endpoints:

GET /carriers

GET /carriers/{carrier_id}

GET /pickup-points/{carrier_id}

GET /pickup-points/details/{pickup_point_id}

GET /pickup-points/search

GET /pickup-points/search-radius

Swagger Status:

Validated manually

---

## SEARCH ENGINE

Status: COMPLETE (v1)

Supported Filters:

- carrier_id
- country_code
- postal_code
- city
- pickup_type
- active

---

## GEOGRAPHIC SEARCH

Status: COMPLETE (v1)

Features:

- Radius search
- Haversine distance calculation

Validated through:

- Pytest
- Swagger UI

---

## PROVIDER LAYER

Status: COMPLETE (v1)

Implemented:

Interface:

- PickupProvider

Providers:

- MockPickupProvider

Tests:

- test_mock_pickup_provider.py

Goal:

Allow future carrier integrations
without changing business logic.

---

## TESTING

Status: STABLE

Current Result:

78 passed
0 failed

Coverage Areas:

- Domain
- Repositories
- Use Cases
- API
- Providers

Known Warning:

StarletteDeprecationWarning
(httpx / testclient)

Decision:

Accepted for now

---

## ARCHITECTURAL DECISIONS

ADR-001

Provider abstraction introduced
before real carrier integrations.

Reason:

Prepare for future carrier providers.

Status:

Implemented

---

ADR-002

One-file-at-a-time workflow.

Process:

1. Modify file
2. py_compile
3. Targeted pytest
4. Global pytest
5. Commit
6. Push

Status:

Active

---

ADR-003

Three-error safeguard.

Rule:

After three Copilot errors on the
same subject or file:

STOP

Actions:

1. Root cause analysis
2. Inspect real project files
3. Return to last stable version
4. Apply minimal verified fix

Status:

Active

---

## KNOWN PROJECT DATA

Demo Carriers:

- carrier-colissimo
- carrier-mondial-relay
- carrier-inpost

Demo Pickup Points:

- pickup-colissimo-paris-rivoli
- pickup-mondial-relay-lyon
- pickup-inpost-defense-locker

---

## BACKLOG

Provider Layer v2

- Provider Registry
- Provider Factory
- Provider Selection

---

Search Engine v2

- distance_km in API response
- sort by distance
- pagination

---

Carrier Integrations

- Colissimo Provider
- Mondial Relay Provider
- InPost Provider

---

Documentation

- Architecture Decision Records (ADR)
- Integration examples
- Provider development guide

---

## NEXT RECOMMENDED STEP

Prepare first real carrier provider design.

Recommended target:

Colissimo Provider

Before implementation:

- identify provider contract
- identify authentication model
- identify search capabilities
- identify pickup point retrieval flow

Current project status:

READY FOR PROVIDER V2 DESIGN
