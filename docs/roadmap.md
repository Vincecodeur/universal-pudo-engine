# Roadmap

Version: 1.0 (Draft)

---

# 1. Purpose

This roadmap defines the evolution of Universal PUDO Engine from the initial foundation through future ecosystem integrations.

Each version introduces a coherent set of capabilities while preserving architectural stability.

The roadmap intentionally separates:

- Business capabilities
- Technical capabilities
- Future product extensions

to avoid feature creep.

---

# 2. Roadmap Overview

| Version | Name                   | Status  |
| ------- | ---------------------- | ------- |
| V1      | Foundation             | Planned |
| V2      | Resolution Engine      | Planned |
| V3      | Intelligence Layer     | Planned |
| V4      | Universal PUDO Portal  | Planned |
| V5      | Commerce Workflows     | Planned |
| V6      | Ecosystem Integrations | Planned |

---

# 3. V1 - Foundation

## Goal

Build a reusable carrier-agnostic PUDO engine.

---

## Business Objectives

Provide a unified way to:

- Search pickup points
- Normalize carrier data
- Abstract carrier APIs

without requiring carrier-specific knowledge.

---

## Technical Objectives

Deliver:

- Domain Model
- Provider Framework
- Python SDK
- REST API
- PostgreSQL Persistence
- Automated Tests

---

## Features

### Pickup Point Search

Search via:

- Address
- Postal Code
- City
- Coordinates

---

### Unified Domain Model

Introduce:

- PickupPoint
- Carrier
- CarrierAccount
- Address
- GeoLocation

---

### Pickup Types

Supported values:

- STORE
- LOCKER

---

### Provider Framework

Support pluggable carrier integrations.

---

### Carrier Lifecycle

Support:

- ACTIVE
- DEPRECATED
- UNLISTED
- SUNSET
- REMOVED

---

### Python SDK

Reusable client library.

---

### REST API

HTTP access layer.

---

### Automated Testing

Unit tests.

Integration tests.

Provider tests.

---

## Carrier Coverage

### MVP

- Colissimo Pickup
- Mondial Relay
- Chronopost Pickup

---

### V1 Expansion

- GLS France
- UPS Access Point
- DPD France

---

## Out of Scope

- Portal
- Maps
- Recommendation Engine
- Resolution Engine
- CMS Plugins

---

## Success Criteria

An external system can:

- Search pickup points
- Use multiple carriers
- Consume a unified model

without carrier-specific implementation.

---

# 4. V2 - Resolution Engine

## Goal

Resolve carrier pickup identifiers from marketplace or customer data.

---

## Business Problem

Some marketplaces provide pickup point addresses without carrier pickup IDs.

Operational teams must manually identify the corresponding pickup point.

---

## Features

### Address Resolution

Input:

- Name
- Address
- Postal Code
- City

Output:

- Carrier
- Pickup ID
- Confidence Score

---

### Matching Engine

Support:

- Typo tolerance
- Address normalization
- Case normalization
- Accent normalization

---

### Confidence Scoring

Return confidence levels for each result.

---

## Out of Scope

- Recommendations
- Operational intelligence

---

## Success Criteria

The engine can identify carrier pickup point IDs from address information with confidence scoring.

---

# 5. V3 - Intelligence Layer

## Goal

Introduce decision support capabilities.

---

## Features

### Recommendation Engine

Rank pickup points.

---

### Pickup Point Scoring

Possible criteria:

- Distance
- Pickup type
- Availability
- Carrier preferences

---

### Closed Pickup Detection

Identify pickup points that are temporarily unavailable when supported by carrier APIs.

---

### Alternative Suggestions

Recommend replacement pickup points.

---

### Caching Layer

Introduce refreshable cache mechanisms.

---

## Success Criteria

The engine provides recommendations instead of simple search results.

---

# 6. V4 - Universal PUDO Portal

## Goal

Provide direct access for non-technical users.

---

## Features

### Pickup Search Interface

Manual search.

---

### Resolution Interface

Manual pickup point resolution.

---

### Carrier Account Management

Transport account configuration.

---

### Carrier Administration

Carrier lifecycle visibility.

---

### Map Support (Evaluation Phase)

Technologies to evaluate:

- OpenStreetMap
- Leaflet
- Mapbox
- Google Maps

Selection to be based on:

- Cost
- Simplicity
- User onboarding effort

---

## Success Criteria

Business users can use the platform without technical knowledge.

---

# 7. V5 - Commerce Workflows

## Goal

Integrate PUDO intelligence into real-world e-commerce scenarios.

---

## Features

### Home Delivery Conversion

Convert:

Home Delivery

to

Pickup Point Delivery

when appropriate.

---

### OMS Workflows

Support OMS integrations.

---

### WMS Workflows

Support WMS integrations.

---

### Marketplace Workflows

Support marketplace order processing.

---

### Pickup Recovery Workflows

Identify alternatives when a selected pickup point becomes unavailable.

---

## Success Criteria

The platform actively supports operational business workflows.

---

# 8. V6 - Ecosystem Integrations

## Goal

Bring Universal PUDO Engine directly into commerce platforms.

---

## Planned Integrations

### WooCommerce

Plugin.

---

### Prestashop

Module.

---

### Shopify

Application.

---

### Magento / Adobe Commerce

Extension.

---

### Shopware

Extension.

---

### Wix

Integration.

---

## Future Candidates

- OMS Connectors
- WMS Connectors
- ERP Connectors
- Marketplace Connectors

---

## Success Criteria

Platforms can consume Universal PUDO Engine without custom development.

---

# 9. Technical Roadmap

## Database

V1:

PostgreSQL

---

## Authentication

Progressive support for carrier authentication methods.

Examples:

- API Key
- OAuth2
- Basic Authentication

---

## Caching

Introduced in V3.

Refresh strategies to be defined according to carrier constraints.

---

## Monitoring

Future capability.

Out of initial scope.

---

# 10. Non-Goals

The project will not become:

- A transport management system
- A warehouse management system
- An OMS
- A marketplace
- A delivery platform

Universal PUDO Engine remains a specialized pickup point abstraction platform.

---

# 11. Roadmap Governance

New features must satisfy at least one of the following:

- Improve carrier abstraction
- Improve pickup point discovery
- Improve pickup point resolution
- Improve operational efficiency
- Improve ecosystem interoperability

Features failing these criteria should be rejected to prevent feature creep.
