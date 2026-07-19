# Universal PUDO Engine Roadmap

## Vision

Universal PUDO Engine is a carrier-agnostic pickup point engine designed to normalize multiple carrier APIs into a single canonical model.

The project demonstrates:

- Hexagonal Architecture
- Domain Driven Design
- Multi-carrier integrations
- SOAP/XML integration
- REST/JSON integration
- Canonical data modeling
- Test-driven development
- Provider abstraction patterns

---

# Current Status

## Tests

✅ 117 automated tests passing

## Live Carriers

✅ Mondial Relay (SOAP/XML)

✅ Colissimo (REST/JSON)

---

# Phase 1 - Foundations

Status: ✅ Completed

Goals:

- Repository setup
- Python project structure
- FastAPI setup
- SQLAlchemy setup
- Alembic setup
- PostgreSQL integration
- Test infrastructure

Deliverables:

- FastAPI application
- Database layer
- Domain layer
- Testing framework

---

# Phase 2 - Provider Architecture

Status: ✅ Completed

Goals:

- Create canonical PickupProvider contract
- Create provider abstraction layer
- Create mock provider

Deliverables:

- PickupProvider
- MockPickupProvider
- Provider test suite

---

# Phase 3 - Multi-Carrier Validation

Status: ✅ Completed

Goals:

- Validate carrier abstraction
- Introduce real carrier-specific models

Deliverables:

- Carrier support structure
- Mapper layer
- Canonical PickupPointModel

---

# Phase 4 - Live Carrier Validation

Status: ✅ Completed

Goals:

- Validate real carrier APIs
- Validate payload mapping
- Create reusable fixtures

Deliverables:

## Mondial Relay

- SOAP integration
- XML fixtures
- ResponseParser
- Mapper

## Colissimo

- REST integration
- JSON fixtures
- Mapper

---

# Phase 5 - Production Live Providers

Status: ✅ Completed

Goals:

- Integrate live carrier APIs into Provider Layer

Deliverables:

## Mondial Relay

- MondialRelayClient
- MondialRelayLiveProvider

## Colissimo

- ColissimoClient
- ColissimoLiveProvider

Results:

- Provider abstraction validated
- Two live provider implementations
- 117 passing tests

---

# Phase 6 - Provider Factory

Status: 🔄 Planned

Goals:

- Centralize provider resolution
- Remove manual provider selection
- Prepare automatic carrier routing

Deliverables:

- ProviderFactory
- ProviderNotFoundError
- Provider Registry
- Provider Factory Test Suite

Architecture Target:

carrier_id
↓
ProviderFactory
↓
Provider
↓
Carrier API

---

# Phase 7 - Dependency Injection & Configuration

Status: 🟡 Planned

Goals:

- Centralized provider configuration
- Automatic client instantiation
- Remove hardcoded dependencies

Deliverables:

- Provider configuration layer
- Settings integration
- Dependency injection

---

# Phase 8 - Provider Registry

Status: 🟡 Planned

Goals:

- Simplify new carrier onboarding

Deliverables:

- Registry pattern
- Dynamic carrier registration
- Extensible architecture

---

# Phase 9 - Provider Health Monitoring

Status: 🟡 Planned

Goals:

- Provider availability checks
- Latency monitoring
- Health reporting

Deliverables:

- ProviderHealth model
- Health endpoints
- Monitoring metrics

---

# Phase 10 - Advanced Canonical Model

Status: 🟡 Planned

Goals:

- Support advanced carrier capabilities

Deliverables:

- CarrierCapability
- CarrierService
- CarrierConstraint
- CarrierOptions

---

# Phase 11 - Performance & Caching

Status: 🟡 Planned

Goals:

- Reduce carrier API calls
- Improve response times

Deliverables:

- Cache layer
- TTL strategy
- Cache invalidation

---

# Phase 12 - Production API Hardening

Status: 🟡 Planned

Goals:

- Production readiness

Deliverables:

- Enhanced OpenAPI
- Structured logging
- Correlation IDs
- Rate limiting

---

# Phase 13 - Additional Carriers

Status: 🟡 Planned

Potential targets:

- DPD
- Chronopost
- UPS
- GLS
- InPost
- Evri
- Yodel

---

# Phase 14 - Observability

Status: 🟡 Planned

Goals:

- Operational visibility

Deliverables:

- Metrics
- Tracing
- Dashboard integration

---

# Phase 15 - Release 1.0

Status: 🟡 Planned

Deliverables:

- Final documentation
- Architecture diagrams
- ADR review
- Release notes
- GitHub showcase quality

Success Criteria:

- Stable architecture
- Multiple live carriers
- Fully documented
- Production-grade design
