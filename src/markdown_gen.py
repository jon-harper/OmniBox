"""
markdown_gen.py

Provides markdown generation tools
"""

import bom
from product import Product
import badge_gen as badge

class MarkdownTools:
    def __init__(self, product: Product) -> None:
        self.product = product
 
    @staticmethod
    def as_url(text : str, link : str) -> str:
        """
        Shorthand for markdown-formatted URL, using parenthesis for an absolute URL.
        """
        return "[{}]({})".format(text, link)

    @staticmethod
    def part_header(part_id:str, partname :str) -> str:
        """
        Annotates a part name with an anchor containing its part id. This allows "source.md#[part_id]" as a URL.

        This is used in headers on the Sourcing document.
        """
        return '<a name="{}"></a> {}'.format(part_id, partname)
    
    @staticmethod
    def author_link(auth : bom.Author) -> str:
        """
        Provides a formatted hyperlink to a contributor's name.
        """
        if not auth:
            return ''
        if auth.url:
            return '[{}]({})'.format(auth.name, auth.url)
        return auth.name

    def part_link(self, part_id : str, part : bom.Part, prefix='') -> str:
        
        ret : str = '[{} {}]({} "{}")'
        if part.part_type == 'Printed':
            ret = ret.format(':material-printer-3d-nozzle:', part.name, part.file_url, "File download")
        elif part.sources:
            ret = ret.format(':material-cart:', part.name, prefix + 'sourcing.md#' + part_id, "Sourcing information")
        else:
            return part.name
        return ret

    def render_badges(self, comp : bom.Component, variant : bom.Variant) -> str:
        ret : str = badge.template_badge(comp.template)
        ckeys = comp.attributes.keys()
        vkeys = variant.attributes.keys()
        if variant.author:
            ret += badge.author_badge(variant.author.name, variant.author.url)
        if 'half' in ckeys:
            ret += badge.half_badge(comp.attributes['half'])
        elif 'half' in vkeys:
            ret += badge.half_badge(variant.attributes['half'])
        if 'length' in ckeys:
            ret += badge.size_badge(comp.attributes['length'])
        elif 'length' in vkeys:
            ret += badge.size_badge(variant.attributes['length'])
        if 'base_depth' in ckeys:
            ret += badge.base_depth_badge(comp.attributes['base_depth'])
        elif 'base_depth' in vkeys:
            ret += badge.base_depth_badge(variant.attributes['base_depth'])
        if 'switch' in ckeys:
            ret += badge.switch_badge(comp.attributes['switch'])
        elif 'switch' in vkeys:
            ret += badge.switch_badge(variant.attributes['switch'])
        if 'display_type' in ckeys:
            ret += badge.display_badge(comp.attributes['display_type'])
        elif 'display_type' in vkeys:
            ret += badge.display_badge(variant.attributes['display_type'])
        if 'count' in ckeys:
            ret += badge.qty_badge(comp.attributes['count'])
        elif 'count' in vkeys:
            ret += badge.qty_badge(variant.attributes['count'])
        if 'mounts' in ckeys:
            ret += badge.extension_badge(comp.attributes['mounts'])
        elif 'mounts' in vkeys:
            ret += badge.extension_badge(variant.attributes['mounts'])
        if 'vent' in ckeys or 'vent' in vkeys:
            ret += badge.vent_badge()
        if 'fan' in ckeys or 'fan' in vkeys:
            ret += badge.fan_badge()
        if 'hsi' in ckeys or 'hsi' in vkeys:
            ret += badge.hsi_badge()
        return ret
    
    @staticmethod
    def format_note(txt : str) -> str:
        return ':octicons-paperclip-24: **General Notes**\n\n{}\n\n'.format(txt)
    
    @staticmethod
    def product_img(url : str, text : str ="", width : str ="240px") -> str:
        w_txt = '{ width="' + width + '" }'
        return "[![{text}]({url}){width}]({url})".format(text=text, url=url, width=w_txt)

    @staticmethod
    def issue_tag(issue_number : int) -> str:
        """
        Adds a caution annotation for a pending fit test.
        """
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)