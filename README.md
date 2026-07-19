# Universal PUDO Engine

Universal PUDO Engine is a carrier-agnostic engine designed to search, normalize, resolve and later recommend pickup points (PUDO) across multiple carrier networks through a unified interface.

The project focuses on interoperability, extensibility and integration simplicity.

---

# Vision

Most carrier networks expose their own APIs, authentication models, data structures and pickup point identifiers.

Universal PUDO Engine provides a common abstraction layer that allows consuming systems to interact with pickup points through a unified model instead of carrier-specific implementations.

The engine is designed to become a reusable foundation for:

- OMS
- WMS
- TMS
- E-commerce platforms
- Marketplaces
- Custom applications

---

# Main Goals

- Search pickup points
- Normalize carrier data
- Abstract carrier APIs
- Resolve pickup point identities
- Provide a reusable SDK
- Provide a reusable REST API

Future versions will introduce:

- Recommendation Engine
- Operational Intelligence
- Business Portal
- CMS Integrations

---

# Core Principles

- Domain First
- Carrier Agnostic
- API Agnostic
- Extensible Architecture
- User-Owned Carrier Accounts
- International Ready

---

# Supported Pickup Types

```text
STORE
LOCKER
```

---

# Initial Carrier Coverage

## MVP

- Colissimo Pickup
- Mondial Relay
- Chronopost Pickup

## V1 Expansion

- GLS France
- UPS Access Point
- DPD France

---

# Architecture

The engine follows a Domain First architecture.

High-level layers:

```text
Domain
↓
Application
↓
Providers
↓
Infrastructure
```

Carrier-specific implementations remain isolated behind providers.

---

# Project Documentation

## Product Documentation

- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md

## Functional Documentation

- docs/domain-model.md
- docs/database-design.md

## Development Documentation

- docs/coding-standards.md
- docs/development-guide.md

---

# Technology Stack

Planned stack:

- Python 3.14+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pytest
- Ruff

---

# Roadmap

| Version | Description            |
| ------- | ---------------------- |
| V1      | Foundation             |
| V2      | Resolution Engine      |
| V3      | Intelligence Layer     |
| V4      | Universal PUDO Portal  |
| V5      | Commerce Workflows     |
| V6      | Ecosystem Integrations |

See:

```text
docs/roadmap.md
```

for details.

---

# Repository Status

Current Status:

```text
Planning & Architecture Phase
```

The repository is currently focused on:

- Product design
- Architecture
- Domain modeling
- Database design

Implementation will start after the project foundations are finalized.

---

# Project Independence

Universal PUDO Engine is an independent project.

It is not affiliated with, endorsed by or dependent on any specific OMS, WMS, marketplace, carrier, software vendor or employer.

All examples, payloads and demonstrations are generic.

---

# Contributing

Contribution guidelines will be provided in a future release.

---

# License

License selection has not yet been finalized.

The project will likely adopt either:

- MIT
- Apache 2.0
