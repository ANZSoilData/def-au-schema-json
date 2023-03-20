'''JSON Schema to Mark-down documentation functions'''

import json
import pandas


def json_schema_to_markdown(json_schema_path, json_schema_file, json_schema_instance_file=""):
    '''Takes a JSON Schema and turns it into a table in a mark-down document.'''

    md_file_name = "docs/ansis-" + json_schema_file.split(".")[0] + ".md"

    schema_file = open(json_schema_path + json_schema_file, "r")
    md_file = open(md_file_name, "w")
    if json_schema_instance_file != "":
        core_entity_file_name = json_schema_instance_file
    else:
        core_entity_file_name = json_schema_file
    core_entity_file = open(json_schema_path + core_entity_file_name, "r")

    schema_root = json.loads(schema_file.read())
    core_entity_schema = json.loads(core_entity_file.read())

    if "oneOf" in core_entity_schema:
        core_entities = []
        for entity in core_entity_schema["oneOf"]:
            core_entities.append(entity["$ref"].split("#")[1])
        has_core_entities = True
    else:
        has_core_entities = False

    schema_definitions = pandas.DataFrame(schema_root["definitions"])

    lines = []

    lines.append("# " + schema_root["title"])

    lines.append("**JSON Schema Location:** " + schema_root["$id"] + "\n")

    lines.append(schema_root["description"] + "\n")

    if "$comment" in schema_root and isinstance(schema_root["$comment"], str):
        lines.append("> " + schema_root["$comment"] + "\n")

    print("has_core_entities: ", has_core_entities)

    if has_core_entities:

        core_lines = []

        for def_key, def_value in schema_definitions.items():
            if def_value["$anchor"] in core_entities:
                core_lines = process_schema_definitions(
                    def_key, def_value, core_lines, json_schema_path, json_schema_file)

        if core_lines != []:
            lines.append("## Core Entities\n")

            lines.append(
                "> Core entities are those primary soil and sample entities that are provided, queried and downloaded in ANSIS.\n")

            lines.append("\n".join(core_lines))

        datatype_lines = []

        for def_key, def_value in schema_definitions.items():
            if def_value["$anchor"] not in core_entities:
                datatype_lines = process_schema_definitions(
                    def_key, def_value, datatype_lines, json_schema_path, json_schema_file)

        if datatype_lines != []:

            lines.append("## Datatype Entities\n")

            lines.append("> Datatype entities refer to structured data object that provide values for properties of core entities. They are only provided as property values in core entities.\n")

            lines.append("\n".join(datatype_lines))

    else:

        def_lines = []

        for def_key, def_value in schema_definitions.items():
            def_lines = process_schema_definitions(
                def_key, def_value, def_lines, json_schema_path, json_schema_file)

        if def_lines != []:
            lines.append("## Entities\n")
            lines.append("\n".join(def_lines))

    md_file.write("\n".join(lines))

    schema_file.close()
    core_entity_file.close()
    md_file.close()


def process_schema_definitions(def_key, def_value, lines, json_schema_path, json_schema_file):
    '''Process each individual definition entry.'''

    print("Processing definition " + def_key + " ...")

    if "properties" in def_value and isinstance(def_value["properties"], dict):

        schema_namespace = json_schema_file.split(".")[0].replace("entities", "ansis")

        lines.append("### " + schema_namespace +
                     ":" + def_value["$anchor"] + "\n")
        lines.append("*" + def_value["title"] +
                     "*. " + def_value["description"] + "\n")

        if "$comment" in def_value and isinstance(def_value["$comment"], str):
            lines.append("> " + def_value["$comment"] + "\n")

        if "required" in def_value and isinstance(def_value["required"], list):
            required_properties = def_value["required"]
        else:
            required_properties = []

        if "ansisPreferred" in def_value and isinstance(def_value["ansisPreferred"], list):
            ansis_preferred_properties = def_value["ansisPreferred"]
        else:
            ansis_preferred_properties = []

        schema_properties = pandas.DataFrame(def_value["properties"])

        lines.append(
            r"| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |")
        lines.append(
            "| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |")

        for prop_key, prop_value in schema_properties.items():

            print("Processing property " + prop_key + " ...")

            if prop_key in required_properties:
                MIN_COUNT = "1"
            else:
                MIN_COUNT = "0"

            if "type" in prop_value and prop_value["type"] == "array":
                MAX_COUNT = "*"
                target_reference = prop_value["items"]["$ref"]
            else:
                MAX_COUNT = "1"
                target_reference = prop_value["$ref"]

            if prop_key in ansis_preferred_properties:
                target_property_preferred = "Y"
            else:
                target_property_preferred = ""

            if target_reference:

                print("Processing reference " + target_reference + " ...")

                target_property = open_json_pointer(
                    json_schema_path, json_schema_file, target_reference)

                target_property_type = ""

                target_property_enum_ref = ""
                target_property_enum = {}
                target_property_vocab = ""
                target_property_comment = ""
                target_property_description = ""

                if "range@type" in target_property and isinstance(target_property["range@type"], (str, list)):
                    if isinstance(target_property["range@type"], list):
                        for index, item in enumerate(target_property["range@type"]):
                            target_property["range@type"][index] = build_range_type_link(
                                schema_namespace, item)
                        target_property_type = "; ".join(
                            target_property["range@type"])
                    if isinstance(target_property["range@type"], str):
                        target_property_type = build_range_type_link(
                            schema_namespace, target_property["range@type"])

                if "$comment" in target_property and isinstance(target_property["$comment"], str) and target_property["$comment"] != "":
                    target_property_comment = r" \[ _" + \
                        target_property["$comment"] + r"_ \]"

                if "description" in target_property and isinstance(target_property["description"], str):
                    target_property_description = target_property["description"]
                target_property_description = (
                    target_property_description + target_property_comment).lstrip(" ")

                if "$ref" in target_property and isinstance(target_property["$ref"], str) and "enum" in target_property["$ref"]:
                    target_property_enum_ref = target_property["$ref"]

                if "allOf" in target_property and isinstance(target_property["allOf"], list):
                    if isinstance(target_property["allOf"][0]["properties"]["hasResult"]["$ref"], str) and "enum" in target_property["allOf"][0]["properties"]["hasResult"]["$ref"]:
                        target_property_enum_ref = target_property[
                            "allOf"][0]["properties"]["hasResult"]["$ref"]

                if target_property_enum_ref != "":
                    target_property_enum = open_json_pointer(
                        json_schema_path, "entities.json", target_property_enum_ref)
                    target_property_vocab = target_property_enum["title"]

            lines.append("| " + prop_key + " | " + MIN_COUNT + ".." + MAX_COUNT + " | " + target_property_preferred +
                         " | " + target_property_type + " | " + target_property_vocab + " | " + target_property_description + " |")

    return lines


def build_range_type_link(schema_namespace, range_type):
    '''Builds a link to an anchor for the definition of the type.'''

    target_namespace = range_type.split(":")[0]
    target_file = target_namespace.replace("ansis","entities")
    target_name = range_type.split(":")[1]

    print("schema_namespace:", schema_namespace, " target_namespace: ", target_namespace)

    range_type_link = range_type

    if target_namespace == "xs":
        range_type_link = "[" + range_type + \
            "](https://www.w3.org/TR/xmlschema-2/#" + target_name + ")"
    else:
        if target_namespace == schema_namespace:
            range_type_link = "[" + range_type + \
                "](#" + range_type.replace(":", "") + ")"
        else:
            range_type_link = "[" + range_type + \
                "](./ansis-" + target_file + ".md#" + \
                range_type.replace(":", "") + ")"

    return range_type_link


def open_json_pointer(json_schema_path, json_schema_file, json_pointer):
    '''Returns a json object (as dictionary) from the location at the provided json_pointer'''

    json_pointer_list = json_pointer.split("#")

    if json_pointer_list[0]:
        target_schema_file = json_pointer_list[0]
    else:
        target_schema_file = json_schema_file

    target_anchor = json_pointer_list[1]

    schema_file = open(json_schema_path + target_schema_file, "r")
    schema_root = json.loads(schema_file.read())

    schema_definitions = pandas.DataFrame(schema_root["definitions"])

    for def_key, def_value in schema_definitions.items():
        print("Searching for anchor " + target_anchor + " in " + def_key + " ...")
        if def_value["$anchor"] == target_anchor:
            return def_value

json_schema_to_markdown("schema/domain/2023-06-30/", "base.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "entities.json", "entity-instance.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "geosparql.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "prov.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "qudt.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "skos.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "sosa.json")
