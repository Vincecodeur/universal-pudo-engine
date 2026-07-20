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

132 / 132 PASSING

Validated Integrations:

✅ Mondial Relay (SOAP/XML)

✅ Colissimo (REST/JSON)

---

# Phase 1 - Foundations

Status: ✅ COMPLETED

---

# Phase 2 - Provider Architecture

Status: ✅ COMPLETED

---

# Phase 3 - Multi-Carrier Validation

Status: ✅ COMPLETED

---

# Phase 4 - Live Carrier Validation

Status: ✅ COMPLETED

---

# Phase 5 - Production Live Providers

Status: ✅ COMPLETED

---

# Phase 6 - Provider Factory

Status: ✅ COMPLETED

---

# Phase 7 - Carrier Synchronization Engine

Status: ✅ COMPLETED

## Phase 7.1 - Sync Engine

✅ COMPLETED

Delivered:

- SyncCarrierPickupPointsUseCase
- ProviderFactory integration
- Live synchronization
- PostgreSQL persistence

---

## Phase 7.3 - Upsert Strategy

✅ COMPLETED

Delivered:

- find_by_carrier_pickup_id()
- upsert()

Business Key:

(carrier_id, carrier_pickup_id)

---

## Phase 7.4 - Data Freshness V1

✅ COMPLETED

Delivered:

- last_synced_at
- Alembic migration
- freshness tracking
- synchronization metadata

---

## Phase 7.5 - Stale Pickup Point Detection

✅ COMPLETED

Delivered:

- find_stale_pickup_points()
- DeactivateStalePickupPointsUseCase
- stale pickup point detection
- automatic deactivation strategy

Current Synchronization Flow:

Carrier API
↓
Provider
↓
SyncCarrierPickupPointsUseCase
↓
last_synced_at
↓
Repository.upsert()
↓
PostgreSQL

Stale Detection:

PostgreSQL
↓
find_stale_pickup_points()
↓
DeactivateStalePickupPointsUseCase
↓
active = False

---

# Phase 8 - Hybrid Search

Status: NEXT PHASE

Objectives:

- PostgreSQL-first search
- Live provider fallback
- Automatic cache population
- Search latency reduction
- Foundation for cache refresh strategy

Architecture:

PostgreSQL
↓
Results Found?
├─ Yes → Return
└─ No
↓
Live Provider
↓
Synchronization
↓
Return

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
- Stale pickup point detection
- Hybrid search capability
- Stable API
- Fully documented architecture
