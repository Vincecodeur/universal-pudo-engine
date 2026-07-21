# v0.10.0 - 2026-07-20

### Fixed

#### Colissimo

- Fixed Colissimo live API payload key by replacing `apikey` with `apiKey`.

#### Chronopost

- Updated default PUDO productCode from `1` to `86` to match Chronopost PUDO documentation.
- Removed empty GET parameters from Chronopost requests.
- Aligned live validation requests with official Chronopost documentation examples.

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
- Real API connectivity validated
- Real XML response validated
- ResponseParser validated
- Mapper validated
- PickupPointModel generation validated

Example validated pickup point:

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
- Real API connectivity validated
- Real payload mapping validated
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

- Real API responses
- Real payload parsing
- Real payload mapping
- PickupPointModel conversion

Current result:

156 / 156 tests passing

## Added

### Chronopost Integration

- ChronopostClient
- ChronopostResponseParser
- ChronopostMapper
- ChronopostPickupProvider
- ChronopostLiveProvider

### Configuration

- chronopost_account_number
- chronopost_password

### Dependency Injection

- Chronopost provider registration
- Chronopost integrated into ProviderFactory
- Chronopost integrated into FastAPI dependencies

### Tests

Added:

- test_client.py
- test_response_parser.py
- test_chronopost_mapper.py
- test_chronopost_pickup_provider.py
- test_chronopost_live_provider.py
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

Total automated tests:

15 passing
0 failing

Architecture status:

3 live carrier integrations validated

- Colissimo
- Mondial Relay
- Chronopost

## [0.6.0-dev] - 2026-07-19

### Added

#### Mondial Relay Live Proof of Concept

- Added Mondial Relay SOAP client foundation
- Added Mondial Relay SECURITY hash generation
- Added SOAP envelope generation for WSI4_PointRelais_Recherche
- Added Mondial Relay SOAP response parser
- Added live test script for Mondial Relay Point Relais search
- Added real parsed Mondial Relay fixture in JSON format
- Added live payload mapping test from parsed Mondial Relay data to PickupPointModel

#### Provider Layer

- Added MondialRelayClient
- Added MondialRelayResponseParser
- Added MondialRelaySecurity
- Added Mondial Relay live payload mapping validation

#### Tests

- Added test_client.py
- Added test_response_parser.py
- Added test_live_payload_mapping.py
- Added official Mondial Relay SECURITY validation test

#### Dependencies

- Added requests dependency for SOAP HTTP calls

### Changed

#### Mondial Relay Mapper

- Updated latitude parsing to support decimal values returned with comma separators
- Updated longitude parsing to support decimal values returned with comma separators

Example:

Before:

48,82619
2,27988

After Mapping:

48.82619
2.27988

#### Provider Test Structure

Provider tests reorganized by carrier:

tests/providers/

- mock/
- colissimo/
- mondial_relay/

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
dict
↓
MondialRelayMapper
↓
PickupPointModel

#### Live Carrier Request

Successfully executed:

WSI4_PointRelais_Recherche

Validated:

- Endpoint connectivity
- SOAP envelope generation
- SECURITY hash generation
- HTTP communication
- XML parsing
- Payload mapping

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

#### Automated Tests

Current verified result:

104 passed
1 warning

### Architecture Validation

Validated architecture:

Carrier Payload
↓
Provider Client
↓
ResponseParser
↓
dict
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

### Known Limitations

The live integration is currently validated through a dedicated test script.

Not yet implemented:

- Live provider integration inside application use cases
- FastAPI live endpoint integration
- XML fixture storage for offline regression testing
- SOAP retry strategy
- SOAP timeout strategy beyond basic requests timeout
- Full Mondial Relay error code mapping
- Opening hours normalization
- LOCKER / RELAY type normalization
- Environment variable based credential management

### Milestone Achieved

First Live Carrier Integration Proof of Concept

Status:

COMPLETED

Validated carrier:

Mondial Relay

Project maturity:

Architecture Proven

- Real Carrier Connectivity Proven
- Real Payload Mapping Proven
