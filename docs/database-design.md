# PostgreSQL Database Design

Version: 1.0 (Draft)

---

# 1. Purpose

This document defines the initial PostgreSQL database design for Universal PUDO Engine V1.

The objective is to translate the domain model into a relational schema while keeping the model simple, extensible and aligned with the current project scope.

This document focuses on V1 and avoids over-engineering future capabilities that are not yet validated by real carrier integrations.

---

# 2. Design Principles

## PostgreSQL First

PostgreSQL is the official database for the project from V1.

SQLite is not considered the primary database strategy.

---

## Domain-Driven Schema

The database schema follows the business domain model.

Core concepts are:

- Carrier
- CarrierAccount
- PickupPoint
- Address
- GeoLocation

---

## Avoid Premature Optimization

Fields are only added when they support a clear V1 use case.

Future capabilities such as detailed opening hours, cache refresh rules, recommendation history or advanced operational intelligence are intentionally deferred.

---

## Carrier Data Ownership

Universal PUDO Engine does not own carrier data.

The platform stores normalized operational data and configuration required to interact with carrier APIs.

Carrier accounts and credentials remain customer-owned.

---

# 3. Tables Overview

V1 introduces the following tables:

- carriers
- carrier_accounts
- pickup_points

Address and geolocation are embedded directly in pickup_points for V1.

This keeps the schema simple while preserving the domain distinction at code level.

---

# 4. Table: carriers

## Purpose

Stores supported carrier integrations.

A carrier integration represents a coherent API, not necessarily a country or a brand.

Example:

- DPD France and DPD UK may be separate integrations if they rely on different APIs.
- Mondial Relay may support multiple countries through one integration if the same API supports them.

---

## Columns

| Column              |         Type | Required | Description                     |
| ------------------- | -----------: | -------: | ------------------------------- |
| id                  |         UUID |      Yes | Internal primary key            |
| code                | VARCHAR(100) |      Yes | Stable technical code           |
| name                | VARCHAR(255) |      Yes | Display name                    |
| lifecycle           |  VARCHAR(50) |      Yes | Integration lifecycle status    |
| supported_countries |       TEXT[] |      Yes | List of supported country codes |
| capabilities        |       TEXT[] |      Yes | List of supported capabilities  |
| created_at          |  TIMESTAMPTZ |      Yes | Creation timestamp              |
| updated_at          |  TIMESTAMPTZ |      Yes | Last update timestamp           |
| last_synced_at      |  TIMESTAMPTZ |      Yes | Last synchronization timestamp  |

---

## Constraints

```sql
ALTER TABLE carriers
ADD CONSTRAINT carriers_code_unique UNIQUE (code);
```

```sql
ALTER TABLE carriers
ADD CONSTRAINT carriers_lifecycle_check
CHECK (lifecycle IN (
    'ACTIVE',
    'DEPRECATED',
    'UNLISTED',
    'SUNSET',
    'REMOVED'
));
```

---

## Example Records

```text
code: colissimo_pickup
name: Colissimo Pickup
supported_countries: {FR}
capabilities: {SEARCH_PICKUP_POINTS, GET_PICKUP_DETAILS}

code: mondial_relay
name: Mondial Relay
supported_countries: {FR, BE}
capabilities: {SEARCH_PICKUP_POINTS, GET_PICKUP_DETAILS}

code: chronopost_pickup
name: Chronopost Pickup
supported_countries: {FR}
capabilities: {SEARCH_PICKUP_POINTS, GET_PICKUP_DETAILS}
```

---

# 5. Table: carrier_accounts

## Purpose

Stores customer-owned carrier account metadata.

The table does not define the final secret storage strategy.

Secrets may later be stored through secured references, encrypted storage or external secret managers.

---

## Columns

| Column                |         Type | Required | Description                        |
| --------------------- | -----------: | -------: | ---------------------------------- |
| id                    |         UUID |      Yes | Internal primary key               |
| carrier_id            |         UUID |      Yes | Reference to carriers.id           |
| account_name          | VARCHAR(255) |      Yes | User-facing account name           |
| status                |  VARCHAR(50) |      Yes | Account status                     |
| credentials_reference | VARCHAR(255) |       No | Reference to stored credentials    |
| metadata              |        JSONB |       No | Provider-specific account metadata |
| created_at            |  TIMESTAMPTZ |      Yes | Creation timestamp                 |
| updated_at            |  TIMESTAMPTZ |      Yes | Last update timestamp              |

---

## Constraints

```sql
ALTER TABLE carrier_accounts
ADD CONSTRAINT carrier_accounts_carrier_fk
FOREIGN KEY (carrier_id)
REFERENCES carriers(id);
```

```sql
ALTER TABLE carrier_accounts
ADD CONSTRAINT carrier_accounts_status_check
CHECK (status IN (
    'ACTIVE',
    'DISABLED',
    'ERROR'
));
```

---

## Notes

No sandbox or production distinction is introduced in V1.

This decision may be revisited later if real carrier integrations require it.

---

# 6. Table: pickup_points

## Purpose

Stores normalized pickup points returned by carrier providers.

In V1, pickup points may be stored for persistence, debugging, future cache preparation or API response consistency.

The initial strategy remains real-time API calls.

---

## Columns

| Column            |           Type | Required | Description                               |
| ----------------- | -------------: | -------: | ----------------------------------------- |
| id                |           UUID |      Yes | Internal primary key                      |
| carrier_id        |           UUID |      Yes | Reference to carriers.id                  |
| carrier_pickup_id |   VARCHAR(255) |      Yes | Pickup identifier provided by the carrier |
| name              |   VARCHAR(255) |      Yes | Pickup point name                         |
| pickup_type       |    VARCHAR(50) |      Yes | STORE or LOCKER                           |
| street_line_1     |   VARCHAR(255) |      Yes | First address line                        |
| street_line_2     |   VARCHAR(255) |       No | Second address line                       |
| postal_code       |    VARCHAR(50) |      Yes | Postal code                               |
| city              |   VARCHAR(255) |      Yes | City                                      |
| state_or_region   |   VARCHAR(255) |       No | Region, state or administrative area      |
| country_code      |        CHAR(2) |      Yes | ISO country code                          |
| formatted_address |           TEXT |       No | Original or formatted full address        |
| latitude          | NUMERIC(10, 7) |      Yes | Latitude                                  |
| longitude         | NUMERIC(10, 7) |      Yes | Longitude                                 |
| opening_hours     |           TEXT |       No | Raw or human-readable opening hours       |
| phone_number      |   VARCHAR(100) |       No | Contact phone number                      |
| email             |   VARCHAR(255) |       No | Contact email                             |
| active            |        BOOLEAN |      Yes | Whether the pickup point is active        |
| services          |          JSONB |       No | Carrier-specific services                 |
| metadata          |          JSONB |       No | Carrier-specific metadata                 |
| created_at        |    TIMESTAMPTZ |      Yes | Creation timestamp                        |
| updated_at        |    TIMESTAMPTZ |      Yes | Last update timestamp                     |
| last_synced_at    |    TIMESTAMPTZ |      Yes | Last synchronization timestamp            |

---

## Constraints

```sql
ALTER TABLE pickup_points
ADD CONSTRAINT pickup_points_carrier_fk
FOREIGN KEY (carrier_id)
REFERENCES carriers(id);
```

```sql
ALTER TABLE pickup_points
ADD CONSTRAINT pickup_points_type_check
CHECK (pickup_type IN (
    'STORE',
    'LOCKER'
));
```

```sql
ALTER TABLE pickup_points
ADD CONSTRAINT pickup_points_carrier_pickup_unique
UNIQUE (carrier_id, carrier_pickup_id);
```

---

# 7. Address Strategy

Address is represented as a Value Object in the domain model.

In PostgreSQL V1, address fields are embedded in the pickup_points table.

This avoids introducing unnecessary joins before a concrete need appears.

---

## Address Fields

```text
street_line_1
street_line_2
postal_code
city
state_or_region
country_code
formatted_address
```

---

## Decision

The model keeps `street_line_1` instead of splitting addresses into:

- building_number
- street_name

Reason:

- carrier APIs may return inconsistent address formats
- address formats differ by country
- marketplace data may be incomplete
- fine-grained parsing is not required for V1

---

# 8. GeoLocation Strategy

GeoLocation is represented as a Value Object in the domain model.

In PostgreSQL V1, geolocation fields are embedded in the pickup_points table.

---

## GeoLocation Fields

```text
latitude
longitude
```

---

## Precision

The recommended PostgreSQL type is:

```sql
NUMERIC(10, 7)
```

This is sufficient for pickup point location use cases.

---

# 9. Opening Hours Strategy

Opening hours are stored as a simple optional text field in V1.

```text
opening_hours TEXT NULL
```

Reason:

- carrier APIs may not provide detailed opening hours
- carriers may use different formats
- some providers may return raw strings
- some providers may return structured data
- some providers may not return opening hours at all

A dedicated OpeningHours model is intentionally deferred.

This decision may be revisited after implementing the first real carrier integrations.

---

# 10. Index Strategy

## carriers

```sql
CREATE INDEX idx_carriers_lifecycle
ON carriers(lifecycle);
```

```sql
CREATE INDEX idx_carriers_supported_countries
ON carriers USING GIN(supported_countries);
```

---

## carrier_accounts

```sql
CREATE INDEX idx_carrier_accounts_carrier_id
ON carrier_accounts(carrier_id);
```

```sql
CREATE INDEX idx_carrier_accounts_status
ON carrier_accounts(status);
```

---

## pickup_points

```sql
CREATE INDEX idx_pickup_points_carrier_id
ON pickup_points(carrier_id);
```

```sql
CREATE INDEX idx_pickup_points_country_postal_code
ON pickup_points(country_code, postal_code);
```

```sql
CREATE INDEX idx_pickup_points_city
ON pickup_points(city);
```

```sql
CREATE INDEX idx_pickup_points_type
ON pickup_points(pickup_type);
```

```sql
CREATE INDEX idx_pickup_points_active
ON pickup_points(active);
```

---

# 11. Future Geospatial Strategy

V1 does not require PostGIS.

Distance calculations can initially be handled at application level.

PostGIS may be introduced later if the project requires:

- radius search at database level
- geospatial indexing
- advanced proximity queries
- large-scale pickup point storage

This avoids adding a database extension before the need is proven.

---

# 12. Future Cache Strategy

V1 uses real-time API calls as the primary strategy.

The database design is compatible with a future cache layer, but cache behavior is not defined yet.

Future fields may include:

- last_synced_at
- source_updated_at
- cache_expires_at
- refresh_strategy
- refresh_frequency

These fields are intentionally excluded from V1 until real carrier constraints are known.

---

# 12.1 Current Freshness Strategy

V1 introduces a minimal freshness tracking model.

Field:

last_synced_at

Purpose:

Track when Universal PUDO Engine successfully synchronized a pickup point from a carrier provider.

Usage:

- synchronization auditing
- stale pickup point detection
- cache management
- future hybrid search strategy

Flow:

Carrier API
↓
Provider
↓
Sync Engine
↓
last_synced_at updated
↓
Repository.upsert()
↓
PostgreSQL

Important:

last_synced_at does not represent carrier-side update timestamps.

It only represents synchronization performed by Universal PUDO Engine.

# 13. Initial SQL Draft

```sql
CREATE TABLE carriers (
    id UUID PRIMARY KEY,
    code VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    lifecycle VARCHAR(50) NOT NULL,
    supported_countries TEXT[] NOT NULL,
    capabilities TEXT[] NOT NULL,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    CONSTRAINT carriers_lifecycle_check CHECK (
        lifecycle IN (
            'ACTIVE',
            'DEPRECATED',
            'UNLISTED',
            'SUNSET',
            'REMOVED'
        )
    )
);
```

```sql
CREATE TABLE carrier_accounts (
    id UUID PRIMARY KEY,
    carrier_id UUID NOT NULL REFERENCES carriers(id),
    account_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    credentials_reference VARCHAR(255),
    metadata JSONB,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    CONSTRAINT carrier_accounts_status_check CHECK (
        status IN (
            'ACTIVE',
            'DISABLED',
            'ERROR'
        )
    )
);
```

```sql
CREATE TABLE pickup_points (
    id UUID PRIMARY KEY,
    carrier_id UUID NOT NULL REFERENCES carriers(id),
    carrier_pickup_id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    pickup_type VARCHAR(50) NOT NULL,
    street_line_1 VARCHAR(255) NOT NULL,
    street_line_2 VARCHAR(255),
    postal_code VARCHAR(50) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state_or_region VARCHAR(255),
    country_code CHAR(2) NOT NULL,
    formatted_address TEXT,
    latitude NUMERIC(10, 7) NOT NULL,
    longitude NUMERIC(10, 7) NOT NULL,
    opening_hours TEXT,
    phone_number VARCHAR(100),
    email VARCHAR(255),
    active BOOLEAN NOT NULL DEFAULT TRUE,
    services JSONB,
    metadata JSONB,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL,
    CONSTRAINT pickup_points_type_check CHECK (
        pickup_type IN (
            'STORE',
            'LOCKER'
        )
    ),
    CONSTRAINT pickup_points_carrier_pickup_unique UNIQUE (
        carrier_id,
        carrier_pickup_id
    )
);
```

---

# 14. V1 Database Success Criteria

The V1 database design is successful if it can support:

- carrier registration
- carrier lifecycle tracking
- carrier account metadata
- normalized pickup point storage
- pickup point type visibility
- search by carrier
- search by country and postal code
- search by city
- future cache extension without redesign

---

# 15. Explicitly Deferred

The following items are intentionally not included in V1:

- detailed opening hours model
- sandbox versus production account distinction
- PostGIS
- cache refresh rules
- recommendation scoring tables
- resolution history
- user portal tables
- CMS plugin tables
- audit logs
- advanced credential encryption strategy

These items will be introduced only when justified by real implementation needs.
