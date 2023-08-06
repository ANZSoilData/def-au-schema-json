# QUDT JSON Objects
**JSON Schema Location:** [qudt.json](qudt.json)

Reusable QUDT objects for structured property values - e.g. a QUDT quantity: a value/unit pair.

## Entities

### QuantityValue

Type: *qudt:QuantityValue*. QUDT QuantityValue. A Quantity Value expresses the magnitude and kind of a quantity and is given by the product of a numerical value n and a unit of measure U. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit.

| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |
| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |
| value | 1..1 |  | [JSON number](https://json-schema.org/understanding-json-schema/reference/type.html) |  | The numerical value. |
| unit | 1..1 |  | [JSON string \(iri\)](https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats) |  | A reference to the unit of measure of a quantity (variable or constant) of interest. \[ _Restricted to the QUDT vocabulary as a compact URI._ \] |


## Enumerations

### Unit

**ANSIS Vocabulary Location:** https://qudt.org/2.1/vocab/unit

Units of measure as defined by QUDT.

> A JSON Schema labelled enumeration.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| unit:DEG | degree (angle) |
| unit:M | meter |
| unit:PERCENT | percent |

