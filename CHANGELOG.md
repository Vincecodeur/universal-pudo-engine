# Changelog

## v1.0.0 - 2026-07-21

### Core Freeze

Universal PUDO Engine reaches the Core Freeze milestone.

This release establishes the repository as the reusable Core for pickup point discovery, normalization and synchronization across multiple carrier networks.

Repository role:

Core

Repository boundary:

Universal PUDO Engine remains the Core repository.

Universal PUDO SaaS will be created as a separate repository.

### Release Status

Current release target:

v1.0.0

Current pytest result:

157 passed
1 warning
0 failed

Validated live carriers:

- Colissimo
- Mondial Relay
- Chronopost

### Licensing

Adopted Apache License 2.0 as the official Universal PUDO Engine license.

The Core can be used in commercial, SaaS and enterprise environments according to the Apache License 2.0 terms.

### Architecture Decisions

Confirmed and documented the following ADRs:

- ADR-0001 - Provider Mapping Strategy
- ADR-0002 - Carrier Credential Ownership Strategy
- ADR-0003 - Core Public Interfaces Strategy
- ADR-0004 - Repository Boundary Strategy

### Repository Boundary

Defined Universal PUDO Engine as the Core repository.

Defined that Universal PUDO SaaS must be developed in a separate repository.

Confirmed that all future carrier integrations must be implemented inside:

universal-pudo-engine

Confirmed that downstream products must consume the Core through versioned releases.

Downstream products include:

- SaaS platforms
- SDKs
- CMS plugins
- OMS integrations
- WMS integrations
- TMS integrations

### Public Core Interfaces

Confirmed the following public Core interfaces:

- PickupProvider
- ProviderFactory
- SearchLivePickupPointsUseCase
- SearchHybridPickupPointsUseCase
- SyncCarrierPickupPointsUseCase

External consumers should use these interfaces instead of internal implementation details.

### Validated Carrier Integrations

#### Colissimo

Validation status:

Live validated

Protocol:

REST / JSON

Validated flow:

Colissimo API
↓
JSON response
↓
ColissimoMapper
↓
PickupPointModel

Live validation result:

20 pickup points returned during validation

#### Mondial Relay

Validation status:

Live validated

Protocol:

SOAP / XML

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

#### Chronopost

Validation status:

Live validated

Protocol:

XML

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

Live validation result:

10 pickup points returned during validation

### Completed Core Capabilities

Completed and validated:

- canonical PickupPoint model strategy
- provider contracts
- provider implementations
- ProviderFactory
- live carrier search
- hybrid search
- synchronization
- stale pickup point detection
- provider health
- database repositories
- FastAPI integration
- real payload fixtures
- automated tests
- architecture documentation

### Testing

Current verified result:

157 passed
1 warning
0 failed

Test coverage includes:

- API routers
- API schemas
- application use cases
- domain models
- domain enums
- domain value objects
- database models
- database repositories
- provider factory
- mock provider
- Colissimo provider
- Mondial Relay provider
- Chronopost provider
- live provider validation
- real fixture validation
- synchronization
- hybrid search
- provider health

### Documentation

Updated Core Freeze documentation:

- README.md
- docs/product-vision.md
- docs/architecture.md
- docs/roadmap.md
- docs/architecture/project_status.md
- docs/architecture/project_structure.txt
- docs/adr/ADR-0003-core-public-interfaces.md
- docs/adr/ADR-0004-repository-boundary.md

### Packaging

Required release alignment:

- pyproject.toml version must be set to 1.0.0
- pyproject.toml development status must be set to Production/Stable
- LICENSE file must contain Apache License 2.0
- README must reference Apache License 2.0

### Future Ecosystem

Moved the following topics out of the Core roadmap:

- SaaS frontend
- authentication
- user management
- organization management
- tenant management
- billing
- subscriptions
- admin portal
- dashboards
- credential vault UI
- SDK packaging
- CMS plugin UI

Future repositories may include:

- universal-pudo-saas
- universal-pudo-sdk-python
- universal-pudo-sdk-typescript
- universal-pudo-cms-woocommerce
- universal-pudo-cms-prestashop

Carrier integrations remain owned by the Core.

### Future Core Versions

Potential future Core versions:

v1.1.0
Add InPost

v1.2.0
Add DPD

v1.3.0
Add GLS

v2.0.0
Breaking changes to public Core interfaces, if required

---

## v0.10.0 - 2026-07-21

### Licensing

- Adopted Apache License 2.0 as the official Universal PUDO Engine license.
- Core can be used in commercial, SaaS and enterprise environments.
- Carrier integrations remain reusable through the Core versioning strategy.

### Fixed

#### Colissimo

- Fixed Colissimo live API payload key by replacing `apikey` with `apiKey`.

#### Chronopost

- Updated default PUDO productCode from `1` to `86` to match Chronopost PUDO documentation.
- Removed empty GET parameters from Chronopost requests.
- Aligned live validation requests with Chronopost documentation examples.
- Aligned Chronopost client test expectations with the current client defaults.

### Validated

#### Chronopost Live Integration

Validated flow:

Chronopost API
↓
XML Response
↓
ChronopostResponseParser
↓
ChronopostMapper
↓
PickupPointModel

Live validation result:

- 10 pickup points returned
- real API connectivity validated
- real XML response validated
- response parser validated
- mapper validated
- PickupPointModel generation validated

Example validated pickup point:

Carrier:

chronopost

Carrier Pickup ID:

750DG

Name:

PAPH POLE AUTONOMIE SERVICES A LA PERSONNE

Postal Code:

92130

City:

ISSY LES MOULINEAUX

Coordinates:

48.824749
2.272234

#### Colissimo Live Integration

Validated flow:

Colissimo REST API
↓
JSON Response
↓
ColissimoMapper
↓
PickupPointModel

Live validation result:

- 20 pickup points returned
- real API connectivity validated
- real payload mapping validated
- PickupPointModel generation validated

Example validated pickup point:

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

Coordinates:

48.8646
2.343

### Phase 10.3 Completed

Validated live integrations:

- Mondial Relay
- Colissimo
- Chronopost

All three carriers successfully validated with:

- real API responses
- real payload parsing
- real payload mapping
- PickupPointModel conversion

### Added

#### Chronopost Integration

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostPickupProvider
- ChronopostLiveProvider

#### Configuration

- chronopost_account_number
- chronopost_password

#### Dependency Injection

- Chronopost provider registration
- Chronopost integrated into ProviderFactory
- Chronopost integrated into FastAPI dependencies

#### Tests

Added Chronopost test coverage:

- test_client.py
- test_response_parser.py
- test_chronopost_mapper.py
- test_chronopost_pickup_provider.py
- test_chronopost_live_provider.py
- test_chronopost_live_validation.py
- test_real_xml_fixture.py

### Validation

Validated carrier stack:

Chronopost API
↓
ChronopostClient
↓
ChronopostResponseParser
↓
ChronopostMapper
↓
PickupPointModel
↓
ChronopostLiveProvider
↓
ProviderFactory

### Result

Architecture status:

3 live carrier integrations validated

Validated carriers:

- Colissimo
- Mondial Relay
- Chronopost

---

## 0.6.0-dev - 2026-07-19

### Added

#### Mondial Relay Live Proof of Concept

- Added Mondial Relay SOAP client foundation.
- Added Mondial Relay SECURITY hash generation.
- Added SOAP envelope generation for WSI4_PointRelais_Recherche.
- Added Mondial Relay SOAP response parser.
- Added live test script for Mondial Relay Point Relais search.
- Added real parsed Mondial Relay fixture in JSON format.
- Added live payload mapping test from parsed Mondial Relay data to PickupPointModel.

#### Provider Layer

- Added MondialRelayClient.
- Added MondialRelayResponseParser.
- Added MondialRelaySecurity.
- Added Mondial Relay live payload mapping validation.

#### Tests

- Added test_client.py.
- Added test_response_parser.py.
- Added test_live_payload_mapping.py.
- Added official Mondial Relay SECURITY validation test.

#### Dependencies

- Added requests dependency for SOAP HTTP calls.

### Changed

#### Mondial Relay Mapper

- Updated latitude parsing to support decimal values returned with comma separators.
- Updated longitude parsing to support decimal values returned with comma separators.

Example:

Before mapping:

48,82619
2,27988

After mapping:

48.82619
2.27988

#### Provider Test Structure

Provider tests reorganized by carrier:

tests/providers/

- mock
- colissimo
- mondial_relay

### Validated

#### Live Mondial Relay SOAP Integration

Validated flow:

Mondial Relay SOAP
↓
HTTP
↓
XML Response
↓
ResponseParser
↓
Dictionary payload
↓
MondialRelayMapper
↓
PickupPointModel

#### Live Carrier Request

Successfully executed:

WSI4_PointRelais_Recherche

Validated:

- endpoint connectivity
- SOAP envelope generation
- SECURITY hash generation
- HTTP communication
- XML parsing
- payload mapping

#### Real Data Validation

Validated real pickup point:

Carrier:

mondial-relay

Carrier Pickup ID:

020243

Location:

ISSY LES MOULINEAUX

Postal Code:

92130

Coordinates:

48.82619
2.27988

Pickup Point Name:

LOCKER CARREFOUR CITY ISSY LES

Address:

14 BOULEVARD VOLTAIRE

### Architecture Validation

Validated architecture:

Carrier Payload
↓
Provider Client
↓
ResponseParser
↓
Dictionary payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
API

Result:

The architecture successfully supports a live carrier integration without modifications to:

- Domain Layer
- Repository Layer
- Database Layer
- API Layer

### Known Limitations At That Stage

At this historical milestone, the live integration was validated through a dedicated test script.

Not yet implemented at that stage:

- Live provider integration inside application use cases
- FastAPI live endpoint integration
- XML fixture storage for offline regression testing
- SOAP retry strategy
- SOAP timeout strategy beyond basic requests timeout
- full Mondial Relay error code mapping
- opening hours normalization
- LOCKER / RELAY type normalization
- environment variable based credential management

### Milestone Achieved

First live carrier integration proof of concept.

Status:

COMPLETED

Validated carrier:

Mondial Relay

Project maturity at that stage:

Architecture Proven
