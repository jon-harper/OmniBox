from dataclasses import dataclass
from typing import Optional, NamedTuple

class Supplier(NamedTuple):
    """
    Defines a provider of Parts.
    """
    name: str   # Provider name
    region: str # Region(s) shipping FROM
    ships: str  # Region(s) shipping TO
    icon: str   # Optional icon
    note: str   # Optional note

SupplierData = dict[str, Supplier]

class SourceUrl(NamedTuple):
    """
    Supplier data for a specific Part.
    """
    supplier : Supplier
    url: str            # location
    note: str           # notes about a given supplier's product

SourceList = list[SourceUrl]

class Author(NamedTuple):
    """
    Accreditation information for a printed Part.
    """
    # author_id: str
    name: str   # Author name
    url: str    # Preferred profile URL
    note: str   # Any notes

AuthorData = dict[str, Author]

class Part(NamedTuple):
    """
    Contains relevant information for both printed and sourced parts.
    """
    name: str                   # Formal part name
    units: str                  # unit of measure
    part_type: str              # category, e.g. fastener, MCU, fan
    icon: Optional[str]         # internal; Material icon key
    file_url: Optional[str]     # STL for printable files
    version: Optional[str]      # Release version (for Core files) or template version (for others)
    image_url: Optional[str]    # internal; display image for major parts
    note: Optional[str]         # internal
    sources: Optional[SourceList] # list of part links
    author: Optional[str]       # Contributor for printable files

PartData = dict[str, Part]

class MaterialsEntry(NamedTuple):
    """
    Return value for a BOM entry.
    """
    part: Part
    qty: float = 1

#Internal
MaterialsData = dict[str, float] #part_id, qty

@dataclass
class Assembly:
    """
    A collection of Parts with a given name, type, and associated attributes.
    """
    name: str
    parts : MaterialsData
    assy_type: str
    attributes: dict[str, str] #name, value

    def has_attr(self, attr : str) -> bool:
        if not self.attributes:
            return False
        return attr in self.attributes.keys()
    
    def attr_value(self, attr: str) -> str:
        if self.has_attr(attr):
            return self.attributes[attr]
        return ''

    def modifier(self) -> str:
        if self.has_attr('modifier'):
            return self.attributes['modifier']
        return ''

AssemblyData = dict[str, Assembly]

VersionList = list[str]

class GlobalData(NamedTuple):
    """
    Global variable for the part database.
    """
    assemblies : AssemblyData
    parts : PartData
    authors : AuthorData
    suppliers : SupplierData
    assembly_types : list[str]
    versions: dict[str, VersionList]