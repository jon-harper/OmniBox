"""
markdown_gen.py

Provides markdown generation tools
"""

import bom
from product import Product

class MarkdownTools:
    def __init__(self, product: Product) -> None:
        self.product = product

    @staticmethod
    def badge(icon: str, url : str, tooltip : str, text : str = None, text_url : str = None):
        if text and text_url:
            return '<div class="jh-badge" title="{}" markdown>[{} {}]({})</div>'.format(
                tooltip, icon, text, url)

        else:
            return '<div class="jh-badge" title="{}" markdown>[{}]({})</div>'.format(
                tooltip, icon, url)

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

    def bom_table(self, assy : bom.Assembly, indent = '') -> str:
        """
        Prints the complete BOM for an assembly with an optional indentation.
        """
        ret = '{}| Type | Part | Qty | UOM |\n{}|------|------|-----|-----|\n'.format(indent, indent)
        for part_id, qty in assy.parts.items():
            ret += self.bom_table_row(part_id, qty, indent)
        return ret
    
    def bom_table_row(self, part_id : str, qty : float, indent = '', part : bom.Part = None) -> str:
        """
        Takes a part_id and quantity and produces an entry for a BOM table.
        Adds icons and links based on part type.
        """
        if not part:
            part = self.product.part_from_id(part_id)
        return "{}| {} | {} | {} | {} |\n".format(indent, part.part_type, self.part_link(part_id), qty, part.units)
    
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