# Universal PUDO Engine Roadmap

## Vision

Universal PUDO Engine is a carrier-agnostic pickup point platform designed to:

- Normalize heterogeneous carrier APIs
- Provide a canonical pickup point model
- Synchronize carrier data into a local database
- Support hybrid search strategies
- Demonstrate integration architecture best practices

Target Architecture:

Carrier APIs
↓
Providers
↓
Canonical Models
↓
Synchronization Engine
↓
PostgreSQL
↓
Search API

---

# Current Status

Current Test Count:

122 passing tests

Validated Integrations:

✅ Mondial Relay (SOAP/XML)

✅ Colissimo (REST/JSON)

Validated Components:

✅ ProviderFactory

✅ SearchLivePickupPointsUseCase

✅ MondialRelayLiveProvider

✅ ColissimoLiveProvider

---

# Phase 1 - Foundations

Status: ✅ Completed

Delivered:

- FastAPI setup
- SQLAlchemy setup
- PostgreSQL integration
- Alembic migrations
- Domain layer
- Repository layer
- API layer
- Testing infrastructure

---

# Phase 2 - Provider Architecture

Status: ✅ Completed

Delivered:

- PickupProvider contract
- Mock provider
- Provider abstraction layer
- Mapping strategy

---

# Phase 3 - Multi-Carrier Validation

Status: ✅ Completed

Delivered:

- Mondial Relay provider
- Colissimo provider
- Canonical PickupPointModel validation

---

# Phase 4 - Live Carrier Validation

Status: ✅ Completed

Delivered:

Mondial Relay:

- Live SOAP integration
- XML validation
- Response parser
- Fixture tests

Colissimo:

- Live REST integration
- JSON validation
- Fixture tests

---

# Phase 5 - Production Live Providers

Status: ✅ Completed

Delivered:

- MondialRelayLiveProvider
- ColissimoLiveProvider
- Client layer
- Mapping layer
- Provider tests

---

# Phase 6 - Provider Factory

Status: ✅ Completed

Delivered:

- ProviderFactory
- ProviderNotFoundError
- SearchLivePickupPointsUseCase
- Factory tests

Architecture:

carrier_id
↓
ProviderFactory
↓
Live Provider

---

# Phase 7 - Carrier Synchronization Engine

Status: 🔄 In Progress

Objective:

Synchronize carrier pickup points into PostgreSQL.

Target Flow:

Carrier API
↓
Live Provider
↓
PickupPointModel
↓
PickupPointRepository
↓
PostgreSQL

Phase 7.1

- SyncCarrierPickupPointsUseCase

Phase 7.2

- Synchronization strategies
- Bulk save support

Phase 7.3

- Data freshness tracking

---

# Phase 8 - Hybrid Search Strategy

Status: Planned

Architecture:

PostgreSQL First
↓
Fallback Live Search
↓
Cache Refresh

Goals:

- Offline-first search
- Reduced provider calls
- Faster response times

---

# Phase 9 - Data Freshness

Planned

Fields under consideration:

- last_sync_at
- last_seen_at
- source

---

# Phase 10 - Capability Normalization

Planned

Future canonical concepts:

- CarrierConstraint
- CarrierService
- CarrierCapability

---

# Phase 11 - Provider Health

Planned

Features:

- Health checks
- Availability monitoring
- Response time tracking

---

# Phase 12 - Additional Carriers

Planned

Candidates:

- DPD
- Chronopost
- GLS
- UPS
- InPost

---

# Phase 13 - Observability

Planned

Features:

- Metrics
- Structured logging
- Tracing

---

# Phase 14 - Release 1.0

Planned

Deliverables:

- Final documentation
- ADR review
- Architecture diagrams
- Production-ready repository

Success Criteria:

- Multiple live carriers
- Hybrid search architecture
- Synchronization engine
- Stable API
- Fully documented
