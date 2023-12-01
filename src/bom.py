from dataclasses import dataclass
from typing import Optional, NamedTuple

class Supplier(NamedTuple):
    """
    Defines a provider of Parts.
    """
    name: str
    region: str
    icon: str
    note: str

SupplierData = dict[str, Supplier]

class SourceUrl(NamedTuple):
    """
    Supplier data for a specific Part.
    """
    supplier : Supplier
    url: str            # location
    note: str # internal; notes about a given supplier

SourceList = list[SourceUrl]

class Author(NamedTuple):
    """
    Accreditation information for a printed Part.
    """
    # author_id: str
    name: str
    url: str
    note: str

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

PartData = dict[str, Part]

class MaterialsEntry(NamedTuple):
    """
    Return value for a BOM entry.
    """
    part: Part
    qty: float = 1

#We return a list but internally store a simple `dict` (MaterialsData)
MaterialsList = list[MaterialsEntry]
#Internal
MaterialsData = dict[str, float] #part_id, qty

class Attribute(NamedTuple):
    """
    An assembly attribute name and value pair for return values.
    """
    name: str
    value: str

@dataclass
class Assembly:
    """
    A collection of Parts with a given name, type, and associated attributes.
    """
    name: str
    parts : MaterialsData
    assy_type: str
    attributes: dict[str, str] #name, value

AssemblyData = dict[str, Assembly]

class GlobalData(NamedTuple):
    """
    Global variable tracking state.
    """
    assemblies : AssemblyData
    parts : PartData
    authors : AuthorData
    suppliers : SupplierData
    assembly_types : list[str]
    part_types : list[str]
    attributes : list[str]