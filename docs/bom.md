---
title: Bill of Materials
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

The Universal Bill of Materials is a base list common to all builds. Additional components based on your build configuration are listed separately.

- There are no affiliate links used on this site.
- The :material-cart: shopping cart icon indicates an external link to a shopping website.
- These links are not an endorsement and for reference only.
- The design allows for longer-than-specified screws in certain locations. The [assembly guide][assembly] notes where substitutions can be made.
- Wiring is only specified for the IEC power socket, power switch, and power supply. Additional wiring and fusing considerations are configuration-specific.

## Universal Bill of Materials

These parts are common to all case builds. See below for additional requirements based on configuration.

| Item                                   | Qty | UOM | Note                                                     |
|----------------------------------------|-----|-----|----------------------------------------------------------|
| [:material-cart: PLA+][bom_pla] or [:material-cart: PETG][bom_petg] filament | 2   | kg  | Typical use is less than 1.5kg (PLA+). |
| [:material-cart: TPU 95A filament][bom_tpu] | 0.05| kg  | Optional. Quantity is maximum estimated.            |
| [:material-cart: 16 awg/1.25mm stranded hookup wire][bom_16awg_wire] | 0.5 | m   | Prefer red.                |
| [:material-cart: Spade connectors, 14-16 awg, Female, Insulated][bom_spade_connector] | 3   | ea  |           |
| [:material-cart: Fork connectors, 14-16 awg, #8, Insulated][bom_fork_connector]       | 1   | ea  | Ring connectors can be used as well. |
| [:material-cart: SPST snap-in rocker switch][bom_switch]        | 1   | ea  | 30mm x 11mm profile. Identical to Creality Ender power switch. |
| [:material-cart: IEC C14 socket with fuse][bom_iec]          | 1   | ea  |                                    |
| Glass Fuse, 5x20mm                     | 1   | ea  | See note below.                                          |
| Compatible MCU                         | 1   | ea  | See the [Supported Parts][support] list.                 |
| Compatible 128x64 or TFT LCD display   | 1   | ea  | See the [Supported Parts][support] list.                 |
| Compatible power supply                | 1   | ea  | See the [Supported Parts][support] list.                 |

!!! note "Note: Glass Fuses"
    Socket fuses do *not* replace the fuses on your board or inline fuses.

    Users will typically want to fuse with fast or medium blow fuses on the socket. Determining the correct fuse for a given configuration is beyond the scope of this documentation. The Oznium blog has an [excellent guide][fuse_guide] on choosing a fuse size.

!!! note "Note: Wiring and Connectors"
    This list is not all-encompassing for wiring. Additional connectors and wiring may be needed, including for [grounding your bed/frame to earth][ground_guide].

### Fasteners

Cases with heat set inserts use shorter fasteners in some locations. Use the Stock list if you are not printing a case with inserts.

OmniBox is largely assembled with M3 screws and is compatible with both socket head and button head cap screws. All links are to socket head screws, where applicable. [Power supplies](#psu-trays) are the exception, and use M4 button head cap screws.

=== "Stock"

    | Fasteners                              | Qty | UOM | Note                                                     |
    |----------------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: M3 x 6mm machine screws][bom_m3_6]    | 4   | ea  |                                                          |
    | [:material-cart: M3 x 8mm machine screws][bom_m3_8]    | 44  | ea  |                                                          |
    | [:material-cart: M3 x 10mm machine screws][bom_m3_10]  | 6   | ea  | May use 12mm instead to simplify materials.              |
    | [:material-cart: M3 x 12mm machine screws][bom_m3_12]  | 8   | ea  |                                                          |
    | [:material-cart: M3 x 20mm machine screws][bom_m3_20]  | 2   | ea  |                                                          |
    | [:material-cart: #6 x 3/4" sharp point wood screws][bom_wood_screw] | 8   | ea  | See note below.             |

=== "HSI"
    
    | Fasteners                              | Qty | UOM | Note                                                     |
    |----------------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: Heat Set Insert, M3, 5mm OD x 4mm L][bom_hsi_m3] | 24  | ea  | Commonly called "Voron-style". |
    | [:material-cart: M3 x 6mm machine screws][bom_m3_6]    | 24  | ea  |                                                          |
    | [:material-cart: M3 x 8mm machine screws][bom_m3_8]    | 28  | ea  |                                                          |
    | [:material-cart: M3 x 10mm machine screws][bom_m3_10]  | 2   | ea  | May use 12mm instead to simplify materials.              |
    | [:material-cart: M3 x 12mm machine screws][bom_m3_12]  | 8   | ea  |                                                          |
    | [:material-cart: M3 x 20mm machine screws][bom_m3_20]  | 2   | ea  |                                                          |
    | [:material-cart: #6 x 3/4" sharp point wood screws][bom_wood_screw] | 8   | ea  | See note below.             |

    Additionally, you will need an [:material-cart: M3 soldering iron tip for heat set inserts][bom_hsi_tips].

!!! note "Note: Sharp Point Wood Screws"
    To substitute #6 x 3/4" with Metric screws, use M3 x 16mm or M3 x 20mm. Equivalent length machine screws can also be used if sharp point screws are unavailable.

!!! note "Heat Set Inserts"
    Starting with v0.9.10, OmniBox exclusively uses "Voron-style" (M3 x 5mm x 4mm) HSIs. User mods that require inserts universally use the Voron-style inserts.

### MicroSD Reader Extensions

Each MCU tray on the [MCU support page](support/mcu.md) has a field for whether a short or long MicroSD card reader extension is necessary (if using one for the front panel).

- Short: [:material-cart: LANMU MicroSD Card Reader Extension][bom_lanmu_micro_sd]
- Long: [:material-cart: ELECTOP MicroSD Card Reader Extension][bom_electop_micro_sd]

## Core Configurations with Fans

Most Core component configurations mount at least one fan. The materials necessary are specified below.

### Base - Front

The base can mount up to three concealed 40mm fans in the intakes. The following are needed to mount *each* fan:

| Item                              | Qty | UOM | Note                                                     |
|-----------------------------------|-----|-----|----------------------------------------------------------|
| [:material-cart: 40x40x10mm axial fan][bom_4010]      | 1   | ea  |                                          |
| [:material-cart: M3 x 16mm machine screws][bom_m3_16] | 4   | ea	| Some fans have recesses that instead use 10-12mm screws. |

### Main Body - Front

There are two versions of the front main body.

=== "Internal 40mm Intake"

    [![illustration][img_front_40mm]{ width="300" }][img_front_40mm]

    This version of the front main body has an optional 40mm fan.

    | Item                              | Qty | UOM | Note                                                     |
    |-----------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: 40x40x10mm axial fan][bom_4010]      | 1   | ea  |                                                          |
    | [:material-cart: M3 x 16mm machine screws][bom_m3_16] | 4   | ea	| Some fans have recesses that instead use 10-12mm screws. |

=== "External 60mm Intake"

    [![illustration][img_front_60mm]{ width="300" }][img_front_60mm]

    This version of the front main body requires an externally mounted 60mm fan.

    | Item                              | Qty | UOM | Note                                                     |
    |-----------------------------------|-----|-----|----------------------------------------------------------|
    | [:material-cart: 60x60x15mm axial fan][bom_6015] | 1   | ea  | May also use 20mm or 25mm thick fans.     |
    | [:material-cart: M4 x 25mm machine screws][bom_m4_25]          | 4   | ea  | Add 10mm to fan depth for thicker fans.                  |
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
    | [:material-cart: M3 x 20mm machine screws][bom_m3_20]  | 8   | ea	| Use 30mm screws for 20mm fans (not recommended).         |
    | [:material-git: Fan Cage][git_fans] | 2   | ea  | :material-printer-3d-nozzle: Printed.                  |
    | [:material-git: Fan Gasket][git_fans] | 2   | ea  | :material-printer-3d-nozzle: Printed TPU. Optional.  |

=== "No Exhaust Fans"

    [![illustration][img_rear_no_fans]{ width="300" }][img_rear_no_fans]

    There are no additional materials required for this version. 

    !!! important
        This rear main body must be used with a rear panel or lid that provides an exhaust fan.

## Tray and Panel Configurations

The Universal Bill of Materials includes the fasteners needed to mount panels and the the required trays. It does not include the hardware needed to attach electronics to those panels and trays.

The [Supported Parts Overview][support] has a full list of parts and mounting locations. Some configurations require additional fasteners or fans.

### PSU Trays

Power supplies are notable for mounting to the tray with M4 x 6mm button head cap screws. See the [list of supported PSUs][psu] for quantities.

!!! note "Note: M4 Screws"
    Socket head cap screws have heads that are too tall to fit the PSU in the case.

### Lower Bay Trays

Each tray (short or long) uses four (4) M3 x 6mm screws to mount the tray. Additional materials are listed on the [Lower Bay Components][lower_bay] page.

### Panel Mounted Parts

Panel mounts are a way of providing external connectors to internal parts, such as the MCU or CPU board USB ports. The [Panel Mounts][panel_mount] page discusses this in more detail.

[support]:          support/index.md    "Overview of supported parts"
[psu]:              support/psu.md      "List of supported PSUs"
[suport_mcu]:       support/mcu.md      "List of supported MCUs"
[support_cpu]:      support/cpu.md      "List of supported SoC CPUs"
[lower_bay]:        support/lower_bay.md "List of supported lower bay components"
[panel_mount]:      support/panel_mounts.md "Panel mount overview"
[assembly]:         assembly/index.md "Assembly documentation"

[img_front_40mm]: img/components/front_40mm.png
[img_front_60mm]: img/components/front_60mm.png
[img_rear_dual_40mm]: img/components/rear_40mm.png
[img_rear_no_fans]: img/components/rear_none.png