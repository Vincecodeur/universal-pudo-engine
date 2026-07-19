# Universal PUDO Engine

Universal PUDO Engine is a carrier-agnostic pickup point integration platform.

The project provides a normalized model for pickup point (PUDO) data across multiple logistics carriers while preserving a stable application, database, and API architecture.

Its primary objective is to prove that heterogeneous carrier payloads can be transformed into a single canonical model without impacting the rest of the system.

---

# Project Goals

The project aims to:

- Normalize carrier-specific pickup point payloads.
- Create a reusable provider architecture.
- Validate a carrier-agnostic domain model.
- Support multiple carrier integrations without changing core application components.
- Build a production-grade foundation for future carrier integrations.

---

# Current Status

Latest verified test result:

```text
104 passed
1 warning
```

Current validation level:

```text
✅ Multi-carrier architecture validated
✅ First live carrier integration validated
✅ Real payload mapping validated
```

---

# Architecture Overview

High-level architecture:

```text
Carrier Payload
        ↓
Provider Client
        ↓
Response Parser
        ↓
Dictionary Payload
        ↓
Provider Mapper
        ↓
PickupPointModel
        ↓
Use Cases
        ↓
API
```

The architecture ensures that carrier-specific payload formats never reach the application layer.

Only normalized models leave the provider layer.

---

# Supported Providers

## Mock Provider

Status:

```text
Validated
```

Capabilities:

- Static pickup point generation
- Automated tests

---

## Colissimo

Status:

```text
Validated (simulated provider)
```

Capabilities:

- Payload mapping
- Provider abstraction
- Automated tests

---

## Mondial Relay

Status:

```text
Live SOAP Proof Of Concept Validated
```

Capabilities:

- SECURITY hash generation
- SOAP envelope generation
- SOAP response parsing
- Real pickup point search
- Real payload mapping
- Automated tests

Validated live flow:

```text
Mondial Relay SOAP
↓
HTTP
↓
XML Response
↓
ResponseParser
↓
dict
↓
MondialRelayMapper
↓
PickupPointModel
```

---

# Project Metrics

Current automated test suite:

```text
104 passing tests
```

Coverage includes:

- Domain layer
- SQLAlchemy models
- Repository layer
- Use cases
- API routers
- Mock provider
- Colissimo provider
- Colissimo mapper
- Mondial Relay provider
- Mondial Relay mapper
- Mondial Relay security
- Mondial Relay client
- Mondial Relay response parser
- Live payload mapping

---

# Live Integration Validation

The first live carrier proof of concept has been successfully validated using Mondial Relay.

Validated request:

```text
WSI4_PointRelais_Recherche
```

Validated components:

```text
✅ Endpoint Connectivity
✅ SECURITY Generation
✅ SOAP Request Generation
✅ HTTP Communication
✅ XML Retrieval
✅ Response Parsing
✅ Payload Mapping
✅ PickupPointModel Creation
```

Example live pickup point:

```text
Carrier ID:

mondial-relay

Pickup Point ID:

020243

City:

ISSY LES MOULINEAUX

Postal Code:

92130

Coordinates:

48.82619
2.27988
```

---

# Project Structure

```text
src/
└── universal_pudo/
    │
    ├── api/
    │
    ├── application/
    │
    ├── domain/
    │
    ├── infrastructure/
    │
    ├── providers/
    │   ├── base/
    │   ├── mock/
    │   ├── colissimo/
    │   └── mondial_relay/
    │
    ├── scripts/
    │   └── test_mondial_relay_live.py
    │
    └── main.py

tests/
├── api/
├── application/
├── domain/
├── infrastructure/
├── data/
└── providers/
```

---

# Provider Validation Matrix

| Provider      | Mapper | Provider | Live Connectivity | Tests |
| ------------- | ------ | -------- | ----------------- | ----- |
| Mock          | N/A    | ✅       | N/A               | ✅    |
| Colissimo     | ✅     | ✅       | ❌                | ✅    |
| Mondial Relay | ✅     | ✅       | ✅                | ✅    |

---

# Accepted Architecture Decisions

## ADR-0001

Provider Mapping Strategy

Decision:

Carrier payloads must never be exposed outside provider implementations.

Canonical model:

```text
PickupPointModel
```

Flow:

```text
Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
API
```

---

# Development Workflow

Recommended workflow:

```text
Business Requirement
↓
Architecture
↓
ADR (if needed)
↓
Tests
↓
Implementation
↓
Pytest
↓
Documentation
↓
Git Commit
```

---

# Current Roadmap

## Phase 1 - Foundations

Status:

```text
Completed
```

Completed:

- Domain Layer
- Database Layer
- Repository Layer
- FastAPI API
- Automated Tests

---

## Phase 2 - Provider Architecture

Status:

```text
Completed
```

Completed:

- PickupProvider Contract
- Provider Mapping Strategy
- ADR-0001

---

## Phase 3 - Multi-Carrier Validation

Status:

```text
Completed
```

Validated:

- Mock
- Colissimo
- Mondial Relay

Result:

```text
PickupPointModel supports multiple carrier payload formats.
```

---

## Phase 4 - First Live Carrier Integration

Status:

```text
Validated
```

Carrier:

```text
Mondial Relay
```

Completed:

- SECURITY
- SOAP Client Foundation
- SOAP Envelope Builder
- Response Parser
- Live Request Validation
- Live Payload Mapping

Validated flow:

```text
Mondial Relay SOAP
↓
HTTP
↓
XML Response
↓
ResponseParser
↓
dict
↓
PickupPointModel
```

---

## Phase 5 - Production Ready Live Provider

Status:

```text
Not Started
```

Planned work:

- Environment-variable based credentials
- XML fixtures
- Retry strategy
- Error mapping
- Opening hours normalization
- FastAPI integration
- Use Case integration

---

## Phase 6 - Additional Carriers

Future candidates:

- Colissimo Live
- DPD
- GLS
- UPS
- InPost
- Chronopost

---

# Current Known Limitations

The live Mondial Relay integration is currently validated through a dedicated script and not yet exposed through application use cases or API endpoints.

Outstanding work:

- Store XML fixtures
- Improve SOAP error handling
- Normalize opening hours
- Normalize pickup point types
- Externalize credentials
- Integrate live providers into application services

---

# Project Health

Architecture Status:

```text
Stable
```

Provider Architecture:

```text
Validated
```

Live Connectivity:

```text
Validated
```

Technical Debt:

```text
Low
```

Current Recommendation:

```text
Finalize documentation
↓
Commit milestone
↓
Start production-ready live provider phase
```
