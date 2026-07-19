# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog.

---

## [0.5.0] - 2026-07-19

### Added

#### Mondial Relay

- Added MondialRelayMapper
- Added MondialRelayPickupProvider
- Added Mondial Relay test fixtures

#### Provider Layer

- Validated multi-carrier mapping strategy
- Validated PickupPointModel with multiple carriers
- Confirmed carrier-agnostic architecture

#### Documentation

- Added ADR-0001 Provider Mapping Strategy
- Added provider_mapping_strategy.md

#### Tests

Added:

- test_mondial_relay_mapper.py
- test_mondial_relay_provider.py

Test suite:

88 → 97 passing tests

### Architecture Validation

Validated:

Colissimo Payload
↓
PickupPointModel

Mondial Relay Payload
↓
PickupPointModel

without modifications to:

- Domain Layer
- Repository Layer
- API Layer
- Database Layer

## [Unreleased]

### Added

#### Project Foundations

- Product vision document
- Architecture document
- Roadmap document
- Domain model document
- PostgreSQL database design document
- Coding standards document
- Development guide document
- Initial README

#### Product Vision

- Definition of Universal PUDO Engine vision
- Scope definition
- Out-of-scope definition
- Long-term product objectives

#### Architecture

- Domain First architecture
- Provider architecture
- Carrier lifecycle strategy
- Internationalization strategy

#### Domain Model

- PickupPoint entity
- Carrier entity
- CarrierAccount entity
- Address value object
- GeoLocation value object

#### Database Design

- PostgreSQL-first strategy
- Carrier schema
- Carrier account schema
- Pickup point schema
- Index strategy

#### Governance

- Coding standards
- Development workflow
- Documentation workflow
- Release workflow

---

## [Planned]

### V1 Foundation

- Python project bootstrap
- pyproject.toml
- PostgreSQL integration
- SQLAlchemy models
- Alembic migrations
- Provider framework
- Colissimo provider
- Mondial Relay provider
- Chronopost provider
- SDK
- REST API

### V2 Resolution Engine

- Pickup point resolution
- Confidence scoring

### V3 Intelligence Layer

- Recommendation engine
- Alternative pickup suggestions

### V4 Universal PUDO Portal

- Web interface
- Manual resolution tools

### V5 Commerce Workflows

- Home delivery conversion
- OMS/WMS workflows

### V6 Ecosystem Integrations

- WooCommerce
- Shopify
- Prestashop
- Magento
- Shopware
- Wix
