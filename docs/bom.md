---
title: Bill of Materials
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

The design allows for screws of multiple lengths (to allow you to use whatever is on hand). The assembly process notes where substitutions can be made. The first list is a "base" list common to all builds. Additional components based on your build configuration are listed separately.

There are no affiliate links used on this site.

## General Components

These parts are common to all case builds. See below for additional requirements based on configuration.

| Item                                   | Qty | UOM | Note                                                     |
|----------------------------------------|-----|-----|----------------------------------------------------------|
| PLA or PLA+ filament                   | 2   | kg  | May be printable in 1kg if using a single color.         |
| M3 x 6mm machine screws                | 4   | ea  |                                                          |
| M3 x 8mm machine screws                | 20  | ea  |                                                          |
| M3 x 16mm machine screws               | 4   | ea  |                                                          |
| M3 hex nuts                            | 2   | ea  |                                                          |
| [#6 x 3/4" sharp point wood screws][1] | 8   | ea  | See note below.                                          |
| M4 x 6mm machine screws                | 4   | ea  |                                                          |
| M4 x 8mm machine screws                | 12  | ea  |                                                          |
| M4 x 12mm machine screws               | 4   | ea  |                                                          |
| M4 x 16mm machine screws               | 4   | ea  |                                                          |
| [SPST snap-in rocker switch][2]        | 1   | ea  | 30mm x 11mm profile. Identical to Creality Ender power switch. |
| MCU (3D printer control board)         | 1   | ea  | See the [Supported Parts][8] list.                       |
| [IEC C14 socket with fuse][3]          | 1   | ea  | Identical profile to Creality Ender series power socket. |
| 128x64 or TFT LCD display              | 1   | ea  | See the [Supported Parts][8] list.                       |

!!! note
    Metric equivalent to #6 x 3/4" is M3 x 20mm. Equivalent length machine screws can also be used if wood screws are unavailable.

## Power Supplies

Currently, two power supplies are supported. You will need one (1) of the following:

| Item                              | Note                                                     |
|-----------------------------------|----------------------------------------------------------|
| [Mean Well RSP-500][5]            | Used in the Ender 5 Plus.                                |
| [Mean Well LRS-350][4]            | Most Ender-series printers use the LRS-350-24.           |

## Additional Components

Some Core component versions have optional fan mounts, while others have ones that are required.

### 1. Base - Front

The base has a concealed, *optional* 40mm fan. The following are needed to mount the fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fans][6]        | 1   | ea  |                                                          |
| M3 x 16mm machine screws          | 4   | ea	| Any length 14-16mm will work.                            |

### 2a. Main Body - Front with 40mm Intake

This version of the front main body has a concealed, *optional* 40mm fan. The following are needed to mount the fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fans][6]        | 1   | ea  |                                                          |
| M3 x 16mm machine screws          | 4   | ea	| Any length 14-16mm will work.                            |

### 2b. Main Body - Front with 60mm Intake

This version of the front main body *requires* an externally mounted 60mm fan.

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [60x60x15mm axial fan][7]         | 1   | ea  | May also use 20mm or 25mm thick fans.                    |
| M4 x 25mm machine screws          | 4   | ea  | Add 10mm to fan depth for thicker fans.                  |

### 3. Main Body - Rear with 40mm Exhausts

This version of the rear main body *requires* two externally mounted 40mm fans.

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fans][6]        | 2   | ea  | May also use 20mm thick fans; this is not recommended due to noise. |
| M3 x 20mm machine screws          | 8   | ea	| Use 30mm screws for 20mm fans.                           |

## Optional Components

### CPU Trays and Display Panels

Most configurations use a display and many will have a CPU. See the git [`Trays/CPU`][9] and [`Panels/Display`][10] folders for mounting information specific to your CPU and display mount.

### Other Supported Parts

See the [Supported Parts Overview][8] for a full list of parts and mounting locations. Some configurations require additional fasteners or fans.

[1]: https://www.amazon.com/gp/product/B08LV4D8SB
[2]: https://www.amazon.com/gp/product/B07QQ22DTB
[3]: https://www.amazon.com/gp/product/B081ZFHRGW
[4]: https://www.meanwell.com/webapp/product/search.aspx?prod=LRS-350
[5]: https://www.meanwell.com/webapp/product/search.aspx?prod=RSP-500
[6]: https://www.amazon.com/dp/B08R9L9YR2
[7]: https://www.amazon.com/Wathai-Exhaust-Cooler-Brushless-Cooling/dp/B07Q2JRYZR
[8]: support/index.md
[9]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[10]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display