"""
Initializes the Python environment. Methods tagged as macros can be called from within
Markdown.
"""

import load_yaml
import bom

def as_url(text : str, link : str) -> str:
    """
    Shorthand for markdown-formatted URL, using parenthesis for an absolute URL.
    """
    return "[{}]({})".format(text, link)

def as_relative_url(text : str, link : str) -> str:
    """
    Shorthand for a markdown relative URL, i.e. one that will be enclosed in braces and has a matching tag.
    """
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
        """
        Adds a caution annotation for a pending fit test.
        """
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
    def bom_table_row(part_id : str, qty : float) -> str:
        """
        Takes a part_id and quantity and produces an entry for a BOM table.
        Adds icons and links based on part type.
        """
        part = part_from_id(part_id)
        return "| {} | {} | {} | {} |".format(part.part_type, part_link(part_id), qty, part.units)
    
    @env.macro
    def part_from_id(part_id : str) -> bom.Part:
        """
        Returns a Part for a given id string.
        """
        return bom_data.parts[part_id]
    
    @env.macro
    def parts() -> bom.PartData:
        """
        Returns a dict of all Parts.
        """
        return bom_data.parts
    
    @env.macro
    def assembly_from_id(assy_id : str) -> bom.Assembly:
        """
        Returns an Assembly for a given id string.
        """
        return bom_data.assemblies[assy_id]
    
    @env.macro
    def assemblies() -> bom.AssemblyData:
        """
        Returns a dict of all Assemblys.
        """
        return bom_data.assemblies
    
    @env.macro
    def author_from_id(author_id : str) -> bom.Author:
        """
        Returns an author for a given id string.
        """
        return bom_data.authors[author_id]
    
    @env.macro
    def part_authors() -> bom.AuthorData:
        """
        Returns a dict of all Authors.
        """

        return bom_data.authors

    @env.macro
    def supplier_from_id(supplier_id : str) -> bom.Supplier:
        """
        Returns a Supplier from an id string.
        """
        return bom_data.suppliers[supplier_id]

    @env.macro
    def suppliers() -> bom.SupplierData:
        """
        Returns a dict of all Suppliers.
        """
        return bom_data.suppliers
    
    @env.macro
    def filter_assemblies(type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.AssemblyData:
        """
        Returns a dict of all assemblies whose types match `type_filter` and/or
        whose attributes match `attribute_filter`.

        Attributes can be further constrained by filtering the value with `attribute_value`.
        """
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
        """
        Returns a dict of all Parts whose types match `type_filter`.
        """
        ret = bom.PartData()
        for part_id, part in bom_data.parts.items():
            if part.part_type == type_filter:
                ret[part_id] = part
        return ret
    
    @env.macro
    def part_types() -> list[str]:
        """
        Returns a list of all Part types.
        """
        return bom_data.part_types
    
    @env.macro
    def assembly_types() -> list[str]:
        """
        Returns a list of assembly types.
        """
        return bom_data.assembly_types
    
    @env.macro
    def assembly_attributes() -> list[str]:
        return bom_data.attributes
    
    @env.macro
    def source_table(part : bom.Part) -> str:
        """
        Returns a full markdown table of the Sources for a given Part.
        """
        ret = \
        "| Source | Ships To | Ships From | Note |\n|---|---|---|---|\n"
        if len(part.sources) == 0:
            ret += '| | | | |\n'
            return ret
        for source in part.sources:
            ret += '| {} | {} | {} | {} |\n'.format(as_url(source.supplier.name, source.url), 
                                               source.supplier.ships,
                                               source.supplier.region, 
                                               source.note)
        return ret
    
    @env.macro
    def part_header(part_id:str, partname :str) -> str:
        """
        Annotates a part name with an anchor containing its part id. This allows "source.md#[part_id]" as a URL.

        This is used in headers on the Sourcing document.
        """
        return '<a name="{}"></a> {}'.format(part_id, partname)
    
    @env.macro
    def part_link(part_id : str) -> str:
        part : bom.Part = bom_data.parts[part_id]
        ret : str = "[{} {}]({})"
        if part.part_type == 'Printed':
            ret = ret.format(':material-printer-3d-nozzle:', part.name, part.file_url)
        elif part.sources:
            ret = ret.format(':material-cart:', part.name, 'sourcing.md#' + part_id)
        else:
            return part.name
        return ret
    
    @env.macro
    def author_link(auth : bom.Author) -> str:
        if not auth:
            return ''
        if auth.url:
            return '[{}]({})'.format(auth.name, auth.url)
        return auth.name
    
    @env.macro
    def sourcing_part_entry(part_id:str, part : bom.Part) -> str:
        if part.image_url:
            return \
"""#### {}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
{}
</div>
<div markdown class="jh-grid-img">
[![{}]({})]({})
</div>
</div>
""".format(part_header(part_id, part.name),
            source_table(part),
            part.name,
            part.image_url,
            part.image_url)
        else:
            return \
"""#### {}

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
{}
</div>
</div>
""".format(part_header(part_id, part.name),
            source_table(part))