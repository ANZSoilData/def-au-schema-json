# ANSIS JSON Schema

## Overview
JSON schema files for the ANSIS project.

## Contents

| Schema | Version    | Comments |
| ------ | ---------- | -------- |
| domain | 2023-06-30 | ANSIS schema broken into manageable sub-schema based on object type (entity, property etc) and source (non-ANSIS elements have their own schema - e.g. `sosa.json` for ... SOSA.) |
| digital-soil-mapping | 2023-06-30 | \[EXPERIMENTAL\] Minimalist structure for the provision of soil property values at a specific location for digital soil mapping. Based on web services that provided data to the [TERN Soil Data Federator](https://aussoilsdsm.esoil.io/site-data/soildatafederator). |

## Documentation
Full documentation of the schema can be found in the [docs folder](../docs/README.md).

## Sample data
Example JSON documents can be found in the [data folder](../data/README.md).