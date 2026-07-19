# Provider Gap Analysis

Status: Draft

Last Updated: 2026-07-19

==================================================
PURPOSE
==================================================

This document compares the current Universal PUDO
Provider Layer with the requirements of a real
carrier integration.

Reference carrier:

Colissimo

Objective:

Identify what is already supported by the
Provider Layer and what may require future
evolution.

This document is intended to support architecture
decision-making before implementing a real
carrier provider.

==================================================
CURRENT PROVIDER LAYER
==================================================

Current Provider Interface:

PickupProvider

Current Provider Implementations:

- MockPickupProvider
- JsonPickupProvider

Current Status:

Provider Layer v1 implemented

Provider tests available

Architecture validated through:

- Unit tests
- Provider tests
- Full pytest execution

Current project status:

78 tests passing

==================================================
CURRENT PICKUPPROVIDER CONTRACT
==================================================

Current methods:

search_pickup_points()

get_pickup_point_details()

Current design philosophy:

Carrier-specific logic remains isolated inside
providers.

Current architecture:

API
↓
Use Cases
↓
Provider
↓
Repository
↓
PostgreSQL

==================================================
CURRENT CAPABILITIES
==================================================

Capability

Search Pickup Points

Status:

SUPPORTED

Current Method:

search_pickup_points()

---

Capability

Retrieve Pickup Point Details

Status:

SUPPORTED

Current Method:

get_pickup_point_details()

---

Capability

Pickup Point Normalization

Status:

SUPPORTED

Reason:

Provider layer can transform carrier payloads
into Universal PUDO models.

---

Capability

Provider Isolation

Status:

SUPPORTED

Reason:

Business layer does not depend on carrier
implementation details.

==================================================
REFERENCE CARRIER
==================================================

Carrier:

Colissimo

Capabilities identified from official
documentation:

- Search pickup points
- Retrieve pickup point details
- Search pickup points by coordinates
- API authentication
- Service supervision endpoint

Assessment target:

Can PickupProvider support those capabilities?

==================================================
SEARCH CAPABILITY ANALYSIS
==================================================

Colissimo supports:

Address-based search.

Universal PUDO supports:

postal_code

city

country_code

Compatibility:

PARTIAL

Reason:

The provider contract does not expose every
parameter used by Colissimo.

Known Colissimo concepts not currently exposed:

- address
- shippingDate
- weight
- filterRelay
- language
- international option

Architecture decision:

Do not modify PickupProvider now.

Reason:

No real implementation has yet demonstrated
that those fields are required.

==================================================
DETAIL CAPABILITY ANALYSIS
==================================================

Colissimo capability:

Retrieve a pickup point by identifier.

Universal capability:

get_pickup_point_details()

Assessment:

FULL MATCH

No architecture changes required.

No contract changes required.

Current provider design is sufficient.

==================================================
COORDINATE SEARCH ANALYSIS
==================================================

Colissimo:

Supports search using latitude and longitude.

Current Universal PUDO:

Supports radius search at repository level.

Current Provider Layer:

Does not expose coordinate search.

Assessment:

PARTIAL GAP

Potential future method:

search_pickup_points_by_coordinates()

Decision:

Do not introduce until required by a real
provider implementation.

==================================================
AUTHENTICATION GAP ANALYSIS
==================================================

Current Provider Layer

Authentication handling:

NONE

Current PickupProvider contract:

No authentication-related methods.

---

Colissimo Requirements

The official documentation references:

- API Key
- Account Number
- Password
- Partner Code

Authentication is required before access
to the pickup point services.
【1-801241】【2-4b5b64】

---

Gap Assessment

GAP EXISTS

Reason:

Provider Layer currently contains no explicit
authentication abstraction.

---

Impact

LOW

Reason:

Authentication can remain entirely inside the
provider implementation.

No Provider contract modification is required.

---

Decision

Do not create:

ProviderCredentials

ProviderAuthenticationService

ProviderAuthManager

before a real carrier integration exists.

==================================================
CONFIGURATION GAP ANALYSIS
==================================================

Current Project

Database configuration exists.

Provider configuration does not exist.

---

Future Colissimo Configuration

Potential settings:

COLISSIMO_API_KEY

COLISSIMO_PARTNER_CODE

COLISSIMO_ACCOUNT_NUMBER

COLISSIMO_PASSWORD

COLISSIMO_BASE_URL

COLISSIMO_TIMEOUT_SECONDS

---

Gap Assessment

PARTIAL GAP

Reason:

There is currently no standard location
for provider configuration.

---

Impact

MEDIUM

Reason:

A live provider will require configuration
management.

---

Decision

Do not introduce ProviderSettings yet.

Keep provider settings local to the first
real implementation.

==================================================
ERROR HANDLING GAP ANALYSIS
==================================================

Current Provider Layer

No dedicated provider exception hierarchy.

---

Potential Provider Errors

Authentication failure

Timeout

Unexpected response

Rate limiting

Unavailable service

Mapping failure

---

Current Support

Generic Python exceptions only.

---

Gap Assessment

GAP EXISTS

---

Impact

MEDIUM

Reason:

A simulated provider does not require dedicated
exception handling.

A live provider eventually will.

---

Potential Future Exceptions

ProviderUnavailableError

ProviderAuthenticationError

ProviderTimeoutError

ProviderResponseError

ProviderMappingError

---

Decision

Backlog

Create only when implementing real API calls.

==================================================
HEALTH CHECK GAP ANALYSIS
==================================================

Colissimo documentation references a supervision
endpoint returning:

[OK]

or

[KO]

for service availability validation.
【1-801241】

---

Current Provider Layer

No monitoring capability.

No health_check() method.

---

Gap Assessment

GAP EXISTS

---

Impact

LOW

Reason:

Health monitoring is not required for a
simulated provider.

---

Potential Future Method

health_check()

Possible result:

Provider Name

Provider Status

Timestamp

---

Decision

Backlog.

==================================================
MAPPING GAP ANALYSIS
==================================================

Current Universal PUDO Fields

carrier_pickup_id

name

street_line_1

street_line_2

postal_code

city

country_code

latitude

longitude

opening_hours

active

---

Colissimo Concepts Identified

Pickup point identifier

Address

Postal code

City

Latitude

Longitude

Opening hours

Distance

Accessibility

Closure indicators
【1-801241】

---

Gap Assessment

SMALL GAP

---

Supported Today

[OK]

identifier

address

postal code

city

latitude

longitude

opening hours

---

Not Explicitly Supported

[TODO]

distance

accessibility

temporary closure

localisation hint

---

Decision

Do not expand PickupPoint model yet.

Validate first whether these fields provide
business value for Universal PUDO.

==================================================
DATA PERSISTENCE GAP ANALYSIS
==================================================

Current Architecture

Repository
↓
PostgreSQL

Provider
↓
Repository

---

Question

Should carrier results be persisted?

---

Current Status

Not implemented.

---

Possible Future Modes

Mode A

Live search only

Provider returns data.

Nothing stored.

---

Mode B

Full synchronization

Provider refreshes PostgreSQL.

---

Mode C

Hybrid cache

Provider fetches live data.

Frequently used data cached.

---

Gap Assessment

NONE FOR NOW

---

Reason

The first objective is Provider validation.

Persistence strategy is a later concern.

==================================================
TESTING GAP ANALYSIS
==================================================

Current Coverage

Domain Tests

Repository Tests

Use Case Tests

API Tests

Provider Tests

---

Current Provider Tests

test_mock_pickup_provider.py

---

Missing Future Tests

test_colissimo_pickup_provider.py

Provider Mapping Tests

Provider Error Tests

Provider Configuration Tests

---

Gap Assessment

EXPECTED GAP

---

Decision

First new testing target:

test_colissimo_pickup_provider.py

==================================================
ARCHITECTURE RISK ASSESSMENT
==================================================

Current State

Provider Layer v1 exists.

Current implementations:

- MockPickupProvider
- JsonPickupProvider

Current architecture has been validated through:

- Provider tests
- Application tests
- Repository tests
- API tests

Current global status:

78 tests passing

---

Risk Category

Provider Contract

Risk Level

LOW

Reason

Current PickupProvider contract already supports
the two main Colissimo capabilities:

- Search pickup points
- Retrieve pickup point details

---

Risk Category

Provider Configuration

Risk Level

MEDIUM

Reason

Provider-specific settings have not yet been
introduced.

A future real integration will require:

- API credentials
- base URL
- timeout configuration

---

Risk Category

Provider Monitoring

Risk Level

LOW

Reason

Current project scope does not require
monitoring features.

Can be added later.

---

Risk Category

Real API Integration

Risk Level

HIGH

Reason

The architecture has not yet been validated
against a live carrier service.

This is precisely why a simulated provider
is recommended first.

==================================================
PRIORITY MATRIX
==================================================

HIGH PRIORITY

[TODO]

ColissimoPickupProvider (Simulated)

Reason

Validates architecture against a carrier-specific
implementation.

---

[TODO]

test_colissimo_pickup_provider.py

Reason

Validates provider contract behaviour.

==================================================

MEDIUM PRIORITY

[TODO]

Provider exceptions

Reason

Required for real API communication.

---

[TODO]

Provider configuration model

Reason

Required for real credentials management.

==================================================

LOW PRIORITY

[TODO]

Provider Registry

---

[TODO]

Provider Factory

---

[TODO]

Provider Selector

---

[TODO]

Provider Health Monitoring

Reason

No current business requirement.

==================================================
CHANGES REQUIRED BEFORE A SIMULATED PROVIDER
==================================================

Required Changes

NONE

---

Reason

Current analysis indicates that:

PickupProvider

- Current PickupPoint model
- Current architecture

are sufficient to build a simulated carrier
provider.

==================================================
CHANGES NOT REQUIRED
==================================================

Do NOT create:

ProviderRegistry

---

Do NOT create:

ProviderFactory

---

Do NOT create:

ProviderSelector

---

Do NOT modify:

FastAPI Routers

---

Do NOT modify:

Existing Use Cases

---

Do NOT modify:

PostgreSQL Schema

---

Do NOT modify:

Repository Layer

---

Reason

No currently identified requirement justifies
these changes.

==================================================
SIMULATED PROVIDER VALIDATION PLAN
==================================================

Step 1

Create:

src/universal_pudo/providers/colissimo/

---

Step 2

Implement:

colissimo_pickup_provider.py

---

Step 3

Create:

tests/providers/test_colissimo_pickup_provider.py

---

Step 4

Validate:

python -m py_compile

---

Step 5

Validate:

pytest tests/providers/test_colissimo_pickup_provider.py -v

---

Step 6

Validate:

pytest

Expected Result:

Existing tests remain green.

==================================================
FINAL VERDICT
==================================================

Question

Can the current architecture support a
simulated Colissimo provider?

Answer

YES

---

Question

Can the current architecture support a
production-ready Colissimo provider
without modifications?

Answer

NO

---

Question

Should PickupProvider be changed before the
first Colissimo implementation?

Answer

NO

---

Question

Should the architecture be redesigned now?

Answer

NO

==================================================
ARCHITECT RECOMMENDATION
==================================================

The current architecture is sufficiently mature
for the next validation milestone.

The next objective should not be another
architecture abstraction.

The next objective should not be another
documentation layer.

The next objective should be:

ColissimoPickupProvider (Simulated)

Reason

This is the smallest possible implementation
capable of validating whether the Provider Layer
is truly suitable for a real transporteur.

==================================================
PROJECT DECISION
==================================================

Current Status

Provider Layer v1 Complete

---

Current Decision

Freeze architecture.

---

Next Technical Milestone

ColissimoPickupProvider (Simulated)

---

Success Condition

Add a carrier-specific provider without changing:

- API Layer
- Use Cases
- Repositories
- Database Schema

---

If that succeeds:

Provider Layer Architecture validated.
