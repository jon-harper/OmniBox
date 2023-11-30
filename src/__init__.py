import load_yaml
import bom

def as_url(text : str, link : str) -> str:
    return "[{}]({})".format(text, link)

def as_relative_url(text : str, link : str) -> str:
    return "[{}][{}]".format(text, link)

def define_env(env):
    """
    Modifies the environment variable with new variables, macros, and filters.
    """
    from os.path import join

    file = env.variables.meta['bom']
    
    global bom_data 
    bom_data = load_yaml.load_yaml(env.variables, join(env.conf.docs_dir, file))
    
    @env.macro
    def issue_tag(issue_number : int) -> str:
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)

    @env.macro
    def product_button(url : str) -> str:
        return as_url(":material-cart: Product Link", url) + "{ .md-button }"

    @env.macro
    def git_button(url : str) -> str:
        return as_relative_url(":material-git: Files", url) + "{ .md-button }"
    
    @env.macro
    def product_img(url : str, text : str ="", width : str ="480px") -> str:
        return "[![{}]({})]({})".format(text, url, url)

    @env.macro
    def bom_table_row(part_id : str, qty : float):
        part = part_from_id(part_id)
        if part.part_type == 'Printed':
            return "| {} | :material-printer-3d-nozzle: {} | {} | {} |".format(part.part_type, as_url(part.name, part.file_url), qty, part.units)
        if part.sources:
            return "| {} | :material-cart: {} | {} | {} |".format(part.part_type, as_url(part.name, 'sourcing.md#' + part_id), qty, part.units)
        return "| {} | {} | {} | {} |".format(part.part_type, part.name, qty, part.units)
    
    @env.macro
    def part_from_id(part_id : str) -> bom.Part:
        return bom_data.parts[part_id]
    
    @env.macro
    def parts() -> bom.PartData:
        return bom_data.parts
    
    @env.macro
    def assembly_from_id(assy_id : str) -> bom.Assembly:
        return bom_data.assemblies[assy_id]
    
    @env.macro
    def assemblies() -> bom.AssemblyData:
        return bom_data.assemblies
    
    @env.macro
    def author_from_id(author_id : str) -> bom.Author:
        return bom_data.authors[author_id]
    
    @env.macro
    def part_authors() -> bom.AuthorData:
        return bom_data.authors

    @env.macro
    def supplier_from_id(supplier_id : str) -> bom.Supplier:
        return bom_data.suppliers[supplier_id]

    @env.macro
    def suppliers() -> bom.SupplierData:
        return bom_data.suppliers
    
    @env.macro
    def filter_assemblies(type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.AssemblyData:
        ret = bom.AssemblyData()
        for assy_id, assy in bom_data.assemblies.items():
            if type_filter == assy.assy_type:
                if assy.attributes and attribute_filter in assy.attributes.keys():
                    if not attribute_value or attribute_value == assy.attributes[attribute_filter]:
                        ret[assy_id] = assy
                ret[assy_id] = assy
            elif assy.attributes and attribute_filter in assy.attributes.keys():
                if not attribute_value or attribute_value == assy.attributes[attribute_filter]:
                    ret[assy_id] = assy
        return ret
    
    @env.macro
    def filter_parts(type_filter : str = '') -> bom.PartData:
        ret = bom.PartData()
        for part_id, part in bom_data.parts.items():
            if part.part_type == type_filter:
                ret[part_id] = part
        return ret
    
    @env.macro
    def part_types() -> list[str]:
        return bom_data.part_types
    
    @env.macro
    def assembly_types() -> list[str]:
        return bom_data.assembly_types
    
    @env.macro
    def assembly_attributes() -> list[str]:
        return bom_data.attributes
    
    @env.macro
    def source_table(part : bom.Part) -> str:
        ret = \
        "| Source | Region | Note |\n|--------|--------|------|\n"
        if len(part.sources) == 0:
            ret += '| | | |\n'
            return ret
        for source in part.sources:
            ret += '| {} | {} | {} |\n'.format(as_url(source.supplier.name, source.url), source.supplier.region, source.note)
        return ret
    
    @env.macro
    def part_header(part_id:str, partname :str) -> str:
        return '<a name="{}"></a> {}'.format(part_id, partname)