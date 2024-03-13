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

{%- set (stock_norm, stock_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.stock)) -%}
{%- set (hsi_norm, hsi_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.hsi)) %}
{%- set (min_hsi, min_hsi_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.min_hsi)) %}
{%- set (min_stock, min_stock_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.min_stock)) %}

This page covers what you need to know before sourcing parts for an OmniBox. At the end of the page,
several sample bills of materials are included, as well.

We cannot (yet) generate a complete, customized Bill of Materials on-demand, but there is a [Print Checklist][checklist] that contains each type of part to print, how many, and a link to the relevant [:octicons-checklist-24: Options & Support][support] page. Every support page entry contains a bill of materials. These quantities can be added to give a total.

The examples given on this page are included give a general idea of what to expect.

## Fasteners

### Cap Screws

OmniBox is largely compatible with both M3 socket head cap screws (SHCS) and button head cap screws (BHCS). Core assembly
has several recessed screw holes that are not compatible with button head screws; otherwise, the two are interchangeable.

All sourcing links are for SHCS.

!!! note
    [:octicons-checklist-24: Power supplies][psu] mount using M4 screws. These are the only M4 screws needed in a build.

### Stock vs. HSI

Printed parts are are either "Stock" (where screws thread into the printed plastic) or "HSI", for heat set inserts.
HSI parts use brass heat set inserts for screw holes. These are more durable than Stock but require purchasing
and installing inserts.

Most components come with both Stock and HSI variants. Those with only one variant are typically Stock-only.

### Sharp Point Wood Screws

To substitute #6 x 3/4" with Metric machine screws, use M3 x 16mm or M3 x 20mm. Equivalent length machine screws can 
be used if sharp point screws are unavailable.

Sharp point screws are only used in Stock builds.

### Heat Set Inserts

OmniBox exclusively uses M3 x 5mm O.D. x 4mm Length ("Voron-style") heat set inserts. User-contributed parts
that require inserts also use these inserts.

Most heat set inserts are installed into open-ended holes, allowing longer-than-specified screws to be used if necessary, e.g., M3 x 8mm instead of 6mm.

## Electrical

### IEC Sockets and Fuses
!!! warning
    IEC socket fuses do **not** replace the fuses on your board or inline fuses.

Most Bases mount a fused IEC C14 power inlet in the back. Users will typically want to fuse with fast or medium blow
fuses on the socket. 

The Oznium blog has an [:material-book-open: excellent guide][fuse_guide] on choosing a fuse size.

### Power Switch

The Base comes with several power switch options. Not all power supplies and switches are compatible; check the
[:octicons-checklist-24: PSU Tray][psu] to determine which switch to use with your power supply.

### Wiring

- Wiring is specified for a configuration including an IEC power socket, power switch, and power supply.
- Additional connectors and wiring may be needed, including for [:material-book-open: grounding your bed/frame to earth][ground_guide].
- *All wiring and fusing considerations are configuration-specific.*

## Minimal Builds

The lists below are starting points to determine what you will need for your own build. These lists are made by
combining the materials lists from a [:octicons-checklist-24: 36mm Base][base] and a [:octicons-checklist-24: Main Body][main_body].

- A complete Core case (Main Body and Base)
- *Fasteners to mount all panels*
- *Fasteners to mount an MCU tray*
- IEC power inlet
- No power switch

### Heat Set Inserts (HSI)

=== "Hardware"
{{ make_indented(fmt.bom_table(min_hsi), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(min_hsi_print), '    ') }}

### Stock

=== "Hardware"
{{ make_indented(fmt.bom_table(min_stock), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(min_stock_print), '    ') }}

## Sample Bill of Materials

The sample builds below contain complete lists of both hardware and printed parts.

Due to the number of possible configurations, wiring is only included for the IEC socket,
power switch, and power supply.

### Basic Stock Build

- MCU: Bigtreetech SKR E3
- Display: Mini12864
- CPU: None
- PSU: Mean Well LRS-350
- 1x 60mm exhaust fan
- 2x 40mm intake fans
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
- 1x 60mm exhaust fan
- 1x 40mm, 1x 50mm intake fans
- Rocker switch
- 5V/3A buck converter
- Basic LM2596 buck converter
- Heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(hsi_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(hsi_print), '    ') }}

[support]:          support/index.md    "Overview of supported parts"
[main_body]:        support/main_body.md "List of Main Body configurations"
[base]:             support/base.md     "List of Base configurations"
[mcu]:              support/mcu.md      "List of supported MCUs"
[psu]:              support/psu.md      "List of supported power supplies"
[display]:          support/display.md  "List of supported Displays"
[support_cpu]:      support/cpu.md      "List of supported SoC CPUs"
[lower_bay]:        support/lower_bay.md "List of supported lower bay components"
[panel_mount]:      support/panel_mounts.md "Panel mount overview"
[assembly]:         assembly/index.md   "Assembly documentation"
[checklist]:        checklist.md        "Checklist of parts to print"