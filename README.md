# Universal PUDO Engine

Universal PUDO Engine is a carrier-agnostic pickup point abstraction platform.

The project provides a normalized model for PUDO (Pick-Up Drop-Off) locations across multiple logistics carriers and exposes a unified API regardless of carrier-specific payload structures.

The primary objective is to validate a scalable provider architecture capable of integrating multiple carriers while maintaining a stable domain model and API surface.

---

# Objectives

The project aims to:

- Normalize carrier-specific pickup point payloads.
- Expose a unified pickup point API.
- Separate business logic from carrier implementations.
- Validate a multi-carrier provider architecture.
- Create a maintainable foundation for future carrier integrations.

---

# Current Status

## Completed

### Domain Layer

- Address
- Geolocation
- PickupPoint
- PickupType
- Carrier
- CarrierAccount
- CarrierCapability
- CarrierLifecycle

### Persistence Layer

- SQLAlchemy models
- Repository pattern
- Alembic migrations
- PostgreSQL support

### Application Layer

- List carriers
- Get carrier details
- Search pickup points
- Get pickup point details

### API Layer

- FastAPI
- OpenAPI / Swagger
- Carrier endpoints
- Pickup point endpoints

### Provider Layer

Validated providers:

- Mock Provider
- Colissimo Provider
- Mondial Relay Provider

Validated mappers:

- Colissimo Mapper
- Mondial Relay Mapper

### Architecture Validation

Validated architecture:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
API

The architecture has been validated with multiple carrier formats without requiring modifications to:

- Domain Layer
- Repository Layer
- Database Layer
- API Layer

---

# Project Metrics

Current test suite:

97 passing tests

Coverage includes:

- Domain entities
- SQLAlchemy models
- Repositories
- Use cases
- API routers
- Colissimo mapper
- Colissimo provider
- Mondial Relay mapper
- Mondial Relay provider

---

# Architecture

## High-Level Architecture

```text
Carrier Payload
        ↓
Provider Mapper
        ↓
PickupPointModel
        ↓
Application Use Cases
        ↓
FastAPI
        ↓
Clients
```

## Provider Responsibility

Providers are responsible for:

- Retrieving carrier data
- Converting carrier payloads
- Exposing normalized pickup points

Business logic never consumes carrier payloads directly.

---

# Project Structure

```text
src/
└── universal_pudo/
    ├── api/
    │   ├── routers/
    │   └── schemas/
    │
    ├── application/
    │   └── use_cases/
    │
    ├── domain/
    │
    ├── infrastructure/
    │   └── database/
    │       ├── models/
    │       └── repositories/
    │
    └── providers/
        ├── base/
        ├── mock/
        ├── colissimo/
        └── mondial_relay/

tests/
├── api/
├── application/
├── domain/
├── infrastructure/
└── providers/

docs/
├── adr/
├── architecture.md
└── roadmap.md
```

---

# Provider Validation Matrix

| Provider      | Mapper | Provider | Tests |
| ------------- | ------ | -------- | ----- |
| Mock          | N/A    | ✅       | ✅    |
| Colissimo     | ✅     | ✅       | ✅    |
| Mondial Relay | ✅     | ✅       | ✅    |

---

# Accepted Architecture Decisions

## ADR-0001

Provider Mapping Strategy

Carrier payloads shall never be exposed outside provider implementations.

Canonical representation:

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

# Running Tests

Run all tests:

```bash
pytest
```

Run provider tests:

```bash
pytest tests/providers -v
```

Run a specific file:

```bash
pytest tests/providers/test_mondial_relay_provider.py -v
```

---

# Development Workflow

Recommended workflow:

```text
Business Requirement
↓
Domain Model
↓
Use Case
↓
Tests
↓
Implementation
↓
Pytest
↓
Git Commit
```

For architecture-impacting changes:

```text
Decision
↓
ADR
↓
Implementation
```

---

# Current Roadmap

## Phase 1 - Foundations

Status: Complete

- Domain Layer
- Repository Layer
- Database Layer
- API Layer
- Testing Foundation

## Phase 2 - Provider Architecture

Status: Complete

- PickupProvider contract
- Provider Mapping Strategy
- ADR-0001

## Phase 3 - Multi-Carrier Validation

Status: Complete

Validated carriers:

- Mock
- Colissimo
- Mondial Relay

Result:

PickupPointModel successfully supports multiple carrier payload formats.

## Phase 4 - First Live Provider

Status: Next

Candidate carriers:

- Mondial Relay
- Colissimo

Expected deliverables:

- Real carrier payload retrieval
- Live provider implementation
- Credential management
- Error handling
- Mapper integration

Success criteria:

```text
Real Carrier Payload
↓
Mapper
↓
PickupPointModel
```

without architecture changes.

## Phase 5 - Additional Carriers

Future candidates:

- DPD
- GLS
- UPS
- InPost

---

# Project Health

Architecture Status: Stable

Provider Layer Status: Validated

Test Status:

✅ 97 / 97 passing

Current Focus:

First live carrier integration.
