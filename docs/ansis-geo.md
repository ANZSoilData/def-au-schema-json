# OGC GeoSPARQL Property Schema
**JSON Schema Location:** [geo.json](geo.json)

JSON Schema definitions of the GeoSPARQL properties used by the ANSIS Domain Ontology.

> Derived from https://raw.githubusercontent.com/ANZSoilData/def-au-domain/main/rdf/domain.ttl and http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf.

## Entities

### geometry

Type: *geo:geometry*. geometry. The default geometry to be used in spatial calculations. It is Usually the most detailed geometry.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| result | 1..1 |  | [JSON string](https://json-schema.org/understanding-json-schema/reference/type.html) |  | A Well-known Text serialization of a geometry object. \[ _Will use the PostGIS EWKT (Extended Well-known Text) form for ANSIS, e.g. SRID=4283;POINT(-42 24). Restrict to GDA94 (EPSG code 4283)._ \] |

