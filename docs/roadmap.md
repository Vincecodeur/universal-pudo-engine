# Universal PUDO Engine Roadmap

## Phase 1 - Foundations

Status: DONE

- Domain Layer
- SQLAlchemy
- Repositories
- FastAPI
- Tests

## Phase 2 - Provider Architecture

Status: DONE

- PickupProvider contract
- Provider Mapping Strategy
- ADR-0001

## Phase 3 - Multi-Carrier Validation

Status: DONE

Carriers validated:

- Mock
- Colissimo
- Mondial Relay

Result:

PickupPointModel successfully supports multiple carrier payloads.

## Phase 4 - Live Provider Integration

Status: NEXT

Candidate 1:

- Mondial Relay Live

Candidate 2:

- Colissimo Live

Deliverables:

- HTTP Client
- Credential Management
- Real Payload Retrieval
- Mapper Integration
- Error Handling

Success Criteria:

Real carrier payload
↓
Mapper
↓
PickupPointModel

without architecture changes.

## Phase 5 - Advanced Provider Layer

Status: FUTURE

Candidates:

- DPD
- InPost
- GLS
- UPS

Decision pending after first live provider.
