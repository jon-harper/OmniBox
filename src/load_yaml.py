"""
Python module for OmniBox documentation generation.
"""

import bom

Part = bom.Part
SourceUrl = bom.SourceUrl

def parse_part_entry(entry : dict) -> Part:
    ret = Part(part_id=entry["id"], 
                name=entry["name"])
    for key, value in entry.items():
        if key == "uom":
            ret.uom = value
        elif key == "icon":
            ret.icon = value
        elif key == "source":
            ret.source = SourceUrl(value["supplier"], value["url"])
        elif key == "image_url":
            ret.image_url = value
        elif key == "note":
            ret.note = value
        # elif key == "bom":
        #     ret.bom = 
    return ret

def load_yaml(part_data : dict, filepath : str):
    import yaml

    f = open(filepath, "r")
    bom_data = yaml.safe_load(f.read())
    
    for entry in bom_data:
        part : Part = parse_part_entry(entry)
        part_data[part.part_id] = part
