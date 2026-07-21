# Universal PUDO Engine

Carrier-agnostic Core for pickup point discovery, normalization and synchronization across multiple logistics carrier networks.

Universal PUDO Engine is a reusable backend Core designed to become the single source of truth for pickup point integrations.

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

==================================================
CURRENT STATUS
==================================================

Repository Status:

CORE FREEZE

Current Version Target:

v1.0.0

Current Test Status:

157 / 157 passing

Validated Live Carriers:

✅ Colissimo

✅ Mondial Relay

✅ Chronopost

Architecture Status:

✅ Core validated

✅ Provider architecture validated

✅ Hybrid search validated

✅ Synchronization validated

✅ Live carrier validation completed

✅ Repository boundary defined

✅ Credential ownership strategy defined

==================================================
WHY THIS PROJECT EXISTS
==================================================

Every carrier exposes different APIs.

Every carrier exposes different payload structures.

Every carrier exposes different identifiers.

Every carrier exposes different naming conventions.

Every carrier exposes different capabilities.

Examples:

Colissimo

- identifiant
- nom
- adresse

Mondial Relay

- Num
- LgNom
- Adresse

Chronopost

- identifiant
- localite
- horaires

Without a normalization layer, every consuming application must implement carrier-specific code.

Universal PUDO Engine solves this problem by providing:

- a canonical PickupPoint model
- provider abstraction
- carrier normalization
- hybrid search capabilities
- synchronization capabilities

Applications integrate once and support many carriers.

==================================================
WHAT THIS REPOSITORY IS
==================================================

Universal PUDO Engine is the reusable Core of the Universal PUDO ecosystem.

Core responsibilities:

- carrier abstraction
- provider contracts
- provider implementations
- carrier clients
- response parsers
- payload mappers
- canonical pickup point model
- live search
- hybrid search
- synchronization
- cache management
- fixture validation
- public Core interfaces
- architecture documentation

==================================================
WHAT THIS REPOSITORY IS NOT
==================================================

This repository does not contain:

- SaaS frontend
- user management
- tenant management
- billing
- subscriptions
- admin portals
- dashboards
- carrier account management UI
- credential vault UI
- CMS-specific interfaces

These responsibilities belong to downstream products.

==================================================
PRODUCT ARCHITECTURE
==================================================

Universal PUDO Ecosystem

Universal PUDO Core
│
├── Universal PUDO SaaS
├── OMS Integrations
├── WMS Integrations
├── TMS Integrations
├── CMS Plugins
└── SDKs

Dependency Direction

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

The Core never depends on:

- SaaS
- Plugins
- SDKs
- OMS
- WMS
- TMS

==================================================
CORE RESPONSIBILITIES
==================================================

The Core owns:

- PickupPointModel
- Pickup Types
- Provider Contracts
- Provider Implementations
- ProviderFactory
- Hybrid Search
- Synchronization
- Provider Discovery
- Carrier Integration Logic
- Public Core Interfaces

The Core does not own:

- Users
- Organizations
- Tenants
- Billing
- Authentication
- Frontend
- Credential Vaults

==================================================
CREDENTIAL OWNERSHIP
==================================================

Universal PUDO Core is credential agnostic.

The Core never owns:

- API Keys
- Passwords
- Tokens
- Carrier Accounts

Ownership Examples

OMS
→ OMS owns credentials

WMS
→ WMS owns credentials

TMS
→ TMS owns credentials

CMS Plugin
→ Plugin owns credentials

SaaS Portal
→ SaaS owns credentials

The Core only consumes carrier connectivity.

Reference:

ADR-0002

==================================================
REPOSITORY BOUNDARY
==================================================

All future carrier integrations belong to:

universal-pudo-engine

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- DPD
- UPS
- GLS
- InPost

SaaS projects, CMS plugins and SDKs must never reimplement carrier integrations.

Carrier propagation strategy:

New Carrier
↓
Core
↓
Release
↓
Dependency Upgrade
↓
SaaS / SDK / CMS
↓
Carrier Available

Reference:

ADR-0004

==================================================
SUPPORTED CARRIERS
==================================================

Colissimo

Protocol:
REST

Format:
JSON

Status:
✅ Live validated

---

Mondial Relay

Protocol:
SOAP

Format:
XML

Status:
✅ Live validated

---

Chronopost

Protocol:
XML

Format:
XML

Status:
✅ Live validated

==================================================
LIVE VALIDATION STATUS
==================================================

Mondial Relay

Validated:

✅ Real API response

✅ Real SOAP payload

✅ Real XML parsing

✅ PickupPointModel mapping

---

Colissimo

Validated:

✅ Real API response

✅ Real JSON payload

✅ Real PickupPointModel mapping

✅ 20 pickup points returned

Validated Example:

Carrier:
colissimo

Carrier Pickup ID:
755000

Name:
BUREAU DE POSTE PARIS LOUVRE

Postal Code:
75001

City:
PARIS

---

Chronopost

Validated:

✅ Real API response

✅ Real XML payload

✅ Real parser validation

✅ Real PickupPointModel mapping

✅ 10 pickup points returned

Validated Example:

Carrier:
chronopost

Carrier Pickup ID:
750DG

Name:
PAPH PÔLE AUTONOMIE SERVICES À LA PERSONNE

Postal Code:
92130

City:
ISSY LES MOULINEAUX

==================================================
ARCHITECTURE PATTERNS
==================================================

The Core uses:

- Hexagonal Architecture
- Domain Driven Design
- Provider Pattern
- Mapper Pattern
- Repository Pattern
- Factory Pattern
- Dependency Injection

==================================================
PUBLIC CORE INTERFACES
==================================================

The following interfaces are considered stable:

- PickupProvider
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

Consumers should use these interfaces.

Consumers should not depend directly on:

- carrier clients
- carrier payloads
- carrier parsers
- carrier mappers
- database implementation details

Reference:

ADR-0003

==================================================
CANONICAL MODEL STRATEGY
==================================================

Carrier payloads are never exposed outside providers.

Flow:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
Consumers

Benefits:

✅ Stable business logic

✅ Stable API layer

✅ Stable persistence layer

✅ Easier carrier onboarding

Reference:

ADR-0001

==================================================
CORE COMPONENTS
==================================================

Domain

- Carrier
- CarrierAccount
- CarrierCapability
- CarrierLifecycle
- PickupPoint
- PickupType
- Address
- Geolocation
- ProviderHealth

Providers

Current provider implementations:

- colissimo
- mondial_relay
- chronopost
- mock
- factory

Each provider may contain:

- client
- parser
- mapper
- live provider
- test fixtures

Use Cases

Current capabilities:

- search pickup points
- search live pickup points
- hybrid search
- synchronization
- stale detection
- provider discovery
- provider health

==================================================
INFRASTRUCTURE
==================================================

Technology Stack

- PostgreSQL
- SQLAlchemy
- Alembic
- FastAPI

==================================================
HYBRID SEARCH
==================================================

Search Request
↓
PostgreSQL Cache
↓
Cache Fresh?
├── Yes → Return Cached Result
└── No
↓
Live Provider
↓
Synchronize Cache
↓
Return Result

Benefits:

- reduced carrier traffic
- faster searches
- persistent pickup point storage
- automatic refresh strategy

==================================================
INSTALLATION
==================================================

Install

pip install -e .

Development Install

pip install -e ".[dev]"

Run Tests

pytest

==================================================
ENVIRONMENT VARIABLES
==================================================

Example variables:

DATABASE_URL

COLISSIMO_API_KEY

MONDIAL_RELAY_ENSEIGNE
MONDIAL_RELAY_PRIVATE_KEY

CHRONOPOST_ACCOUNT_NUMBER
CHRONOPOST_PASSWORD

Secrets must never be committed.

==================================================
LIVE VALIDATION SCRIPTS
==================================================

Location:

src/universal_pudo/scripts/

Available scripts:

- test_colissimo_live.py
- test_mondial_relay_live.py
- test_chronopost_live.py

Validation Flow

Carrier API
↓
Real Response
↓
Parser
↓
Mapper
↓
PickupPointModel

==================================================
TESTING
==================================================

Current Result:

157 / 157 passing

Coverage includes:

✅ Domain

✅ Use Cases

✅ Repositories

✅ Providers

✅ Parsers

✅ Mappers

✅ FastAPI

✅ Synchronization

✅ Live Provider Validation

✅ Fixture Validation

Run All Tests

pytest

==================================================
ADDING A NEW CARRIER
==================================================

All carrier integrations must be implemented in the Core.

Typical implementation:

providers/<carrier>/

- client.py
- mapper.py
- response_parser.py
- live_provider.py

tests/providers/<carrier>/

- test_client.py
- test_mapper.py
- test_response_parser.py
- test_live_provider.py
- test_real_fixture.py

Validation Flow:

Carrier API
↓
Real Response
↓
Parser
↓
Mapper
↓
PickupPointModel
↓
Tests

Once released in the Core, downstream projects obtain the new carrier through a dependency upgrade.

==================================================
FUTURE ECOSYSTEM
==================================================

Planned repositories:

universal-pudo-engine

Core

universal-pudo-saas

SaaS Platform

universal-pudo-sdk-python

Python SDK

universal-pudo-sdk-typescript

TypeScript SDK

universal-pudo-cms-woocommerce

WooCommerce Plugin

universal-pudo-cms-prestashop

PrestaShop Plugin

Carrier integrations remain implemented exclusively inside Universal PUDO Engine.

==================================================
VERSIONING STRATEGY
==================================================

v1.0.0

Core Freeze

v1.1.0

Add InPost

v1.2.0

Add DPD

v1.3.0

Add GLS

v2.0.0

Breaking changes to public interfaces

==================================================
ROADMAP
==================================================

Completed

✅ Foundations

✅ Provider Architecture

✅ Multi-carrier Validation

✅ Live Carrier Validation

✅ Provider Factory

✅ Synchronization Engine

✅ Hybrid Search

✅ FastAPI Integration

✅ Chronopost Integration

✅ Three Live Carrier Validations

✅ Credential Ownership Strategy

✅ Repository Boundary Strategy

---

Core Freeze Remaining

- Final documentation validation
- Version alignment
- Release tag creation

---

Next Repository

universal-pudo-saas

Responsibilities:

- frontend
- authentication
- organizations
- tenants
- carrier account management
- credential vault
- administration
- dashboards

The SaaS consumes the Core.

The SaaS never reimplements carrier integrations.

==================================================
DOCUMENTATION
==================================================

Key documentation:

docs/product-vision.md

docs/architecture.md

docs/roadmap.md

docs/architecture/project_status.md

docs/adr/

ADRs

ADR-0001
Provider Mapping Strategy

ADR-0002
Credential Ownership Strategy

ADR-0003
Core Public Interfaces

ADR-0004
Repository Boundary Strategy

==================================================
LICENSE
==================================================

Apache License 2.0

Copyright (c) 2026 Vincent Gueret

This project is distributed under the Apache License Version 2.0.

See LICENSE for details.
