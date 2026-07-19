# ADR-0001 - Provider Mapping Strategy

Status: Accepted

Date: 2026-07-19

==================================================
CONTEXT
==================================================

Universal PUDO Engine must support multiple
carrier pickup point providers.

Examples:

- Colissimo
- Mondial Relay
- InPost
- DPD
- GLS
- UPS

Each carrier exposes different payload formats.

Examples:

Colissimo

identifiant
nom
adresse1
localite

Mondial Relay

Num
LgNom
LgAdr1
Ville

InPost

name
address
location

A common strategy is required to avoid
architecture divergence.

==================================================
DECISION
==================================================

Carrier payloads shall never be exposed outside
provider implementations.

Each provider is responsible for mapping its
native payload into the canonical internal
representation.

Canonical representation:

PickupPointModel

Flow:

Carrier Payload
↓
Provider Mapper
↓
PickupPointModel
↓
Use Cases
↓
API

==================================================
CONSEQUENCES
==================================================

Positive

✅ Stable API layer

✅ Stable Use Cases

✅ Stable Repository layer

✅ Stable database schema

✅ Easy onboarding of new carriers

✅ No carrier-specific conditionals in
business logic

---

Negative

⚠ Individual mapper required for each carrier

⚠ Additional maintenance effort per provider

==================================================
REJECTED ALTERNATIVES
==================================================

Alternative 1

Expose carrier payloads directly.

Reason rejected:

Would tightly couple business logic
to transport carriers.

---

Alternative 2

Create carrier-specific domain models.

Reason rejected:

Would multiply application complexity.

---

Alternative 3

Introduce Provider Registry and
Provider Factory now.

Reason rejected:

Current project requirements do not justify
those abstractions.

==================================================
VALIDATION
==================================================

Validated by:

MockPickupProvider

JsonPickupProvider

ColissimoPickupProvider

84 automated tests passing.

==================================================
RESULT
==================================================

PickupPointModel remains the canonical pickup
point representation.

All future carriers must implement a
provider-specific mapper converting their
payload into PickupPointModel.
