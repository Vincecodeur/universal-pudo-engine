# Live Provider Strategy

Status: Draft

---

## OBJECTIVE

Replace static provider data with real carrier data.

Current:

Static Data
↓
Mapper
↓
PickupPointModel

Target:

Carrier API
↓
Provider Client
↓
Mapper
↓
PickupPointModel

---

## PROVIDER CANDIDATES

1. Mondial Relay
2. Colissimo

Current Recommendation:

Mondial Relay

Reason:

- Documentation available
- Credentials available
- Point Relais API documented
- Good candidate for first live provider

---

## ARCHITECTURAL PRINCIPLES

Provider implementations must not expose:

- SOAP payloads
- HTTP responses
- Carrier-specific DTOs

Only:

PickupPointModel

may leave the provider layer.

---

## NEW COMPONENTS

Phase 4 introduces:

providers/
└── mondial_relay/
├── mapper.py
├── mondial_relay_pickup_provider.py
├── security.py
├── client.py
└── payloads.py

---

## IMPLEMENTATION ORDER

Step 1

SECURITY generation

Input:

- Enseigne
- Private Key

Output:

- SECURITY hash

Step 2

SOAP Client

Goal:

- Execute Point Relais request

Step 3

Response Parsing

Goal:

- Extract payload

Step 4

Mapper Integration

Goal:
Payload
↓
PickupPointModel

Step 5

Provider Integration

Goal:
Live Provider
↓
Use Cases

---

## SUCCESS CRITERIA

A real Mondial Relay Point Relais request returns:

PickupPointModel

without changing:

- Domain Layer
- Repository Layer
- API Layer

---

## NON GOALS

Not included:

- DPD
- GLS
- UPS
- Plugin architecture
- Registry
- Factory

These topics are postponed until the first live provider
is successfully integrated.
