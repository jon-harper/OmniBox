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

    def part_link(self, part_id : str) -> str:
        part : bom.Part = self.product.parts[part_id]
        ret : str = "[{} {}]({})"
        if part.part_type == 'Printed':
            ret = ret.format(':material-printer-3d-nozzle:', part.name, part.file_url)
        elif part.sources:
            ret = ret.format(':material-cart:', part.name, 'sourcing.md#' + part_id)
        else:
            return part.name
        return ret

    def bom_table(self, v : bom.Variant, indent = '') -> str:
        """
        Prints the complete BOM for an assembly with an optional indentation.
        """
        ret = '{}| Type | Part | Qty | UOM |\n{}|------|------|-----|-----|\n'.format(indent, indent)
        for part_id, qty in v.parts.items():
            ret += self.bom_table_row(part_id, qty, indent)
        return ret
    
    def bom_table_row(self, part_id : str, qty : float, indent = '', part : bom.Part = None) -> str:
        """
        Takes a part_id and quantity and produces an entry for a BOM table.
        Adds icons and links based on part type.
        """
        if not part:
            part = self.product.partFromId(part_id)
        return "{}| {} | {} | {} | {} |\n".format(indent, part.part_type, self.part_link(part_id), qty, part.units)
    
    def component_badges(self, comp : bom.Component) -> str:
        badge_text = badge.version_badge(comp.version)
        keys = comp.attributes.keys()
        if 'mcu_count' in keys:
            badge_text += badge.mcu_count_badge(comp.attributes['mcu_count'])
        if 'base_depth' in keys:
            badge_text += badge.base_depth_badge(comp.attributes['base_depth'])
        if 'switch' in keys:
            badge_text +=  badge.switch_badge(comp.attributes['switch'])
        if 'display_type' in keys:
            badge_text += badge.display_badge(comp.attributes['display_type'])
        return badge_text
    
    def variant_badges(self, variant : bom.Variant) -> str:
        if variant.author:
            ret = badge.author_badge(variant.author.name, variant.author.url)
        else:
            ret = ''
        if variant.attributes:
            # keys = variant.attributes.keys()
            if self.product.has_hsi(variant):
                ret += badge.hsi_badge()
        return ret
        
    def component_entry(self, comp : bom.Component):
        badge_text = self.component_badges(comp)

        #single variant
        if len(comp.variants) == 1:
            v = comp.variants[0]
            if not badge_text:
                badge_text = ''
            badge_text += self.variant_badges(v)
            if badge_text:
                badge_text += '\n\n'
            return '### {name}\n\n{badge}\n\n{table}'.format(
                name=comp.name,
                badge=badge_text,
                table=self.bom_table(v))
        
        # Multiple variants
        indent = '    '
        ret = '### {name}\n\n'.format(name=comp.name)
        if badge_text:
            ret += '{badge}\n\n'.format(badge=badge_text)
        for v in comp.variants:
            section = '=== "{}"\n'.format(v.name)
            badge_text = self.variant_badges(v)
            if badge_text:
                section += '{}{}\n{}\n'.format(indent, badge_text, indent)
            section += self.bom_table(v, indent)
            ret += section
        return ret

    def source_table(self, part : bom.Part) -> str:
        """
        Returns a full markdown table of the Sources for a given Part.
        """
        ret = \
        "| Source | Ships To | Ships From | Note |\n|---|---|---|---|\n"
        if len(part.sources) == 0:
            ret += '| | | | |\n'
            return ret
        for source in part.sources:
            ret += '| {} | {} | {} | {} |\n'.format(MarkdownTools.as_url(source.supplier.name, source.url), 
                                               source.supplier.ships,
                                               source.supplier.region, 
                                               source.note)
        return ret

    def sourcing_part_entry(self, part_id:str, part : bom.Part) -> str:
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
""".format(MarkdownTools.part_header(part_id, part.name),
            self.source_table(part),
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
""".format(MarkdownTools.part_header(part_id, part.name),
            self.source_table(part))