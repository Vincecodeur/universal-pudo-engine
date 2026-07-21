# Universal PUDO Engine Roadmap

## 1. Vision

Universal PUDO Engine is a carrier-agnostic Core engine designed to:

- normalize heterogeneous carrier APIs
- provide a canonical pickup point model
- support live carrier search
- synchronize carrier data into PostgreSQL
- support hybrid search strategies
- expose stable public Core interfaces
- enable future SaaS, SDK, CMS, OMS, WMS and TMS integrations

This roadmap now represents the Core roadmap.

The SaaS roadmap will live in a separate repository.

## 2. Current Status

Repository:

universal-pudo-engine

Repository role:

Reusable Core

Current release candidate:

v1.0.0

Current status:

CORE FREEZE CANDIDATE

Automated tests:

157 passed
1 warning
0 failed

Validated live carrier integrations:

- Colissimo
- Mondial Relay
- Chronopost

Architecture status:

Proven extensible

Repository boundary:

Core and SaaS separated

License:

Apache License 2.0

## 3. Core Completion Summary

The Core currently includes:

- domain model
- provider contracts
- carrier-specific provider implementations
- ProviderFactory
- live carrier search
- hybrid search
- synchronization engine
- stale pickup point detection
- provider health
- FastAPI integration
- real response fixtures
- automated tests
- architecture documentation
- ADR-0001
- ADR-0002
- ADR-0003
- ADR-0004

## 4. Phase 1 - Foundations

Status:

COMPLETED

Delivered:

- project structure
- Python package structure
- core domain concepts
- initial FastAPI application
- testing foundation
- documentation foundation

## 5. Phase 2 - Provider Architecture

Status:

COMPLETED

Delivered:

- PickupProvider contract
- mock provider
- provider abstraction
- provider testing strategy
- canonical pickup point model foundation

## 6. Phase 3 - Multi-Carrier Validation

Status:

COMPLETED

Delivered:

- Colissimo provider foundation
- Mondial Relay provider foundation
- carrier-specific mapping strategy
- provider-specific tests
- ADR-0001 Provider Mapping Strategy

## 7. Phase 4 - Live Carrier Validation

Status:

COMPLETED

Delivered:

- live API connectivity proof
- real carrier payload retrieval
- real payload parsing
- real payload mapping
- real fixture storage
- live validation scripts

Validated carriers:

- Mondial Relay
- Colissimo
- Chronopost

## 8. Phase 5 - Production Live Providers

Status:

COMPLETED

Delivered:

- ColissimoLiveProvider
- MondialRelayLiveProvider
- ChronopostLiveProvider
- live provider test coverage
- integration with application use cases

## 9. Phase 6 - Provider Factory

Status:

COMPLETED

Delivered:

- ProviderFactory
- provider resolution by carrier
- supported carrier discovery
- provider factory tests
- public interface alignment with ADR-0003

Result:

Use cases no longer need to manually construct carrier providers.

## 10. Phase 7 - Carrier Synchronization Engine

Status:

COMPLETED

### 10.1 Phase 7.1 - Sync Engine

Status:

COMPLETED

Delivered:

- SyncCarrierPickupPointsUseCase
- synchronization flow from provider to repository
- persistence of pickup points

### 10.2 Phase 7.3 - Upsert Strategy

Status:

COMPLETED

Delivered:

- pickup point upsert support
- update existing pickup points
- create missing pickup points
- preserve canonical identity

### 10.3 Phase 7.4 - Data Freshness V1

Status:

COMPLETED

Delivered:

- last_synced_at support
- cache freshness validation
- freshness-based search behavior

### 10.4 Phase 7.5 - Stale Pickup Point Detection

Status:

COMPLETED

Delivered:

- find_stale_pickup_points()
- DeactivateStalePickupPointsUseCase
- stale pickup point detection
- automatic deactivation strategy

## 11. Phase 8 - Hybrid Search

Status:

COMPLETED

### 11.1 Phase 8.1 - Hybrid Search Core

Status:

COMPLETED

Delivered:

- SearchHybridPickupPointsUseCase
- PostgreSQL-first search
- live provider fallback
- automatic cache population
- automatic synchronization after live search

### 11.2 Phase 8.2 - Fresh Cache Strategy

Status:

COMPLETED

Delivered:

- cache freshness validation
- repository freshness checks
- stale cache refresh
- cache TTL configuration

### 11.3 Phase 8.3 - FastAPI Integration

Status:

COMPLETED

Delivered:

- ProviderFactory dependency injection
- Colissimo provider integration
- Mondial Relay provider integration
- Chronopost provider integration
- hybrid search exposed through FastAPI
- live carrier search accessible through API routes

Current search flow:

API Request
↓
SearchHybridPickupPointsUseCase
↓
Repository Search
↓
Results Found?
↓
If no results:
ProviderFactory
↓
Live Provider
↓
Upsert
↓
Return

If results found:
Cache Fresh?
↓
If fresh:
Return Cache

If stale:
Live Provider
↓
Refresh
↓
Upsert
↓
Return

## 12. Phase 9 - Provider Health

Status:

COMPLETED

Delivered:

- ProviderHealth domain concept
- provider health use case
- provider health schema
- health router tests
- provider health tests

Purpose:

- support diagnostics
- prepare monitoring
- expose provider status
- improve operational visibility

## 13. Phase 10 - Chronopost Integration

Status:

COMPLETED

Delivered:

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostPickupProvider
- ChronopostLiveProvider
- ProviderFactory integration
- FastAPI dependency integration
- XML fixture validation
- automated tests

Validated flow:

Chronopost API
↓
ChronopostClient
↓
ChronopostResponseParser
↓
ChronopostMapper
↓
PickupPointModel
↓
ChronopostLiveProvider
↓
ProviderFactory
↓
Use Case
↓
FastAPI

Result:

Third live carrier integrated successfully without architecture refactoring.

## 14. Phase 10.3 - Live Carrier Validation

Status:

COMPLETED

Delivered:

- Mondial Relay live validation
- Colissimo live validation
- Chronopost live validation

Validated:

- real API connectivity
- real payload retrieval
- real payload parsing
- real payload mapping
- PickupPointModel generation
- fixture creation

Results:

Mondial Relay
SOAP / XML validated

Colissimo
REST / JSON validated

Chronopost
XML validated

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

## 15. Phase 11 - Universal PUDO Core Completion

Status:

COMPLETED

Delivered:

- ADR-0001 Provider Mapping Strategy
- ADR-0002 Carrier Credential Ownership Strategy
- ADR-0003 Core Public Interfaces Strategy
- ADR-0004 Repository Boundary Strategy
- Apache License 2.0 selected
- public Core interfaces documented
- Core / SaaS boundary documented
- repository responsibility clarified
- future ecosystem separated from Core roadmap
- automated test suite validated
- project structure updated
- Core Freeze documentation prepared

## 16. Core Freeze v1.0.0

Status:

READY AFTER DOCUMENTATION AND PACKAGING ALIGNMENT

Required before final tag:

- README.md aligned to v1.0.0
- docs/product-vision.md aligned to v1.0.0
- docs/architecture.md aligned to v1.0.0
- docs/roadmap.md aligned to v1.0.0
- docs/architecture/project_status.md aligned to v1.0.0
- docs/architecture/project_structure.txt aligned to current repository structure
- CHANGELOG.md aligned to v1.0.0
- pyproject.toml version set to 1.0.0
- pyproject.toml classifier set to Production/Stable
- Apache License 2.0 present
- pytest passing

Current verified pytest result:

157 passed
1 warning
0 failed

## 17. Completed Core Scope

The following topics are completed for the Core v1.0.0 milestone:

- carrier abstraction
- provider architecture
- provider factory
- canonical pickup point model
- live carrier search
- hybrid search
- synchronization
- stale pickup point detection
- provider health
- FastAPI integration
- real carrier validation
- fixture validation
- architecture documentation
- repository boundary documentation
- Apache 2.0 license decision

## 18. Removed From Core Roadmap

The following items are no longer part of this Core roadmap.

They belong to future repositories or downstream projects:

- Frontend MVP
- SaaS Layer
- Embedded Integration Layer
- SDK Layer
- CMS Adapter Layer
- Billing
- User management
- Tenant management
- Authentication
- Admin portal
- Dashboards
- Credential vault UI

## 19. Future Ecosystem

The following projects may be created separately after Core Freeze.

### 19.1 universal-pudo-saas

Repository role:

SaaS product

Responsibilities:

- frontend
- authentication
- users
- organizations
- tenants
- carrier accounts
- credential management
- admin portal
- dashboards
- reporting

The SaaS consumes the Core.

The SaaS never reimplements carrier integrations.

### 19.2 universal-pudo-sdk-python

Repository role:

Python SDK

Responsibilities:

- developer wrappers
- typed interfaces
- helper methods
- integration examples

The SDK consumes the Core.

The SDK does not implement provider logic.

### 19.3 universal-pudo-sdk-typescript

Repository role:

TypeScript SDK

Responsibilities:

- typed client interfaces
- frontend integration helpers
- developer experience

The SDK consumes the Core.

The SDK does not implement provider logic.

### 19.4 universal-pudo-cms-woocommerce

Repository role:

WooCommerce plugin

Responsibilities:

- WooCommerce checkout integration
- WooCommerce configuration
- CMS-specific credential storage
- checkout pickup point selection UI

The plugin consumes the Core.

The plugin never reimplements carrier integrations.

### 19.5 universal-pudo-cms-prestashop

Repository role:

PrestaShop plugin

Responsibilities:

- PrestaShop checkout integration
- PrestaShop configuration
- CMS-specific credential storage
- checkout pickup point selection UI

The plugin consumes the Core.

The plugin never reimplements carrier integrations.

## 20. Future Core Releases

Future carrier integrations remain inside Universal PUDO Engine.

Potential future Core versions:

v1.1.0
Add InPost

v1.2.0
Add DPD

v1.3.0
Add GLS

v2.0.0
Breaking changes to public Core interfaces, if required

## 21. Backlog

### Option B - Managed Carrier Credentials Inside The Core

Status:

Rejected for now

Reason:

Would create unnecessary coupling between the Core and carrier credential management.

Future consideration:

May be reconsidered only if a future SaaS business model requires it.

### Billing

Status:

Backlog

Reason:

Business model not yet defined.

Billing belongs to future SaaS work, not to the Core.

## 22. Definition Of Done For Core v1.0.0

Universal PUDO Engine Core v1.0.0 is considered complete when:

- ADR-0001 is present
- ADR-0002 is present
- ADR-0003 is present
- ADR-0004 is present
- Apache License 2.0 is present
- Colissimo is live validated
- Mondial Relay is live validated
- Chronopost is live validated
- 157 automated tests pass
- Core / SaaS separation is documented
- pyproject.toml is set to version 1.0.0
- README.md is aligned with Core Freeze
- product-vision.md is aligned with Core Freeze
- architecture.md is aligned with Core Freeze
- roadmap.md is aligned with Core Freeze
- project_status.md is aligned with Core Freeze
- CHANGELOG.md contains v1.0.0
- project_structure.txt reflects the real repository structure
- final release commit is created
- tag v1.0.0 is created

At that point:

# Universal PUDO Engine

Core v1.0.0 completed
