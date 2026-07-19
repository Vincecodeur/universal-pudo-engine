# Colissimo Analysis

Status: Draft

Last Updated: 2026-07-19

==================================================
PURPOSE
==================================================

This document analyses the Colissimo Pickup Point
service from the perspective of the Universal PUDO
Engine.

The objective is to determine whether the current
Universal PUDO architecture can support a future
Colissimo integration without major redesign.

This document focuses exclusively on pickup point
capabilities.

Out of scope:

- Shipment creation
- Label generation
- Tracking
- Return management
- Customs procedures
- Manifest generation

==================================================
DOCUMENT SOURCES
==================================================

Analysis based on official Colissimo Pickup Point
documentation.

The documentation describes a "Web Service Choix
de Livraison" that allows retrieval of:

- Post Offices
- Pickup Points
- Pickup Lockers

The service provides:

- Address-based pickup point search
- Pickup point detail retrieval
- Coordinate-based pickup point search

REST and SOAP interfaces are referenced.

==================================================
BUSINESS SCOPE
==================================================

Universal PUDO objective:

Provide a carrier-independent search engine for:

- Pickup points
- Lockers
- Collection locations

Colissimo objective:

Provide pickup point information for Colissimo
delivery services.

Common objective:

Return available pickup locations to end users.

==================================================
COLISSIMO SERVICE OVERVIEW
==================================================

Service Name:

Web Service Choix de Livraison

Purpose:

Return pickup locations available for parcel
delivery.

Returned location types may include:

- Post Offices
- Pickup Stores
- Pickup Lockers

Current Universal PUDO equivalent:

PickupPoint

Compatibility assessment:

Good.

==================================================
IDENTIFIED COLISSIMO CAPABILITIES
==================================================

Capability 1

Pickup Point Search

Colissimo Method:

findRDVPointRetraitAcheminement

Purpose:

Search pickup locations from a postal address.

Result:

Multiple pickup locations.

Universal PUDO Equivalent:

search_pickup_points()

Compatibility:

Partial

Reason:

Universal PUDO currently supports:

- postal_code
- city
- country_code

but does not support all Colissimo parameters.

---

Capability 2

Pickup Point Details

Colissimo Method:

findPointRetraitAcheminementByID

Purpose:

Retrieve a single pickup point from its identifier.

Result:

One pickup point.

Universal PUDO Equivalent:

get_pickup_point_details()

Compatibility:

Good

Reason:

Functionally equivalent behaviour.

---

Capability 3

Coordinate Search

Colissimo Method:

findPointRetraitAcheminementByLongitudeLatitude

Purpose:

Search pickup points from latitude and longitude.

Universal PUDO Equivalent:

search_pickup_points_by_radius

Compatibility:

Partial

Reason:

Universal PUDO performs coordinate search from
its local repository.

Colissimo performs coordinate search directly
against its service.

==================================================
ACCESS MODES
==================================================

Colissimo documentation references:

SOAP

REST

Universal PUDO preference:

REST

Reasons:

- Simpler implementation
- Easier testing
- Better fit with FastAPI
- Reduced complexity

SOAP support should remain a future option.

==================================================
AUTHENTICATION ANALYSIS
==================================================

The documentation references multiple
authentication modes.

Known mechanisms include:

- API Key
- Account Number
- Password
- Partner Code

Provider implication:

Authentication logic must remain isolated
inside ColissimoPickupProvider.

The following layers must remain unaware
of authentication details:

- API
- Use Cases
- Repositories
- Database Models

Architecture compatibility:

Good

Current architecture already allows
provider-specific authentication.

==================================================
SEARCH INPUT ANALYSIS
==================================================

Current Universal PUDO Search Inputs

Supported:

- carrier_id
- country_code
- postal_code
- city
- pickup_type
- active

---

Colissimo Search Inputs Identified

The documentation references the following inputs:

- address
- zipCode
- city
- countryCode
- weight
- shippingDate
- filterRelay
- requestId
- lang
- optionInter

Compatibility Assessment:

PARTIAL

Reason:

Universal PUDO currently supports only a subset
of Colissimo search inputs.

==================================================
GAP ANALYSIS - INPUTS
==================================================

Supported Today

[OK]

postal_code

city

country_code

---

Not Supported Today

[TODO]

address

weight

shippingDate

filterRelay

requestId

lang

optionInter

---

Architecture Decision

Do not modify PickupProvider yet.

Reason:

A first simulated provider can operate using only:

- city
- postal_code
- country_code

Additional fields should only be added after
a real implementation demonstrates the need.

==================================================
RESPONSE ANALYSIS
==================================================

The Colissimo documentation describes responses
containing pickup point information.

Observed response concepts include:

- pickup point identifier
- street information
- postal code
- city
- latitude
- longitude
- distance from requested address
- opening hours
- accessibility indicators
- closure indicators
- location hints

==================================================
UNIVERSAL PUDO MODEL COMPARISON
==================================================

Current PickupPoint model contains:

id

carrier_id

carrier_pickup_id

==================================================
ARCHITECTURE FIT ASSESSMENT
==================================================

Current Universal PUDO Architecture

API
↓
Use Cases
↓
Repositories
↓
PostgreSQL

Provider Layer

PickupProvider
↓
MockPickupProvider

Assessment:

GOOD

The current Provider Layer can be extended without
modifying the existing architecture.

---

Use Cases Compatibility

Current Use Cases:

- GetCarrier
- ListCarriers
- GetPickupPoint
- ListPickupPoints
- SearchPickupPoints
- SearchPickupPointsByRadius

Assessment:

GOOD

No current use case requires modification to
support a simulated Colissimo provider.

---

API Compatibility

Current Endpoints:

GET /carriers

GET /carriers/{carrier_id}

GET /pickup-points/{carrier_id}

GET /pickup-points/details/{pickup_point_id}

GET /pickup-points/search

GET /pickup-points/search-radius

Assessment:

GOOD

All current endpoints can continue to operate
without modification.

Carrier-specific logic should remain hidden
behind the Provider Layer.

==================================================
CONFIGURATION ANALYSIS
==================================================

Current Project Configuration

Database configuration exists.

Provider-specific configuration does not exist.

Potential future Colissimo configuration:

COLISSIMO_API_KEY

COLISSIMO_PARTNER_CODE

COLISSIMO_ACCOUNT_NUMBER

COLISSIMO_PASSWORD

COLISSIMO_BASE_URL

COLISSIMO_TIMEOUT_SECONDS

Assessment:

PARTIAL

The architecture can support configuration
management, but provider-specific settings
have not yet been introduced.

Decision:

Do not implement configuration objects before
a real Colissimo integration is started.

==================================================
PROVIDER EXCEPTION ANALYSIS
==================================================

Current Status

Provider-specific exceptions do not exist.

Potential future exceptions:

ProviderUnavailableError

ProviderAuthenticationError

ProviderTimeoutError

ProviderResponseError

ProviderMappingError

Assessment:

PARTIAL

Not required for a simulated provider.

Will become important for a live API integration.

Decision:

Keep in backlog until real API communication
is introduced.

==================================================
MONITORING ANALYSIS
==================================================

The Colissimo documentation references a service
supervision page returning:

[OK]

or

[KO]

to indicate service availability.
【1-29fb61】

Current Universal PUDO support:

No provider monitoring capability.

Potential future method:

health_check()

Assessment:

PARTIAL

Useful for production operations.

Not required for Provider Layer validation.

Decision:

Backlog.

==================================================
RISK ANALYSIS
==================================================

LOW RISK

- Simulated Colissimo provider
- Static pickup point dataset
- Provider contract validation
- Provider unit testing

---

MEDIUM RISK

- Response mapping accuracy
- Opening hours normalization
- Distance handling

---

HIGH RISK

- Live API integration
- Authentication management
- SOAP support
- API rate limits
- Availability management
- Error normalization

==================================================
CURRENT GAPS SUMMARY
==================================================

Gap 1

No provider configuration layer.

Priority:

LOW

---

Gap 2

No provider exception hierarchy.

Priority:

MEDIUM

---

Gap 3

No provider health monitoring.

Priority:

LOW

---

Gap 4

No provider-level coordinate search.

Priority:

LOW

---

Gap 5

No real carrier implementation.

Priority:

HIGH

Reason:

The provider contract has not yet been validated
against a carrier-specific implementation.

==================================================
FINAL VERDICT
==================================================

Can the current architecture support a
simulated Colissimo provider?

YES

---

Can the current architecture support a
production-grade Colissimo integration
without modification?

NO

---

Does the architecture require redesign before
implementing a simulated provider?

NO

---

Should PickupProvider be modified now?

NO

Reason:

There is currently no validated evidence that
the existing contract is insufficient.

==================================================
RECOMMENDED PROJECT DECISION
==================================================

Proceed with:

ColissimoPickupProvider (Simulated)

Do NOT proceed immediately with:

- Provider Registry
- Provider Factory
- Provider Selector
- Provider Monitoring
- Live Colissimo API Integration

Reason:

The simulated provider is the minimum step
required to validate the current architecture.

==================================================
NEXT STEP
==================================================

Create:

src/universal_pudo/providers/colissimo/

Files:

- **init**.py
- colissimo_pickup_provider.py

Then create:

tests/providers/test_colissimo_pickup_provider.py

Validation workflow:

1. python -m py_compile

2. pytest tests/providers/test_colissimo_pickup_provider.py -v

3. pytest

Expected result:

78 existing tests remain green

plus

new Colissimo provider tests.

==================================================
ARCHITECT CONCLUSION
==================================================

The Universal PUDO Engine architecture is mature
enough to begin validating real carrier concepts.

The next milestone should focus on proving that
a carrier-specific implementation can be added
without modifying:

- API Layer
- Use Cases
- Repository Layer
- Database Schema

The recommended validation vehicle is:

ColissimoPickupProvider (Simulated)

Only after this validation should the project
consider a real Colissimo API integration.
