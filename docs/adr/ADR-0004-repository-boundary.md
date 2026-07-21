# ADR-0004 - Repository Boundary Strategy

Status: Accepted

Date: 2026-07-21

==================================================
CONTEXT
==================================================

Universal PUDO Engine has reached a stable Core milestone.

The project now includes:

- Domain Model
- Provider Contracts
- ProviderFactory
- Hybrid Search
- Synchronization Engine
- Live Carrier Validation
- FastAPI Integration
- Automated Tests

Validated carriers:

- Colissimo
- Mondial Relay
- Chronopost

The long-term vision includes:

- Universal PUDO Core
- Universal PUDO SaaS
- SDKs
- CMS Plugins
- OMS Integrations
- WMS Integrations
- TMS Integrations

A decision is required regarding repository ownership and responsibility boundaries.

==================================================
DECISION
==================================================

Universal PUDO Engine remains the Core repository.

The Core repository owns:

- carrier integrations
- provider contracts
- provider implementations
- carrier clients
- carrier parsers
- carrier mappers
- canonical models
- synchronization
- hybrid search
- provider discovery
- public Core interfaces

A separate repository will be created for:

Universal PUDO SaaS

The SaaS consumes the Core.

The Core never depends on the SaaS.

==================================================
CARRIER INTEGRATION RULE
==================================================

All new carrier integrations must be implemented exclusively inside:

universal-pudo-engine

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- InPost
- DPD
- GLS
- UPS

SaaS projects, SDKs and CMS plugins must never reimplement carrier integrations.

==================================================
PROPAGATION STRATEGY
==================================================

New carriers are propagated through Core version upgrades.

Example:

Universal PUDO Engine v1.0.0

- Colissimo
- Mondial Relay
- Chronopost

Universal PUDO Engine v1.1.0

- Colissimo
- Mondial Relay
- Chronopost
- InPost

Universal PUDO SaaS upgrades from:

v1.0.0
to
v1.1.0

Result:

InPost becomes available automatically.

The same rule applies to:

- SaaS projects
- SDKs
- CMS plugins
- OMS integrations
- WMS integrations
- TMS integrations

==================================================
CORE RESPONSIBILITIES
==================================================

The Core owns:

- PickupPointModel
- ProviderFactory
- PickupProvider
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase
- Carrier synchronization
- Carrier validation
- Provider contracts

The Core does not own:

- users
- organizations
- tenants
- authentication
- billing
- subscriptions
- admin portals
- dashboards
- credential vault UI

==================================================
SAAS RESPONSIBILITIES
==================================================

The SaaS owns:

- frontend
- authentication
- users
- organizations
- tenants
- carrier accounts
- credential management
- administration
- dashboards
- reporting

The SaaS uses the Core.

The Core never uses the SaaS.

==================================================
CMS PLUGIN RESPONSIBILITIES
==================================================

CMS plugins own:

- CMS configuration
- CMS UI
- Checkout integration
- Credential storage
- Plugin packaging

CMS plugins use the Core.

CMS plugins never reimplement carrier integrations.

==================================================
SDK RESPONSIBILITIES
==================================================

SDKs own:

- developer tooling
- wrappers
- helper functions
- typed interfaces

SDKs consume the Core.

SDKs do not implement provider logic.

==================================================
DEPENDENCY DIRECTION
==================================================

Allowed:

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

Forbidden:

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

==================================================
VERSIONING STRATEGY
==================================================

Carrier additions are released through Core versions.

Examples:

v1.0.0
Core Freeze

v1.1.0
Add InPost

v1.2.0
Add DPD

v1.3.0
Add GLS

Minor versions are preferred when public interfaces remain compatible.

Major versions are reserved for breaking changes.

Example:

v2.0.0

Breaking change in public Core interfaces.

==================================================
PUBLIC INTERFACES
==================================================

The following interfaces are considered stable:

- PickupProvider
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

Downstream systems must use these interfaces.

Downstream systems must not depend directly on:

- carrier clients
- carrier parsers
- carrier payloads
- carrier mappers
- internal database implementation details

==================================================
CONSEQUENCES
==================================================

Positive

✅ Clear Core responsibility

✅ Clear SaaS responsibility

✅ Reusable carrier integrations

✅ Easier SDK development

✅ Easier CMS plugin development

✅ Easier OMS/WMS/TMS integrations

✅ Strong architectural boundaries

✅ Single source of truth for carrier connectivity

Negative

⚠ Requires versioning discipline

⚠ Requires dependency upgrades in SaaS projects

⚠ Requires release management

==================================================
RESULT
==================================================

Universal PUDO Engine becomes the official reusable Core.

Universal PUDO SaaS will be developed in a separate repository.

All carrier integrations are implemented once inside the Core and propagated to SaaS, SDKs and plugins through versioned releases.
