# ANSIS JSON Schema - Design Principles

> Currently a catch-all growing organically as the work proceeds. Will be mashed into something
> coherent at the end.

## Overview

Documents all the decisions made, and patterns adopted when creating the schema. If a decision seems
odd, check here first for submitting an issue - the may be an explanation.

## Core practices

### JSON Schema Version
[2020-12] - anchors behave properly in XMLSpy; not supported supported by Visual Studio Code
(highest supported is [draft-07]) when editing schema, but fine when hand-crafting instance
documents (if anything works better than doing the same in XMLSpy).

### Schema documents
The `domain` schema is made up of multiple sub-schema documents derived from the ANSIS ontology
`domain.ttl` and supporting ontologies (e.g. SOSA and PROV). (Initial attempts as a single schema
generated a document too large to be parsed by many editors):
- `base.json`, `entities.json`, `enum.json`, `properties.json`: ANSIS entity and property
definitions with enumeration objects linking to ANSIS vocabularies.
- `geo.json`, `prov.json`, `qudt.json`, `sosa.json`: schema derived from external ontologies.
- `context.json`: {experimental} JSON-LD context document (see Linked Data Alignment below).

Application schema should only need a `application.json` schema file linking to the subset of the
entities and properties needed by the application use case. I hope.

*The JSON Schema must be treated as* views *entirely derived from, or linking to, the ANSIS domain*
*ontology and vocabularies. Any changes to the structure and definitions of entities, properties*
*and vocabularies must first be dealt with in the domain ontology.*

###  Schema locations
During development, schema can be directly accessed through https://anzsoildata.github.io/def-au-schema-json/schema,
e.g.:
- https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/entities.json

ANZSoilData [GitHub Pages](https://pages.github.com/) will also used for schema `$id`s. Upon release
the domain/path will switch to https://anzsoil.org/def/au/schema/json/, e.g.:
- https://anzsoil.org/def/au/schema/json/domain/2023-06-30/entities

### Handling ANSIS observable properties
ANSIS makes extensive use of `observable properties` to capture metadata about the observation that
was made to determine an environmental property's value. Values are captured as a
[`sosa:Observation`](https://www.w3.org/TR/vocab-ssn/#SOSAObservation) and means that environmental
property values should always be a JSON object with the required SOSA properties. To fit into the
encoding pattern established for this schema some tweaks are required
1. The `sosa:observedProperty` is the json key.
1. The required/optional SOSA properties will be set on a property-by-property basis. Quantitative
lab results will have stricter metadata requirements than qualitative field observations.

Core schema observable properties should therefore not be considered sosa:Observations, but can be
directly mapped on to them.

## Linked Data Alignment
[JSON-LD] keywords will be used to help align the JSON schema and instance documents with the ANSIS
domain ontology. As part of a schema definition they provide a non-standard keyword that links a
JSON schema object to its equivalent ANSIS Ontology definition. As the property of a JSON schema
object they help identify and type objects.

The `@id` keyword ([definition](https://www.w3.org/TR/json-ld/#node-identifiers)) in a schema object
definition it is a non-standard keyword that binds the JSON schema definition to the OWL/RDF
definition. In both cases it is the id of the entity, property, vocabulary (enum) or concept (enum
item). The form is an expanded HTTP URI. E.g. https://anzsoil.org/def/au/domain/SoilSite. The schema
`@id` will match the object's `@type` property value.

> The use of expanded URIs allows quick access to the domain ontology by ... clicking on the link.

The `type` keyword  - adapted from the JSON-LD `@type` key ([definition](https://www.w3.org/TR/json-ld/#specifying-the-type)) -
is a property of an object that specifies its type according to both the ANSIS ontology and the JSON
schema - each ontology entity will have a schema object. The value will be a constant for each
schema object. The form will be a compact URI ([CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216/)).
E.g. `ansis:SoilSite`. The `type` value, when expanded to a full URI, will match the object's schema
`@id` value.

> The use of compact URIs helps minimise the size of the object/document/response.

The `curiPrefix` keyword - adapted from the JSON-LD `@context` key ([definition](https://www.w3.org/TR/json-ld/#the-context)) -
is a property of an schema that will bind the curi prefix to the ful URI. This XML namespaces.
The form will be a URL linking to an authoritative ANSIS context document.

> The bare minimum initial use will be to declare the namespaces used in `id` and `type` CURIES.

## Dirty hacks

### $schema keyword
When `additionalProperties` is false the `$schema` needs to be explicitly declared as a property
otherwise (some/all?) validators will reject it.

[draft-07]: https://json-schema.org/draft-07/schema#
[2020-12]:  https://json-schema.org/draft/2020-12/schema
[JSON-LD]:  https://json-ld.org/