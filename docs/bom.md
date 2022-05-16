---
title: Bill of Materials
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

The design allows for screws of multiple lengths, i.e. to let you use what's on hand. The assembly process notes where substitutions can be made. This is a generic or "ideal" list.

## Generic Bill of Materials

| Item                              | Qty | UOM | Note                                                    |
|-----------------------------------|-----|-----|---------------------------------------------------------|
| PLA/PLA+ Filament                 | 2   | kg  | Final use is closer to 1kg if printed in a single color |
| M3 x 6mm machine screws           | 12  | ea  |                                                         |
| M3 x 8mm machine screws           | 12  | ea  |                                                         |
| M3 x 12mm machine screws          | 20  | ea	|                                                         |
| M3 x 16mm machine screws          | 2   | ea  |                                                         |
| [#6 x 3/4" sharp point wood screws](https://www.amazon.com/gp/product/B08LV4D8SB) | 8   | ea  | **OR** M3 x 20mm                                        |
| M4 x 8mm machine screws           | 14  | ea  |                                                         |
| M4 x 16mm machine screws          | 4   | ea  |                                                         |
| [SPST toggle switch](https://www.amazon.com/gp/product/B07QQ22DTB) | 1   | ea  | Identical profile to Creality Ender power switch. |
| [Meanwell-type PSU](https://www.amazon.com/MEAN-WELL-LRS-350-24-350-4W-Switchable/dp/B013ETVO12) | 1   | ea  | Meanwell-type refers to mounting pattern (M4, 150mm x 50mm). Compatible with all Ender PSUs. |
| 3D Printer control board (MCU)    | 1   | ea  | Currently only the [BTT Octopus](https://www.amazon.com/BIGTREETECH-Motherboard-Compatible-Firmware-Raspberry/dp/B094NPRYDP) is supported. |
| Raspberry Pi 3B+ or 4B (CPU)      | 1   | ea  | (Optional) For OctoPrint/Klipper users |
| [IEC C14 Socket with Fuse](https://www.amazon.com/gp/product/B081ZFHRGW) | 1   | ea  | Identical profile to Creality Ender series power socket. |
| [40x40x10mm Fans](https://www.amazon.com/dp/B08R9L9YR2) | 2 | ea  | 5V, 12V, or 24V |
| A 12864-style display or emulator | 1   | ea  | Includes: Stock Creality 12864, Mini 12864 displays, and [BTT 3.5](https://www.amazon.com/BIGTREETECH-Upgrade-Touch-Controller-Display-Motherboard/dp/B07VWGFKLZ) displays |

## Optional Components

| Item                              | Qty | UOM |Note |
|-----------------------------------|-----|-----|-----|
| [USB C Panel Mount extension cable](https://www.amazon.com/gp/product/B086W7C58P/) | 1 | ea | Not needed if using UART with Klipper; any brand should work. |
| [MicroSD to MicroSD extension cable](https://www.amazon.com/gp/product/B09CKRDFTH) | 1 | ea | This is not the same profile as the more popular LANMU connector. |
 
## Connectors

Connectors are not included in the basic BOM (with the exception of the IEC power connector) because this is up to the end user. The included two panel profiles use JST SM connectors for everything but the hotend, which uses a 2-pin, 2-row [Molex Micro Fit 3.0](https://www.digikey.com/en/product-highlight/m/molex-connector/micro-fit-3-interconnect-system) panel mount connector. I get mine through [Digikey](https://www.digikey.com/en/products/detail/molex/0430200200/252490) along with the [mating pins](https://www.digikey.com/en/products/detail/molex/0430310009/252485).

For the JST SM connectors, you can find [a kit on Amazon for about $15](https://www.amazon.com/gp/product/B07D9HRDT6).