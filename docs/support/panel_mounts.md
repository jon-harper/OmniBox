---
title: Panel Mounts
summary: A list of panel-mounted components supported by OmniBox
authors: Jon Harper
date: 2022-07-22
prefix: ../
---

{% import 'format.md' as format with context %}

## Using Panel Mounts

 Panel mounts allow you to disconnect components without opening up the case. Some examples:

 - USB extensions for a webcam.
 - MicroSD extensions for an MCU or SBC.
 - Rear panel connectors for disconnecting the printer's wiring harness.

 Each panel type comes with a template for making your own panels. See [Creating New Panels](#creating-new-panels) below for more.

### Fans

OmniBox supports fans up to as large as 120mm. See the [:octicons-checklist-24: Fans][fans] page for a list of all fan options.

### MicroSD Extensions

These are availabe in short or long versions and are typically used with MCUs, though they can also be used with a CPU, such as a Raspberry Pi.

Most MCUs recommend either a short MicroSD extension (15cm/6" long) or longer (48cm/18") should be used.

{{ format.part_link('microsd_ext_short', prefix=prefix ) }}{ .md-button }

{{ format.part_link('microsd_ext_long', prefix=prefix) }}{ .md-button }

### USB Extensions

Right angle connectors are often a good choice, particularly for CPUs and large MCUs.

{{ format.part_link('usb2_typea_panel_mount', prefix=prefix) }}{ .md-button }

{{ format.part_link('usb2_typeb_panel_mount', prefix=prefix) }}{ .md-button }

{{ format.part_link('usb3_panel_mount', prefix=prefix) }}{ .md-button }

{{ format.part_link('usbc_panel_mount', prefix=prefix) }}{ .md-button }

### Keystone Jacks

These are commonly used on the front, side, or rear panels. A blank plate can occupy an unused jack cutout.

{{ format.part_link('usb3_keystone', prefix=prefix)}}{ .md-button }

{{ format.part_link('hmdi_keystone', prefix=prefix) }}{ .md-button }

{{ format.part_link('ethernet_keystone', prefix=prefix) }}{ .md-button }

{{ format.part_link('usbc_keystone', prefix=prefix) }}{ .md-button }

### Other Connectors

JST SM and Molex's Micro Fit 3.0 connectors can both be panel-mounted. These are useful when creating detachable wiring harnesses.

#### JST SM

!!! warning "Warning: Avoid JST SM as a hotend connector for enclosed printers"

These are good, low-current (3A max) connectors for devices such as limit switches, lights, steppers, and fans. However, they are larger than connectors with similar pin spacings.

{{ format.part_link('kit_jst_sm', prefix=prefix) }}{ .md-button }

Further reading: [:material-book-open: JST SM on The Clockmaker Project][clk_jst_sm]

#### Molex Micro Fit 3.0

These make excellent connectors for printers, particularly for hotends. They are rated to 5 Amperes with standard pins (9.5A with gold pins).

Connectors up to 2 row, 24 positions are available.

{{ format.part_link('kit_molex_mf3', prefix=prefix) }}{ .md-button }

Further reading: [:material-book-open: Molex Micro Fit 3.0 on The Clockmaker Project][clk_mf3]

#### XT-60

This connector is most well known for RC electronics and Creality printer beds. They should be used with 12 AWG wire for their rated current, though 13 AWG/2.5mm^2^ is often used for 220W beds.

{{ format.part_link('xt60_male_panel_mount', prefix=prefix) }}{ .md-button }

{{ format.part_link('xt60_female_panel_mount', prefix=prefix) }}{ .md-button }

Further reading: [:material-book-open: XT-60 on The Clockmaker Project][clk_xt60]

#### Molex Mini Fit Jr.

Mini Fit Jr connectors are commonly seen in computers for the ATX and PCIE connectors. They are reliable connectors rated up to 9.5A with 18 AWG (~1 mm^2^) wires.

{{ format.part_link('molex_minifit_2pos', prefix=prefix) }}{ .md-button }

{{ format.part_link('molex_minifit_4pos', prefix=prefix) }}{ .md-button }

Further reading: [:material-book-open: Mini Fit Jr on The Clockmaker Project][clk_mfj]

## Creating New Panels

In addition to templates for the panels themselves, template cutouts are available for panel-mounted connectors.

[:material-git: Panel Mounts][git_panel_mounts]{ .md-button }

The solid bodies in the `STEP` and Fusion 360 files:

- Have sufficient clearance to insert the connector; and
- Are the correct thickness for the connector (e.g. for panel mount ears to engage).

The Fusion 360 file also contains sketches for cut-and-paste.

### Other Templates

[Ginger Saw][contrib_ginger_saw] published on Printables a more extensive set of JST SM panel mounts, up to 10 pins.

[:octicons-link-external-24: JST SM Panel Mounts for 1.5-2mm panels][src_jst_panel_mounts]{ .md-button }

[fans]: fans.md

[img_rear]: ../img/components/rear.webp
[img_front]: ../img/components/front_panel.webp
[img_side]: ../img/components/side.webp