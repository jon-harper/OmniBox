---
title: Bill of Materials
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

The Universal Bill of Materials is a base list common to all builds. Additional components based on your build configuration are listed separately.

- There are no affiliate links used on this site.
- The :material-cart: shopping cart icon indicates an external link.
- The design allows for longer-than-specified screws in certain locations. The [assembly guide][assembly] notes where substitutions can be made.
- Wiring is only specified for the IEC power socket, power switch, and power supply. Additional wiring for the MCU and CPU are configuration-specific.

## Universal Bill of Materials

These parts are common to all case builds. See below for additional requirements based on configuration.

| Item                                   | Qty | UOM | Note                                                     |
|----------------------------------------|-----|-----|----------------------------------------------------------|
| PLA/PLA+ filament                      | 2   | kg  | Typical use is less than 1.5kg.                          |
| TPU 95A filament                       | 0.05| kg  | **Optional.** Quantity is maximum estimated.             |
| M3 x 8mm machine screws                | 50  | ea  |                                                          |
| M3 x 12mm machine screws               | 6   | ea  |                                                          |
| M3 x 20mm machine screws               | 2   | ea  |                                                          |
| [:material-cart: #6 x 3/4" sharp point wood screws][bom_wood_screw] | 8   | ea  | See note below.             |
| 16 awg stranded hookup wire            | 0.5 | m   | Red or black.                                            |
| [:material-cart: Spade connectors, 14-16 awg, Female Insulated][bom_spade_connector] | 3   | ea  |                      |
| [:material-cart: Fork connectors, 14-16 awg, Insulated][bom_fork_connector]       | 1   | ea  |                          |
| [:material-cart: SPST snap-in rocker switch][bom_switch]        | 1   | ea  | 30mm x 11mm profile. Identical to Creality Ender power switch. |
| MCU (3D printer control board)         | 1   | ea  | See the [Supported Parts][support] list.                 |
| [:material-cart: IEC C14 socket with fuse][bom_iec]          | 1   | ea  | Identical profile to Creality Ender series power socket. |
| Fuse, 5x20mm, Glass, Fast Blow         | 1   | ea  | See note below. |
| 128x64 or TFT LCD display              | 1   | ea  | See the [Supported Parts][support] list.                 |
| Compatible power supply                | 1   | ea  | See the [Supported Parts][support] list.                 |

<!-- | M3 x 6mm machine screws                | 4   | ea  |                                                          |
| M4 x 6mm machine screws                | 4   | ea  |                                                          | -->

!!! note "Note: Sharp Point Wood Screws"
    To substitute #6 x 3/4" with Metric screws, use M3 x 16mm or M3 x 20mm. Equivalent length machine screws can also be used if sharp point screws are unavailable.

!!! note "Note: Fast Blow Glass Fuses"
    You will need a fuse of the correct amperage for your power supply. If you are on 120V AC power and have a 350W power supply, a 3 amp fuse should be sufficient, for example.

    Determining the correct fuse for a given printer is beyond the scope of this documentation.

## Heat Set Inserts (HSIs)

If you are a printing an HSI case, you will need:

| Item                                   | Qty | UOM | Note                                                     |
|----------------------------------------|-----|-----|----------------------------------------------------------|
| [:material-cart: Heat Set Insert, M3, 4.6mm OD][bom_hsi_m3] | 24  | ea  | Tested with knurled inserts, 5.7mm length. Larger diameters may not work. |
| [:material-cart: M3 soldering iron tip for heat set inserts][bom_hsi_tips] | 1 | ea | |

## Core Configurations with Fans

Most Core component configurations mount at least one fan. The materials necessary are specified below.

### Base - Front

The base can mount up to three concealed 40mm fans in the intakes. The following are needed to mount *each* fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [:material-cart: 40x40x10mm axial fan][bom_4010]  | 1   | ea  |                                          |
| M3 x 16mm machine screws          | 4   | ea	| Some fans have recesses that instead use 10-12mm screws. |

### Main Body - Front

There are two versions of the front main body.

=== "Internal 40mm Intake"

    [![illustration][img_front_40mm]{ width="300" }][img_front_40mm]

    This version of the front main body has an optional 40mm fan.

    | Item                              | Qty | UOM | Note                                                     |
    |-----------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: 40x40x10mm axial fan][bom_4010]  | 1   | ea  |                                                          |
    | M3 x 16mm machine screws          | 4   | ea	| Some fans have recesses that instead use 10-12mm screws. |

=== "External 60mm Intake"

    [![illustration][img_front_60mm]{ width="300" }][img_front_60mm]

    This version of the front main body requires an externally mounted 60mm fan.

    | Item                              | Qty | UOM | Note                                                     |
    |-----------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: 60x60x15mm axial fan][bom_6015] | 1   | ea  | May also use 20mm or 25mm thick fans.     |
    | M4 x 25mm machine screws          | 4   | ea  | Add 10mm to fan depth for thicker fans.                  |
    | [:material-git: Fan Cage][git_fans] | 1   | ea  | :material-printer-3d-nozzle: Printed.                  |
    | [:material-git: Fan Gasket][git_fans] | 1   | ea  | :material-printer-3d-nozzle: Printed TPU. Optional.  |

### Main Body - Rear

The rear body also has two versions: one with dual exhausts and one without any.

=== "Dual 40mm Exhausts"

    [![illustration][img_rear_dual_40mm]{ width="300" }][img_rear_dual_40mm]

    This version adds two (2) externally mounted 40mm fans.

    | Item                              | Qty | UOM | Note                                                     |
    |-----------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: 40x40x10mm axial fans][bom_4010] | 2   | ea  |                                          |
    | M3 x 20mm machine screws          | 8   | ea	| Use 30mm screws for 20mm fans (not recommended).         |
    | [:material-git: Fan Cage][git_fans] | 2   | ea  | :material-printer-3d-nozzle: Printed.                  |
    | [:material-git: Fan Gasket][git_fans] | 2   | ea  | :material-printer-3d-nozzle: Printed TPU. Optional.  |

=== "No Exhaust Fans"

    [![illustration][img_rear_no_fans]{ width="300" }][img_rear_no_fans]

    There are no additional materials required for this version. 

    !!! important
        This rear main body must be used with a rear panel or lid that provides an exhaust fan.

## Tray and Panel Configurations

The Universal Bill of Materials includes the fasteners needed to mount panels and the the required trays. It does *not* include the hardware needed to attach anything to those panels and trays, as these are specific the hardware.

### Power Supply Trays

Currently, two power supply models are supported. You will need one (1) of the following:

| Item                              | Note                                                     |
|-----------------------------------|----------------------------------------------------------|
| [:material-cart: Mean Well LRS-350][bom_lrs350]   | Most Creality Ender-series printers use the LRS-350-24.  |
| [:material-cart: Mean Well RSP-500][bom_rsp500]   | **(Beta)** RSP-500-24 is used in the Ender 5 Plus.       |

### CPU Trays and Display Panels

Most configurations use a display and many have an SBC, such as a Raspberry Pi. See the [:material-git:`Trays/CPU`][git_cpu] and [:material-git:`Panels/Display`][git_display] folders for mounting information specific to your CPU tray and display panel.

### Other Supported Parts

See the [Supported Parts Overview][support] for a full list of parts and mounting locations. Some configurations require additional fasteners or fans.

[support]: support/index.md
[assembly]: assembly_v2/index.md

[img_front_40mm]: img/components/front_40mm.png
[img_front_60mm]: img/components/front_60mm.png
[img_rear_dual_40mm]: img/components/rear_40mm.png
[img_rear_no_fans]: img/components/rear_none.png