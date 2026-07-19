# Colissimo Provider Design

Status: Draft

Last Updated: 2026-07-19

==================================================
OBJECTIVE
==================================================

Design the future Colissimo pickup point provider
for the Universal PUDO Engine.

The purpose of this document is to validate that
the current Provider Layer architecture can support
a real carrier integration without requiring major
changes to:

- FastAPI
- Use Cases
- Repository Layer
- PostgreSQL Schema

This document focuses only on pickup point search
and pickup point retrieval.

No production implementation is planned at this stage.

==================================================
SOURCE REFERENCES
==================================================

This design is based on Colissimo's official
Web Service Choix de Livraison documentation.

The documentation states that Colissimo provides
services allowing:

- Pickup point search from an address
- Pickup point lookup by identifier
- Pickup point search from latitude and longitude

The service is available through SOAP and REST
interfaces.

Authentication may use API Key or account-based
credentials depending on the integration scenario.

Official documentation also references a
supervision endpoint returning:

[OK]
or
[KO]

to indicate service availability.

==================================================
CURRENT UNIVERSAL PUDO ARCHITECTURE
==================================================

Current architecture:

API
↓
Use Case
↓
Repository
↓
PostgreSQL

Current Provider Layer:

PickupProvider
↓
MockPickupProvider

Future target:

PickupProvider
├── MockPickupProvider
├── ColissimoPickupProvider
├── MondialRelayProvider
├── InPostProvider
└── FutureProviders

==================================================
PROVIDER RESPONSIBILITIES
==================================================

A provider is responsible for carrier-specific logic.

Provider responsibilities:

- Search pickup points
- Retrieve pickup point details
- Map carrier-specific responses
- Normalize carrier-specific fields
- Handle carrier-specific errors
- Handle carrier authentication

Provider responsibilities do NOT include:

- FastAPI routing
- Database migrations
- Repository management
- Swagger schemas
- Global business orchestration

==================================================
COLISSIMO INTEGRATION GOALS
==================================================

Carrier:
Colissimo

Target capability:
Pickup Point Search

Main business objectives:

1. Search pickup points

2. Retrieve pickup point details

3. Normalize results into Universal PUDO format

4. Prepare future shipment integrations

5. Validate Provider Layer architecture

==================================================
CURRENT PICKUPPROVIDER CONTRACT
==================================================

Current methods:

search_pickup_points()

get_pickup_point_details()

Current search filters:

- carrier_id
- country_code
- postal_code
- city

Current status:

Compatible with MockPickupProvider.

Compatibility with Colissimo still requires analysis.

==================================================
COLISSIMO CAPABILITIES IDENTIFIED
==================================================

Capability #1

Search pickup points from address.

Colissimo method:

findRDVPointRetraitAcheminement

Purpose:

Return pickup points nearest to an address.

==================================================

Capability #2

Retrieve pickup point details.

Colissimo method:

findPointRetraitAcheminementByID

Purpose:

Return detailed information about a specific
pickup point.

==================================================

Capability #3

Search pickup points from coordinates.

Colissimo method:

findPointRetraitAcheminementByLongitudeLatitude

Purpose:

Return pickup points nearest to a latitude /
longitude pair.

==================================================
ACCESS MODES
==================================================

The Colissimo documentation explicitly references:

SOAP

and

REST

Universal PUDO preferred strategy:

REST first.

Rationale:

- Simpler integration
- Easier testing
- Better alignment with FastAPI architecture
- Lower implementation complexity

SOAP remains a future option if necessary.

==================================================
AUTHENTICATION DESIGN
==================================================

Colissimo documentation references multiple
authentication modes.

Known authentication mechanisms:

- API Key
- Account Number
- Password
- Partner Code

Universal PUDO design principle:

Authentication must remain entirely inside
ColissimoPickupProvider.

The following layers must never manage
authentication logic:

- FastAPI
- Use Cases
- Repositories
- Database Models

Potential future configuration:

COLISSIMO_API_KEY

COLISSIMO_PARTNER_CODE

COLISSIMO_ACCOUNT_NUMBER

COLISSIMO_PASSWORD

Actual required credentials must be validated
during implementation.

Current status:

Not implemented.

==================================================
HEALTH CHECK DESIGN
==================================================

Colissimo documentation references a service
supervision endpoint returning:

[OK]

or

[KO]

Purpose:

Determine whether the Colissimo Pickup Point
service is available.

Potential future method:

health_check()

Potential return:

Provider: Colissimo

Status: Healthy

Timestamp: Current UTC Time

Current PickupProvider contract:

Does not contain health_check().

Decision:

Do not introduce health_check() in Provider v1.

Add only when provider monitoring becomes
a product requirement.

Current status:

Backlog.

==================================================
SEARCH DESIGN
==================================================

Current Universal PUDO search capability:

carrier_id

country_code

postal_code

city

Colissimo search capability includes:

address

zipCode

city

countryCode

weight

shippingDate

filterRelay

requestId

language

international option

Gap analysis:

Universal PUDO does not currently expose:

- address
- weight
- shippingDate
- filterRelay
- requestId
- language
- international option

Architecture decision:

Do not extend PickupProvider yet.

Start with the currently supported Universal PUDO
inputs:

country_code

postal_code

city

Additional parameters should only be added
after validation against a real implementation.

==================================================
COORDINATE SEARCH DESIGN
==================================================

Colissimo supports:

Search by latitude and longitude.

Universal PUDO currently supports:

Radius Search

using local coordinates stored in PostgreSQL.

Possible strategies:

Strategy A

Use local radius search only.

Strategy B

Call Colissimo coordinate search endpoint.

Strategy C

Query Colissimo and normalize results before
returning them.

Recommended strategy:

Begin with a simulated provider.

Delay geographic endpoint integration until
Provider Layer validation is complete.

==================================================
PICKUP POINT DETAILS DESIGN
==================================================

Current PickupProvider method:

get_pickup_point_details(
pickup_point_id
)

Colissimo capability:

findPointRetraitAcheminementByID

Compatibility:

Good

Reason:

Both concepts are functionally equivalent.

No contract changes required.

Current status:

Compatible.

==================================================
UNIVERSAL FIELD MAPPING
==================================================

Universal PUDO Field

id

Source:

Generated by Universal PUDO.

---

carrier_id

Source:

carrier-colissimo

---

carrier_pickup_id

Source:

Colissimo Point Retrait identifier.

---

name

Source:

Pickup Point name.

---

street_line_1

Source:

Address line.

---

street_line_2

Source:

Optional address complement.

---

postal_code

Source:

Postal code.

---

city

Source:

City.

---

country_code

Source:

Country code.

---

latitude

Source:

Latitude.

---

longitude

Source:

Longitude.

---

opening_hours

Source:

Opening hour structure returned by Colissimo.

Initial strategy:

Convert into a simple string representation.

---

active

Source:

Derived field.

True by default unless unavailable.

==================================================
MAPPING EXAMPLE
==================================================

Colissimo Field
↓
Universal PUDO Field

Point Retrait Identifier
↓
carrier_pickup_id

Label
↓
name

Address
↓
street_line_1

Zip Code
↓
postal_code

City
↓
city

Country Code
↓
country_code

Latitude
↓
latitude

Longitude
↓
longitude

Opening Hours
↓
opening_hours

==================================================
PROVIDER ERROR STRATEGY
==================================================

Provider-specific issues must be isolated.

Potential future exception hierarchy:

ProviderUnavailableError

ProviderAuthenticationError

ProviderTimeoutError

ProviderResponseError

ProviderMappingError

Current project:

No dedicated provider exceptions exist.

Decision:

Do not create exception hierarchy before the
first provider implementation.

Current status:

Backlog.

==================================================
PERSISTENCE STRATEGY
==================================================

Question:

Should Colissimo results be stored in PostgreSQL?

Possible approaches:

Approach A

Live provider only.

Results are returned to the application but
never stored.

---

Approach B

Cache provider.

Results are retrieved and stored locally.

---

Approach C

Hybrid model.

Results are retrieved live and cached when
necessary.

---

Recommended V1 approach:

Live simulated provider.

No persistence.

No synchronization process.

Reason:

Validate architecture before adding
data refresh complexity.

==================================================
PROVIDER LIFECYCLE
==================================================

Provider maturity roadmap:

Level 1

MockPickupProvider

Purpose:

Validate provider abstraction.

Status:

Completed.

---

Level 2

JsonPickupProvider

Purpose:

Validate provider independence from PostgreSQL.

Status:

Implemented in repository structure.

---

Level 3

ColissimoPickupProvider (Simulated)

Purpose:

Validate architecture against a carrier-specific
implementation without external dependencies.

Features:

- Static Colissimo-like dataset
- Pickup point search
- Pickup point details
- Provider tests

Status:

Planned.

---

Level 4

ColissimoPickupProvider (Live API)

Purpose:

Connect to actual Colissimo API.

Features:

- Authentication
- API communication
- Response mapping
- Error handling

Status:

Future.

==================================================
IMPLEMENTATION PHASES
==================================================

Phase 1

Architecture Design

Deliverables:

- colissimo_provider_design.md
- colissimo_analysis.md
- provider_gap_analysis.md

Status:

Completed after documentation review.

---

Phase 2

Simulated Provider

Deliverables:

src/universal_pudo/providers/colissimo/

Files:

- **init**.py
- colissimo_pickup_provider.py

Goal:

Validate PickupProvider contract.

Dependencies:

None.

Status:

Next implementation target.

---

Phase 3

Provider Tests

Deliverables:

tests/providers/test_colissimo_pickup_provider.py

Validation:

- py_compile
- targeted pytest
- global pytest

Success criteria:

Existing 78 tests continue to pass.

---

Phase 4

Contract Review

Objective:

Verify whether PickupProvider remains sufficient
once confronted with a carrier implementation.

Questions:

- Are additional methods required?
- Is coordinate search needed?
- Is health_check needed?
- Are provider-specific settings needed?

---

Phase 5

Live API Preparation

Objective:

Prepare real Colissimo integration.

Topics:

- authentication
- timeout handling
- error handling
- configuration management

==================================================
ARCHITECTURAL DECISIONS
==================================================

Decision 001

Provider-specific logic must remain inside
provider implementations.

Reason:

Avoid carrier-specific behaviour leaking into
business logic.

Status:

Approved.

---

Decision 002

The public API must remain carrier-agnostic.

Reason:

Clients should not depend on a specific carrier.

Status:

Approved.

---

Decision 003

A simulated carrier provider must exist before
a live provider implementation.

Reason:

Validate design without network dependency.

Status:

Approved.

---

Decision 004

Do not modify PickupProvider until a real-world
requirement proves that a change is required.

Reason:

Avoid premature abstraction.

Status:

Approved.

==================================================
SUCCESS CRITERIA
==================================================

The Colissimo Provider Design will be considered
validated when:

1. A simulated ColissimoPickupProvider exists.

2. The provider implements PickupProvider.

3. Search functionality works.

4. Pickup point detail retrieval works.

5. Existing APIs remain unchanged.

6. Existing repositories remain unchanged.

7. Existing PostgreSQL schema remains unchanged.

8. Existing test suite remains green.

9. No Provider Layer redesign is required.

==================================================
KNOWN RISKS
==================================================

Risk:

Current PickupProvider contract may not expose
all parameters used by Colissimo.

Mitigation:

Validate with simulated provider first.

---

Risk:

Additional carrier fields may not fit into the
current PickupPoint model.

Mitigation:

Perform mapping review before persistence.

---

Risk:

Colissimo availability handling may require
provider monitoring.

Mitigation:

Keep health_check in backlog.

==================================================
FINAL ARCHITECT ASSESSMENT
==================================================

Current Provider Layer:

Suitable for simulated provider implementation.

Current Provider Layer:

Not yet proven for a production-grade carrier
integration.

No architecture redesign is currently justified.

The recommended next technical milestone is:

ColissimoPickupProvider (Simulated)

This milestone will provide the first real test
of the Provider architecture against a carrier-
specific implementation.

==================================================
NEXT PROJECT STEP
==================================================

Create:

src/universal_pudo/providers/colissimo/

Files:

- **init**.py
- colissimo_pickup_provider.py

Then create:

tests/providers/test_colissimo_pickup_provider.py

Validation workflow:

1. py_compile

2. provider pytest

3. global pytest

Expected result:

78 existing tests remain green

- new provider tests

without any architecture change.
