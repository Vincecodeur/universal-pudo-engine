# ADR-0003

## Title

Core Public Interfaces Strategy

## Status

Accepted

## Date

2026-07-21

---

# Context

Universal PUDO Engine is designed to support multiple implementations:

- SaaS Portal
- OMS Integrations
- WMS Integrations
- TMS Integrations
- SDKs
- CMS Plugins

A decision is required to define which interfaces are officially exposed by the Core.

The objective is to prevent future implementations from accessing internal infrastructure directly.

---

# Decision

All external consumers must interact with the Core through public contracts only.

The following interfaces are considered public and stable.

---

# Provider Contract

PickupProvider

Responsibilities:

- Search pickup points
- Retrieve pickup point details

Methods:

- search_pickup_points()
- get_pickup_point_details()

---

# Provider Resolution

ProviderFactory

Responsibilities:

- Provider discovery
- Provider resolution

Methods:

- get_provider()
- supported_carriers()

---

# Search Interfaces

SearchLivePickupPointsUseCase

Responsibilities:

- Direct carrier search

---

SearchHybridPickupPointsUseCase

Responsibilities:

- PostgreSQL-first search
- Cache freshness management
- Live provider fallback

---

# Synchronization Interface

SyncCarrierPickupPointsUseCase

Responsibilities:

- Carrier synchronization
- Cache population

---

# Consumer Rules

The following components are authorized to use public interfaces:

- Frontend Layer
- SaaS Layer
- OMS Integrations
- WMS Integrations
- TMS Integrations
- SDK Layer
- CMS Integrations

---

# Forbidden Dependencies

External consumers must not directly access:

- SQLAlchemy models
- Database sessions
- Database settings
- Carrier clients
- Carrier parsers
- Carrier mappers

These components remain internal implementation details.

---

# Consequences

Benefits:

- Stable public API
- Clear architectural boundaries
- Easier refactoring
- Improved maintainability
- Consistent integration patterns

Trade-offs:

- Additional abstraction layer
- Some infrastructure features remain inaccessible directly

---

# Result

Universal PUDO Core exposes a small, stable public surface area while preserving internal implementation freedom.
