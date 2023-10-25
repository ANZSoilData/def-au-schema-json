# ANSIS JSON Schema - 2023-07-31

## Overview
JSON schema files for the ANSIS project, first version.

## Contents

| Schema | Title    | Description |
| ------ | ---------- | -------- |
| [ansis.json](ansis.json) | ANSIS Root Entity Schema | Identifies root elements currently served by ANSIS. |
| [entities.json](entities.json) | ANSIS Soil Domain Entity Schema | JSON Schema definitions of the complete list of entities (features in GIS speak) defined in or imported by the ANSIS Domain Ontology. |
| [enum.json](enum.json) | ANSIS Soil Domain Enumerations | ANSIS controlled vocabularies converted to JSON schema enumerations. Follow the link under the vocabulary's title for full definitions. |
| [properties.json](properties.json) | ANSIS Soil Domain Property Schema | JSON Schema definitions of the complete list of properties defined in the ANSIS Domain Ontology. These definitions are referenced by objects in feature/entity schema and may be referenced by multiple objects - i.e. the scope (domain) of a property is not restricted to a single object (entity). |
| [properties-chemical.json](properties-chemical.json) | ANSIS Soil Chemical Property Schema | JSON Schema definitions of the complete list of soil chemical properties defined in the ANSIS Domain Ontology. Derived from Soil Chemical Methods – Australasia. (The 'Green Book'.) |
| [properties-physical.json](properties-physical.json) | ANSIS Soil Physical Property Schema | JSON Schema definitions of the complete list of soil physical properties defined in the ANSIS Domain Ontology. Derived from Soil Physical Measurement and Interpretation for Land Evaluation. (The 'Brown Book'.) |
| [base.json](base.json) | ANSIS JSON Base Schema | Base properties and objects used to identify, type and link entities, bind them to schema, and otherwise describe objects from a system, rather than domain, perspective. |
| [geo.json](geo.json) | OGC GeoSPARQL Property Schema | JSON Schema definitions of the GeoSPARQL properties used by the ANSIS Domain Ontology. |
| [prov.json](prov.json) | PROV Entity Schema | JSON Schema definitions of the PROV Ontology entities used by ANSIS. |
| [qudt.json](qudt.json) | QUDT JSON Objects | Reusable QUDT objects for structured property values - e.g. a QUDT quantity: a value/unit pair. |
| [skos.json](skos.json) | SKOS JSON Objects | Reusable SKOS objects for vocabulary entries. Created to provide a definition for skos:Concept references elsewhere in the schema. Actually implemented with enumerations in JSON instances. |
| [sosa.json](sosa.json) | SOSA Entity Schema | JSON Schema definitions of the [SOSA](https://www.w3.org/TR/vocab-ssn/) entities used by ANSIS. |
