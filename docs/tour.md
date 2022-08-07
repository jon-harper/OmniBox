---
title: A Guided Tour
summary: Visual tour of OmniBox
authors: Jon Harper
date: 2022-08-04
---

This is a visual tour of an OmniBox. This page demonstrates:

1. What each part does; and
2. How OmniBox fits together.

Links are provided to the respective git folder for each component type.

## Core Components

[![the five core components][1]][1]

Core components form the basis of every electronics case. They can be found in the [`Core`][14] folder in the GitHub repository.

There are five (5) Core components: three (3) universal parts and two (2) that have variations.

1. Main Body - Front
2. Main Body - Crossbar
3. Main Body - Rear
4. Base - Front
5. Base - Rear

### Universal Core Parts

These parts are required. They do not have variations.

#### Base - Front

This is part of a pair that covers the power supply. There is a 30mm x 11mm rocker switch cutout in front, as well as air vents and an optional 40mm fan.

#### Base - Rear 

The back covers the rest of the power supply and mounts a fused IEC power plug.

#### Main Body - Crossbar

This is a simple crossbar that covers the joint between the lids and front display.

#### STLs

| Part                       | Printed Qty | Link     |
|----------------------------|-------------|----------|
| `Base - Front.stl`         | 1           | [STL][1] |
| `Base - Rear.stl`          | 1           | [STL][2] |
| `Main Body - Crossbar.stl` | 1           | [STL][3] |

### Core Parts with Variants

Your power supply unit (PSU) will mount underneath the main body. The [`Core`][14] folder has one subfolder for each supported PSU.

Currently the two supported PSUs are:

- Mean Well LRS-350
- Mean Well RSP-500

#### Main Body - Front

The front main body comes in two variations to choose from. If you print the version with a 60mm intake fan, you will need to print the appropriate [fan cage][6] and (optionally) a TPU gasket.

| 40mm Optional Fan | 60mm External Fan |
|-------------------|-------------------|
| ![front with 40mm fan mount][34] | ![front with 60mm fan cutout][35]

| Variation                                | Printed Qty |LRS-350 Link | RSP-500 Link |
|------------------------------------------|-------------|--------------|--------------|
| `Main Body - Front with 40mm Intake.stl` | 1           | [STL][7]     | [STL][9]     |
| `Main Body - Front with 60mm Intake.stl` | 1           | [STL][8]     | [STL][10]    |

#### Main Body - Rear

The rear main body also comes in two variations. For the dual 40mm fan version, you will also need to print [40mm fan cages][6] and (optionally) TPU gaskets.

| Dual 40mm Fans  | No Fan Mounts |
|-----------------|---------------|
| ![rear with 40mm fan cuouts][36] | ![rear body without fan cutouts][37]

| Variation                                | Printed Qty | LRS-350 Link | RSP-500 Link |
|------------------------------------------|-------------|--------------|--------------|
| `Main Body - Rear No Fans.stl`           | 1            | [STL][11]   | [STL][15]   | 
| `Main Body - Rear with 40mm Exhausts.stl`| 1            | [STL][12]   | [STL][16]   |

## Trays

[![the three types of trays][2]][2]

| Trays           | Qty     | Folder Link | Notes     |
|-----------------|---------|-------------|-----------|
| MCU tray        | 1       | [Link][22]  |           |
| CPU tray        | 1       | [Link][20]  | Print a blank cover if unused. |
| Lower bay trays | 0-4     | [Link][21]  | Optional. |

The links above are to folders instead of individual `.STL` files. You will need to choose the right `.STL` files for your components. Each folder has a `readme.md` with information about product support and any attribution credits.

Templates are usually available in both STEP and Fusion 360 format to add support for new products.

### MCU Tray

MCU trays mount a microcontroller unit--your 3D printer board.

[List of supported MCUs][24]

### Lower Bay

The lower bay is a configurable area to mount parts like buck converters and MOSFETs.

[List of supported lower bay parts][25]

### CPU Tray

The CPU tray is an optional mount for a Raspberry Pi. There is a blank cover if you do not use a Raspberry Pi or other SoC CPU.

[List of supported CPUs][23]

## Panels

[![callout of each panel type][3]][3]

1. Front panel
2. Display panel
3. Lid
4. Rear panel (not visible)
5. Fan cage (see [next section](#fan-cages))

| Panels        | Qty | Folder Link | Notes |
|---------------|-----|-------------|-------|
| Display Mount | 1   | [Link][26]  |       |
| Front Panel   | 1   | [Link][27]  |       |
| Lid           | 1-2 | [Link][28]  |       |
| Rear Panel    | 1   | [Link][29]  | See [directions](#rear-panel) below. |

As with trays, the links above are to folders rather than individual `.STL` files. Panels have a range of supported parts and options. 

There is a blank STEP and Fusion template for each panel category. Additionally, all panel variations have both STEP and Fusion source files.

### Front Panel

The front panel serves as an air vent and location to put an SD card reader extension. USB panel mount extensions are also a common accessory.

### Display Panel

This area mounts numberous types of displays, from the basic 128x64 display to Raspbery Pi TFTs.

### Lid(s)

The lid is both a way into your case and a configurable panel.

There are two types of lids: full-length and half-length lids. You can either print one (1) full-length lid or two (2) half-length lids.

### Rear Panel

The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is also available for customization.

Rear panels with panel mounted connectors are an active area of work.

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| [`Generic`][30]  | These have large holes for passing wires through and come in a number of common variations. | ...You want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [`Custom`][31]   | Designed for users of common printer configurations. | ...Your printer has a configuration available. |
| [`Molex`][32]    | Use Molex Micro Fit 3 panel mounted connectors. Wiring diagrams for each panel are included. | ...You plan to create a wiring harness for an enclosed printer. |
| [`Template`][33] | A Fusion template with profiles for panel mounted connectors and fans. | ...You want to create your own panel. |

## Fan Cages

Externally mounted fans use [fan cages][13] to cover the fan blades. There are a large number of fan sizes supported, each with a matching gasket.

[1]: img/printed_parts/core.png
[2]: img/printed_parts/trays.png
[3]: img/printed_parts/panels.png
[4]: printing.md#core-parts-with-variants
[5]: support/boards.md
[6]: https://github.com/jon-harper/OmniBox/tree/main/Fan%20Cages
[7]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Front%20with%2040mm%20Intake.stl
[8]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Front%20with%2060mm%20Intake.stl
[9]: ttps://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20RSP-500/Main%20Body%20-%20Front%20with%2040mm%20Intake.stl
[10]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20RSP-500/Main%20Body%20-%20Front%20with%2060mm%20Intake.stl
[11]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Rear%20No%20Fans.stl
[12]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Rear%20with%2040mm%20Exhausts.stl
[13]: https://github.com/jon-harper/OmniBox/tree/main/Fan%20Cages
[14]: https://github.com/jon-harper/OmniBox/tree/main/Core/
[15]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20RSP-500/Main%20Body%20-%20Rear%20No%20Fans.stl
[16]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20RSP-500/Main%20Body%20-%20Rear%20with%2040mm%20Exhausts.stl
[20]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[21]: https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay
[22]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU
[23]: support/boards.md#soc-cpu-boards
[24]: support/boards.md#mcu-boards
[25]: support/lower_bay.md
[26]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[27]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel
[28]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid
[29]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel
[30]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Generic
[31]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Custom
[32]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Molex
[33]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Template
[34]: img/examples/front_40mm.png
[35]: img/examples/front_60mm.png
[36]: img/examples/rear_40mm.png
[37]: img/examples/rear_no_fans.png