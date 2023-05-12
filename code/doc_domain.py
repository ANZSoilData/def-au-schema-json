'''JSON Schema to Mark-down documentation functions'''

import json
import pandas
import dpath

# Yes ... this needs major refactoring into smaller functions.
# ... and explanatory comments.

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

    schema_definitions = pandas.DataFrame(schema_root["$defs"])

    lines = []

    lines.append("# " + schema_root["title"])

    lines.append("**JSON Schema Location:** " + schema_root["$id"] + "\n")

    lines.append(schema_root["description"] + "\n")

    if "$comment" in schema_root and isinstance(schema_root["$comment"], str):
        lines.append("> " + schema_root["$comment"] + "\n")

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


def json_enum_to_markdown(json_schema_path, json_enum_file):
    '''Takes a JSON Enumeration Schema and turns it into a table in a mark-down document.'''

    md_file_name = "docs/ansis-" + json_enum_file.split(".")[0] + ".md"

    enum_file = open(json_schema_path + json_enum_file, "r")
    md_file = open(md_file_name, "w")

    enum_root = json.loads(enum_file.read())

    lines = []

    lines.append("# " + enum_root["title"])

    lines.append("**JSON Schema Location:** " + enum_root["$id"] + "\n")

    lines.append(enum_root["description"] + "\n")

    if "$comment" in enum_root and isinstance(enum_root["$comment"], str):
        lines.append("> " + enum_root["$comment"] + "\n")

    enum_definitions = pandas.DataFrame(enum_root["$defs"])

    for enum_key, enum_value in enum_definitions.items():

        if enum_key != "curiPrefix":

            print("Processing enum", enum_key, "...")

            lines.append("## " + enum_value["title"] + "\n")

            if "@id" in enum_value and isinstance(enum_value["@id"], str):

                enum_uri_prefix = enum_value["@id"].split(":")[0]
                print("enum_uri_prefix: " + enum_uri_prefix)

                if "@context" in enum_root and enum_uri_prefix in enum_root["@context"]:
                    print(enum_root["@context"].get(enum_uri_prefix))
                    enum_location = "[" + enum_value["@id"] + "](" + enum_root["@context"].get(enum_uri_prefix) + enum_value["@id"].split(":")[1] + ")"
                else:
                    enum_location = enum_value["@id"]

                lines.append("**ANSIS Vocabulary Location:** " + enum_location + "\n")

            if "@id" in enum_value and isinstance(enum_value["@id"], list):

                enum_locations = []

                for item in enum_value["@id"]:
                    enum_uri_prefix = item.split(":")[0]
                    print("enum_uri_prefix: " + enum_uri_prefix)

                    if "@context" in enum_root and enum_uri_prefix in enum_root["@context"]:
                        print(enum_root["@context"].get(enum_uri_prefix))
                        enum_location = "[" + item + "](" + enum_root["@context"].get(enum_uri_prefix) + item.split(":")[1] + ")"
                    else:
                        enum_location = item
                    
                    enum_locations.append(enum_location)

                lines.append("**ANSIS Vocabulary Location:** " + "; ".join(enum_locations) + "\n")

            if "description" in enum_value and isinstance(enum_value["description"], str):
                lines.append(enum_value["description"] + "\n")

            if "$comment" in enum_value and isinstance(enum_value["$comment"], str):
                lines.append("> " + enum_value["$comment"] + "\n")

            if "oneOf" in enum_value and isinstance(enum_value["oneOf"], list):
                lines.append(
                    r"| ID/JSON Value | Preferred Label |")
                lines.append(
                    "| ---------- | --------------- |")

                for item in enum_value["oneOf"]:
                    lines.append("| " + item["const"] + " | " + item["description"] + " |")

            lines.append("\n")

    md_file.write("\n".join(lines))

    enum_file.close()
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

        if def_value["properties"] != {}:
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
            else:
                MAX_COUNT = "1"

            if prop_key in ansis_preferred_properties:
                target_property_preferred = "Y"
            else:
                target_property_preferred = ""
                
            target_reference = []
            
            if "$ref" in prop_value and isinstance(prop_value["$ref"], str):
                target_reference.append(prop_value)
                ref_count = ""
            if "oneOf" in prop_value and isinstance(prop_value["oneOf"], list):
                if "$ref" in prop_value["oneOf"] and isinstance(prop_value["oneOf"]["$ref"], str):
                    target_reference.append(prop_value["oneOf"])
                    ref_count = "multi-ref --- "
            if "items" in prop_value and isinstance(prop_value["items"], dict):
                if "$ref" in prop_value["items"] and isinstance(prop_value["items"]["$ref"], str):
                    target_reference.append(prop_value["items"])
                    ref_count = ""
                if "oneOf" in prop_value["items"] and isinstance(prop_value["items"]["oneOf"], list):
                    if "$ref" in prop_value["items"]["oneOf"] and isinstance(prop_value["items"]["oneOf"]["$ref"], str):
                        target_reference.append(prop_value["items"]["oneOf"])
                        ref_count = "multi-ref --- "

            if isinstance(target_reference, list) and len(target_reference) > 0:

                print("Processing reference for", prop_key, "...")

                target_property_dict = open_json_property(
                    json_schema_path, json_schema_file, target_reference)
                
                target_property = target_property_dict["value"]
                nested_property = target_property_dict["nestedValue"]
                target_range = target_property_dict["range@type"]
                nested_range = target_property_dict["nestedRange@type"]

                target_property_type = ""
                nested_property_type = ""

                target_property_enum_ref = []
                target_property_enum = {}
                target_property_vocab_list = []
                target_property_vocab = ""
                target_property_comment = ""
                target_property_description = ""
                nested_property_comment = ""
                nested_property_description = ""

                for index, item in enumerate(target_range):
                    target_range[index] = build_range_type_link(
                        schema_namespace, item)
                target_property_type = "; ".join(
                    target_range)

                for index, item in enumerate(nested_range):
                    nested_range[index] = build_range_type_link(
                        schema_namespace, item)
                nested_property_type = "; ".join(
                    nested_range)
                if len(nested_property_type) > 0:
                    final_property_type = nested_property_type
                else:
                    final_property_type = target_property_type
                            
                if "$comment" in nested_property and isinstance(nested_property["$comment"], str) and nested_property["$comment"] != "":
                    nested_property_comment = " " + nested_property["$comment"]

                if "$comment" in target_property and isinstance(target_property["$comment"], str) and target_property["$comment"] != "":
                    target_property_comment = (r" \[ _" + \
                        target_property["$comment"] + nested_property_comment + r"_ \]").lstrip(" ")

                if "description" in nested_property and isinstance(nested_property["description"], str):
                    nested_property_description = " " + nested_property["description"]

                if "description" in target_property and isinstance(target_property["description"], str):
                    target_property_description = target_property["description"]

                target_property_description = (
                    ref_count + target_property_description + nested_property_description + target_property_comment).lstrip(" ")

                target_property_enum_ref_string = dpath.get(target_property, "/$ref", default="")
                if isinstance(target_property_enum_ref_string,str) and "enum" in target_property_enum_ref_string:
                    target_property_enum_ref.append(target_property_enum_ref_string)
                nested_property_enum_ref_string = dpath.get(nested_property, "/$ref", default="")
                if isinstance(nested_property_enum_ref_string,str) and "enum" in nested_property_enum_ref_string:
                    target_property_enum_ref.append(nested_property_enum_ref_string)
                
                target_property_enum_ref_string = dpath.get(target_property, "/allOf/*/properties/hasResult/$ref", default="")
                if isinstance(target_property_enum_ref_string,str) and "enum" in target_property_enum_ref_string:
                    target_property_enum_ref.append(target_property_enum_ref_string)
                nested_property_enum_ref_string = dpath.get(nested_property, "/allOf/*/properties/hasResult/$ref", default="")
                if isinstance(nested_property_enum_ref_string,str) and "enum" in nested_property_enum_ref_string:
                    target_property_enum_ref.append(nested_property_enum_ref_string)

                target_property_enum_ref_string = dpath.get(nested_property, "/allOf/*/properties/hasResult/oneOf/0/$ref", default="")
                if isinstance(target_property_enum_ref_string,str) and "enum" in target_property_enum_ref_string:
                    target_property_enum_ref_list = dpath.get(nested_property, "/allOf/*/properties/hasResult/oneOf", default=[])
                    for item in target_property_enum_ref_list:
                        target_property_enum_ref_string = dpath.get(item, "/$ref", default="")
                        if isinstance(target_property_enum_ref_string,str) and "enum" in target_property_enum_ref_string:
                            target_property_enum_ref.append(target_property_enum_ref_string)
                nested_property_enum_ref_string = dpath.get(nested_property, "/allOf/*/properties/hasResult/oneOf/0/$ref", default="")
                if isinstance(nested_property_enum_ref_string,str) and "enum" in nested_property_enum_ref_string:
                    nested_property_enum_ref_list = dpath.get(nested_property, "/allOf/*/properties/hasResult/oneOf", default=[])
                    for item in nested_property_enum_ref_list:
                        nested_property_enum_ref_string = dpath.get(item, "/$ref", default="")
                        if isinstance(nested_property_enum_ref_string,str) and "enum" in nested_property_enum_ref_string:
                            target_property_enum_ref.append(nested_property_enum_ref_string)
                
                if target_property_enum_ref != []:
                    for item in target_property_enum_ref:
                        target_property_enum = open_json_enum(
                            json_schema_path, "enum.json", item)
                        target_property_vocab_list.append("[" + target_property_enum["title"] + "](" + "./ansis-enum#" + target_property_enum["title"].lower().replace(" ", "-") + ")")

                target_property_vocab_list = list(set(target_property_vocab_list))

                target_property_vocab = "; ".join(target_property_vocab_list)

            lines.append("| " + prop_key + " | " + MIN_COUNT + ".." + MAX_COUNT + " | " + target_property_preferred +
                         " | " + final_property_type + " | " + target_property_vocab + " | " + target_property_description + " |")

        lines.append("\n")

    return lines


def build_range_type_link(schema_namespace, range_type):
    '''Builds a link to an anchor for the definition of the type.'''

    range_type_anchor = range_type.lower().replace(":", "")
    target_namespace = range_type.split(":")[0]
    target_file = target_namespace.replace("ansis","entities")
    target_name = range_type.split(":")[1]

    range_type_link = range_type

    if target_namespace == "xs":
        range_type_link = "[" + range_type + \
            "](https://www.w3.org/TR/xmlschema-2/#" + target_name + ")"
    else:
        if target_namespace == schema_namespace:
            range_type_link = "[" + range_type + \
                "](#" + range_type_anchor + ")"
        else:
            range_type_link = "[" + range_type + \
                "](./ansis-" + target_file + "#" + \
                range_type_anchor + ")"

    return range_type_link


def open_json_property(json_schema_path, json_schema_file, json_pointer):
    '''Returns a json object (as dictionary) from the location at the provided json_pointer'''

    json_pointer_list = json_pointer[0]["$ref"].split("#")

    if json_pointer_list[0]:
        target_schema_file = json_pointer_list[0]
    else:
        target_schema_file = json_schema_file

    target_anchor = json_pointer_list[1]

    schema_file = open(json_schema_path + target_schema_file, "r")
    schema_root = json.loads(schema_file.read())

    schema_definitions = pandas.DataFrame(schema_root["$defs"])

    def_dict = {}

    for def_key, def_value in schema_definitions.items():
        if dpath.get(def_value, "/$anchor", default = "") == target_anchor:
            print("Found anchor " + target_anchor + " in " + def_key + " ...")
            def_dict["nestedValue"] = {}
            def_dict["value"] = def_value
            break
        if "$defs" in def_value and isinstance(def_value["$defs"], dict):
            def_dict["value"] = def_value
            nested_schema_definitions = pandas.DataFrame(def_value["$defs"])
            for nested_def_key, nested_def_value in nested_schema_definitions.items():
                if nested_def_value["$anchor"] == target_anchor:
                    print("Found nested anchor " + target_anchor + " in " + nested_def_key + " ...")
                    def_dict["nestedValue"] = nested_def_value
                    break

    range_list = []
    range_list_value = []
    nested_range_list = []
    nested_range_list_value = []

    for rangeType in json_pointer:
        rangeType_list = rangeType["$ref"].split("#")
        rangeType_anchor = rangeType_list[1]
        for def_key, def_value in schema_definitions.items():                
            if def_value["$anchor"] == rangeType_anchor:
                range_list_value = dpath.get(def_value, "/range@type", default = [])
                break
            nested_schema_definitions = dpath.get(def_value, "/$defs", default = {})
            if isinstance(nested_schema_definitions, dict):
                for nested_def_key, nested_def_value in nested_schema_definitions.items():
                    if dpath.get(nested_def_value, "/$anchor", default = "") == rangeType_anchor:
                        range_list_value = dpath.get(def_value, "/range@type", default = [])
                        nested_range_list_value = dpath.get(nested_def_value, "/range@type", default = [])
                        break

    schema_file.close()

    if isinstance(range_list_value, list):
        range_list.extend(range_list_value)
    if isinstance(range_list_value, str):
        range_list.append(range_list_value)
    if isinstance(nested_range_list_value, list):
        nested_range_list.extend(nested_range_list_value)
    if isinstance(nested_range_list_value, str):
        nested_range_list.append(nested_range_list_value)

    def_dict["range@type"] = range_list
    def_dict["nestedRange@type"] = nested_range_list

    return def_dict

def open_json_enum(json_schema_path, json_schema_file, json_pointer):
    '''Returns a json object (as dictionary) from the location at the provided json_pointer'''

    json_pointer_list = json_pointer.split("#")

    if json_pointer_list[0]:
        target_schema_file = json_pointer_list[0]
    else:
        target_schema_file = json_schema_file

    target_anchor = json_pointer_list[1]

    schema_file = open(json_schema_path + target_schema_file, "r")
    schema_root = json.loads(schema_file.read())

    schema_definitions = pandas.DataFrame(schema_root["$defs"])

    def_dict = {}

    for def_key, def_value in schema_definitions.items():
        if dpath.get(def_value, "/$anchor", default = "") == target_anchor:
            print("Found anchor " + target_anchor + " in " + def_key + " ...")
            def_dict = def_value
            break

    schema_file.close()

    return def_dict

# json_schema_to_markdown("schema/domain/2023-06-30/", "base.json")

json_schema_to_markdown("schema/domain/2023-06-30/", "entities.json", "entity-instance.json")

# json_schema_to_markdown("schema/domain/2023-06-30/", "geo.json")

# json_schema_to_markdown("schema/domain/2023-06-30/", "prov.json")

# json_schema_to_markdown("schema/domain/2023-06-30/", "qudt.json")

# json_schema_to_markdown("schema/domain/2023-06-30/", "skos.json")

# json_schema_to_markdown("schema/domain/2023-06-30/", "sosa.json")

# json_enum_to_markdown("schema/domain/2023-06-30/", "enum.json")
