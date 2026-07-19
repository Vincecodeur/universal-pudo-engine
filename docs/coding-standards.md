# Coding Standards

Version: 1.0 (Draft)

---

# Purpose

This document defines the coding standards used throughout Universal PUDO Engine.

The objective is to ensure:

- Consistency
- Readability
- Maintainability
- Extensibility

These standards apply to all contributors.

The rules defined here should remain stable regardless of future functional evolution.

---

# Core Principles

## Readability First

Code is read far more often than it is written.

Prioritize clarity over cleverness.

---

## Explicit Over Implicit

Prefer:

```python
pickup_point.is_active()
```

over:

```python
pickup_point.check()
```

---

## Domain First

Business concepts belong to the domain layer.

Carrier implementations belong to the provider layer.

Infrastructure concerns belong to the infrastructure layer.

---

## Simplicity First

Avoid introducing abstractions before a real need exists.

Do not create classes, interfaces or services solely for hypothetical future use cases.

---

## Single Responsibility

Each class, function and module should have one primary responsibility.

---

# Naming Conventions

## Classes

Use PascalCase.

Examples:

```python
PickupPoint
Carrier
CarrierAccount
SearchPickupPointsUseCase
MondialRelayProvider
```

---

## Functions

Use snake_case.

Examples:

```python
search_pickup_points()
resolve_pickup_point()
get_pickup_details()
```

---

## Variables

Use snake_case.

Examples:

```python
pickup_point
carrier_account
supported_countries
```

---

## Constants

Use UPPER_CASE.

Examples:

```python
DEFAULT_TIMEOUT
MAX_RESULTS
```

---

## Files

Use snake_case.

Examples:

```text
pickup_point.py
carrier_account.py
search_pickup_points.py
```

---

# Type Hints

Type hints are mandatory for all public methods.

Example:

```python
def search_pickup_points(
    postal_code: str
) -> list[PickupPoint]:
    ...
```

---

## Avoid

```python
def search(postal_code):
    ...
```

---

# Docstrings

Public classes and public functions must include docstrings.

Use concise descriptions.

Example:

```python
class PickupPoint:
    """
    Represents a carrier pickup location.
    """
```

---

# Comments

Comments should explain:

- Why

not:

- What

Bad:

```python
# Increment counter
counter += 1
```

Good:

```python
# Carrier API may return duplicate records.
# Counter tracks unique entries only.
```

---

# Layer Responsibilities

## Domain Layer

May contain:

- Entities
- Value Objects
- Enums
- Domain Services

Must not contain:

- Database code
- HTTP code
- Provider code

---

## Application Layer

May contain:

- Use Cases
- DTOs
- Workflow orchestration

Must not contain:

- Provider-specific implementations

---

## Provider Layer

May contain:

- API calls
- Authentication
- Request transformations
- Response transformations

Must not contain:

- Core business logic

---

## Infrastructure Layer

May contain:

- Database access
- Configuration
- Logging
- External technical concerns

Must not contain:

- Business rules

---

# Provider Standards

Every provider should expose a consistent interface.

Providers must transform carrier-specific responses into domain objects.

Consumers must never receive raw carrier payloads.

---

## Example

Good:

```python
PickupPoint
```

Bad:

```python
MondialRelayRawPickupPointResponse
```

outside provider code.

---

# Exception Handling

Never raise generic exceptions.

Avoid:

```python
raise Exception("Error")
```

Prefer:

```python
raise PickupPointNotFoundError(...)
```

or

```python
raise CarrierAuthenticationError(...)
```

---

# Logging

Use structured logging whenever possible.

Logs should contain useful operational information.

Avoid logging secrets, tokens or credentials.

---

# Secrets

The following must never be committed:

- API keys
- Access tokens
- Secrets
- Passwords
- Credentials

Secrets must be loaded through configuration mechanisms.

---

# Testing Standards

## Unit Tests

Required for:

- Domain entities
- Value objects
- Use cases

---

## Integration Tests

Required for:

- Providers
- Database integrations

---

## Mock Providers

Every provider integration should support testing through mock implementations whenever feasible.

---

# Database Standards

Business entities drive schema design.

Database constraints should enforce business rules where possible.

Database-specific logic must not leak into the domain layer.

---

# API Standards

APIs expose domain concepts.

APIs must not expose carrier-specific structures.

---

# Backward Compatibility

Public interfaces should remain stable whenever possible.

Breaking changes should be documented in:

```text
CHANGELOG.md
```

---

# Documentation Standards

Whenever a feature is completed:

The following files must be reviewed:

- README.md
- CHANGELOG.md

Relevant documentation must be updated before considering the work complete.

---

# Architecture Integrity Rules

The following are considered architectural violations:

- Domain layer depending on provider code.
- Domain layer depending on database code.
- Business rules implemented inside provider adapters.
- Direct carrier-specific logic inside public APIs.

These patterns should be rejected during reviews.

---

# Success Criteria

The codebase is considered compliant when:

- Naming is consistent.
- Type hints are present.
- Layers remain independent.
- Providers remain isolated.
- Business logic remains centralized in the domain and application layers.
- New carriers can be added without architectural redesign.
