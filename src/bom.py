from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BOMEntry:
    part_id: str
    qty: int

BOMEntryList = List[BOMEntry]

@dataclass
class SourceUrl:
    supplier: str
    url: str

@dataclass
class Part:
    part_id: str
    name: str
    uom: str = "Ea" #unit of measure
    icon: Optional[str] = None
    source: Optional[SourceUrl] = None
    image_url: Optional[str] = None
    note: Optional[str] = None
    bom: Optional[BOMEntryList] = None

PartData = dict[Part]