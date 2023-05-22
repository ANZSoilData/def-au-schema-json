# OGC GeoSPARQL Property Schema
**JSON Schema Location:** geo.json

JSON Schema definitions of the GeoSPARQL properties used by the ANSIS Domain Ontology.

> Derived from https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/rdf/domain.ttl and http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf.

## Entities

### geo:wktLiteral

*WKT Literal*. A Well-known Text serialization of a geometry object.

> Will use the PostGIS EWKT (Extended Well-known Text) form for ANSIS, e.g. SRID=4283;POINT(-42 24). Restrict to GDA94 (EPSG code 4283).


