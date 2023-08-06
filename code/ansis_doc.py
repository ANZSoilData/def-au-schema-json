'''JSON Schema to Mark-down documentation functions'''

import json
import dpath


def json_schema_to_markdown(json_schema_file_path, json_schema_file_name, contains_enum=False):
    '''Take a JSON Schema and turns it into a table in a mark-down document.'''

    md_file_name = "docs/ansis-" + json_schema_file_name.split(".")[0] + ".md"

    schema_file = open(json_schema_file_path + json_schema_file_name, "r", encoding="utf8")

    md_file = open(md_file_name, "w", encoding="utf8")

    schema_root = json.loads(schema_file.read())

    schema_definitions = {}

    if "$defs" in schema_root:
        schema_definitions = schema_root["$defs"]
    else:
        schema_definitions["Document"] = schema_root

    lines = []

    lines.append("# " + schema_root["title"])

    lines.append("**JSON Schema Location:** [" + schema_root["$id"] + "](" + schema_root["$id"] + ")\n")

    lines.append(schema_root["description"] + "\n")

    if "$comment" in schema_root and isinstance(schema_root["$comment"], str):
        lines.append("> " + schema_root["$comment"] + "\n")

    def_lines = []

    for def_key, def_value in schema_definitions.items():
        def_lines = process_schema_definitions(
            def_key, def_value, def_lines, json_schema_file_path, json_schema_file_name)

    if def_lines:
        lines.append("## Entities\n")
        lines.append("\n".join(def_lines))

    if contains_enum:
        lines.append("## Enumerations\n")
        for enum_key, enum_value in schema_definitions.items():
            lines = process_enum_definitions(enum_key, enum_value, lines, schema_file, 2)

    md_file.write("\n".join(lines))

    schema_file.close()

    md_file.close()


def json_enum_to_markdown(json_schema_path, json_enum_file, include_header=True):
    '''Takes a JSON Enumeration Schema and turns it into a table in a mark-down document.'''

    md_file_name = "docs/ansis-" + json_enum_file.split(".")[0] + ".md"

    enum_file = open(json_schema_path + json_enum_file, "r", encoding="utf8")
    md_file = open(md_file_name, "w", encoding="utf8")

    enum_root = json.loads(enum_file.read())

    lines = []

    if include_header:
        lines.append("# " + enum_root["title"])

        lines.append("**JSON Schema Location:** " + enum_root["$id"] + "\n")

        lines.append(enum_root["description"] + "\n")

        if "$comment" in enum_root and isinstance(enum_root["$comment"], str):
            lines.append("> " + enum_root["$comment"] + "\n")

        header_level = 1
    else:
        lines.append("## Enumerations")
        header_level = 2

    enum_definitions = enum_root["$defs"]

    for enum_key, enum_value in enum_definitions.items():
        lines = process_enum_definitions (enum_key, enum_value, lines, enum_root, header_level)

    md_file.write("\n".join(lines))

    enum_file.close()
    md_file.close()


def process_enum_definitions (enum_key, enum_value, lines, enum_root, header_level=1):
    '''Process each individual definition entry.'''

    enum_test = dpath.get(enum_value, "/oneOf/0/const", default = False)

    print("enum_test:", enum_test)

    if enum_key != "curiPrefix" and enum_test:

        print("Processing enum", enum_key, "...")

        lines.append("#" * (header_level + 1) + " " + enum_value["title"] + "\n")

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
                if "$comment" in item and isinstance(item["$comment"], str) and item["$comment"] != "":
                    enum_value_comment = (r" \[ _" +  item["$comment"] + r"_ \]")
                else:
                    enum_value_comment = ""
                lines.append("| " + item["const"] + " | " + item["description"] + enum_value_comment + " |")

        lines.append("\n")

    return lines


def process_schema_definitions(def_key, def_value, lines, json_schema_file_path, json_schema_file_name):
    '''Process each individual definition entry.'''

    print("Processing definition " + def_key + " ...")

    # enum_test = dpath.get(def_value, "/oneOf/0/const", default = False)

    # get base properties for an entity

    required_properties = []
    preferred_properties = []
    base_properties = {}

    if "properties" in def_value and isinstance(def_value["properties"], dict):
        base_properties = def_value["properties"]
    if "required" in def_value and isinstance(def_value["required"], list):
        required_properties = def_value["required"]
    if "_preferred" in def_value and isinstance(def_value["_preferred"], list):
        preferred_properties = def_value["_preferred"]

    if "allOf" in def_value and isinstance(def_value["allOf"], list):
         for thing in def_value["allOf"]:
            if "properties" in thing and isinstance(thing["properties"], dict):
                base_properties = thing["properties"]
            if "required" in thing and isinstance(thing["required"], list):
                required_properties = thing["required"]
            if "_preferred" in thing and isinstance(thing["_preferred"], list):
                preferred_properties = thing["_preferred"]

    if base_properties and isinstance(base_properties, dict): #and not enum_test:

        schema_namespace = json_schema_file_name.split(".")[0]

        # rename entities and base
        schema_namespace = schema_namespace.replace("entities", "ansis")
        schema_namespace = schema_namespace.replace("base", "ansis-base")

        lines.append("### " + def_key + "\n")
        lines.append("Type: *" + schema_namespace + ":" + def_key +
                     "*. " + def_value["title"] + ". " + def_value["description"] + "\n")

        if "$comment" in def_value and isinstance(def_value["$comment"], str):
            lines.append("> " + def_value["$comment"] + "\n")

        # if def_value["properties"] != {}:
        lines.append(
            r"| Property | Value Count | ANSIS Preferred | Type | Vocabulary | Description \[ _Comment_ \] |")
        lines.append(
            "| -------- | ----------- | --------------- | ---- | ---------- | ------------------------- |")

        for prop_key, prop_value in base_properties.items():

            print("Processing property " + prop_key + " ...")

            if prop_key in required_properties:
                MIN_COUNT = "1"
            else:
                MIN_COUNT = "0"

            if "type" in prop_value and prop_value["type"] == "array":
                MAX_COUNT = "*"
            else:
                MAX_COUNT = "1"

            if prop_key in preferred_properties:
                target_property_preferred = "Y"
            else:
                target_property_preferred = ""

            md_property_type = ""
            md_property_vocab = ""
            md_property_description = ""

            target_reference = []

            if "$ref" in prop_value and isinstance(prop_value["$ref"], str):
                target_reference.append(prop_value)
            if "oneOf" in prop_value and isinstance(prop_value["oneOf"], list):
                if "$ref" in prop_value["oneOf"] and isinstance(prop_value["oneOf"]["$ref"], str):
                    target_reference.append(prop_value["oneOf"])
            if "items" in prop_value and isinstance(prop_value["items"], dict):
                if "$ref" in prop_value["items"] and isinstance(prop_value["items"]["$ref"], str):
                    target_reference.append(prop_value["items"])
                if "oneOf" in prop_value["items"] and isinstance(prop_value["items"]["oneOf"], list):
                    if "$ref" in prop_value["items"]["oneOf"] and isinstance(prop_value["items"]["oneOf"]["$ref"], str):
                        target_reference.append(prop_value["items"]["oneOf"])
                        ref_count = "multi-ref --- "

            if isinstance(target_reference, list) and len(target_reference) > 0:

                print("Processing reference for", prop_key, "...")

                target_property_dict = get_property_def(
                    json_schema_file_path, json_schema_file_name, target_reference)

                if "type" in target_property_dict and isinstance(target_property_dict["type"], str):
                    md_property_type = target_property_dict["type"]
                elif "refType" in target_property_dict and isinstance(target_property_dict["_refType"], str):
                    md_property_type = target_property_dict["_refType"]

                if "description" in target_property_dict and isinstance(target_property_dict["description"], str):
                    md_property_description = target_property_dict["description"]

                if "enumeration" in target_property_dict and isinstance(target_property_dict["enumeration"], str):
                    md_property_vocab = target_property_dict["enumeration"]

            lines.append("| " + prop_key + " | " + MIN_COUNT + ".." + MAX_COUNT + " | " + target_property_preferred +
                         " | " + md_property_type + " | " + md_property_vocab + " | " + md_property_description + " |")

        lines.append("\n")

    return lines


def get_property_def(json_schema_file_path, json_schema_file_name, json_pointers):
    '''Builds a property definition from the provided pointer'''

    for pointer in json_pointers:
        pointer_list = pointer["$ref"].split("#")
        pointer_schema_file = pointer_list[0]
        if pointer_schema_file:
            target_schema_file = pointer_schema_file
        else:
            target_schema_file = json_schema_file_name

        schema_file = open(json_schema_file_path + target_schema_file, "r")
        schema_root = json.loads(schema_file.read())

        pointer_path = pointer_list[1]
        pointer_keys = list(filter(None, pointer_path.split("/$defs/")))

        property_def = {}

        property_def = get_property_def_attributes(schema_root, pointer_keys, json_schema_file_name)

        return property_def


def get_property_def_attributes(schema_root, pointer_keys, json_schema_file_name):

    property_def = {}
    property_comment = []
    property_description_comment = ""
    property_description = []

    if pointer_keys[0] in ["_astd","_obs","_rel"]:
        target_path_root = "/$defs/" + pointer_keys[0] + "/$defs/"
        pointer_keys.remove(pointer_keys[0])
    else:
        target_path_root = "/$defs/"

    target_position = 0
    full_path = target_path_root + '/$defs/'.join(pointer_keys)
    schema_def = dpath.get(schema_root, full_path, default=[])

    property_defs = process_pointer(schema_def, json_schema_file_name, property_def={})

    # loop through pointer definitions to build a description with comments
    for pointer in pointer_keys:
        if target_position > 0:
            target_path = target_path + '/$defs/' + pointer
        else:
            target_path = target_path_root + pointer
        property_description_value = dpath.get(schema_root, target_path + "/description", default="")
        if property_description_value != "":
            property_description.append(property_description_value)
        property_comment_value = dpath.get(schema_root, target_path + "/$comment", default="")
        if property_comment_value != "":
            property_comment.append(property_comment_value)
        target_position = target_position + 1

    if "type" in property_defs:
        property_def["type"] = "; ".join(property_defs["type"])
    if "enumeration" in property_defs:
        property_def["enumeration"] = "; ".join(property_defs["enumeration"])
    if property_comment:
        property_description_comment = " \[ _" + " ".join(property_comment) + "_ \]"
    if property_description:
        property_def["description"] = " ".join(property_description) + property_description_comment

    return property_def


def process_pointer(pointer, json_schema_file_name, property_def=None):

    if property_def:
        if "type" in property_def:
            property_type = property_def["type"]
        else:
            property_type = []
        if "enumeration" in property_def:
            property_enum = property_def["enumeration"]
        else:
            property_enum = []
    else:
        property_def = {}
        property_type = []
        property_enum = []

    if "$ref" in pointer and isinstance(pointer["$ref"],str):
        if pointer["$ref"].find("enum.json") > -1:
            if "Enumeration" not in property_type:
                property_type.append("Enumeration")
            property_enum.append(build_md_link_from_ref(pointer["$ref"], json_schema_file_name))
        elif pointer["$ref"].find("/$defs/pointer") > -1:
            property_type.append("Pointer")
            if "_refType" in pointer and isinstance(pointer["_refType"],str):
                property_type.append(build_md_link_from_ref(pointer["_refType"], json_schema_file_name))
        elif "allOf" in pointer["$ref"] and isinstance(pointer["$ref"]["allOf"],list):
            for each in pointer["$ref"]["allOf"]:
                allof = process_pointer(each, json_schema_file_name, property_def)
                if "type" in allof and isinstance(allof["type"],list):
                    property_def["type"] = allof["type"]
                if "enumeration" in allof and isinstance(allof["enumeration"],list):
                    property_def["enumeration"] = allof["enumeration"]
        elif "oneOf" in pointer["$ref"] and isinstance(pointer["$ref"]["oneOf"],list):
            for each in pointer["$ref"]["oneOf"]:
                oneof = process_pointer(each, json_schema_file_name, property_def)
                if "type" in oneof and isinstance(oneof["type"],list):
                    property_def["type"] = oneof["type"]
                if "enumeration" in oneof and isinstance(oneof["enumeration"],list):
                    property_def["enumeration"] = oneof["enumeration"]
        else:
            property_type_link = build_md_link_from_ref(pointer["$ref"], json_schema_file_name)
            if property_type_link not in property_type:
                property_type.append(property_type_link)
        property_def["type"] = property_type
        property_def["enumeration"] =  property_enum
    elif "properties" in pointer and isinstance(pointer["properties"],dict):
        if "result" in pointer["properties"] and isinstance(pointer["properties"]["result"],dict):
            property_def = process_pointer(pointer["properties"]["result"], json_schema_file_name, property_def)
    elif "allOf" in pointer and isinstance(pointer["allOf"],list):
        for each in pointer["allOf"]:
            allof = process_pointer(each, json_schema_file_name, property_def)
            if "type" in allof and isinstance(allof["type"],list):
                property_def["type"] = allof["type"]
            if "enumeration" in allof and isinstance(allof["enumeration"],list):
                property_def["enumeration"] = allof["enumeration"]
    elif "oneOf" in pointer and isinstance(pointer["oneOf"],list):
        for each in pointer["oneOf"]:
            oneof = process_pointer(each, json_schema_file_name, property_def)
            if "type" in oneof and isinstance(oneof["type"],list):
                property_def["type"] = oneof["type"]
            if "enumeration" in oneof and isinstance(oneof["enumeration"],list):
                property_def["enumeration"] = oneof["enumeration"]
    else:
        if "format" in pointer and isinstance(pointer["format"],str):
            property_type.append("[JSON string \(" + pointer["format"] + "\)](https://json-schema.org/understanding-json-schema/reference/string.html#built-in-formats)")
        elif "type" in pointer and isinstance(pointer["type"],str):
            property_type.append("[JSON " + pointer["type"] + "](https://json-schema.org/understanding-json-schema/reference/type.html)")
        property_def["type"] = property_type

    return property_def


def build_md_link_from_ref(ref_string, json_schema_file_name):
    '''Builds a link to an anchor for the definition of the type.'''

    ref_label = ref_string.rsplit('/', 1)[-1]

    if ref_string.find(json_schema_file_name) > -1:
        ref_path = "#" + ref_label
    else:
        ref_path = ref_string.replace("./", "./ansis-")
        ref_path = ref_path.replace(".json", ".md")
        ref_path = ref_path.replace("/$defs/", "")

    md_link = "[" + ref_label + "](" + ref_path + ")"

    return md_link


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

json_enum_to_markdown("schema/domain/2023-07-31/", "enum.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "base.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "entities.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "geo.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "proj.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "prov.json")

# json_schema_to_markdown("schema/domain/2023-07-31/", "qudt.json", True)

# json_schema_to_markdown("schema/domain/2023-07-31/", "sosa.json")
