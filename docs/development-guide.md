# Development Guide

Version: 1.0 (Draft)

---

# Purpose

This document describes how to develop, maintain and contribute to Universal PUDO Engine.

It focuses on:

- Development workflow
- Project setup
- Tooling
- Testing
- Git workflow

Coding conventions are defined separately in:

docs/coding-standards.md

---

# Project Philosophy

Development follows a Domain First approach.

The expected implementation flow is:

Business Requirement
↓
Domain Model
↓
Use Case
↓
Tests
↓
Implementation
↓
Documentation
↓
Commit

Code should never drive business design.

Business design drives the code.

---

# Technology Stack

## Language

Python 3.14+

---

## API Framework

FastAPI

Reason:

- Modern
- Excellent typing support
- Automatic OpenAPI documentation
- Widely adopted

---

## Database

PostgreSQL

Reason:

- Production-grade
- Strong ecosystem
- Suitable for future growth

---

## ORM

SQLAlchemy

Reason:

- Mature
- Flexible
- Well supported

---

## Migrations

Alembic

Reason:

- Standard migration tool for SQLAlchemy

---

## Testing

Pytest

Reason:

- Industry standard
- Strong ecosystem

---

## Linting

Ruff

Reason:

- Fast
- Modern
- Consolidates multiple tools

---

# Repository Structure

Current structure:

```text
universal-pudo-engine/
│
├── docs/
├── src/
├── tests/
├── scripts/
├── migrations/
└── .github/
```

Subdirectories should only be created when they become necessary.

Avoid speculative folder creation.

---

# Development Workflow

## Step 1

Start from a documented requirement.

The requirement must be traceable to:

- product-vision.md
- roadmap.md
- domain-model.md
- architecture.md

---

## Step 2

Update the domain model if necessary.

Business concepts must be defined before implementation.

---

## Step 3

Create or update tests.

Prefer:

Test First

when practical.

---

## Step 4

Implement the feature.

---

## Step 5

Run validation.

Tests must pass.

Linting must pass.

---

## Step 6

Update documentation.

Review:

- README.md
- CHANGELOG.md
- Relevant documents

before considering work complete.

---

# Git Workflow

## Branch Strategy

Initial strategy:

```text
main
```

only.

Additional branches may be introduced if project complexity increases.

---

## Commit Philosophy

Commits should represent meaningful business or technical milestones.

Good:

```text
Add PickupPoint domain entity

Implement Mondial Relay provider

Create carrier lifecycle model
```

Bad:

```text
Fix stuff

Updates

Changes
```

---

# Documentation Workflow

When a major decision is taken:

1. Update the relevant document.
2. Create an ADR if the decision is architectural.
3. Keep architecture and implementation aligned.

Documentation is part of the deliverable.

---

# Database Workflow

## Schema Changes

Any schema change should follow:

Domain Model
↓
Database Design
↓
Alembic Migration
↓
Implementation

Avoid modifying the schema without updating design documents.

---

# Provider Development Workflow

All carrier integrations follow the same process.

## Step 1

Study carrier API.

---

## Step 2

Map carrier response fields.

---

## Step 3

Normalize data into domain objects.

---

## Step 4

Implement provider.

---

## Step 5

Create provider integration tests.

---

## Step 6

Update documentation.

---

# Testing Strategy

## Unit Tests

Cover:

- Domain entities
- Value objects
- Use cases

---

## Integration Tests

Cover:

- Providers
- Database interactions

---

## Mock Providers

Use mock providers whenever feasible.

Provider tests should not depend on carrier availability.

---

# Error Management

Prefer explicit errors.

Examples:

```text
CarrierAuthenticationError

PickupPointNotFoundError

CarrierUnavailableError

ProviderConfigurationError
```

Avoid generic exceptions.

---

# Configuration Management

Application configuration must be externalized.

Examples:

- Environment variables
- Configuration files

Credentials must never be hardcoded.

---

# Security Guidelines

Never commit:

- Passwords
- API Keys
- Access Tokens
- Secrets

Never expose credentials in:

- Logs
- Examples
- Documentation

---

# Release Process

Before a release:

- Tests pass
- Documentation updated
- CHANGELOG updated
- Version updated

A release is not complete until documentation reflects reality.

---

# Future Evolution

This guide should evolve only when:

- Tooling changes
- Workflow changes
- Project governance changes

Business changes belong elsewhere.

The guide must remain focused on development practices.
