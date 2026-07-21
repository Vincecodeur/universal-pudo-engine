# Universal PUDO Engine Architecture

## 1. Objective

Universal PUDO Engine provides a unified Core interface for pickup point retrieval across multiple carrier APIs.

The application normalizes heterogeneous carrier responses into a single canonical PickupPoint model.

The Core is designed to be consumed by multiple downstream systems without requiring each system to implement carrier-specific logic.

Downstream systems may include:

- SaaS platforms
- OMS systems
- WMS systems
- TMS systems
- CMS plugins
- SDKs
- Checkout applications

This repository remains the Core repository.

It is not the SaaS product.

## 2. Current Architecture Status

Current status:

CORE FREEZE CANDIDATE

Current version target:

v1.0.0

Current automated test status:

157 passed
1 warning
0 failed

Validated live carriers:

- Colissimo
- Mondial Relay
- Chronopost

The architecture has been validated by integrating three live carriers without requiring a refactor of the domain layer, repository layer or public Core interfaces.

## 3. Architectural Style

The Core uses the following architectural patterns:

- Hexagonal Architecture
- Domain Driven Design
- Provider Pattern
- Mapper Pattern
- Repository Pattern
- Factory Pattern
- Dependency Injection

## 4. High-Level Architecture

Conceptual flow:

Consumer
↓
FastAPI or Direct Core Interface
↓
Application Use Case
↓
ProviderFactory
↓
PickupProvider
↓
Carrier Client
↓
Carrier API
↓
Carrier Parser / Mapper
↓
PickupPointModel
↓
Use Case Result
↓
Consumer

## 5. Repository Boundary

Repository:

universal-pudo-engine

Responsibility:

Reusable Core

The Core repository owns:

- carrier integrations
- provider contracts
- provider implementations
- carrier clients
- carrier response parsers
- carrier payload mappers
- canonical domain models
- synchronization
- hybrid search
- provider discovery
- public Core interfaces
- architecture documentation

The Core repository does not own:

- SaaS frontend
- authentication
- users
- organizations
- tenants
- billing
- subscriptions
- admin portals
- dashboards
- credential vault UI
- CMS-specific UI
- SDK packaging

Repository boundary decision:

ADR-0004 - Repository Boundary Strategy

## 6. Dependency Direction

Allowed dependency direction:

SaaS
↓
Core

CMS Plugin
↓
Core

SDK
↓
Core

OMS
↓
Core

WMS
↓
Core

TMS
↓
Core

Forbidden dependency direction:

Core
↓
SaaS

Core
↓
CMS Plugin

Core
↓
SDK

Core
↓
Billing

Core
↓
Authentication

Core
↓
Frontend

The Core must never depend on downstream products.

## 7. Public Core Interfaces

Defined by:

ADR-0003 - Core Public Interfaces Strategy

Stable public interfaces:

- PickupProvider
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

External consumers should use these interfaces.

External consumers must not depend directly on:

- SQLAlchemy models
- database sessions
- database settings
- carrier clients
- carrier response parsers
- carrier mappers
- native carrier payloads

## 8. Domain Layer

The domain layer contains the core business concepts of pickup point discovery.

Current domain structure:

- enums
- models
- value objects

Core domain concepts include:

- Carrier
- CarrierAccount
- CarrierCapability
- CarrierLifecycle
- PickupPoint
- PickupType
- Address
- Geolocation
- ProviderHealth

The domain layer must remain independent from carrier-specific payloads.

## 9. Canonical Pickup Point Model

Carrier payloads are normalized into the canonical internal representation:

PickupPointModel

Mapping strategy:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
Consumers

This strategy is defined by:

ADR-0001 - Provider Mapping Strategy

Benefits:

- stable business logic
- stable API layer
- stable persistence layer
- easier carrier onboarding
- no carrier-specific conditionals in application use cases
- no native carrier payloads exposed to consumers

## 10. Application Layer

The application layer contains use cases.

Implemented use cases include:

- get_carrier
- get_pickup_point
- get_provider_health
- list_carriers
- list_pickup_points
- search_pickup_points
- search_live_pickup_points
- search_hybrid_pickup_points
- sync_carrier_pickup_points
- deactivate_stale_pickup_points

The application layer orchestrates domain logic, repositories and providers.

## 11. Provider Layer

The provider layer encapsulates carrier-specific implementations.

Current provider structure:

- base
- chronopost
- colissimo
- mondial_relay
- factory
- json
- mock

### 11.1 PickupProvider Contract

The base provider contract is:

PickupProvider

Responsibilities:

- search pickup points
- retrieve pickup point details
- return canonical models

### 11.2 ProviderFactory

ProviderFactory is implemented.

Responsibilities:

- provider discovery
- provider resolution
- supported carrier listing
- decoupling consuming use cases from provider construction

Examples:

carrier_id: colissimo
resolved provider: ColissimoLiveProvider

carrier_id: mondial_relay
resolved provider: MondialRelayLiveProvider

carrier_id: chronopost
resolved provider: ChronopostLiveProvider

ProviderFactory is part of the public Core interfaces defined by ADR-0003.

## 12. Carrier Integrations

### 12.1 Colissimo

Protocol:

REST

Format:

JSON

Components:

- ColissimoClient
- ColissimoMapper
- ColissimoLiveProvider
- ColissimoPickupProvider
- response_extractor

Validation status:

Live validated

Validated flow:

Colissimo API
↓
JSON response
↓
ColissimoMapper
↓
PickupPointModel

### 12.2 Mondial Relay

Protocol:

SOAP

Format:

XML

Components:

- MondialRelayClient
- MondialRelayResponseParser
- MondialRelaySecurity
- MondialRelayMapper
- MondialRelayLiveProvider
- MondialRelayPickupProvider

Validation status:

Live validated

Validated flow:

Mondial Relay SOAP API
↓
XML response
↓
MondialRelayResponseParser
↓
MondialRelayMapper
↓
PickupPointModel

### 12.3 Chronopost

Protocol:

XML

Components:

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostPickupProvider
- ChronopostLiveProvider

Validation status:

Live validated

Validated flow:

Chronopost API
↓
XML response
↓
ChronopostResponseParser
↓
ChronopostMapper
↓
PickupPointModel

Validated output:

- real API connectivity
- real XML response
- response parser validation
- mapper validation
- PickupPointModel generation
- live provider validation

## 13. Infrastructure Layer

The infrastructure layer currently contains database implementation details.

Technology stack:

- PostgreSQL
- SQLAlchemy
- Alembic

Responsibilities:

- database session management
- SQLAlchemy models
- repositories
- migrations
- persistence
- query execution

External consumers must not depend directly on the infrastructure layer.

## 14. Database and Persistence

Database package structure:

- models
- repositories
- base.py
- session.py
- settings.py

Current database models include:

- CarrierModel
- CarrierAccountModel
- PickupPointModel

Current repositories include:

- CarrierRepository
- CarrierAccountRepository
- PickupPointRepository

Current migrations:

- initial schema
- add pickup point last synced at

## 15. Synchronization Architecture

Synchronization is implemented.

Core synchronization use case:

SyncCarrierPickupPointsUseCase

Purpose:

- retrieve pickup points from live providers
- convert provider results to canonical models
- persist pickup points into PostgreSQL
- support cache population
- support future refresh strategies

Current synchronization flow:

Carrier API
↓
Live Provider
↓
PickupPointModel
↓
SyncCarrierPickupPointsUseCase
↓
PickupPointRepository
↓
PostgreSQL

## 16. Hybrid Search Architecture

Hybrid Search is implemented.

Core hybrid search use case:

SearchHybridPickupPointsUseCase

Search strategy:

PostgreSQL cache first
↓
Cache freshness validation
↓
Return cached results if fresh
↓
Fallback to live provider if missing or stale
↓
Synchronize returned pickup points
↓
Return results to consumer

Benefits:

- faster repeated searches
- reduced carrier API usage
- persistent pickup point storage
- automatic refresh strategy
- better scalability

## 17. Provider Health

Provider Health is implemented.

Purpose:

- expose provider health status
- support diagnostics
- support operational visibility
- prepare future monitoring and observability layers

Domain concept:

ProviderHealth

Use case:

GetProviderHealthUseCase

API schema:

provider_health.py

API router:

health.py

## 18. API Layer

Technology:

FastAPI

Current API coverage includes:

- carrier routes
- pickup point routes
- health routes
- schemas
- dependencies

The API layer is one consumer of the Core.

The API layer must not become the only way to consume the Core.

Future systems may consume the Core directly through public use cases and provider contracts.

## 19. Credential Ownership Architecture

Defined by:

ADR-0002 - Carrier Credential Ownership Strategy

Decision:

The Core is credential agnostic.

The Core never owns:

- API keys
- passwords
- tokens
- carrier accounts
- credential vaults

Credential ownership examples:

OMS
owns credentials

WMS
owns credentials

TMS
owns credentials

CMS Plugin
owns credentials

SaaS Portal
owns credentials

The Core only consumes carrier connectivity.

## 20. Testing Architecture

Current automated test result:

157 passed
1 warning
0 failed

Test coverage areas:

- API routers
- API schemas
- application use cases
- domain entities
- domain enums
- domain value objects
- database models
- database repositories
- provider factory
- mock provider
- Colissimo provider
- Mondial Relay provider
- Chronopost provider
- live provider validation
- real fixture validation
- synchronization
- hybrid search
- provider health

Current test structure:

- tests/api
- tests/application
- tests/domain
- tests/infrastructure
- tests/providers
- tests/data
- tests/fixtures

## 21. Current Project Structure

The project structure is documented in:

docs/architecture/project_structure.txt

The Core repository currently contains:

- docs
- migrations
- src
- tests
- README.md
- CHANGELOG.md
- LICENSE
- pyproject.toml
- alembic.ini
- .env.example

No SaaS-specific implementation is present in the Core repository.

## 22. Core Completion Status

The Core currently includes:

- canonical model strategy
- provider mapping strategy
- credential ownership strategy
- public Core interface strategy
- repository boundary strategy
- three live carrier integrations
- provider factory
- synchronization engine
- hybrid search
- provider health
- FastAPI integration
- real fixtures
- automated tests

This supports the Core Freeze v1.0.0 milestone.

## 23. Future Architecture Direction

Future product layers must be implemented outside this repository.

Future repositories may include:

- universal-pudo-saas
- universal-pudo-sdk-python
- universal-pudo-sdk-typescript
- universal-pudo-cms-woocommerce
- universal-pudo-cms-prestashop

Future carrier integrations must remain inside the Core.

Potential future Core releases:

v1.1.0
Add InPost

v1.2.0
Add DPD

v1.3.0
Add GLS

v2.0.0
Breaking changes to public Core interfaces, if required
