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

155 / 155 PASSING

Validated Integrations:

✅ Colissimo (REST/JSON)
✅ Mondial Relay (SOAP/XML)
✅ Chronopost (XML)

Architecture Status:

✅ Proven Extensible

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

Status: COMPLETED

## Phase 8.1 - Hybrid Search Core

✅ COMPLETED

Delivered:

- SearchHybridPickupPointsUseCase
- PostgreSQL-first search
- Live provider fallback
- Automatic cache population
- Automatic synchronization after live search

---

## Phase 8.2 - Fresh Cache Strategy

✅ COMPLETED

Delivered:

- hybrid_search_cache_ttl_days
- Repository cache freshness validation
- is_cache_fresh()
- Automatic refresh on stale cache
- Cache TTL configuration

---

## Phase 8.3 - FastAPI Integration

✅ COMPLETED

Delivered:

- Provider dependency injection
- get_provider_factory()
- ColissimoLiveProvider integration
- MondialRelayLiveProvider integration
- SearchHybridPickupPointsUseCase exposed through FastAPI
- Live carrier search accessible via API
- Hybrid Search enabled on /pickup-points/search

Current Search Flow:

API Request
↓
SearchHybridPickupPointsUseCase
↓
Repository Search
↓
Results Found?
├─ No
│ ↓
│ ProviderFactory
│ ↓
│ Live Provider
│ ↓
│ upsert()
│ ↓
│ Return
│
└─ Yes
↓
is_cache_fresh()
↓
Fresh ?
├─ Yes → Return Cache
└─ No
↓
Live Provider
↓
Refresh
↓
upsert()
↓
Return

# Phase 9 - Provider Health

Status: Planned

---

# Phase 10 - Chronopost Integration

Status: ✅ COMPLETED

Delivered:

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostPickupProvider
- ChronopostLiveProvider
- ProviderFactory integration
- FastAPI dependency integration
- XML fixture validation
- Automated tests

Result:

Third live carrier integrated successfully without architecture refactoring.

Validated Flow:

Chronopost
↓
Client
↓
Parser
↓
Mapper
↓
PickupPointModel
↓
Live Provider
↓
ProviderFactory
↓
Use Case
↓
FastAPI

# Phase 11 - Platform Hardening

Status: Planned

Objectives:

- Provider health monitoring
- Carrier diagnostics
- Retry policies
- Timeout strategies
- Extended carrier metadata
- Carrier capability registry
