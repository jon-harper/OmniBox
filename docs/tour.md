---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 2022-08-04
---

This is a visual tour of an OmniBox. This page demonstrates:

1. What the core parts of OmniBox are, along with their variations;
2. What trays and panels do; and
3. How these pieces fit together.

Links are provided to the respective git folder for each component type.

## :material-alpha-c-box: Core Components

Core components form the basis of every electronics case. They can be found in the [`Core`][14] folder in the GitHub repository.

There are five (5) Core components: three (3) universal parts and two (2) that have variations.

[![the five core components][1]][1]

These are the components, as numbered in the picture above.

1. :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front
2. :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar
3. :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear
4. :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front
5. :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear

### Universal Parts

These are required and do not have variations.

#### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front

This is the front of two base pieces that cover the power supply. There is a 30mm x 11mm rocker switch cutout in front, as well as air vents and an optional 40mm fan.

#### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear 

The back covers the rest of the power supply and mounts a fused IEC power plug.

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar

This is a crossbar that joins and covers the joint between the lids and front display.

#### STLs

| Part                       | Printed Qty | Link     |
|----------------------------|-------------|----------|
| `Base - Front.stl`         | 1           | [STL][41] |
| `Base - Rear.stl`          | 1           | [STL][42] |
| `Main Body - Crossbar.stl` | 1           | [STL][43] |

### Core Parts with Variants

Your power supply unit (PSU) will mount underneath the main body. The [`Core`][14] folder has one subfolder for each supported PSU.

Currently the two supported PSUs are:

- Mean Well LRS-350
- Mean Well RSP-500 **(Preliminary)**

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front

The front main body comes in two variations to choose from.

The version with a 60mm external fan additional requires the appropriate [:material-alpha-f-box: :material-alpha-c-box-outline: fan cage][6]. Optionally, a TPU gasket can also be used with the fan cage.

| 40mm Optional Fan | 60mm External Fan |
|-------------------|-------------------|
| ![front with 40mm fan mount][34] | ![front with 60mm fan cutout][35]

| Variation                                | Printed Qty | LRS-350 Link | RSP-500 Link |
|------------------------------------------|-------------|--------------|--------------|
| `Main Body - Front with 40mm Intake.stl` | 1           | [STL][7]     | [STL][9]     |
| `Main Body - Front with 60mm Intake.stl` | 1           | [STL][8]     | [STL][10]    |

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear

The rear main body also comes in two variations. For the dual 40mm fan version, you will also need to print [40mm :material-alpha-f-box: :material-alpha-c-box-outline: fan cages][6] and (optionally) TPU gaskets.

| Dual 40mm Fans  | No Fan Mounts |
|-----------------|---------------|
| ![rear with 40mm fan cuouts][36] | ![rear body without fan cutouts][37]

| Variation                                | Printed Qty | LRS-350 Link | RSP-500 Link |
|------------------------------------------|-------------|--------------|--------------|
| `Main Body - Rear No Fans.stl`           | 1            | [STL][11]   | [STL][15]   | 
| `Main Body - Rear with 40mm Exhausts.stl`| 1            | [STL][12]   | [STL][16]   |

## :material-alpha-t-box: Trays

Trays are used for mounting parts internally. They come in three types:

[![the three types of trays][2]][2]

1. :material-alpha-t-box: :material-alpha-m-box-outline: MCU tray
2. :material-alpha-t-box: :material-alpha-l-box-outline: Lower bay tray
3. :material-alpha-t-box: :material-alpha-c-box-outline: CPU tray

Tray templates are available in both `STEP` and Fusion 360 format to add support for new products.

### :material-alpha-t-box: :material-alpha-m-box-outline: MCU tray

MCU trays mount a microcontroller unit--your 3D printer board.

[List of supported MCUs][24]

### :material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay

The lower bay is a configurable area to mount parts like buck converters and MOSFETs.

[List of supported lower bay parts][25]

### :material-alpha-t-box: :material-alpha-c-box-outline: CPU Tray

The CPU tray is an optional mount for a Raspberry Pi. There is a blank cover if you do not use a Raspberry Pi or other SoC CPU.

[List of supported CPUs][23]

## :material-alpha-p-box: Panels

[![callout of each panel type][3]][3]

1. :material-alpha-p-box: :material-alpha-f-box-outline: Front panel
2. :material-alpha-p-box: :material-alpha-d-box-outline: Display panel
3. :material-alpha-p-box: :material-alpha-l-box-outline: Lid
4. :material-alpha-p-box: :material-alpha-r-box-outline: Rear panel (not visible)
5. :material-alpha-f-box: :material-alpha-c-box-outline: Fan cage (see [next section](#fans))

| Panels        | Qty | Folder Link | Notes |
|---------------|-----|-------------|-------|
| Rear Panel    | 1   | [Link][29]  | See [directions](#rear-panel) below. |

Panels have a range of supported parts and options. There is a blank `STEP` and Fusion 360 template for each panel category. Additionally, all panel variations have `STEP` source files. Fusion 360 files are also usually available.

As with trays, links in this section are to folders rather than individual `.STL` files.

### :material-alpha-p-box: :material-alpha-f-box-outline: Front Panel

The front panel serves as an air vent and location to put a MicroSD card reader extension. USB extensions are also a common accessory.

- Files: [`Panels/Front Panel`][27]
- [Supported parts][44]

### :material-alpha-p-box: :material-alpha-d-box-outline: Display Panel

This area mounts LCD displays, from the basic 128x64 character display to Raspbery Pi TFTs.

- Files: [`Panels/Display`][26]
- [Supported parts][45]

### :material-alpha-p-box: :material-alpha-l-box-outline: Lid(s)

The lid is both a way into your case and a configurable panel. There are two types of lids: full-length and half-length lids. You can either print one (1) full-length lid or two (2) half-length lids.

- Files: [`Panels/Lids`][28]
- (A full list of supported parts is not yet available)

### :material-alpha-p-box: :material-alpha-r-box-outline: Rear Panel

The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is also available for customization.

Rear panels with panel mounted connectors are an active area of work.

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| [`Generic`][30]  | These have large holes for passing wires through and come in a number of common variations. | ...You want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [`Custom`][31]   | Designed for users of common printer configurations. | ...Your printer has a configuration available. |
| [`Micro Fit 3`][32]    | Use Molex Micro Fit 3 panel mounted connectors. Pinout diagrams for each panel are included. | ...You plan to create a wiring harness for an enclosed printer. |
| [`Template`][33] | A Fusion 360 template with profiles for panel mounted connectors and fans. | ...You want to create your own panel. |

## :material-alpha-f-box: Fans

![render of a case with two 40mm fans and a 60mm fan mounted externally][38]

Externally mounted fans use :material-alpha-f-box: :material-alpha-c-box-outline: [fan cages][13] to cover the fan blades. There are a large number of fan sizes supported, each with a matching TPU :material-alpha-f-box: :material-alpha-g-box-outline: fan gasket. The gaskets are optional and serve to reduce noise.

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
[13]: support/fans.md
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
[32]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Micro%20Fit%203
[33]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Template
[34]: img/examples/front_40mm.png
[35]: img/examples/front_60mm.png
[36]: img/examples/rear_40mm.png
[37]: img/examples/rear_no_fans.png
[38]: img/examples//rear_fans.png
[41]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front.stl
[42]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear.stl
[43]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Crossbar.stl
[44]: http://127.0.0.1:8000/OmniBox/support/panel_mounts/
[45]: support/displays.md