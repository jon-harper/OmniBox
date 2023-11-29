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
    load_yaml.load_yaml(env.variables, join(env.conf.docs_dir, file))
    
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
    def bom_table_row(parts: bom.PartData, part_id : str, qty : float):
        part = parts[part_id]
        return "| {} | {} | {} |".format(part.name, qty, part.units)