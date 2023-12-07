"""
Initializes the Python environment. Methods tagged as macros can be called from within
Markdown.
"""

import load_yaml
import bom
from markdown_gen import MarkdownTools as fmt

from product import Product

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
    version = env.variables.meta['bom_version_str']
    
    global bom_data 
    bom_data = load_yaml.load_yaml(env.variables, join(env.conf.docs_dir, file))

    global product
    product = Product(assemblies=bom_data.assemblies,
                      parts=bom_data.parts,
                      part_versions=bom_data.versions[version])
    env.variables['fmt'] = fmt(product)
    env.variables['product'] = product

    @env.macro
    def issue_tag(issue_number : int) -> str:
        """
        Adds a caution annotation for a pending fit test.
        """
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)

    @env.macro
    def product_button(url : str) -> str:
        return fmt.as_url(":material-cart: Product Link", url) + "{ .md-button }"

    @env.macro
    def git_button(url : str) -> str:
        return as_relative_url(":material-git: Files", url) + "{ .md-button }"
    
    @env.macro
    def product_img(url : str, text : str ="", width : str ="480px") -> str:
        return "[![{}]({})]({})".format(text, url, url)

    @env.macro
    def parts() -> bom.PartData:
        """
        Returns a dict of all Parts active for the current Product.
        """
        return product.parts
    
   
    @env.macro
    def assemblies() -> bom.AssemblyData:
        """
        Returns a dict of all Assemblys active for the current Product.
        """
        return product.assemblies
  
    @env.macro
    def filter_assemblies(type_filter : str = '', attribute_filter: str = '', attribute_value: str = '') -> bom.AssemblyData:
        """
        Returns a dict of all assemblies whose types match `type_filter` and/or
        whose attributes match `attribute_filter`.

        Attributes can be further constrained by filtering the value with `attribute_value`.
        """
        return product.filter_assemblies(type_filter, attribute_filter, attribute_value)
    
    @env.macro
    def filter_parts(type_filter : str = '') -> bom.PartData:
        """
        Returns a dict of all Parts whose types match `type_filter`.
        """
        ret = bom.PartData()
        for part_id, part in product.parts.items():
            if part.part_type == type_filter:
                ret[part_id] = part
        return ret
    
    @env.macro
    def part_types() -> list[str]:
        """
        Returns a list of all Part types.
        """
        return product.part_types
    
    @env.macro
    def assembly_types() -> list[str]:
        """
        Returns a list of assembly types.
        """
        return product.assembly_types
       
    @env.macro
    def section_assemblies(assys : bom.AssemblyData) -> dict[bom.AssemblyData]:
        """
        Splits up an AssemblyData into unique names and returns a diction of `AssemblyData`
        with the names as keys.
        """
        ret : dict[bom.AssemblyData] = {}
        for key, assy in assys.items():
            if assy.name not in ret.keys():
                ret[assy.name] = {}
            ret[assy.name][key] = assy
        return ret
      
    