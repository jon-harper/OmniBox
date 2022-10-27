---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 2022-08-04
---

This is a visual tour of an OmniBox. This page demonstrates:

1. The core parts of OmniBox and their variations;
2. Trays and panels; and
3. How these pieces fit together.

Links are provided to the respective git folder for each component type.

## Identifying Components

To help quickly identify a component, we use icons next to component names. The first letter is a filled-in box for what category a part is from:

- :material-alpha-c-box: Core
- :material-alpha-t-box: Tray
- :material-alpha-p-box: Panel
- :material-alpha-f-box: Fan

The following letters identify the name of the component, usually one or two letters. Examples: 

- :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front (a Core component)
- :material-alpha-p-box: :material-alpha-l-box-outline: Lid (a type of Panel)

## Overview

<figure markdown>
  [![overview of an omnibox][21]][21]
  <figcaption>A generic, finished OmniBox.</figcaption>
</figure>

The configuration in the image above will be our example in this guide. We will start with the Core components and move on to the trays and panels that make OmniBox so modular. 

## :material-alpha-c-box: Core Components

Core components form the basis of every case. Core files be found in the [`Core`][git_core] folder in the GitHub repository.

There are two types of Core components, Base and Main Body. A typical OmniBox build has three parts for the main body and two for the base.

!!! important
    Most Core components come with the option of using heat set inserts. These `STL` files have `HSI` in the name.

<figure markdown>
  [![the core of an OmniBox][1]][1]
  <figcaption>The core components of an OmniBox with fans and power supply mounted.</figcaption>
</figure>

- :material-alpha-c-box: :material-alpha-b-box-outline: Base
    - :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front
    - :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear
    - :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-u-box-outline: Base - Unified (replaces the above two)
- :material-alpha-c-box: :material-alpha-m-box-outline: Main Body
    - :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar
    - :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front    
    - :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear
### Base

#### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front

[![front base][31]{ width="480" }][31]
[![front base][32]{ width="480" }][32]

This is the front of two base pieces that cover the power supply. There is a 30mm x 11mm rocker switch cutout in front, as well as air vents and optional 40mm fan mounts.

#### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear 

[![front base][33]{ width="480" }][33]
[![front base][34]{ width="480" }][34]

The back covers the rest of the power supply and mounts a fused IEC power plug.

This component is available with heat set inserts.

#### :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-u-box-outline: Base - Unified

For owners of large-format printers, the base can be printed as a single piece instead of two. The unified base replaces the rear and front pieces.

This component is available with heat set inserts.

### Main Body

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar

[![crossbar][25]{ width="480" }][25]
[![crossbar][26]{ width="480" }][26]

This is a crossbar that joins and covers the joint between the lids and front display. There are no variations to the crossbar.

- [GitHub Folder][git_main_body_crossbar]

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front

[![front main body][27]{ width="480" }][27]
[![front main body][28]{ width="480" }][28]

The front main body comes in two variations to choose from.

The version with a 60mm external fan additional requires the appropriate [:material-alpha-f-box: :material-alpha-c-box-outline: fan cage][6]. Optionally, a TPU gasket can also be used with the fan cage.

#### :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear

[![rear main body][29]{ width="480" }][29]
[![rear main body][30]{ width="480" }][30]

The rear main body also comes in two variations. For the dual 40mm fan version, you will also need to print [40mm :material-alpha-f-box: :material-alpha-c-box-outline: fan cages][6] and (optionally) TPU gaskets.

## :material-alpha-t-box: Trays and Power Supply

Trays are used for mounting parts internally. There are four (4) types of trays:

<figure markdown>
  [![the three types of trays][2]{ width="640" }][2]
  <figcaption>The four types of trays in red.</figcaption>
</figure>

- :material-alpha-t-box: :material-alpha-p-box-outline: Power supply mount
- :material-alpha-t-box: :material-alpha-m-box-outline: MCU tray
- :material-alpha-t-box: :material-alpha-l-box-outline: Lower bay tray
- :material-alpha-t-box: :material-alpha-c-box-outline: CPU tray

Tray templates are available in both `STEP` and Fusion 360 format to add support for new products.

### :material-alpha-t-box: :material-alpha-p-box-outline: Power Supply Mount

[![power supply mount][57]{ width="480" }][57]
[![power supply mount][58]{ width="480" }][58]

Power supply mounts slide up from underneath the case. Currently two power supplies are supported; a template is availabe to add support for more.

- [GitHub Folder][git_psu]
- Supported power supplies:
    - Mean Well LRS-350 series
    - Mean Well RSP-500 series

### :material-alpha-t-box: :material-alpha-m-box-outline: MCU Tray

[![mcu tray][37]{ width="480" }][37]
[![mcu tray][38]{ width="480" }][38]

MCU trays mount a microcontroller unit--your 3D printer board.

- [GitHub Folder][git_mcu]
- [List of supported MCUs][9]

### :material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays

[![lower bay tray][41]{ width="480" }][41]
[![lower bay tray][42]{ width="480" }][42]

The lower bay is a configurable area to mount parts like buck converters and MOSFETs. There are four dedicated lower bay trays locations and two more that can occupy an unused CPU tray bay.

- [GitHub Folder][git_lower_bay]
- [List of supported lower bay parts][10]

### :material-alpha-t-box: :material-alpha-c-box-outline: CPU Tray

[![cpu tray][39]{ width="480" }][39]
[![cpu tray][40]{ width="480" }][40]

The CPU tray is an optional mount for a Raspberry Pi or other SoC. There are two CPU trays; one is on each side of the case. An unused tray is replaced by a [Side Panel](#side-panels).

- [GitHub Folder][git_cpu]
- [List of supported CPUs][11]

## :material-alpha-p-box: Panels

<figure markdown>
  [![callout of panels and fan cage][3]{ width="640" }][3]
  <figcaption>The six types of panels.</figcaption>
</figure>

- :material-alpha-p-box: :material-alpha-f-box-outline: Front panel
- :material-alpha-p-box: :material-alpha-d-box-outline: Display panel
- :material-alpha-p-box: :material-alpha-l-box-outline: Lid
- :material-alpha-p-box: :material-alpha-r-box-outline: Rear panel
- :material-alpha-p-box: :material-alpha-s-box-outline: Side panel
- :material-alpha-p-box: :material-alpha-b-box-outline: Bottom panel

Panels cover the outside of OmniBox and mount of a range of options. Front, side, and rear panels are typically used for connectors and fans.

Panels have a range of supported parts and options. There is a blank `STEP` and Fusion 360 template for each panel category to create new panels.

### :material-alpha-p-box: :material-alpha-f-box-outline: Front Panel

[![front panel][43]{ width="480" }][43]
[![front panel][44]{ width="480" }][44]

The front panel serves as an air vent and location to put a MicroSD card reader extension. USB extensions are also a common accessory.

- GitHub Folder: [`Panels/Front Panel`][git_front_panel]
- [Supported parts][7]

### :material-alpha-p-box: :material-alpha-s-box-outline: Side Panel

[![side panel][49]{ width="480" }][49]
[![side panel][50]{ width="480" }][50]

Side panel(s) replace a CPU tray and often mount connectors or fans. A blank side panel can also be used.

- GitHub Folder: [`Panels/Side Panel`][git_side_panel]

### :material-alpha-p-box: :material-alpha-b-box-outline: Bottom Panel

[![bottom panel][53]{ width="480" }][53]
[![bottom panel][54]{ width="480" }][54]

The bottom panels act as a cover for the underside of the case. A fully enclosed option is available to keep dust out.

- GitHub Folder: [`Panels/Bottom Panel`][git_bottom_panel]

### :material-alpha-p-box: :material-alpha-d-box-outline: Display Panel

[![display panel][45]{ width="480" }][45]
[![display panel][46]{ width="480" }][46]


This area mounts LCD displays, from the basic 128x64 character display to Raspbery Pi TFTs.

- GitHub Folder: [`Panels/Display`][git_display]
- [List of supported displays][8]

### :material-alpha-p-box: :material-alpha-l-box-outline: Lid(s)

[![lid][47]{ width="480" }][47]
[![lid][48]{ width="480" }][48]

The lid is both a way into your case and a configurable panel. There are two types of lids: short and long lids. You can either print one (1) long lid or two (2) short lids.

- GitHub Folder: [`Panels/Lids`][git_lid]
- See the README in the link above for a list of supported configurations.

### :material-alpha-p-box: :material-alpha-r-box-outline: Rear Panel

[![rear panel][51]{ width="480" }][51]
[![rear panel][52]{ width="480" }][52]

The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is also available for customization.

Rear panels with panel mounted connectors are an active area of work.

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| [`Generic`][git_generic_rear]  | These have large holes for passing wires through and come in a number of common variations. | ...You want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [`Custom`][git_custom_rear]   | Designed for users of common printer configurations. | ...Your printer has a configuration available. |
| [`Micro Fit 3`][git_molex_rear]    | Use Molex Micro Fit 3 panel mounted connectors. Pinout diagrams for each panel are included. | ...You plan to create a wiring harness for an enclosed printer. |
| [`Template`][git_rear_template] | A Fusion 360 template with profiles for panel mounted connectors and fans. | ...You want to create your own panel. |

## :material-alpha-f-box: Fans

[![external fan cages][55]{ width="480" }][55]
[![external fan cages][56]{ width="480" }][56]

Externally mounted fans use [:material-alpha-f-box: :material-alpha-c-box-outline: fan cages][6] to cover the fan blades. There are a large number of fan sizes supported, each with a matching TPU :material-alpha-f-box: :material-alpha-g-box-outline: fan gasket. The gaskets are optional and serve to reduce noise.

- GitHub Folder: [`Fans`][git_fans]
- [Supported Fans][6]

[1]:  img/components/core.png
[2]:  img/components/trays.png
[3]:  img/components/panels.png
[4]:  printing.md#core-parts-with-variants
[5]:  support/boards.md
[6]:  support/fans.md
[7]:  support/panel_mounts.md
[8]:  support/displays.md
[9]:  support/boards.md#mcu-boards
[10]: support/lower_bay.md
[11]: support/boards.md#soc-cpu-boards

[21]: img/components/overview.png
[22]: img/components/core.png
[23]: img/components/trays.png
[24]: img/components/panels.png
[25]: img/components/crossbar.png#only-light
[26]: img/components/crossbar_dark.png#only-dark
[27]: img/components/main_front.png#only-light
[28]: img/components/main_front_dark.png#only-dark
[29]: img/components/main_rear.png#only-light
[30]: img/components/main_rear_dark.png#only-dark
[31]: img/components/base_front.png#only-light
[32]: img/components/base_front_dark.png#only-dark
[33]: img/components/base_rear.png#only-light
[34]: img/components/base_rear_dark.png#only-dark
[35]: img/components/base_unified.png#only-light
[36]: img/components/base_unified_dark.png#only-dark
[37]: img/components/mcu.png#only-light
[38]: img/components/mcu_dark.png#only-dark
[39]: img/components/cpu.png#only-light
[40]: img/components/cpu_dark.png#only-dark
[41]: img/components/lower_bay.png#only-light
[42]: img/components/lower_bay_dark.png#only-dark
[43]: img/components/front_panel.png#only-light
[44]: img/components/front_panel_dark.png#only-dark
[45]: img/components/display.png#only-light
[46]: img/components/display_dark.png#only-dark
[47]: img/components/lid.png#only-light
[48]: img/components/lid_dark.png#only-dark
[49]: img/components/side.png#only-light
[50]: img/components/side_dark.png#only-dark
[51]: img/components/rear.png#only-light
[52]: img/components/rear_dark.png#only-dark
[53]: img/components/bottom.png#only-light
[54]: img/components/bottom_dark.png#only-dark
[55]: img/components/external_fan.png#only-light
[56]: img/components/external_fan_dark.png#only-dark
[57]: img/components/psu.png#only-light
[58]: img/components/psu_dark.png#only-dark