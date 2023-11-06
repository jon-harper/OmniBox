from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BOMEntry:
    part_id: str
    amount: int = 1

BOMEntryList = List[BOMEntry]

@dataclass
class SourceUrl:
    supplier: str    # supplier name
    url: str         # location
    note: str = None # internal; notes about a given supplier

@dataclass
class Part:
    part_id: str                    # Unique ID
    name: str                       # Formal part name
    units: str = "Ea"                 # unit of measure
    icon: Optional[str] = None      # interal; Material icon
    file_url: Optional[str] = None  # STL for printable files
    image_url: Optional[str] = None # internal; display image for major parts
    note: Optional[str] = None      # internal; TBD
    requires: Optional[BOMEntryList] = None         # dependent bill of materials
    supplier_urls: Optional[List[SourceUrl]] = None # list of part links

PartData = dict[Part]