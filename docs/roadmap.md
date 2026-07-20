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

139 / 139 PASSING

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

## Phase 7.3 - Upsert Strategy

✅ COMPLETED

## Phase 7.4 - Data Freshness V1

✅ COMPLETED

## Phase 7.5 - Stale Pickup Point Detection

✅ COMPLETED

Delivered:

- find_stale_pickup_points()
- DeactivateStalePickupPointsUseCase
- stale pickup point detection
- automatic deactivation strategy

---

# Phase 8 - Hybrid Search

Status: IN PROGRESS

## Phase 8.1 - Hybrid Search Core

✅ COMPLETED

Delivered:

- SearchHybridPickupPointsUseCase
- PostgreSQL-first search
- Live provider fallback
- Automatic cache population
- Automatic synchronization after live search

## Phase 8.2 - Fresh Cache Strategy

✅ COMPLETED

Delivered:

- hybrid_search_cache_ttl_days
- Repository cache freshness validation
- is_cache_fresh()
- Automatic refresh on stale cache
- Cache TTL configuration

Current Search Flow:

Search Request
↓
PostgreSQL Search
↓
Results Found?
├─ No
│ ↓
│ Live Provider
│ ↓
│ last_synced_at
│ ↓
│ upsert()
│ ↓
│ Return
│
└─ Yes
↓
is_cache_fresh()
↓
Fresh?
├─ Yes → Return Cache
└─ No
↓
Live Provider
↓
upsert()
↓
Return

---

# Phase 8.3 - FastAPI Integration

Status: NEXT PHASE

Objectives:

- Replace SearchPickupPointsUseCase
- Use SearchHybridPickupPointsUseCase in API
- Expose Hybrid Search through FastAPI

---

# Phase 8.4 - Search Metrics

Status: Planned

Features:

- cache_hit
- cache_miss
- live_refresh

---

# Phase 9 - Provider Health

Status: Planned

---

# Phase 10 - Additional Carriers

Status: Planned
