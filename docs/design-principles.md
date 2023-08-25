# ANSIS JSON Schema - Design Principles the work proceeds. Will be mashed into something
> coherent at the end.

## Overview

Documents all the decisions made, and patterns adopted when creating the schema. If a decision seems
odd, check here first for submitting an issue - the may be an explanation.

## Core practices

### JSON Schema Version
ANSIS uses JSON Schema version [2020-12]. This is supported by the validators/editors used by ANSIS
staff:
- Altova XMLSpy - best for creating and validating schema documents
- Microsoft Visual Studio Code - best for creating and validating example documents.

### Schema documents
The `domain` schema is made up of multiple sub-schema documents derived from the ANSIS ontology
`domain.ttl` and supporting ontologies (e.g. SOSA and PROV). (Initial attempts as a single schema
generated a document too large to be parsed by many editors):
- `base.json`, `entities.json`, `enum.json`, `properties.json`, `properties-chemical.json`,
`properties-physical.json`: ANSIS entity and property definitions with enumeration objects linking
to ANSIS vocabularies.
- `geo.json`, `prov.json`, `qudt.json`, `sosa.json`: schema derived from external ontologies.

*The JSON Schema must be treated as* views *entirely derived from, or linking to, the ANSIS domain*
*ontology and vocabularies. Any changes to the fundamental structure and definitions of entities,*
*properties and vocabularies must first be dealt with in the domain ontology.*

###  Schema locations
During development, schema can be directly accessed through https://anzsoildata.github.io/def-au-schema-json/schema,
e.g.:
- https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-07-31/entities.json

ANZSoilData [GitHub Pages](https://pages.github.com/) will also used for schema `$id`s. Upon release
the domain/path will switch to https://anzsoil.org/def/au/schema/json/, e.g.:
- https://anzsoil.org/def/au/schema/json/domain/2023-06-30/entities

### Additional properties
Properties prefixed with an underscore extend the JSON Schema to provide additional validation
constraints, or information about sub-schema.
> These are not processed by an schema validator but they are used by the code that generates
documentation so should be modifed with care, if ever.

Additional properties include:
- `_preferred`: a variation on `required` listing properties ANSIS would like provided if possible.
- `_curiPrefix`: links the prefixes used in compact URIs throughout the document. For example:
`"ansis": "https://anzsoil.org/def/au/domain/"` means that the `ansis:` in `ansis:SoilSite` can be
replaced with `https://anzsoil.org/def/au/domain/`, becoming
`https://anzsoil.org/def/au/domain/SoilSite`.
- `_att`, `_obs` and `_rel`: 'helpful' properties in `properties.json` that group property
definitions into simple attributes (`_att`), observable properties (`_obs` - see below), and
relationships - JSON pointers - to other objects (`_rel`).

### Handling ANSIS observable properties
ANSIS makes extensive use of `observable properties` to capture metadata about the observation that
was made to determine an environmental property's value. Values are captured as an object based on a
[`sosa:Observation`](https://www.w3.org/TR/vocab-ssn/#SOSAObservation) and means that environmental
property values should always be a JSON object with the required SOSA properties. To fit into the
encoding pattern established for this schema some tweaks are required
1. The `sosa:observedProperty` is the json key.
1. The required/optional SOSA properties will be set on a property-by-property basis. Quantitative
lab results will have stricter metadata requirements than qualitative field observations.

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

The `_curiPrefix` keyword - adapted from the JSON-LD `@context` key ([definition](https://www.w3.org/TR/json-ld/#the-context)) -
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