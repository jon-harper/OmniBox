import bom

Part = bom.Part
SourceUrl = bom.SourceUrl

def parse_json_part(entry: dict, part : Part) -> None:
    for key, value in entry.items():
        if key == "units":
            part.uom = value
        elif key == "icon":
            part.icon = value
        elif key == "image":
            part.image_url = value
        elif key == "icon":
            part.icon = value
        elif key == "note":
            part.note = value
        elif key == "links":
            pass
        #    ret.source = SourceUrl(value["supplier"], value["url"])

def load_json(part_data : dict, filepath : str):
    import json
    with open(filepath, "r") as f:
        bom_data = json.load(f)

    config_data = bom_data['config']
    assert(config_data['id'] == "test")
    assert(config_data['baseUrl'] == "https://raw.githubusercontent.com/jon-harper/OmniBox/main")

    for entry in bom_data['parts']:
        part = Part(part_id = entry["id"], 
               name = entry["name"])
        parse_json_part(entry, part)
        part_data[part.part_id] = part

    # consume components here