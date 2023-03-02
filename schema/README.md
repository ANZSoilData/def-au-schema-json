# ANSIS JSON Schema

## Overview
JSON schema files for the ANSIS project.

## Contents

| Schema | Version    | Comments |
| ------ | ---------- | -------- |
| core   | 0.0        | **\[DEPRECATED\]** Monster schema in one document (`domain.json`). Too large to be processed by many validators and/or editors. Will be humanely destroyed. |
| domain | 2023-06-30 | ANSIS schema broken into manageable sub-schema based on object type (entity, property etc) and source (non-ANSIS elements have their own schema - e.g. `sosa.json` for ... SOSA.) |

## Documentation
Full documentation of the schema can be found in the [docs folder](../docs/README.md).

## Sample data
Example JSON documents can be found in the [data folder](../data/README.md).