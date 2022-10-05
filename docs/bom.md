---
title: Bill of Materials
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

The Universal Bill of Materials is a base list common to all builds. Additional components based on your build configuration are listed separately.

There are no affiliate links used on this site.

!!! note
    The design allows for longer-than-specified screws in certain locations. The [assembly guide](assembly/index.md) notes where substitutions can be made.

!!! note
    Wiring is only specified for the IEC power socket, power switch, and power supply. Additional wiring for the MCU and CPU are configuration-specific.

## Universal Bill of Materials

These parts are common to all case builds. See below for additional requirements based on configuration.

| Item                                   | Qty | UOM | Note                                                     |
|----------------------------------------|-----|-----|----------------------------------------------------------|
| PLA or PLA+ filament                   | 2   | kg  | May be printable in 1kg if using a single color.         |
| TPU 95A filament                       | 0.05| kg  | **Optional.** Quantity is maximum estimated.             |
| M3 x 6mm machine screws                | 4   | ea  |                                                          |
| M3 x 8mm machine screws                | 20  | ea  |                                                          |
| M3 x 16mm machine screws               | 4   | ea  |                                                          |
| M3 hex nuts                            | 2   | ea  |                                                          |
| [#6 x 3/4" sharp point wood screws][1] | 8   | ea  | See note below.                                          |
| M4 x 6mm machine screws                | 4   | ea  |                                                          |
| M4 x 8mm machine screws                | 12  | ea  |                                                          |
| M4 x 12mm machine screws               | 4   | ea  |                                                          |
| M4 x 16mm machine screws               | 4   | ea  |                                                          |
| 16 awg wire                            | 0.5 | m   | Red or black.                                            |
| [Spade connectors, 14-16 awg, Female][13] | 3   | ea  |                                                       |
| [Fork connectors, 14-16 awg][12]       | 1   | ea  |                                                          |
| [SPST snap-in rocker switch][2]        | 1   | ea  | 30mm x 11mm profile. Identical to Creality Ender power switch. |
| MCU (3D printer control board)         | 1   | ea  | See the [Supported Parts][8] list.                       |
| [IEC C14 socket with fuse][3]          | 1   | ea  | Identical profile to Creality Ender series power socket. |
| 128x64 or TFT LCD display              | 1   | ea  | See the [Supported Parts][8] list.                       |
| Compatible power supply                | 1   | ea  | See [Power Supplies](#power-supplies) below.             |

!!! note
    To substitute #6 x 3/4" with Metric screws, use M3x16mm or M3 x 20mm. Equivalent length machine screws can also be used if sharp point screws are unavailable.

## Power Supplies

Currently, two power supply models are supported. You will need one (1) of the following:

| Item                              | Note                                                     |
|-----------------------------------|----------------------------------------------------------|
| [Mean Well LRS-350][4]            | Most Creality Ender-series printers use the LRS-350-24.  |
| [Mean Well RSP-500][5]            | **(Preliminary)** RSP-500-24 is used in the Ender 5 Plus.  |

## :material-alpha-c-box: Core Configurations with Fans

Externally mounted fans require a printed [:material-alpha-f-box: :material-alpha-c-box-outline: fan cage][11] that matches the size of the fan. These are specified below.

### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front

The base has an optional 40mm fan. The following are needed to mount the fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fan][6]         | 1   | ea  |                                                          |
| M3 x 16mm machine screws          | 4   | ea	| Any length 14-16mm will work.                            |

### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front

There are two versions of the front main body.

#### Internal 40mm Intake

This version of the front main body has an optional 40mm fan. The following are needed to mount the fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fan][6]         | 1   | ea  |                                                          |
| M3 x 16mm machine screws          | 4   | ea	| Any length 14-16mm will work.                            |

#### External 60mm Intake

This version of the front main body requires an externally mounted 60mm fan.

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [60x60x15mm axial fan][7]         | 1   | ea  | May also use 20mm or 25mm thick fans.                    |
| M4 x 25mm machine screws          | 4   | ea  | Add 10mm to fan depth for thicker fans.                  |
| Printed [:material-alpha-f-box: :material-alpha-c-box-outline: fan cage][11]            | 1   | ea  | TPU gasket is optional.                                  |

### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear

The rear body also has two versions: one with dual exhausts and one without any.

#### Dual 40mm Exhausts

This version of the requires two (2) externally mounted 40mm fans.

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [40x40x10mm axial fans][6]        | 2   | ea  |                                                          |
| M3 x 20mm machine screws          | 8   | ea	| Use 30mm screws for 20mm fans (not recommended).         |
| Printed [:material-alpha-f-box: :material-alpha-c-box-outline: fan cage][11]            | 2   | ea  | TPU gaskets are optional.                                |

#### No Exhaust Fans

There are no additional materials required for this version. 

!!! warning
    This rear main body must be used with a :material-alpha-p-box: :material-alpha-r-box-outline: rear panel or :material-alpha-p-box: :material-alpha-l-box-outline: lid that provides an exhaust fan.

## :material-alpha-t-box: Tray and :material-alpha-p-box: Panel Configurations

### :material-alpha-t-box: :material-alpha-c-box-outline: CPU Trays and :material-alpha-p-box: :material-alpha-d-box-outline: Display Panels

Most configurations use a display and many have an SBC, such as a Raspberry Pi. See the git [`Trays/CPU`][9] and [`Panels/Display`][10] folders for mounting information specific to your CPU tray and display panel.

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
[11]: https://github.com/jon-harper/OmniBox/Fans
<!-- Fork connectors -->
[12]: https://www.amazon.com/Baomain-Insulated-Connector-Electrical-Terminal/dp/B01B1DL4OA 
<!-- Spade connectors -->
[13]: https://www.amazon.com/gp/product/B07FQB6WXP      