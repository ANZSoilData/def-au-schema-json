# ANSIS JSON Schema - Design Principles

> Currently a catch-all growing organically as the work proceeds. Will be mashed into something
> coherent at the end.

## Overview

Documents all the decisions made, and patterns adopted when creating the schema. If a decision seems
odd, check here first for submitting an issue - the may be an explanation.

## Core practices

### Version
 [draft-07] - highest supported by Visual Studio Code, would prefer to use the latest
[2020-12].

### Schema documents
The `core` schema collection is made up of three schema documents. The naming and content are
broadly aligned with the ANSIS ontology RDF files (the ANSIS ontology `domain.ttl` file is split
here into `entities.json` and `properties.json`):
- `entities.json`: class definitions with references to properties.json and enums.json.
- `properties.json`: property definitions.
- `enums.json`: vocabulary definitions.
- `context.json`: {experimental} JSON-LD context document (see Linked Data Alignment below).

Application schema should only need a `entities.json` file. The subset of properties needed by an
application can be references to properties.json in `core`. The same applies for enumerations.
properties and enumerations are references as they may be used by multiple objects.

###  Schema locations
During development, schema can be directly accessed through https://anzsoildata.github.io/def-au-schema-json/,
e.g.:
- https://anzsoildata.github.io/def-au-schema-json/schema/core/0.0/entities.json

ANZSoilData [GitHub Pages](https://pages.github.com/) will also used for schema `$id`s. Upon release
the domain/path will switch to https://anzsoil.org/def/au/schema/json/, e.g.:
- https://anzsoil.org/def/au/schema/json/core/1.0/entities

## Linked Data Alignment
[JSON-LD] keywords will be used to help align the JSON schema and instance documents with the ANSIS
domain ontology. As part of a schema definition they provide a non-standard keyword that links a
JSON schema object to its equivalent ANSIS Ontology definition. As the property of a JSON schema
object they help identify and type objects.

> It is possible, no promises, that the use of these keywords could mean standard ANSIS output could
be converted to RDF by a JSON-LD parser. (This will be tested in the [JSON-LD Playground](https://json-ld.org/playground/).)
Linked Data RDF support will be a bonus and will be discarded if it causes issues defining coherent
JSON schema.

The `@id` keyword ([definition](https://www.w3.org/TR/json-ld/#node-identifiers)) has two uses:
- In a schema object definition it is a non-standard keyword that binds the JSON schema definition
to the OWL/RDF definition. In both cases it is the id of the entity, property, vocabulary (enum) or
concept (enum item). The form is an expanded HTTP URI. E.g. https://anzsoil.org/def/au/domain/SoilSite.
The schema `@id` will match the object's `@type` property value.
- As a property of a JSON object it is the Linked Data identifier of the object. Dereferencing the
URI will return a JSON object (initial default behaviour, in the future: content negotiation). The
form is an expanded HTTP URI. E.g. https://data.ansis.net/id/example/soilsite/042.

> The use of expanded URIs allows quick access to the domain ontology by ... clicking on the link.

The `@type` keyword ([definition](https://www.w3.org/TR/json-ld/#specifying-the-type)) is a property
of an object that specifies its type according to both the ANSIS ontology and the JSON schema - each
ontology entity will have a schema object. The value will be a constant for each schema object. The
form will be a compact URI ([CURIE](https://www.w3.org/TR/2010/NOTE-curie-20101216/)). E.g.
`ansis:SoilSite`. The `@type` value, when expanded to a full URI, will match the object's schema
`@id` value.

> The use of compact URIs helps minimise the size of the object/document/response.

The `@context` keyword ([definition](https://www.w3.org/TR/json-ld/#the-context)) is a property of
an object that will bind The form will be a URL linking to an authoritative ANSIS context document.
The context JSON keys and @type values on to the HTTP URIs identifying them in the ANSIS ontology.

> The bare minimum initial use will be to declare the namespaces used in `@type` CURIES.

## Dirty hacks

### $schema keyword
When `additionalProperties` is false the `$schema` needs to be explicitly declared as a property
otherwise (some/all?) validators will reject it.

[draft-07]: https://json-schema.org/draft-07/schema#
[2020-12]:  https://json-schema.org/draft/2020-12/schema
[JSON-LD]:  https://json-ld.org/