# ADR-0002

## Title

Carrier Credential Ownership Strategy

## Status

Accepted

## Context

Universal PUDO Engine is designed to be embedded into:

- OMS
- WMS
- TMS
- CMS
- Checkout
- SaaS

A decision was required regarding carrier credential ownership.

Two options were evaluated.

Option A

Credentials are owned by the application hosting the engine.

Option B

Credentials are owned by the Universal PUDO Core.

## Decision

Option A selected.

Universal PUDO Core never owns carrier credentials.

Carrier credentials are owned by the implementation layer.

Examples:

OMS
→ OMS owns credentials

WMS
→ WMS owns credentials

TMS
→ TMS owns credentials

CMS Plugin
→ Plugin owns credentials

SaaS Portal
→ SaaS owns credentials

The Core only consumes carrier connectivity through adapters.

## Consequences

Benefits

- Lower coupling
- Easier OMS integration
- Easier WMS integration
- Easier TMS integration
- Easier portability
- Clear separation of concerns

Trade-offs

- SaaS layer must implement credential management
- CMS plugins must implement credential management

## Future Consideration

Option B is moved to backlog.

Managed carrier credentials inside the Core may be reconsidered in the future if a SaaS business model requires it.
