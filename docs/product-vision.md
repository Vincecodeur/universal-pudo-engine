# Universal PUDO Engine

## Vision

Universal PUDO Engine est un moteur universel de recherche et de sélection de points relais multi-transporteurs.

L'objectif du projet est de fournir une couche d'abstraction unique permettant de rechercher, normaliser et sélectionner des points relais indépendamment du transporteur utilisé.

Le moteur doit être réutilisable dans différents contextes :

- OMS
- WMS
- TMS
- Checkout
- CMS
- SaaS

Le moteur constitue le coeur de l'écosystème Universal PUDO.

Toutes les implémentations doivent être construites autour de ce coeur sans créer de dépendance fonctionnelle ou technique vers une implémentation spécifique.

---

# Core Principles

## Carrier Agnostic

Le moteur ne doit contenir aucune logique métier dépendante d'un transporteur spécifique.

Chaque transporteur est intégré via :

- Provider Pattern
- Mapper Pattern
- Adapter Pattern

Le moteur doit supporter :

- Colissimo
- Mondial Relay
- Chronopost
- GLS
- UPS
- DPD
- InPost
- autres transporteurs

sans modification du domaine métier.

---

## Build Once, Consume Anywhere

Le moteur doit pouvoir être consommé par plusieurs produits ou plateformes.

Exemples :

- OMS
- WMS
- TMS
- Checkout
- SDK
- CMS
- SaaS

Une seule implémentation métier doit être maintenue.

---

# Product Architecture

L'écosystème Universal PUDO est constitué de plusieurs couches.

## Universal PUDO Core

Le Core est le produit principal.

Responsabilités :

- abstraction transporteurs
- recherche de points relais
- normalisation des données
- orchestration des providers
- sélection de points relais
- hybrid search

Le Core ne contient pas :

- gestion utilisateurs
- gestion organisations
- portail SaaS
- paiement
- billing
- credential management

---

## Universal PUDO SaaS

Le SaaS est une implémentation du Core.

Responsabilités :

- utilisateurs
- organisations
- dashboard
- administration
- comptes transporteurs
- authentification

Le SaaS utilise le Core.

Le Core ne dépend jamais du SaaS.

---

## Universal PUDO Integration Layer

Permet l'intégration du moteur dans :

- OMS
- WMS
- TMS
- Checkout

Le système hôte reste propriétaire :

- des credentials transporteurs
- de l'authentification
- de la configuration métier

---

## Universal PUDO SDK

Permet une intégration simplifiée dans :

- applications Python
- applications TypeScript
- intégrations custom

---

## Universal PUDO CMS Layer

Permet l'intégration dans :

- WooCommerce
- PrestaShop
- Shopify
- Magento

---

# Credential Ownership Strategy

## Architectural Decision

ADR-0002

Décision retenue :

Host Managed Credentials

Le Universal PUDO Core n'est jamais propriétaire des credentials transporteurs.

Le Core est credential agnostic.

---

## OMS

Les credentials appartiennent à l'OMS.

Exemple :

- API Key Colissimo
- Identifiants GLS
- Credentials Chronopost

Le Core consomme uniquement les connecteurs fournis par l'OMS.

---

## WMS

Les credentials appartiennent au WMS.

Le Core ne stocke rien.

---

## TMS

Les credentials appartiennent au TMS.

Le Core ne stocke rien.

---

## CMS Plugins

Le plugin CMS gère les credentials.

Le Core ne stocke rien.

---

## SaaS

Le SaaS peut gérer ses propres comptes transporteurs.

Cette responsabilité appartient au SaaS Layer.

Pas au Core.

---

# Current Architecture

Architecture utilisée :

- Hexagonal Architecture
- Domain Driven Design
- Provider Pattern
- Mapper Pattern
- Repository Pattern
- Factory Pattern
- Dependency Injection

---

# Current Status

## Validated Carriers

- Colissimo
- Mondial Relay
- Chronopost

## Automated Tests

155 passing tests

## Proven Components

- ProviderFactory
- Hybrid Search
- Synchronization Engine
- FastAPI Integration
- Live Provider Architecture

---

# Roadmap Objectives

## Short Term

- Validation live Colissimo
- Validation live Chronopost
- Création des fixtures réelles

---

## Medium Term

- Frontend MVP
- Carte OpenStreetMap
- Sélection de points relais
- Universal PUDO SaaS

---

## Long Term

- OMS Integration Layer
- WMS Integration Layer
- TMS Integration Layer
- SDK
- CMS Plugins
- SaaS Platform

---

# Out Of Scope For Now

Les éléments suivants ne sont pas prioritaires :

- Billing
- Stripe
- Invoicing
- Subscriptions

Ils restent dans le backlog.

---

# Final Goal

Créer une plateforme universelle de recherche et de sélection de points relais capable d'être utilisée :

- directement par des utilisateurs finaux via un portail SaaS
- intégrée dans un OMS
- intégrée dans un WMS
- intégrée dans un TMS
- intégrée dans un CMS
- intégrée dans un checkout

tout en conservant un coeur métier unique, indépendant et réutilisable.
