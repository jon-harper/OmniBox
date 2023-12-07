"""
product.py

Handles filtering, sorting, and versioning for BOM data.
"""

import bom

class Product:
    version : str
    local_url_prefix: str
    assemblies : bom.AssemblyData
    parts : bom.PartData
    part_types: list[str]
    assembly_types: list[str]

    def __init__(self, 
                 assemblies : bom.AssemblyData, 
                 parts: bom.PartData,
                 part_versions: bom.VersionList, 
                 prefix : str = ''):
        self.local_url_prefix = prefix
        self.assemblies = {}
        self.parts = {}
        self.part_types = []
        self.assembly_types = []
        
        invalid : list[str] = []
        for part_id, part in parts.items():
            if part.version and part.version not in part_versions:
                invalid.append(part_id)
            else:
                self.parts[part_id] = part
                if part.part_type not in self.part_types:
                    self.part_types.append(part.part_type)

        for assy_id, assy in assemblies.items():
            for part_id in assy.parts.keys():
                if part_id not in invalid:
                    self.assemblies[assy_id] = assy
                    if assy.assy_type not in self.assembly_types:
                        self.assembly_types.append(assy.assy_type)

    def filter_assemblies(self, type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.AssemblyData:
        """
        Returns a dict of all assemblies whose types match `type_filter` and/or
        whose attributes match `attribute_filter`.

        Attributes can be further constrained by filtering the value with `attribute_value`.
        """
        ret = bom.AssemblyData()
        if type_filter and type_filter not in self.assembly_types:
            return ret

        for assy_id, assy in self.assemblies.items():
            if type_filter and type_filter == assy.assy_type:
                if assy.attributes and attribute_filter in assy.attributes.keys():
                    if not attribute_value or attribute_value == assy.attributes[attribute_filter]:
                        ret[assy_id] = assy
                ret[assy_id] = assy
            elif assy.attributes and attribute_filter in assy.attributes.keys():
                if not attribute_value or attribute_value == assy.attributes[attribute_filter]:
                    ret[assy_id] = assy
        return ret

    def part_from_id(self, part_id : str) -> bom.Part:
        return self.parts.get(part_id)
    
