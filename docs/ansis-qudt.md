# QUDT JSON Objects
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/qudt.json

Reusable QUDT objects for structured property values - e.g. a QUDT quantity: a value/unit pair.

## Entities

### qudt:QuantityValue

*QUDT QuantityValue*. A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure U. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| value | 1..1 |  | [xs:decimal](https://www.w3.org/TR/xmlschema-2/#decimal); [xs:integer](https://www.w3.org/TR/xmlschema-2/#integer) |  | The numerical value. |
| unit | 1..1 |  | [xs:anyURI](https://www.w3.org/TR/xmlschema-2/#anyURI) |  | A reference to the unit of measure of a quantity (variable or constant) of interest. \[ _Restricted to the QUDT vocabulary as a compact URI._ \] |