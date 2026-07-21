# Universal PUDO Engine Product Vision

## 1. Vision

Universal PUDO Engine is a carrier-agnostic Core engine for pickup point discovery, normalization and synchronization across multiple logistics carrier networks.

The objective of the project is to provide a reusable backend Core that allows different applications to search, normalize and consume pickup points without implementing carrier-specific logic in each consuming system.

Universal PUDO Engine is designed to become the single source of truth for pickup point integrations.

The Core can be consumed by:

- SaaS platforms
- OMS systems
- WMS systems
- TMS systems
- Checkout applications
- CMS plugins
- SDKs

This repository is the Core repository.

It is not the SaaS product.

The SaaS product will live in a separate repository.

## 2. Project Status

Current repository status:

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

Current maturity:

Production-ready architectural Core demonstration

## 3. Why This Project Exists

Each pickup point carrier exposes different APIs, protocols, data formats and naming conventions.

Examples:

Colissimo exposes REST / JSON payloads.

Mondial Relay exposes SOAP / XML payloads.

Chronopost exposes XML payloads.

Without a normalization layer, every consuming application would need to implement carrier-specific logic for:

- API calls
- authentication parameters
- response parsing
- error handling
- payload mapping
- pickup point normalization
- supported service options
- provider-specific edge cases

Universal PUDO Engine solves this by providing:

- a canonical PickupPoint model
- provider contracts
- provider implementations
- carrier-specific clients
- carrier-specific parsers
- carrier-specific mappers
- live search use cases
- hybrid search use cases
- synchronization use cases
- provider discovery through ProviderFactory
- a stable public Core interface

Applications integrate once with the Core and can progressively support multiple carriers.

## 4. Core Principles

### 4.1 Carrier Agnostic Core

The Core must not expose native carrier payloads to consuming applications.

All carrier payloads must be converted into the canonical internal representation:

PickupPointModel

The canonical mapping strategy is documented in:

ADR-0001 - Provider Mapping Strategy

Canonical flow:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
Consumers

### 4.2 Build Once, Consume Anywhere

Carrier integrations must be implemented once inside the Core.

Downstream systems must consume the Core instead of reimplementing carrier integrations.

Downstream systems include:

- SaaS platforms
- OMS systems
- WMS systems
- TMS systems
- CMS plugins
- SDKs
- Checkout applications

### 4.3 Credential Agnostic Core

The Core must never own carrier credentials.

The Core does not own:

- API keys
- passwords
- tokens
- carrier accounts
- credential vaults
- user credential management UIs

Credential ownership is external to the Core and depends on the consuming implementation.

Credential ownership strategy is documented in:

ADR-0002 - Carrier Credential Ownership Strategy

Examples:

OMS
owns carrier credentials

WMS
owns carrier credentials

TMS
owns carrier credentials

CMS plugin
owns carrier credentials

SaaS portal
owns carrier credentials

The Core only consumes carrier connectivity.

### 4.4 Stable Public Interfaces

External consumers must interact with the Core through official public interfaces.

Public interfaces are documented in:

ADR-0003 - Core Public Interfaces Strategy

Stable public interfaces:

- PickupProvider
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

Consumers must not depend directly on:

- SQLAlchemy models
- database sessions
- database settings
- carrier clients
- carrier parsers
- carrier mappers
- native carrier payloads

### 4.5 Repository Boundary

Universal PUDO Engine remains the Core repository.

Universal PUDO SaaS will be developed in a separate repository.

Repository boundary strategy is documented in:

ADR-0004 - Repository Boundary Strategy

All future carrier integrations must be implemented inside:

universal-pudo-engine

The following repositories or products must never reimplement carrier integrations:

- universal-pudo-saas
- SDKs
- CMS plugins
- OMS integrations
- WMS integrations
- TMS integrations

Carrier propagation rule:

New Carrier
↓
Core implementation
↓
Core release
↓
Dependency upgrade
↓
SaaS / SDK / CMS / OMS / WMS / TMS
↓
Carrier available

## 5. Product Architecture

The Universal PUDO ecosystem is composed of several independent layers.

### 5.1 Universal PUDO Core

Repository:

universal-pudo-engine

Responsibilities:

- canonical pickup point model
- provider contracts
- provider implementations
- carrier clients
- carrier response parsers
- carrier payload mappers
- live search
- hybrid search
- synchronization
- provider discovery
- provider health
- fixture validation
- FastAPI integration
- architecture documentation
- public Core interfaces

The Core owns carrier integration logic.

The Core does not own:

- users
- organizations
- tenants
- authentication
- billing
- subscriptions
- SaaS frontend
- admin portal
- dashboards
- credential vault UI

### 5.2 Universal PUDO SaaS

Future repository:

universal-pudo-saas

The SaaS will consume the Core.

The SaaS will own:

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
- billing, if a business model requires it later

The SaaS must not reimplement carrier integrations.

### 5.3 OMS / WMS / TMS Integration Layers

OMS, WMS and TMS systems may consume the Core directly or through adapters.

The host system remains responsible for:

- authentication
- user access
- business configuration
- carrier credentials
- operational workflows

The Core remains responsible for:

- carrier abstraction
- pickup point search
- pickup point normalization
- provider execution

### 5.4 CMS Plugins

CMS plugins may consume the Core to expose pickup point selection during checkout.

CMS plugins own:

- CMS-specific UI
- CMS configuration
- checkout integration
- credential storage
- plugin packaging

CMS plugins must not reimplement carrier integrations.

### 5.5 SDKs

SDKs may be created later to simplify developer adoption.

SDKs own:

- wrappers
- typed interfaces
- helper functions
- developer experience

SDKs consume the Core.

SDKs do not implement provider logic.

## 6. Current Architecture

Implemented architectural patterns:

- Hexagonal Architecture
- Domain Driven Design
- Provider Pattern
- Mapper Pattern
- Repository Pattern
- Factory Pattern
- Dependency Injection

Current technical stack:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- pytest

## 7. Validated Carriers

### 7.1 Colissimo

Protocol:

REST

Format:

JSON

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

### 7.2 Mondial Relay

Protocol:

SOAP

Format:

XML

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

### 7.3 Chronopost

Protocol:

XML

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

## 8. Current Quality Status

Automated tests:

157 passed
1 warning
0 failed

Validated test areas:

- API routers
- API schemas
- application use cases
- domain models
- domain value objects
- database models
- database repositories
- provider factory
- mock provider
- Colissimo provider
- Mondial Relay provider
- Chronopost provider
- live provider mapping
- real fixture validation
- synchronization
- hybrid search
- provider health

The successful integration of Chronopost after Colissimo and Mondial Relay validates that the Core can onboard a third carrier without architectural refactoring.

## 9. Core Freeze Criteria

The Core can be considered ready for v1.0.0 when the following criteria are true:

- ADR-0001 accepted
- ADR-0002 accepted
- ADR-0003 accepted
- ADR-0004 accepted
- Apache License 2.0 selected
- Colissimo live validated
- Mondial Relay live validated
- Chronopost live validated
- ProviderFactory implemented
- Hybrid Search implemented
- Synchronization implemented
- Provider Health implemented
- FastAPI integration implemented
- Repository boundary documented
- Core / SaaS separation documented
- 157 automated tests passing
- pyproject.toml version aligned to 1.0.0
- README aligned to v1.0.0
- CHANGELOG aligned to v1.0.0
- project_status.md aligned to v1.0.0
- roadmap.md aligned to Core Freeze

## 10. Out Of Scope For The Core

The following topics are out of scope for the Core repository:

- SaaS frontend
- user management
- tenant management
- organization management
- billing
- Stripe
- subscriptions
- invoices
- admin portal
- dashboards
- credential vault UI
- CMS-specific checkout UI
- SDK packaging

These topics belong to future repositories or downstream products.

## 11. Future Ecosystem

Planned future repositories may include:

- universal-pudo-saas
- universal-pudo-sdk-python
- universal-pudo-sdk-typescript
- universal-pudo-cms-woocommerce
- universal-pudo-cms-prestashop

Future carrier integrations must continue to be implemented in the Core.

Potential future carrier roadmap:

v1.1.0
Add InPost

v1.2.0
Add DPD

v1.3.0
Add GLS

v2.0.0
Breaking changes to public Core interfaces, if required

## 12. Final Goal

The final goal of Universal PUDO Engine is to provide a clean, reusable and extensible Core for pickup point discovery and normalization.

The Core must remain independent from any specific SaaS implementation, CMS plugin, SDK, OMS, WMS or TMS.

The Core must be stable enough to support future products through versioned releases.

Universal PUDO Engine v1.0.0 represents the Core Freeze milestone.
