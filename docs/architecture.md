# Architecture

Version: 1.0 (Draft)

---

# 1. Purpose

This document describes the architectural foundations of Universal PUDO Engine.

The objective is to provide a carrier-agnostic engine capable of searching, normalizing, resolving and later recommending pickup points (PUDO) through a unified interface.

This document focuses on architectural decisions and principles.

Detailed diagrams are maintained separately within the diagrams directory.

---

# 2. Architectural Principles

## Domain First

Business concepts drive the architecture.

Carrier-specific implementations must never become the core of the system.

The business model remains stable even when transport providers evolve.

---

## Carrier Agnostic

The engine must expose a unified interface regardless of carrier implementation details.

Consumers interact with standardized business models rather than carrier-specific APIs.

---

## Extensible

Adding a new carrier should require:

- implementing a new provider
- registering the provider

without modifying the core business engine.

---

## API Independent

The business engine must not depend on:

- REST APIs
- Web interfaces
- SDK implementations

The engine remains usable through multiple exposure layers.

---

## Integration Lifecycle Awareness

Carrier integrations evolve over time.

The architecture must support:

- ACTIVE
- DEPRECATED
- UNLISTED
- SUNSET
- REMOVED

without impacting the rest of the platform.

---

## International Ready

The initial scope targets France.

The architecture must support international expansion without redesign.

---

# 3. High-Level Architecture

The platform is organized around three major layers:

1. Domain Layer
2. Application Layer
3. Integration Layer

External consumers interact through:

- Python SDK
- REST API
- Future Portal
- Future Commerce Plugins

The core business logic remains centralized inside the engine.

Reference:

See future architecture diagrams.

---

# 4. Domain Layer

The Domain Layer contains all business concepts.

The domain must not contain:

- HTTP logic
- Database logic
- Transport provider implementations

---

## Core Business Entities

### PickupPoint

Represents a location where parcels can be delivered or collected.

---

### Carrier

Represents a transport provider.

Examples:

- Colissimo
- Mondial Relay
- Chronopost
- GLS
- UPS
- DPD France

---

### CarrierAccount

Represents customer-owned credentials used to access carrier services.

---

### Address

Represents a normalized postal address.

---

### GeoLocation

Represents geographical coordinates.

---

# 5. Pickup Point Model

PickupPoint is the primary business entity.

A PickupPoint must always expose its type.

Supported values:

- STORE
- LOCKER

Examples:

STORE:

- convenience store
- parcel shop
- merchant partner

LOCKER:

- parcel locker
- automated locker
- self-service collection point

The pickup type must always remain visible to consuming applications.

---

# 6. Application Layer

The Application Layer orchestrates business operations.

Typical use cases include:

- Search Pickup Points
- Retrieve Pickup Point Details
- Resolve Pickup Point Identity
- Recommend Pickup Points (future)

Business workflows are implemented here.

The Application Layer coordinates the Domain Layer and Provider Layer.

---

# 7. Provider Architecture

Providers act as adapters between carrier APIs and the business engine.

The engine never directly depends on a carrier API.

---

## Provider Responsibilities

Providers are responsible for:

- Authentication
- API calls
- Data transformation
- Error handling
- Response normalization

---

## Provider Independence

Each carrier integration represents a coherent API.

Example:

If a single API supports:

- France
- Belgium
- Luxembourg

a single provider may be sufficient.

Conversely:

If different countries expose different APIs, different providers are required.

Example:

- DPD France
- DPD UK

would be treated as separate integrations.

---

## Initial Providers

MVP:

- Colissimo Provider
- Mondial Relay Provider
- Chronopost Provider

V1 Expansion:

- GLS Provider
- UPS Provider
- DPD France Provider

## Provider Validation Matrix

| Carrier       | Mapper | Provider | Tests |
| ------------- | ------ | -------- | ----- |
| Mock          | N/A    | ✅       | ✅    |
| Colissimo     | ✅     | ✅       | ✅    |
| Mondial Relay | ✅     | ✅       | ✅    |

Current test count:

97 passing tests

Architecture assumption validated:

Different carrier payload formats can be normalized into PickupPointModel without modifications to:

- Domain Layer
- Repository Layer
- API Layer
- Database Layer

---

# 8. Carrier Capabilities

Not every carrier exposes the same features.

The architecture therefore allows capability declarations.

Examples:

- SEARCH_PICKUP_POINTS
- GET_PICKUP_DETAILS
- RESOLVE_PICKUP_POINT

Capabilities may evolve independently for each provider.

---

# 9. Data Strategy

The engine does not own carrier data.

Carrier data remains owned by customers and carriers.

The engine acts as a normalization and orchestration layer.

---

## Initial Strategy

Version 1:

Real-time API calls.

---

## Future Strategy

Hybrid model:

- Refreshable cache
- Real-time fallback

Refresh intervals will be defined when operational requirements become clearer.

---

# 10. Database Strategy

Primary database:

PostgreSQL

Objectives:

- persistence
- configuration
- provider settings
- future caching
- future analytics

The architecture assumes PostgreSQL from the beginning of the project.

---

# 11. Security

Carrier credentials remain owned by customers.

The platform must store credentials securely.

Provider implementations are responsible for authentication details.

The core engine must remain authentication-agnostic.

---

# 12. Future Extensions

The architecture must support future modules without requiring a redesign.

Planned future components include:

- Resolution Engine
- Recommendation Engine
- Operational Intelligence
- Web Portal
- OMS Integrations
- WMS Integrations
- CMS Plugins
- Marketplace Integrations

All future modules should reuse the existing Domain Layer.

---

# 13. Diagram Strategy

Architectural diagrams are intentionally maintained outside this document.

Reason:

- diagrams evolve faster than architecture principles
- easier maintenance
- clearer versioning

Future directory:

docs/diagrams/

Examples:

- context-diagram
- high-level-architecture
- provider-flow
- domain-model
- resolution-engine

This document references diagrams but does not contain them directly.

---

# 14. Architectural Success Criteria

The architecture is considered successful if:

- adding a carrier requires no core redesign
- new countries can be supported without rewriting the domain
- consumers do not need carrier-specific knowledge
- future portals and plugins reuse the same business engine
- the business model remains independent from transport provider implementations

The Domain Layer remains the single source of truth for business logic.
