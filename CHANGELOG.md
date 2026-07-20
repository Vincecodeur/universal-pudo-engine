# Changelog

## [Unreleased]

### Added

- last_synced_at field
- freshness tracking
- Alembic migration for synchronization metadata
- find_stale_pickup_points()
- DeactivateStalePickupPointsUseCase
- stale pickup point detection

### Changed

- Synchronization now tracks last synchronization date
- Synchronization metadata is persisted
- Pickup points can now be identified as stale
- Automatic stale pickup point deactivation strategy introduced

### Tests

- Added freshness tracking tests
- Added stale pickup point repository tests
- Added stale pickup point use case tests

### Current Status

132 / 132 tests passing

### Git History

89579e1

feat(sync): add freshness tracking and synchronization metadata

ef76bc5

feat(sync): add stale pickup point detection

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
