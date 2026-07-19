# ORM Mapping

Version: 1.0 (Draft)

---

# Purpose

This document defines how business domain objects are mapped to SQLAlchemy ORM models and PostgreSQL tables.

The objective is to clearly separate:

- Domain Layer
- Persistence Layer

while ensuring consistent data representation.

---

# Architectural Principle

Domain objects remain independent from:

- SQLAlchemy
- PostgreSQL
- Alembic

ORM models are implementation details of the persistence layer.

---

# Mapping Overview

| Domain Object  | ORM Model           | PostgreSQL Table |
| -------------- | ------------------- | ---------------- |
| Carrier        | CarrierModel        | carriers         |
| CarrierAccount | CarrierAccountModel | carrier_accounts |
| PickupPoint    | PickupPointModel    | pickup_points    |

---

# Carrier Mapping

## Domain

```python
Carrier
```

Represents a carrier integration.

---

## ORM

```python
CarrierModel
```

Represents a database record.

---

## Table

```sql
carriers
```

---

## Field Mapping

| Domain              | Database            |
| ------------------- | ------------------- |
| carrier_id          | id                  |
| code                | code                |
| name                | name                |
| lifecycle           | lifecycle           |
| supported_countries | supported_countries |
| capabilities        | capabilities        |

---

# CarrierAccount Mapping

## Domain

```python
CarrierAccount
```

Represents customer-owned carrier credentials.

---

## ORM

```python
CarrierAccountModel
```

---

## Table

```sql
carrier_accounts
```

---

## Field Mapping

| Domain       | Database     |
| ------------ | ------------ |
| account_id   | id           |
| carrier_id   | carrier_id   |
| account_name | account_name |
| status       | status       |

---

# PickupPoint Mapping

## Domain

```python
PickupPoint
```

Main business entity.

---

## ORM

```python
PickupPointModel
```

---

## Table

```sql
pickup_points
```

---

## Direct Fields

| Domain        | Database          |
| ------------- | ----------------- |
| pickup_id     | carrier_pickup_id |
| carrier_id    | carrier_id        |
| name          | name              |
| pickup_type   | pickup_type       |
| active        | active            |
| opening_hours | opening_hours     |

---

# Address Mapping

Address remains a Value Object in the domain.

It is flattened into table columns.

---

## Domain

```python
Address
```

---

## Database

```sql
street_line_1
street_line_2
postal_code
city
state_or_region
country_code
formatted_address
```

---

# GeoLocation Mapping

GeoLocation remains a Value Object in the domain.

It is stored as primitive columns.

---

## Domain

```python
GeoLocation
```

---

## Database

```sql
latitude
longitude
```

---

# Why Value Objects Are Flattened

V1 intentionally avoids:

- additional tables
- additional joins
- unnecessary complexity

This keeps read and write operations simple.

---

# Future Evolution

Future versions may introduce:

- Repository Pattern
- Domain ↔ ORM mappers
- PostGIS integration
- Dedicated cache entities

without modifying the domain model.

---

# Explicit Non-Goals

V1 does not implement:

- bidirectional ORM relationships
- repository abstraction
- CQRS
- event sourcing
- domain events

These additions require demonstrated business value before adoption.

---

# Success Criteria

The ORM layer is considered successful if:

- Domain objects remain SQLAlchemy-free.
- Database implementation details remain outside the domain.
- New providers can reuse the same persistence model.
- New countries can be supported without schema redesign.
