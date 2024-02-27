---
title: Bill of Materials
summary: Guide to selecting parts for OmniBox.
authors: Jon Harper
date: 2022-05-15
bom_sample:
  stock: 
    - comp_base_rocker_0_9_11: 0
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
    - comp_base_toggle_0_9_11: 1
    - comp_mb_0_9_11: 1
    - comp_btt_octopus_v2 : 0
    - comp_mw_lrs350 : 1
    - comp_btt_hdmi5 : 0
    - comp_carry_lid : 1
    - comp_rear_generic_60mm_fan : 0
    - comp_fp_vent : 1
    - comp_btm_hex_v3 : 0
    - comp_btm_hex_v3 : 1
    - comp_cpu_universal_v3 : 3 #40mm fan with HSI
    - comp_side_50mm_v2 : 1
    - comp_side_blank_v2 : 0
    - comp_side_blank_v2 : 0
  test:
    - comp_base_rocker_0_9_11: 1
    - comp_mb_0_9_11: 1
    - comp_btt_octopus_v2 : 0
    - comp_mw_lrs450: 1
    - comp_generic_12864 : 0
    - comp_cpu_universal_v3: 3
    - comp_fp_sd : 1
    - comp_rear_generic_60mm_fan : 0
    - comp_btm_hex_v3 : 1
    - comp_btm_mw_v3: 0
    - comp_carry_lid : 3
    - comp_blank_lid : 2
    - comp_side_40mm_v2 : 0
    - comp_side_50mm_v2 : 0
    - comp_side_blank_v2 : 0
    - comp_sslhong_buck : 3
---

{% import 'format.md' as fmt with context %}

The Bill of Materials is a base list common to all builds. Additional components (including fasteners) are listed separately below.

{%- set (stock_norm, stock_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.stock)) -%}
{%- set (hsi_norm, hsi_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.hsi)) %}
{%- set (test_norm, test_print) = splitPrintedMaterials(materialsFromYamlComponentList(bom_sample.test)) %}
    
## Fasteners

### Cap Screws

OmniBox is largely compatible with both M3 socket head cap screws (SHCS) and button head cap screws (BHCS). Core assembly
has several recessed screw holes that are not compatible with button head screws; otherwise, button head screws can be used
freely in place of socket head screws.

All sourcing links are for SHCS.

!!! note
    [Power supplies](#psu-trays) mount using M4 screws.

### Sharp Point Wood Screws

!!! note 
    Sharp point screws are only used in stock builds.

To substitute #6 x 3/4" with Metric screws, use M3 x 16mm or M3 x 20mm. Equivalent length machine screws can also be used if sharp point screws are unavailable.

### Heat Set Inserts

OmniBox exclusively uses "Voron-style" (M3 x 5mm O.D. x 4mm Length) heat set inserts. User-contributed parts that require inserts also use these inserts.

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

## Sample Bill of Materials

Below are two minimal bills of materials for a very simple build and a more advanced build that includes inserts and
more involved wiring.

Due to the number of possible configurations, wiring is only included for the IEC socket, power switch, and power supply.

### Simple Stock Build

- MCU: Bigtreetech SKR E3
- Display: Mini12864
- CPU: None
- 60mm exhaust fan
- Dual 40mm intake fans
- Rocker switch
- No heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(stock_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(stock_print), '    ') }}

### Intermediate HSI Build

- MCU: Bigtreetech Octopus 1.1
- Display: Bigtreetech HDMI5
- CPU: Raspberry Pi 4B
- 60mm exhaust fan
- 40mm, 50mm intake fans
- Toggle switch
- Heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(hsi_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(hsi_print), '    ') }}

### 0.9.11 Validation Build

!!! note
    This is a developer reference section and will be removed before release.

- MCU: Bigtreetech Octopus 1.1
- Display: Generic 12864
- CPU: Raspberry Pi 4B
- PSU: Mean Well LRS-450
- 60mm exhaust fan
- 2x 40mm, 1x 50mm intake fans
- Rocker switch
- Front panel SD card extension
- 5V/3A buck converter
- Heat set inserts

=== "Hardware"
{{ make_indented(fmt.bom_table(test_norm), '    ') }}
=== "Printed"
{{ make_indented(fmt.bom_table(test_print), '    ') }}

[support]:          support/index.md    "Overview of supported parts"
[mcu]:              support/mcu.md      "List of supported MCUs"
[psu]:              support/psu.md      "List of supported power supplies"
[display]:          support/display.md  "List of supported Displays"
[support_cpu]:      support/cpu.md      "List of supported SoC CPUs"
[lower_bay]:        support/lower_bay.md "List of supported lower bay components"
[panel_mount]:      support/panel_mounts.md "Panel mount overview"
[assembly]:         assembly/index.md   "Assembly documentation"
