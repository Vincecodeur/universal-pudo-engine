# Universal PUDO Engine

Universal PUDO Engine is a carrier-agnostic pickup point platform designed to normalize pickup point data from multiple logistics carriers and expose a unified API for search, synchronization, caching and monitoring.

The project demonstrates production-style integration architecture using:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Repository Pattern
- Provider Pattern
- Dependency Injection
- Automated Testing

---

# Current Status

Version: Phase 9.1

Test Coverage:

145 / 145 PASSING

Supported Live Providers:

✅ Colissimo

✅ Mondial Relay

Project Status:

✅ Active Development

✅ Fully Tested

✅ Documentation Synchronized

✅ GitHub Synchronized

---

# Key Features

## Hybrid Search Engine

The platform uses a hybrid search strategy.

Search Request

↓

PostgreSQL Cache

↓

Cache Fresh?

├─ Yes → Return Cached Results

└─ No

↓

Live Carrier API

↓

Synchronize PostgreSQL

↓

Return Results

Benefits:

- Reduced API traffic
- Faster response times
- Automatic cache refresh
- Data persistence
- Provider abstraction

---

## Multi-Carrier Architecture

Each carrier is isolated behind a provider abstraction.

Current Providers:

| Carrier       | Status  |
| ------------- | ------- |
| Colissimo     | ✅ Live |
| Mondial Relay | ✅ Live |

New carriers can be added without changing the API layer.

---

## Pickup Point Synchronization

Implemented capabilities:

✅ Synchronization Engine

✅ Upsert Strategy

✅ last_synced_at Tracking

✅ Automatic Refresh

✅ Stale Pickup Point Detection

✅ Deactivation Strategy

---

## FastAPI API

### Carriers

```http
GET /carriers/
```

List all carriers.

```http
GET /carriers/{carrier_id}
```

Get carrier details.

---

### Pickup Points

```http
GET /pickup-points/search
```

Hybrid search endpoint.

Supported filters:

- carrier_id
- country_code
- postal_code
- city
- pickup_type
- active

Example:

```http
GET /pickup-points/search?country_code=FR
```

---

```http
GET /pickup-points/details/{pickup_point_id}
```

Retrieve pickup point details.

---

```http
GET /pickup-points/search-radius
```

Radius-based search.

Example:

```http
GET /pickup-points/search-radius?latitude=48.8566&longitude=2.3522&radius_km=10
```

---

### Health Monitoring

```http
GET /health/providers
```

Provider Health API.

Current response example:

```json
[
  {
    "provider_name": "colissimo",
    "status": "UP",
    "response_time_ms": null
  },
  {
    "provider_name": "mondial-relay",
    "status": "UP",
    "response_time_ms": null
  }
]
```

---

# Architecture

```text
FastAPI
│
├── Carriers API
│
├── Pickup Points API
│   │
│   └── SearchHybridPickupPointsUseCase
│       │
│       ├── PostgreSQL Cache
│       ├── Freshness Validation
│       ├── Provider Fallback
│       └── Synchronization
│
└── Health API
    │
    └── GetProviderHealthUseCase
        │
        └── ProviderFactory
```

---

# Project Structure

```text
src/universal_pudo/

├── api/
├── application/
├── domain/
├── infrastructure/
├── providers/
└── scripts/

tests/

├── api/
├── application/
├── domain/
├── infrastructure/
└── providers/
```

---

# Database

Technology:

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations

Key entities:

- Carrier
- CarrierAccount
- PickupPoint

Pickup Point freshness management is based on:

```text
last_synced_at
```

and configurable TTL cache validation.

---

# Provider Dependency Injection

Providers are created centrally through:

```python
get_provider_factory()
```

Current implementation:

```text
ProviderFactory
├── ColissimoLiveProvider
└── MondialRelayLiveProvider
```

This architecture simplifies:

- testing
- provider replacement
- future carrier onboarding

---

# Testing

Current status:

```text
145 / 145 PASSING
```

Testing layers:

✅ Domain Tests

✅ Use Case Tests

✅ Repository Tests

✅ Provider Tests

✅ FastAPI Endpoint Tests

✅ Live Payload Validation

✅ Synchronization Tests

✅ Health Monitoring Tests

---

# Roadmap

Completed:

✅ Phase 1 - Foundations

✅ Phase 2 - Provider Architecture

✅ Phase 3 - Multi-Carrier Validation

✅ Phase 4 - Live Carrier Validation

✅ Phase 5 - Production Providers

✅ Phase 6 - Provider Factory

✅ Phase 7.1 - Synchronization Engine

✅ Phase 7.3 - Upsert Strategy

✅ Phase 7.4 - Freshness Tracking

✅ Phase 7.5 - Stale Detection

✅ Phase 8.1 - Hybrid Search Core

✅ Phase 8.2 - Fresh Cache Strategy

✅ Phase 8.3 - FastAPI Integration

✅ Phase 9.1 - Provider Health API

Next:

⏳ Phase 9.2 - Response Time Monitoring

⏳ Phase 9.3 - Real Connectivity Checks

⏳ Phase 9.4 - Health History

⏳ Phase 10 - Additional Carriers

---

# Engineering Principles

- Domain-driven structure
- Dependency Injection
- Provider abstraction
- Repository Pattern
- Explicit synchronization strategy
- Automated testing
- Documentation synchronization
- Incremental architecture evolution

## Features

- Multi-carrier pickup point search engine
- PostgreSQL persistence layer
- Hybrid Search (Database + Carrier API)
- Automatic pickup point synchronization
- Carrier lifecycle management
- Provider health monitoring

Supported carriers:

- Colissimo (Live API)
- Mondial Relay (Live API)
- Chronopost (Live API)

Architecture patterns:

- Provider Pattern
- Factory Pattern
- Repository Pattern
- Dependency Injection

---

# License

Personal portfolio and learning project.
