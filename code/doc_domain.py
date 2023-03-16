'''JSON Schema to Mark-down documentation functions'''

import json
import pandas

def json_schema_to_markdown(json_schema_path, json_schema_file):

    '''Takes a JSON Schema and turns it into a table in a mark-down document.'''

    schema_file = open(json_schema_path + json_schema_file, "r")
    core_entity_file = open(json_schema_path + "entity-instance.json", "r")
    md_file = open("docs/ansis-entities.md", "w")

    schema_root = json.loads(schema_file.read())
    core_entity_schema = json.loads(core_entity_file.read())

    core_entities = core_entity_schema["oneOf"]

    core_entities = []
    for entity in core_entity_schema["oneOf"]:
        core_entities.append(entity["$ref"].split("#")[1])

    schema_definitions = pandas.DataFrame(schema_root["definitions"])

    lines = []

    lines.append("# " + schema_root["title"])

    lines.append("**JSON Schema Location:** " + schema_root["$id"] + "\n")

    lines.append(schema_root["description"] + "\n")

    lines.append("> " + schema_root["$comment"] + "\n")

    lines.append("## Core Entities\n")

    for def_key, def_value in schema_definitions.items():
        if def_value["$anchor"] in core_entities:
            lines = process_schema_definitions(def_key, def_value, lines, json_schema_path)

    lines.append("## Other Entities\n")

    for def_key, def_value in schema_definitions.items():
        if def_value["$anchor"] not in core_entities:
            lines = process_schema_definitions(def_key, def_value, lines, json_schema_path)

    md_file.write("\n".join(lines))

    schema_file.close()
    core_entity_file.close()
    md_file.close()

def process_schema_definitions(def_key, def_value, lines, json_schema_path):

    '''Process each individual definition entry.'''
    
    print("Processing definition " + def_key + " ...")
    lines.append("### " + def_value["title"] + " - `ansis:" + def_value["$anchor"] + "`\n")
    lines.append(def_value["description"] + "\n")
    if "$comment" in def_value:
        lines.append("> " + def_value["$comment"] + "\n")
    if "required" in def_value:
        required_properties = def_value["required"]
    if "properties" in def_value:
        schema_properties = pandas.DataFrame(def_value["properties"])
        lines.append("| Property | Value Count | Type | Description |")
        lines.append("| -------- | ----------- | ---- | ----------- |")
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
            if target_reference:
                print("Processing reference " + target_reference + " ...")
                target_property = open_json_pointer(json_schema_path, "entities.json", target_reference)
                # if isinstance(target_property["type"], (list, str)):
                #     if isinstance(target_property["type"], list):
                #         target_property_type = "; ".join(target_property["type"])
                #     else:
                #         target_property_type = target_property["type"]
                # else:
                #     target_property_type = ""
                target_property_type = ""
                target_property_description = ""
                if "range@type" in target_property and isinstance(target_property["range@type"], (str,list)):
                    if isinstance(target_property["range@type"], list):
                        target_property_type = "; ".join(target_property["range@type"])
                    if isinstance(target_property["range@type"], str):
                        target_property_type = target_property["range@type"]
                if "description" in target_property and isinstance(target_property["description"], str):
                    target_property_description = target_property["description"]
            lines.append("| " + prop_key + " | " + MIN_COUNT + ".." + MAX_COUNT + " | " + target_property_type + " | " + target_property_description + " |")
    return lines

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
            print(target_anchor + " found.")
            return def_value
        else:
            print(target_anchor + " not found.")

json_schema_to_markdown("schema/domain/2023-06-30/", "entities.json")

# target_object = open_json_pointer("schema/domain/2023-06-30/", "entities.json", "./geosparql.json#hasGeometry")
# print(target_object["title"])

# open_json_pointer("schema/digital-soil-mapping/2023-06-30/", "dsm.json", "../../domain/2023-06-30/base.json#ld-id")
