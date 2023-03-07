# ANSIS JSON(-LD) Schema

> **Active development of ANSIS Schema is in the branch version-0.0. Switch to that branch for the**
> **latest, but not necessarily stable, versions of the schema.**

## Overview

This repository holds JSON (with a JSON-LD flavour) Schema developed for the Australian National
Soil Information System ([ANSIS](https://ansis.net/)). The authoritative ANSIS information model has
been developed as an OWL/RDF ontology, also published in this GitHub organisation at
[`ANZSoilData/def-au-domain`][def-au-domain]. These schema are a representation of that ontology.
They do not introduce new domain entities or properties, and all definitions are copied verbatim
from `def-au-domain`. They are created to support JSON representations of data suitable for use in
'typical' web APIs and for processing by widely used programming libraries. As such they remove some
OWL/RDF artefacts necessary for the definition of a robust ontology* but not commonly required for
JSON objects.

> \* These artefacts reflect the fundamental importance of set theory and reasoning to OWL/RDF. We
> anticipate that future versions ANSIS will provide Semantic Web APIs that support reasoning and
> inferencing. The JSON schema and RDF approaches should therefore be considered complimentary.

Several collections of schema will be provided:
- The `domain` schema represents the full ANSIS information model as structured data (i.e. related
complex objects). ANSIS data providers should refer to this schema for guidance on what data ANSIS
may require for all of its use cases.
- Additional 'application schema' will define subsets of the `domain` schema for particular use
cases. These may denormalise the data for certain data types - e.g. GIS Layers or spreadsheets.
ANSIS data providers should use these schema for guidance on supporting a specific ANSIS use case.

The principles guiding the design of the schema are documented [here](./docs/design-principles.md).


## Contributing

Please raise any issues in MS Teams in the ANSIS *1.3.2 Data Standards Project* team chat.

Non-ANSIS project members can contact [Peter Wilson](mailto:peter.wilson@csiro.au).

When providing feedback or raising issues, please note the relationship between the JSON schema
and the domain ontology:
1. Contributions concerning the definitions of entities, properties and enumerations (vocabularies)
relate to the domain ontology and should be made in the context of the domain ontology.
2. Contributions concerning the use of JSON Schema and using documents generated to conform to these
scheme should be made in this context.

We urge contributors to be familiar with the [domain ontology][def-au-domain],
[JSON Schema](https://json-schema.org/) and the
[JSON Schema Specification](https://json-schema.org/specification.html).

> This work currently uses `draft-07` of the specification.


## Navigating this repository

This repository is broken into four folders:
1. The [`schema`](schema/) folder holds the collections of ANSIS schema.
2. The [`data`](data/) folder holds example JSON documents (e.g. an example SoilSite).
3. The [`docs`](docs/) folder holds documentation of the schema.
4. The [`figs`](figs/) folder holds images used by documents elsewhere in the repository.

[def-au-domain]: https://github.com/ANZSoilData/def-au-domain