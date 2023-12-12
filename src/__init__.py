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
    version = env.variables.meta['bom_template_str']
    
    global bom_data 
    bom_data = load_yaml.load_yaml(env.variables, join(env.conf.docs_dir, file))

    global product
    product = Product(components=bom_data.components,
                      parts=bom_data.parts,
                      templates=bom_data.templates[version])
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

    