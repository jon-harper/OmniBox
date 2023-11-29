"""
Loads a YAML bill of materials, parses it, and injects
the result into the provided environment variable.
"""

import bom

def load_yaml(env_variables, filepath : str):
    import yaml

    f = open(filepath, 'r')
    bom_data = yaml.safe_load(f.read())
    
    parser = BOMParser(bom_data)
    env_variables['base_url'] = parser.base_url
    env_variables['parts'] = parser.parts
    env_variables['suppliers'] = parser.suppliers
    env_variables['part_authors'] = parser.authors
    env_variables['assemblies'] = parser.assemblies
    

class BOMParser():
    def __init__(self, yaml_data : dict) -> None:
        config = yaml_data['config']
        self.base_url = config['baseUrl']
        
        self.suppliers = bom.SupplierData()
        if 'suppliers' in yaml_data:
            for key, entry in yaml_data['suppliers'].items():
                self.suppliers[key] = self.parseSupplier(entry)
        
        self.authors = bom.AuthorData()
        if 'authors' in yaml_data:
            for key, entry in yaml_data['authors'].items():
                self.authors[key] = self.parseAuthor(entry)

        assert('parts' in yaml_data)
        self.parts = bom.PartData()
        for key, entry in yaml_data['parts'].items():
            self.parts[key] = self.parsePart(entry)

        self.assemblies = self.parseAssemblies(yaml_data['assemblies'])

    def parseSupplier(self, entry : dict) -> bom.Supplier:
        return bom.Supplier(
            name=entry['name'], 
            region=entry.get('region', 'Worldwide'), 
            icon=entry.get('icon', ''),
            note=entry.get('note', ''))

    def parsePart(self, entry : dict) -> bom.Part:
        return bom.Part(name=entry['name'],
                       units=entry.get('units', 'Ea'),
                       icon=entry.get('icon', None),
                       file_url=entry.get('file', None),
                       version=entry.get('version', None),
                       note=entry.get('note', None),
                       sources=self.parseSources(entry.get('sources', None)),
                       image_url=entry.get('img', None))
    
    def parseSources(self, entry : dict) -> bom.SourceList:
        ret = bom.SourceList()
        if not entry:
            return ret
        for supplier_id, source_data in entry.items():
            source = bom.SourceUrl(self.suppliers[supplier_id],
                                   url = source_data['url'],
                                   note=entry.get('note', ''))
            ret.append(source)
        return ret
    
    def parseAuthor(self, entry: dict) -> bom.Author:
        return bom.Author(name=entry['name'], 
                          url=entry['url'],
                          note=entry.get('note', ''))
    
    def parseAssemblies(self, entries : dict[str, dict]) -> bom.AssemblyData:
        ret : bom.AssemblyData = {}
        deferred : bom.AssemblyData = {}

        # Process the entries and flag any that refer to subassemblies
        for assy_id, values in entries.items():
            is_deferred : bool = False

            assy = bom.Assembly (name=values.get('name', ''),
                                 parts=bom.MaterialsData(),
                                 assy_type=values.get('type', ''),
                                 attributes=values.get('attributes'))
            
            #check if we refer to any subassemblies, then defer for later processing
            parts = values['parts']
            for part_id, qty in parts.items():
                if part_id in deferred.keys() or part_id in ret.keys():
                    is_deferred = True
                assy.parts[part_id] = qty

            # Build up dicts of both deferred and completed assemblies
            if is_deferred:
                deferred[assy_id] = assy
            else:
                ret[assy_id] = assy
        
        # Process the deferred subassemblies.
        # Limit possible iterations to 10 to catch loops.
        iterations : int = 0
        processing : dict = {}
        while iterations < 10 and deferred:
            # Swap the list of in-process and pending subassemblies
            processing = deferred.copy()
            deferred = {}

            combined : bom.PartData = {}
            

            for assy_id, assy in processing.items():
                skip : bool = False
                for sub_id in assy.parts.keys():
                    # Check if this contains references to assemblies not yet processed;
                    # defer if needed and catch it the next pass.
                    if sub_id in deferred.keys():
                        deferred[assy_id] = assy
                        skip = True
                        break
                if skip:
                    break
                for sub_id in assy.parts.keys():
                    # Found a subassembly, break it down
                    if sub_id in ret.keys():
                        # Multiply everything by the quantity of subassemblies
                        mult : int = round(assy.parts[sub_id])
                        for part_id, qty in ret[sub_id].parts.items():
                            # Check if the part is already in the final list.
                            # Add to the existing value if so, assign if not.
                            if part_id in assy.parts.keys():
                                combined[part_id] += qty * mult
                            else:
                                combined[part_id] = qty * mult
                    else:
                        combined[sub_id] = assy.parts[sub_id]
                assy.parts = combined
                # Add to the finished list
                ret[assy_id] = assy
                combined = {}
        # Ensure we didn't catch a loop
        assert(len(deferred) == 0)

        return ret