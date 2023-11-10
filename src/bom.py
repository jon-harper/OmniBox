from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BOMEntry:
    part_id: str
    amount: int = 1
    entry_type: str

BOMEntryList = List[BOMEntry]

@dataclass
class Supplier:
    supplier_id: str
    name: str
    region: str = 'Worldwide'
    icon: Optional[str] = None
    note: Optional[str] = None

@dataclass
class SourceUrl:
    supplier_id: str    # supplier name
    url: str         # location
    note: Optional[str] = None # internal; notes about a given supplier

@dataclass
class Part:
    part_id: str                    # Unique ID
    name: str                       # Formal part name
    units: str = "Ea"                 # unit of measure
    icon: Optional[str] = None      # interal; Material icon
    file_url: Optional[str] = None  # STL for printable files
    image_url: Optional[str] = None # internal; display image for major parts
    note: Optional[str] = None      # internal; TBD
    supplier_urls: Optional[List[SourceUrl]] = None # list of part links

PartData = dict[Part]