# ANSIS Python Hacks

## doc_domain

Generates markdown documents containing rtables for each object in schema in the ANSIS Domain JSON
Schema.

> Very specific to the organisation of files/folders in this repo. Often assumes relative path
> names.

```python
def json_schema_to_markdown(
    json_schema_path,               # path to the JSON Schema file to be documented
    json_schema_file,               # name of the JSON Schema file to be documented
    json_schema_instance_file=""    # name of the JSON Schema file identifying core entities to be processed first
)
```

## doc_enum

Gets a JSON-LD representation of a vocabulary from [RVA](https://vocabs.ardc.edu.au/) and converts
it to a simple JSON schema [labelled enumeration](https://github.com/json-schema-org/json-schema-spec/issues/57).
The result is placed in `ansis-enum-working.json` and is then copied into `../schema/enum.json`
manually.

> Process is semi-automated as call to RVA services can fail.

- `const` is the concept's `@id` (compact URI)
- `description` is the concept's `prefLabel`

```python
def get_ansis_enum(
    concept_scheme_id_token,    # the schema specific ID (last part of the container URI)
    base_uri,                   # schema base URI
    prefix,                     # namespace prefix to be used in `const` compact URI.
    working_file_name="code/ansis-enum-working.json"    # output file
)
```

## Dependencies

> The following libraries need to be installed.

### pandas

JSON object manipulation.

`pip install pandas`

### requests

HTTP requests.

`pip install requests`