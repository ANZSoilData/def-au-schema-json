# SKOS JSON Objects
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/skos.json

Reusable SKOS objects for vocabulary entries.

> Created to provide a definition for skos:Concept references elsewhere in the schema. Actually implemented with enumerations in JSON instances.

## Entities

### skos:Concept

*SKOS Concept*. Concepts are the units of thought — ideas, meanings, or (categories of) objects and events—which underlie many knowledge organization systems. As such, concepts exist in the mind as abstract entities which are independent of the terms used to label them.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| prefLabel | 1..1 |  | [xs:string](https://www.w3.org/TR/xmlschema-2/#string) |  | The preferred label for the Concept. |
| definition | 0..1 |  | [xs:string](https://www.w3.org/TR/xmlschema-2/#string) |  | A complete explanation of the intended meaning of a concept. |