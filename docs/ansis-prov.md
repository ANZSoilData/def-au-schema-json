# PROV Entity Schema
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/prov.json

JSON Schema definitions of the PROV Ontology entities used by ANSIS.

## Core Entities

> Core entities are those primary soil and sample entities that are provided, queried and downloaded in ANSIS.

### prov:Activity

*PROV Activity*. An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| $schema | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | \[ _The JSON schema for the object. For use when "additionalProperties": false and therefore a property names $schema reference is a Bad Thing._ \] |
| @context | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. \[ _After: https://www.w3.org/TR/json-ld/#the-context_ \] |
| @id | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. \[ _After: https://www.w3.org/TR/json-ld/#node-identifiers_ \] |
| @type | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. \[ _After: https://www.w3.org/TR/json-ld/#specifying-the-type_ \] |
| relatedActivity | 0..1 |  | [prov:Activity](#provActivity); [sosa:Actuation](./ansis-sosa.md#sosaActuation); [sosa:Observation](./ansis-sosa.md#sosaObservation); [sosa:Sampling](./ansis-sosa.md#sosaSampling); [ansis:SiteVisit](./ansis-entities.md#ansisSiteVisit); [ansis:Treatment](./ansis-entities.md#ansisTreatment) |  | link to an activity related to this context \[ _[ISSUE] ontology has contradictory range/rangeIncludes statements_ \] |
| name | 0..1 |  |  |  | A name for some thing. |
### prov:Agent

*PROV Agent*. An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| $schema | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | \[ _The JSON schema for the object. For use when "additionalProperties": false and therefore a property names $schema reference is a Bad Thing._ \] |
| @context | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. \[ _After: https://www.w3.org/TR/json-ld/#the-context_ \] |
| @id | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. \[ _After: https://www.w3.org/TR/json-ld/#node-identifiers_ \] |
| @type | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. \[ _After: https://www.w3.org/TR/json-ld/#specifying-the-type_ \] |
| name | 0..1 |  |  |  | A name for some thing. |
### prov:Organization

*PROV Organization*. An organization is a social or legal institution such as a company, society, etc.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| $schema | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | \[ _The JSON schema for the object. For use when "additionalProperties": false and therefore a property names $schema reference is a Bad Thing._ \] |
| @context | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. \[ _After: https://www.w3.org/TR/json-ld/#the-context_ \] |
| @id | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. \[ _After: https://www.w3.org/TR/json-ld/#node-identifiers_ \] |
| @type | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. \[ _After: https://www.w3.org/TR/json-ld/#specifying-the-type_ \] |
| name | 0..1 |  |  |  | A name for some thing. |
### prov:Person

*PROV Person*. Person agents are people.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| $schema | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | \[ _The JSON schema for the object. For use when "additionalProperties": false and therefore a property names $schema reference is a Bad Thing._ \] |
| @context | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. \[ _After: https://www.w3.org/TR/json-ld/#the-context_ \] |
| @id | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. \[ _After: https://www.w3.org/TR/json-ld/#node-identifiers_ \] |
| @type | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. \[ _After: https://www.w3.org/TR/json-ld/#specifying-the-type_ \] |
| name | 0..1 |  |  |  | A name for some thing. |
### prov:Project

*PROV Project*. A Project is a planned activity with a budget, a sponsor, and a leader.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| $schema | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | \[ _The JSON schema for the object. For use when "additionalProperties": false and therefore a property names $schema reference is a Bad Thing._ \] |
| @context | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. \[ _After: https://www.w3.org/TR/json-ld/#the-context_ \] |
| @id | 0..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. \[ _After: https://www.w3.org/TR/json-ld/#node-identifiers_ \] |
| @type | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. \[ _After: https://www.w3.org/TR/json-ld/#specifying-the-type_ \] |
| hasLeader | 0..1 |  |  |  | An organization is a social or legal institution such as a company, society, etc. |
| hasSponsor | 0..* |  |  |  | An organization is a social or legal institution such as a company, society, etc. |
| name | 0..1 |  |  |  | A name for some thing. |
| label | 0..1 |  |  |  | A human-readable name for the object. |