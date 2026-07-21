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

156 / 156 PASSING

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

# Phase 10.3

Live Validation

Status:

✅ COMPLETED

Delivered:

✅ Mondial Relay live validation
✅ Colissimo live validation
✅ Chronopost live validation

Validated:

- Real API connectivity
- Real payload retrieval
- Real payload parsing
- Real payload mapping
- PickupPointModel generation
- Fixture creation

Results:

Mondial Relay
✅ SOAP/XML validated

Colissimo
✅ REST/JSON validated

Chronopost
✅ XML validated

End-to-end flow validated:

Carrier API
↓
Payload
↓
Parser / Mapper
↓
PickupPointModel
↓
Provider
↓
Factory
↓
Use Case

Result:

3 live carrier integrations validated end-to-end.

---

# Phase 11

Universal PUDO Core Completion

Goals:

- provider contracts
- adapter contracts
- architecture stabilization
- ADR creation

---

# Phase 12

Frontend MVP

Goals:

- search page
- Leaflet
- OpenStreetMap
- multi-carrier display
- point selection

---

# Phase 13

SaaS Layer

Goals:

- users
- tenants
- organizations
- carrier accounts
- carrier activation
- credentials vault
- admin portal

Important:

Credentials are managed by the SaaS Layer.

Not by the Core.

---

# Phase 14

Embedded Integration Layer

Goals:

- OMS adapter
- WMS adapter
- TMS adapter
- checkout adapter

Important:

Credentials remain owned by the host system.

---

# Phase 15

SDK Layer

Goals:

- Python SDK
- TypeScript SDK
- Public API

---

# Phase 16

CMS Adapter Layer

Goals:

- WooCommerce
- PrestaShop
- Shopify
- Magento

Important:

Credentials are managed by the CMS plugin.

Not by the Core.

---

# Phase 17

Advanced Features

- distance calculation
- recommendations
- scoring
- ranking
- advanced filtering

---

# Phase 18

Platform Hardening

- provider health
- retries
- diagnostics
- observability
- monitoring

---

# Backlog

## Option B (Not Selected)

Managed Carrier Credentials inside Universal PUDO Core

Status:
Rejected for now

Reason:

Would create unnecessary coupling between the Core and transporteur connectivity management.

---

## Billing

Status:
Backlog

Reason:

Business model not yet defined.
