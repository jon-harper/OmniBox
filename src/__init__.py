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
    def issue_tag(issue_number : int):
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)

    @env.macro
    def product_button(url):
        return as_url(":material-cart: Product Link", url) + "{ .md-button }"

    @env.macro
    def git_button(url):
        return as_relative_url(":material-git: Files", url) + "{ .md-button }"
    
    @env.macro
    def product_img(url, text="", width="480px"):
        return "[![{}]({})]({})".format(text, url, url)

    @env.macro
    def bom_table_row(part_id : str, qty : float):
        part = part_from_id(part_id)
        if part.part_type == 'Printed':
            return "| :material-printer-3d-nozzle: {} | {} | {} | {} |".format(part.part_type, as_url(part.name, part.file_url), qty, part.units)
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