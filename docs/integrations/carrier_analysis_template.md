# Carrier Analysis Template

==================================================
GENERAL INFORMATION
==================================================

Carrier Name:

Country:

Integration Type:

API Documentation:

Sandbox Available:

Authentication Mechanism:

Contact Information:

---

## BUSINESS CAPABILITIES

Pickup Point Search

Supported:
[ ]

Notes:

Pickup Point Details

Supported:
[ ]

Notes:

Shipping Creation

Supported:
[ ]

Notes:

Tracking

Supported:
[ ]

Notes:

Cancellation

Supported:
[ ]

Notes:

---

## AUTHENTICATION

Method:

API Key:
[ ]

OAuth2:
[ ]

Basic Auth:
[ ]

Mutual TLS:
[ ]

Other:
[ ]

Notes:

---

## TECHNICAL ENDPOINTS

Pickup Search Endpoint:

Method:

Input Parameters:

Output Parameters:

Rate Limits:

Notes:

---

Pickup Detail Endpoint:

Method:

Input Parameters:

Output Parameters:

Rate Limits:

Notes:

---

## DATA MAPPING

Carrier Field
→ Universal PUDO Field

Example:

pickup_id
→ carrier_pickup_id

label
→ name

city
→ city

postalCode
→ postal_code

---

## ERROR MANAGEMENT

Error Codes:

Timeout Strategy:

Retry Strategy:

Fallback Strategy:

---

## PROVIDER GAP ANALYSIS

Supported by current architecture:

[ ]

Requires PickupProvider change:

[ ]

Requires model change:

[ ]

Requires API change:

[ ]

Requires database change:

[ ]

Details:

---

## TEST STRATEGY

Unit Tests

Required:
[ ]

Integration Tests

Required:
[ ]

Provider Tests

Required:
[ ]

Swagger Validation

Required:
[ ]

---

## FINAL VERDICT

Provider Complexity:

LOW
MEDIUM
HIGH

Architecture Compatible:

YES
NO

Required Changes:

List here.

---

## IMPLEMENTATION PRIORITY

Priority:

LOW
MEDIUM
HIGH

Estimated Business Value:

LOW
MEDIUM
HIGH
