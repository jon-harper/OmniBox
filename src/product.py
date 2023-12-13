"""
product.py

Handles filtering, sorting, and versioning for BOM data.
"""

import bom

class Product:
    version : str
    local_url_prefix: str
    components : bom.ComponentData
    parts : bom.PartData
    part_types: list[str]
    assembly_types: list[str]

    def __init__(self, 
                 components : bom.ComponentData, 
                 parts: bom.PartData,
                 templates: bom.TemplateList, 
                 prefix : str = ''):
        self.local_url_prefix = prefix
        self.components = {}
        self.parts = parts
        self.part_types = []
        self.assembly_types = []

        for part in parts.values():
            if part.part_type not in self.part_types:
                self.part_types.append(part.part_type)
        
        for comp_id, comp in components.items():
            if not comp.template or comp.template in templates:
                self.components[comp_id] = comp
                if comp.comp_type not in self.assembly_types:
                    self.assembly_types.append(comp.comp_type)

    def filterComponents(self, type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.ComponentData:
        """
        Returns a dict of all assemblies whose types match `type_filter` and/or
        whose attributes match `attribute_filter`.

        Attributes can be further constrained by filtering the value with `attribute_value`.
        """
        ret = bom.ComponentData()
        if type_filter and type_filter not in self.assembly_types:
            return ret

        for comp_id, comp in self.components.items():
            if type_filter and type_filter == comp.comp_type:
                if comp.attributes and attribute_filter in comp.attributes.keys():
                    if not attribute_value or attribute_value == comp.attributes[attribute_filter]:
                        ret[comp_id] = comp
                ret[comp_id] = comp
            elif comp.attributes and attribute_filter in comp.attributes.keys():
                if not attribute_value or attribute_value == comp.attributes[attribute_filter]:
                    ret[comp_id] = comp
        return ret

    def partFromId(self, part_id : str) -> bom.Part:
        return self.parts.get(part_id)
    
    def filterParts(self, part_type: str) -> bom.PartData:
        if part_type not in self.part_types:
            return {}
        ret : bom.PartData = {}
        for part_id, part in self.parts.items():
            if part.part_type == part_type:
                ret[part_id] = part
        return ret
    
    def has_hsi(self, v : bom.Variant) -> bool:
        if 'hsi' in v.attributes.keys():
            return True
        return False

    def sortComponents(self, values : list[bom.Component]) -> list[bom.Component]:
        return sorted(values, key=lambda v : v.name)

    def sortParts(self, values : list[bom.Part]) -> list [bom.Part]:
        return sorted(values, key=lambda v : v.name)