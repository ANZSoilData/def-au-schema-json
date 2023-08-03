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

def get_concept_narrower_concepts(uri):
    '''Gets a concept's narrower concepts.'''

    concept_request = requests.get(
        uri,
        headers = {"Accept": "application/json"})
    
    narrower_concepts = []

    if concept_request.status_code == 404:
        narrower_concepts = "Not Found"
    else:
        concept_response = json.loads(concept_request.text)
        if "narrower" in concept_response["result"]["primaryTopic"] and isinstance(concept_response["result"]["primaryTopic"]["narrower"], list):
            narrower_concepts = concept_response["result"]["primaryTopic"]["narrower"]
            for concept in narrower_concepts:
                narrower_concepts = narrower_concepts + get_concept_narrower_concepts(concept["_about"])

    return narrower_concepts

def get_ansis_enum(concept_scheme_id_token, base_uri, prefix, working_file_name="code/ansis-enum-working.json"):
    '''Convert an ANSIS SKOS Concept Scheme into a JSON Schema Enum.'''

    print("Processing", prefix + ":" + concept_scheme_id_token, "...")

    working_file = open(working_file_name, "w")

    concept_scheme_request = requests.get(
            base_uri + concept_scheme_id_token,
            headers = {"Accept": "application/json"})

    if concept_scheme_request.status_code == 200:

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

        if "member" in concept_scheme_json:
            for item in concept_scheme_json["member"]:
                enum_object_value = {}
                if isinstance(item, dict):
                    member_uri = item["_about"]
                if isinstance(item, str):
                    member_uri = item
                const = get_compact_uri(member_uri, base_uri, prefix)
                print("    ... adding", const, "...")
                enum_object_value["const"] = const
                enum_object_value["description"] = get_concept_preflabel(member_uri)
                enum_object_oneof.append(enum_object_value)
                narrower_concepts = get_concept_narrower_concepts(member_uri)
                if isinstance(narrower_concepts, list):
                    for narrower in narrower_concepts:
                        enum_object_value = {}
                        if isinstance(narrower, dict):
                            member_uri = narrower["_about"]
                        if isinstance(narrower, str):
                            member_uri = item
                        const = get_compact_uri(member_uri, base_uri, prefix)
                        print("    ... adding", const, "...")
                        enum_object_value["const"] = const
                        enum_object_value["description"] = get_concept_preflabel(member_uri)
                        enum_object_oneof.append(enum_object_value)
            enum_object["oneOf"] = enum_object_oneof
        else:
            enum_object["$comment"] = "No skos:members found."

        enum = {}

        enum_key = concept_scheme_id_token.replace("-"," ").title().replace(" ", "")

        enum[enum_key] = enum_object

        ansis_enum = json.dumps(enum, indent=4)

        print("    ... writing to file ...")

        working_file.write(ansis_enum)

    else:
        print ("    ... request not OK:", concept_scheme_request.status_code, "...")
        working_file.write(concept_scheme_request.text)

    print ("... done.")

    working_file.close()

get_ansis_enum("Disturbance-of-site", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Soil-permeability", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Field-texture-mineral", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Field-texture-organic", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Surface-condition", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Lithology-coarse-fragments", "http://anzsoil.org/def/au/asls/land-surface/", "ls") # issues with content

# get_ansis_enum("Lithology-rock-outcrop", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Lithology-rock", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Lithology-unconsolidated", "http://anzsoil.org/def/au/asls/substrate/", "subst")

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

# get_ansis_enum("Relief", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-bio", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-extra", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-gravity", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-ice", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-internal", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-precipitation", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-stand", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-streamflow", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-agent-wind", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Aggradation", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Rock-alteration", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Landform-element-name", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Landform-pattern-name", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Landform-pattern-erosional", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Erosion-type", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Microrelief-type-gilgai", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Microrelief-type-hummocky", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Microrelief-type-other", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Artificial-aggregates-structure", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pedality-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Consistence-plasticity-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Cutans-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Fabric-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Mottle-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pans-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Profile-construction", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Carbonate-effervescence", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Texture-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Thickness-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Depth-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Gravel-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Classifier-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Order-code", "http://anzsoil.org/def/au/asc/", "asc") # 404

# get_ansis_enum("Mottle-colour", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Microrelief-component-biotic", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Microrelief-component-sampled", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Pans-continuity", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Mottle-contrast", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Consistence-plasticity-degree", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Erosion-severity-gully", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-mass-movement", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-rill", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-scald", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-sheet", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-stream-bank", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-tunnel", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-wave", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-severity-wind", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Inundation-depth", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Erosion-depth-gully", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Channel-depth-width", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Horizon-code", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Pore-diameter", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Root-size", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Channel-directionality", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Boundary-distinctness", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Cutans-distinctness", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Mottle-distinctness", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Coarse-fragments-distribution", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Elevation-evaluation-means", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Fabric-type", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Inundation-frequency", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Rock-genesis-hardened-artificial", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Rock-genesis-hardened-chemical", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Rock-genesis-hardened-evaporite", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Rock-genesis-sediments", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Rock-genesis-unweathered", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Rock-genesis-weathered", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Geomorphology-mode", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Geomorphology-status", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Substrate-grain-size", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Channel-integration", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Segregations-magnetic-attributes", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Segregations-nature", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Substrate-mineral-composition", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Channel-migration", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Soil-water-status", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Microrelief-proportions-gilgai", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Relative-inclination", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Runoff", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Boundary-shape", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Segregations-form", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Coarse-fragments-size", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Mottle-size", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Segregations-size", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Slope-procedure", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Slope-class", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Slope-modal", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Channel-spacing", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Substrate-discontinuity-spacing", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Erosion-state", "http://anzsoil.org/def/au/asls/land-surface/", "ls")

# get_ansis_enum("Consistence-stickiness", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Consistence-strength", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Segregations-strength", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Material-strength", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Field-texture", "http://anzsoil.org/def/au/asls/substrate/", "subst")

# get_ansis_enum("Water-repellence", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Cracks-width", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("structure-pedality-compound", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")

# get_ansis_enum("Location-in-element", "http://anzsoil.org/def/au/asls/landform/", "lf")

# get_ansis_enum("Location-in-toposequence", "http://anzsoil.org/def/au/asls/landform/", "lf") # 404

# get_ansis_enum("structure-pedality-compound", "http://anzsoil.org/def/au/asls/soil-profile/", "sp")