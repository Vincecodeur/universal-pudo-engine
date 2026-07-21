# Universal PUDO Engine Architecture

## Objective

Provide a unified interface for pickup-point retrieval across multiple carrier APIs.

The application normalizes heterogeneous carrier responses into a single canonical PickupPoint model.

---

# Architectural Style

- Hexagonal Architecture
- Domain Driven Design
- Provider Pattern
- Mapper Pattern
- Factory Pattern

---

# High-Level Architecture

Client
↓
FastAPI
↓
Use Cases
↓
Provider Layer
↓
Carrier APIs

---

# Current Flow

SearchPickupPointsUseCase
↓
PickupProvider
↓
Live Provider
↓
Carrier Client
↓
Carrier API

---

# Provider Layer

## Contract

PickupProvider

Responsibilities:

- Search pickup points
- Retrieve pickup point details
- Return canonical models

---

## Implementations

### MockPickupProvider

Purpose:

- Offline development
- Testing
- Local demonstrations

---

### MondialRelayLiveProvider

Flow:

MondialRelayLiveProvider
↓
MondialRelayClient
↓
SOAP Request
↓
XML Response
↓
MondialRelayResponseParser
↓
MondialRelayMapper
↓
PickupPointModel

---

### ColissimoLiveProvider

Flow:

ColissimoLiveProvider
↓
ColissimoClient
↓
REST Request
↓
JSON Response
↓
ColissimoMapper
↓
PickupPointModel

---

# Domain Layer

Core entities:

## Carrier

Represents a carrier.

Examples:

- Mondial Relay
- Colissimo

---

## PickupPoint

Canonical pickup point representation.

Key attributes:

- carrier_id
- carrier_pickup_id
- name
- address
- postal_code
- city
- country_code
- latitude
- longitude

---

# Infrastructure Layer

## Database

Technology:

- PostgreSQL
- SQLAlchemy
- Alembic

Responsibilities:

- Persistence
- Queries
- Migrations

---

# API Layer

Technology:

- FastAPI

Endpoints currently available:

- GET /carriers
- GET /carriers/{carrier_id}
- GET /pickup-points
- GET /pickup-points/details/{pickup_point_id}
- GET /pickup-points/search

---

# Carrier Integrations

## Mondial Relay

Protocol:

SOAP

Format:

XML

Components:

- MondialRelayClient
- MondialRelayResponseParser
- MondialRelayMapper
- MondialRelayLiveProvider

Validation Status:

✅ Live validated

✅ XML fixture validated

✅ Automated tests validated

---

## Colissimo

Protocol:

REST

Format:

JSON

Components:

- ColissimoClient
- ColissimoMapper
- ColissimoLiveProvider

Validation Status:

✅ Live validated

✅ JSON fixture validated

✅ Automated tests validated

---

## Chronopost

Protocol:

XML

Components:

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostLiveProvider

Validation Status:

✅ Live validated
✅ XML fixture validated
✅ Automated tests validated

# Test Architecture

Current Status:

✅ 156 tests passing

Coverage Areas:

- Domain layer
- API layer
- Database layer
- Repository layer
- Mapper layer
- Client layer
- Live Provider layer
- Fixture validation

---

# Planned Architecture

## Provider Factory

carrier_id
↓
ProviderFactory
↓
Provider

Examples:

- colissimo → ColissimoLiveProvider
- mondial-relay → MondialRelayLiveProvider

Purpose:

- Remove manual provider selection
- Simplify carrier onboarding

---

# Quality Goals

- High test coverage
- Clear separation of concerns
- Extensible carrier architecture
- Canonical data model
- Production-ready design

# Synchronization Architecture (Planned)

The project uses a hybrid strategy.

Search Strategy:

PostgreSQL
↓
Primary Source

Carrier APIs
↓
Fallback Source

Future Synchronization Flow:

Carrier API
↓
ProviderFactory
↓
Live Provider
↓
PickupPointModel
↓
PickupPointRepository
↓
PostgreSQL

Components:

- SyncCarrierPickupPointsUseCase
- ProviderFactory
- PickupPointRepository
- Live Providers

Benefits:

- Faster searches
- Reduced carrier API usage
- Offline search capability
- Better scalability

### ChronopostLiveProvider

Flow:

ChronopostLiveProvider
↓
ChronopostClient
↓
Chronopost XML API
↓
ChronopostResponseParser
↓
ChronopostMapper
↓
PickupPointModel

# Credential Ownership Strategy

## Decision

Universal PUDO Core is credential agnostic.

The Core never stores:

- API Keys
- Passwords
- Tokens
- Carrier Accounts

The Core only consumes carrier connectivity.

---

# Credential Ownership Matrix

OMS

Owns:

- carrier credentials

Uses:

- Universal PUDO Core

---

WMS

Owns:

- carrier credentials

Uses:

- Universal PUDO Core

---

TMS

Owns:

- carrier credentials

Uses:

- Universal PUDO Core

---

CMS Plugin

Owns:

- carrier credentials

Uses:

- Universal PUDO Core

---

SaaS Portal

Owns:

- carrier credentials

Uses:

- Universal PUDO Core

---

# Architecture Layers

Universal PUDO Core

↓

Frontend Layer

↓

SaaS Layer

↓

Embedded Integration Layer

↓

SDK Layer

↓

CMS Layer

↓

Advanced Features

↓

Platform Hardening
