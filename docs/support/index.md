---
title: Parts Overview
summary: A list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-03
---

This is an overview of components supported by OmniBox. The linked git folders should contain both an `STL` for printing and `STEP` files for modification. Fusion 360 source files are also usually available.

!!! tip
    Looking for a part that isn't listed? [Open an issue!][git_issues]

## Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays in red.</figcaption>
</figure>

### Power Supplies

OmniBox supports the Mean Well LRS-350 and clones (e.g., Landy-branded). There is preliminary support for the Mean Well RSP-500.

A template is available to add additional support.

| Power Supply                        | Note                                                     |
|-------------------------------------|----------------------------------------------------------|
| [Mean Well LRS-350][git_psu_lrs350] | Most Creality Ender-series printers use the LRS-350-24.  |
| [Mean Well RSP-500][git_psu_rsp500] | **(Preliminary)** RSP-500-24 is used in the Ender 5 Plus.|

### Other Trays

- [MCU Boards][mcu] for MCU Trays
- [SoC CPUs][cpu] for CPU Trays
- [Lower Bay Components][lower_bay] lists parts mountable on a Lower Bay Tray

## Panels

<figure markdown>
  [![the three types of trays][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

### Display Screen Panels

[Display Panels][displays] are used for LCD displays, including Raspberry Pi TFTs.

### Front, Side, and Rear Panels

These panels are typically used for [panel mounted connectors and extensions][panel_mounts] and mounting [fans][fans].

Generic rear panels are available with cutouts to pass wiring directly without using connectors.

## Fans

An assortment of fans are supported and include cages and optional TPU shims. See the [Fans][fans] page for a full list.

The front and rear main bodies come in versions with and without fans. The rear panel and lid can also be used for mounting fans.

See the [Guided Tour][tour] to help choose the best configuration for your available parts.

[panel_mounts]: panel_mounts.md
[cpu]: cpu.md
[mcu]: mcu.md
[displays]: displays.md
[lower_bay]: lower_bay.md
[fans]: fans.md
[tour]: ../tour.md
[9]: ../tour.md#core-parts-with-variants

[img_trays]:  ../img/components/trays.png
[img_panels]:  ../img/components/panels.png