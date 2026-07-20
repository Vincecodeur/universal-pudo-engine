# Universal PUDO Engine Roadmap

## Vision

Universal PUDO Engine is a carrier-agnostic pickup point platform designed to:

- Normalize heterogeneous carrier APIs
- Provide a canonical pickup point model
- Synchronize carrier data into PostgreSQL
- Support hybrid search strategies
- Demonstrate integration architecture best practices

---

# Current Status

Current Test Count:

128 / 128 PASSING

Validated Integrations:

✅ Mondial Relay (SOAP/XML)

✅ Colissimo (REST/JSON)

---

# Phase 1 - Foundations

Status: ✅ COMPLETED

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

Status: ✅ COMPLETED

Delivered:

- PickupProvider contract
- Mock provider
- Provider abstraction layer
- Mapping strategy

---

# Phase 3 - Multi-Carrier Validation

Status: ✅ COMPLETED

Delivered:

- Canonical PickupPointModel
- Mondial Relay provider
- Colissimo provider
- Multi-provider validation

---

# Phase 4 - Live Carrier Validation

Status: ✅ COMPLETED

Delivered:

- Mondial Relay live SOAP validation
- Colissimo live REST validation
- Real fixture generation
- Payload validation

---

# Phase 5 - Production Live Providers

Status: ✅ COMPLETED

Delivered:

- MondialRelayLiveProvider
- ColissimoLiveProvider
- Provider tests
- Client abstraction

---

# Phase 6 - Provider Factory

Status: ✅ COMPLETED

Delivered:

- ProviderFactory
- ProviderNotFoundError
- SearchLivePickupPointsUseCase

Architecture:

carrier_id
↓
ProviderFactory
↓
Live Provider

---

# Phase 7 - Carrier Synchronization Engine

Status: ✅ COMPLETED

## Phase 7.1 - Sync Engine

Delivered:

✅ SyncCarrierPickupPointsUseCase

Features:

- Provider resolution through ProviderFactory
- Live carrier synchronization
- Pickup point persistence
- Synchronization statistics

---

## Phase 7.3 - Upsert Strategy

Delivered:

✅ find_by_carrier_pickup_id()

✅ upsert()

Business Key:

(carrier_id, carrier_pickup_id)

Benefits:

- Repeatable synchronization
- Duplicate prevention
- Existing pickup point updates
- Stable synchronization behavior

---

## Phase 7.4 - Data Freshness V1

Delivered:

✅ last_synced_at

✅ Alembic migration

✅ Model update

✅ Repository support

✅ Sync engine integration

Benefits:

- Synchronization traceability
- Future stale pickup point detection
- Future cache strategy support
- Foundation for hybrid search

Current Synchronization Flow:

Carrier API
↓
Provider
↓
SyncCarrierPickupPointsUseCase
↓
last_synced_at update
↓
Repository.upsert()
↓
PostgreSQL

---

# Phase 7.5 - Stale Pickup Point Detection

Status: Planned

Objectives:

- Detect stale pickup points
- Identify outdated synchronized data
- Prepare automatic cleanup strategy

---

# Phase 8 - Hybrid Search

Status: Planned

Architecture:

PostgreSQL First
↓
Fallback Live Search
↓
Synchronization Refresh

Goals:

- Offline-first search
- Reduced provider calls
- Faster response times

---

# Phase 9 - Provider Health

Status: Planned

Features:

- Health checks
- Availability monitoring
- Response time tracking

---

# Phase 10 - Additional Carriers

Status: Planned

Candidates:

- DPD
- Chronopost
- GLS
- UPS
- InPost

---

# Success Criteria

- Multi-carrier support
- Live carrier integrations
- Repeatable synchronization
- Data freshness tracking
- Hybrid search capability
- Stable API
- Fully documented architecture
