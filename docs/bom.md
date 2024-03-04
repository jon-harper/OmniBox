---
title: Bill of Materials
summary: Guide to selecting parts for OmniBox.
authors: Jon Harper
date: 2022-05-15
bom_sample:
  stock: 
    - comp_base_toggle_0_9_11: 0
    - comp_mb_0_9_11: 0
    - comp_btt_skr_e3_v2 : 0
    - comp_mw_lrs350 : 0
    - comp_mini_12864 : 0
    - comp_carry_lid : 0
    - comp_rear_generic_60mm_fan : 0
    - comp_fp_vent : 1
    - comp_btm_hex_v3 : 0
    - comp_btm_hex_v3 : 1
    - comp_side_40mm_v2 : 0
    - comp_side_40mm_v2 : 0
    - comp_side_blank_v2 : 0
    - comp_side_blank_v2 : 0
  hsi:
    - comp_base_rocker_0_9_11: 1
    - comp_mb_0_9_11: 1
    - comp_btt_skr_3_v2 : 0
    - comp_mw_lrs350 : 1
    - comp_generic_12864 : 0
    - comp_carry_lid : 3
    - comp_blank_lid : 2
    - comp_rear_generic_60mm_fan : 0
    - comp_fp_sd : 1
    - comp_btm_hex_v3 : 0
    - comp_btm_hex_v3 : 1
    - comp_cpu_universal_v3 : 3 #40mm fan with HSI
    - comp_side_50mm_v2 : 1
    - comp_side_rj45_usb_ext_v2 : 0
    - comp_side_blank_v2 : 0
    - comp_sslhong_buck : 3
    - comp_basic_lm2596: 0
  min_hsi:
    - comp_base_iec_0_9_11: 1
    - comp_mb_0_9_11: 1
  min_stock:
    - comp_base_iec_0_9_11: 0
    - comp_mb_0_9_11: 0
---

{% import 'format.md' as fmt with context %}

The Bill of Materials is a base list common to all builds. Additional components (including fasteners) are listed separately below.

{%- set (stock_norm, stock_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.stock)) -%}
{%- set (hsi_norm, hsi_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.hsi)) %}
{%- set (min_hsi, _) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.min_hsi)) %}
{%- set (min_stock, _) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.min_stock)) %}

## Fasteners

### Cap Screws

OmniBox is largely compatible with both M3 socket head cap screws (SHCS) and button head cap screws (BHCS). Core assembly
has several recessed screw holes that are not compatible with button head screws; otherwise, button head screws can be used
freely in place of socket head screws.

All sourcing links are for SHCS.

!!! note
    [Power supplies][psu] mount using M4 screws.

### Sharp Point Wood Screws

!!! note 
    Sharp point screws are only used in stock builds.

To substitute #6 x 3/4" with Metric screws, use M3 x 16mm or M3 x 20mm. Equivalent length machine screws can also be used if sharp point screws are unavailable.

### Heat Set Inserts

OmniBox exclusively uses M3 x 5mm O.D. x 4mm Length ("Voron-style") heat set inserts. User-contributed parts that require inserts also use these inserts.

Most heat set inserts are installed open-ended, allowing longer-than-specified screws to be used if necessary, e.g., M3 x 10mm instead of 8mm.

## Electrical

### IEC Sockets and Fuses
!!! warning
    IEC socket fuses do **not** replace the fuses on your board or inline fuses.

Most Bases mount a fused IEC C14 power inlet in the back. Users will typically want to fuse with fast or medium blow
fuses on the socket. 

The Oznium blog has an [excellent guide][fuse_guide] on choosing a fuse size.

### Power Switch

The Base comes with several power switch options. Not all power supplies are compatible with all switches; check the
[PSU Tray][psu] to determine which switch to use with your power supply.

### Wiring

- Wiring is specified for a configuration including an IEC power socket, power switch, and power supply.
- Additional connectors and wiring may be needed, including for [grounding your bed/frame to earth][ground_guide].
- *All wiring and fusing considerations are configuration-specific.*

## Minimal Builds

The lists below are starting points to estimate how many fasteners you will need for your own build.

- A complete Core case (Main Body and Base)
- No trays or panels specified.
- Fasteners needed to mount panels.
- Fasteners for an MCU tray.
- IEC power inlet
- No specified power switch.

### Heat Set Inserts (HSI)

{{ fmt.bom_table(min_hsi) }}

### Stock

{{ fmt.bom_table(min_stock) }}

## Sample Bill of Materials

The sample builds below contain complete lists of both hardware and printed parts.

Due to the number of possible configurations, wiring is only included for the IEC socket,
power switch, and power supply.

### Basic Stock Build

- MCU: Bigtreetech SKR E3
- Display: Mini12864
- CPU: None
- PSU: Mean Well LRS-350
- 60mm exhaust fan
- Dual 40mm intake fans
- Toggle switch
- No heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(stock_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(stock_print), '    ') }}

### Assembly HSI Build

This is the materials list for the case illustrated in the [Assembly Guide][assembly].

- MCU: Bigtreetech SKR 3
- Display: Generic 12864
- CPU: Raspberry Pi 4B
- PSU: Mean Well LRS-350
- 60mm exhaust fan
- 40mm, 50mm intake fans
- Rocker switch
- 5V/3A buck converter
- Basic LM2596 buck converter
- Heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(hsi_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(hsi_print), '    ') }}

[support]:          support/index.md    "Overview of supported parts"
[mcu]:              support/mcu.md      "List of supported MCUs"
[psu]:              support/psu.md      "List of supported power supplies"
[display]:          support/display.md  "List of supported Displays"
[support_cpu]:      support/cpu.md      "List of supported SoC CPUs"
[lower_bay]:        support/lower_bay.md "List of supported lower bay components"
[panel_mount]:      support/panel_mounts.md "Panel mount overview"
[assembly]:         assembly/index.md   "Assembly documentation"
