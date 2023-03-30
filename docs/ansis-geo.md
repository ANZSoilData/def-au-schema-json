# OGC GeoSPARQL Property Schema
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/geo.json

JSON Schema definitions of the GeoSPARQL properties used by the ANSIS Domain Ontology.

> Derived from https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/rdf/domain.ttl and http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf.

## Entities

### geo:wktLiteral

*WKT Literal*. A Well-known Text serialization of a geometry object.

> Will use the PostGIS EWKT (Extended Well-known Text) form for ANSIS. Restrict to GDA 2020 (EPSG:7844)?


