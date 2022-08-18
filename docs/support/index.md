---
title: Parts Overview
summary: A list of parts supported by OmniBox
authors: Jon Harper
date: 2022-07-03
---

This is an overview of components supported by OmniBox. The linked git folders should contain both an `STL` for printing and `STEP` files for modification. Fusion 360 source files are also usually available.

## Power Supplies

OmniBox supports the Mean Well LRS-350 and clones (e.g., Landy). There is preliminary support for the Mean Well RSP-500.

The main body comes in different versions for power supply compatibility. Each power supply has a git folder under `Core`, e.g `Core/Mean Well LRS-350`. After you [choose a front and rear main body version][9], print the STLs from the folder that matches your power supply.

| Power Supply                      | Note                                                     |
|-----------------------------------|----------------------------------------------------------|
| [Mean Well LRS-350][7]            | Most Creality Ender-series printers use the LRS-350-24.  |
| [Mean Well RSP-500][8]            | **(Preliminary)** RSP-500-24 is used in the Ender 5 Plus.|

## Trays

### CPU and MCU Trays

See [CPU and MCU Boards][2] for a list of boards with existing trays.

### Lower Bay Trays

OmniBox has a lower bay for mounting parts such as buck converters and solid state elays (SSRs). Some trays mount multiple parts or an added 40mm fan.

See [Lower Bay Components][4] for a complete list of parts with trays available.

## Display Screen Panels

[Display Panels][3] are used for LCD displays. Note that these are not the same as Raspberry Pi screens.

## Front and Rear Panels

These panels are typically used for [panel mounted connectors and extensions](panel_mounts.md).

Generic rear panels are available with cutouts to pass wiring directly without using connectors.

## Fans

An assortment of fans are supported and include cages and optional TPU shims. See the [Fans][5] page for a full list.

The front and rear main bodies come in versions with and without fans. The rear panel and lid can also be used for mounting fans.

See the [Guided Tour][6] to help choose the best configuration for your available parts.

[1]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel
[2]: boards.md
[3]: displays.md
[4]: lower_bay.md
[5]: fans.md
[6]: ../tour.md
[7]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20LRS-350
[8]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20RSP-500
[9]: ../tour.md#core-parts-with-variants