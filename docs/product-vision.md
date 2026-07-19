# Universal PUDO Engine

Version: 1.0 (Draft)

---

# Vision

Universal PUDO Engine is a transport-agnostic engine designed to search, normalize, resolve and later recommend pickup points (PUDO) across multiple carrier networks through a unified interface.

The engine aims to eliminate carrier-specific complexity by exposing a common domain model, SDK and API that can be consumed by OMS, WMS, OXM, TMS, marketplaces, e-commerce platforms and custom applications.

The project focuses on portability, interoperability and extensibility.

---

# Problem Statement

Carrier pickup point networks expose different APIs, authentication mechanisms, data structures and search methods.

Consequently, every consuming system must implement carrier-specific logic.

This creates several operational challenges:

- Pickup point information is fragmented across carriers.
- Marketplaces may provide pickup addresses without carrier identifiers.
- Carrier APIs evolve independently.
- New carriers require new integrations.

A normalized abstraction layer is required.

---

# Mission

Provide a reusable engine capable of:

- Searching pickup points
- Normalizing carrier data
- Abstracting carrier APIs
- Exposing a Python SDK
- Exposing a REST API
- Supporting future resolution and recommendation capabilities

The engine must remain independent from any user interface.

---

# Core Principles

## API Agnostic

Consumers must not need to understand transporteur-specific APIs.

---

## Carrier Agnostic

All carriers must expose a common domain model.

---

## Extensible

New carriers must be added without modifying the core business engine.

---

## User-Owned Connections

Carrier accounts remain owned by customers.

The engine acts as a normalization and orchestration layer above carrier APIs.

---

## Simplicity First

Dependencies requiring:

- Cloud account creation
- Billing activation
- Credit card registration
- Advanced developer knowledge

must provide a strong and measurable value.

Otherwise, simpler alternatives should be preferred.

---

## International Ready

The first implementation targets France.

The architecture must support international expansion without redesign.

---

# Scope

## Included

### Search

Search pickup points using:

- Address
- Postal code
- City
- Coordinates

---

### Normalization

Convert carrier-specific responses into a unified model.

---

### Carrier Abstraction

Expose a single interface for all supported carriers.

---

### Python SDK

Provide a reusable Python SDK.

---

### REST API

Provide a reusable HTTP API.

---

### Provider Framework

Support isolated carrier integrations.

---

### Integration Lifecycle Management

Support integration lifecycle statuses:

- ACTIVE
- DEPRECATED
- UNLISTED
- SUNSET
- REMOVED

---

# Out Of Scope

The following features are explicitly excluded from the first version.

## User Portal

Planned for a future release.

---

## Interactive Maps

Planned for a future release.

---

## CMS Plugins

Planned for future releases:

- WooCommerce
- Shopify
- Prestashop
- Magento
- Shopware
- Wix

---

## Mobile Applications

Out of scope.

---

## Recommendation Engine

Future release.

---

## Operational Intelligence

Future release.

---

# Domain Model

## PickupPoint

A PickupPoint can be:

- STORE
- LOCKER

The pickup type must always be visible and exposed to consumers.

---

# Initial Carrier Coverage

## MVP

- Colissimo Pickup
- Mondial Relay
- Chronopost Pickup

---

## V1 Expansion

- GLS France
- UPS Access Point
- DPD France

---

# Integration Strategy

An integration represents a coherent API.

A single integration may support multiple countries when:

- Authentication is shared
- Endpoints are shared
- Data models are shared

Separate APIs require separate integrations.

---

# Long-Term Vision

Universal PUDO Engine is intended to become the foundation of a larger ecosystem composed of:

- Core Engine
- Python SDK
- REST API
- Business Portal
- Commerce Connectors
- OMS Integrations
- WMS Integrations
- CMS Plugins

The engine remains the single source of business logic.
