'''JSON-LD ConceptScheme to JSON Schema Enum functions'''

import json
import requests

def get_compact_uri(uri, base_uri, prefix):
    '''Generate a compact URI for the input uri. Replaces the base_uri with the prefix plus a colon.'''

    compact_uri = uri.replace(base_uri, prefix + ":")

    return compact_uri


def get_concept_preflabel(uri):
    '''Gets a concept's prefLabel.'''

    concept_request = requests.get(
        uri,
        headers = {"Accept": "application/json"})
    
    if concept_request.status_code == 404:
        pref_label = "Not Found"
    else:
        concept_response = json.loads(concept_request.text)
        pref_label = concept_response["result"]["primaryTopic"]["prefLabel"]["_value"]
    
    return pref_label


def get_ansis_enum(concept_scheme_id_token, base_uri, prefix, working_file_name="code/ansis-enum-working.json"):
    '''Convert an ANSIS SKOS Concept Scheme into a JSON Schema Enum.'''

    working_file = open(working_file_name, "w")

    concept_scheme_request = requests.get(
            base_uri + concept_scheme_id_token,
            headers = {"Accept": "application/json"})

    concept_scheme_response = json.loads(concept_scheme_request.text)

    concept_scheme_json = concept_scheme_response["result"]["primaryTopic"]

    enum_object = {}

    enum_object["$anchor"] = concept_scheme_id_token.lower()

    enum_object["@id"] = get_compact_uri(concept_scheme_json["_about"], base_uri, prefix)

    enum_object["title"] = concept_scheme_json["prefLabel"]["_value"]

    if "definition" in concept_scheme_json and isinstance(concept_scheme_json["definition"], str):
        enum_object["description"] = concept_scheme_json["definition"]

    enum_object["type"] = "string"

    enum_object_oneof = []

    for item in concept_scheme_json["member"]:
        enum_object_value = {}
        if isinstance(item, dict):
            member_uri = item["_about"]
        if isinstance(item, str):
            member_uri = item
        enum_object_value["const"] = get_compact_uri(member_uri, base_uri, prefix)
        enum_object_value["description"] = get_concept_preflabel(member_uri)
        enum_object_oneof.append(enum_object_value)

    enum_object["oneOf"] = enum_object_oneof

    enum = {}

    enum_key = concept_scheme_id_token.replace("-"," ").title().replace(" ", "")

    enum[enum_key] = enum_object

    ansis_enum = json.dumps(enum, indent=4)

    working_file.write(ansis_enum)

    working_file.close()

# get_ansis_enum("Disturbance-of-site", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Soil-permeability", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Field-texture-mineral", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Field-texture-organic", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Surface-condition", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Lithology-coarse-fragments", "http://anzsoil.org/def/au/asls/land-surface/", "ls") # issues with content

# get_ansis_enum("Lithology-rock", "http://anzsoil.org/def/au/asls/substrate/", "subst") # scheme not found

# get_ansis_enum("Lithology-unconsolidated", "http://anzsoil.org/def/au/asls/substrate/", "subst") # scheme not found

# get_ansis_enum("Mottle-abundance", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Rock-outcrop-abundance", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Pore-abundance-fine", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pore-abundance-coarse", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Root-abundance", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Segregations-abundance", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Coarse-fragments-abundance", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Cutans-abundance", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Coarse-fragments-shape", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Inundation-duration", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Landform-element-type", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Microrelief-agent-biotic", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Pans-cementation", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# # get_ansis_enum("Horizon-suffix", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Colour-moisture-status", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pedality-grade-pedal", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pedality-grade-apedal", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pedality-size", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Channel-development", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Channel-pattern", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Erosion-severity", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

get_ansis_enum("Relief", "http://anzsoil.org/def/au/asls/landform/", "lf")
