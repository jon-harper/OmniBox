---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 20core-08-04
---

This is a visual tour of an OmniBox. This page demonstrates:

1. The core parts of OmniBox and their variations;
2. Trays and panels; and
3. How these pieces fit together.

Links are provided to the respective git folder for each component type.

!!! note

    Links to external sites are tagged with icons to identify purpose:

    - A link with the :material-git: Git icon points to the OmniBox GitHub. 
    - Sample links to shopping websites have a :material-cart: icon next to them.

## Overview

<figure markdown>
  [![overview of an omnibox][img_overview]][img_overview]{ width="640" }
  <figcaption>A finished OmniBox.</figcaption>
</figure>

The configuration in the image above will be our example in this guide. We will start with the Core components and move on to the trays and panels that make OmniBox so modular. 

## Core Components

Core components form the basis of every case. Core files be found in the [:material-git: `Core`][git_core] folder in the GitHub repository.

!!! important
    Most Core components come with the option of using heat set inserts. These `STL` files have `HSI` in the name.

<figure markdown>
  [![the core of an OmniBox][img_core]][img_core]
  <figcaption>The core components of an OmniBox with fans and power supply mounted.</figcaption>
</figure>

There are two types of Core components, Base and Main Body. A typical OmniBox build has three parts for the main body and two for the base.

- Base
    - Front
    - Rear
    - Unified (replaces the above two)
- Main Body
    - Crossbar
    - Front
    - Rear
### Base

#### Base - Front

[![front base][img_base_front]{ width="480" }][img_base_front]

This is the front of two base pieces that cover the power supply. There is a 30mm x 11mm rocker switch cutout in front, as well as air vents and optional 40mm fan mounts.

- [:material-git: GitHub Folder][git_base_front]

#### Base - Rear 

[![front base][img_base_rear]{ width="480" }][img_base_rear]

The back covers the rest of the power supply and mounts a fused IEC power plug.

- [:material-git: GitHub Folder][git_base_rear]
- This component is available with heat set inserts.
 Base - Unified

[![front base][img_base_unified]{ width="480" }][img_base_unified]

For owners of large-format printers, the base can be printed as a single piece instead of two. The unified base replaces the rear and front pieces.

- [:material-git: GitHub Folder][git_base_unified]
- This component is available with heat set inserts.

### Main Body

#### Main Body - Crossbar

[![callout of the crossbar][img_crossbar]{ width="480" }][img_crossbar]

This is a crossbar that joins and covers the joint between the lids and front display.

- [:material-git: GitHub Folder][git_main_body_crossbar]
- There are no variations to the crossbar.

#### Main Body - Front

[![front main body with internal fan][img_main_front]{ width="480" }][img_main_front]

The front main body comes in two variations to choose from:

=== "Internal 40mm Fan"

    [![front main body with internal fan][img_front_40]{ width="360" }][img_front_40]

=== "External 60mm Fan"

    [![front main body with external fan][img_front_60]{ width="360" }][img_front_60]

The version with a 60mm external fan additional requires the appropriate [fan cage][fans]. Optionally, a TPU gasket can also be used with the fan cage.

- [:material-git: GitHub Folder][git_main_body_front]
- This component is available with heat set inserts.

#### Main Body - Rear

The rear main body comes in two variations:

=== "Dual 40mm Fans"

    [![rear main body with dual fans][img_rear_dual]{ width="360" }][img_rear_dual]

=== "No Fan Mounts"

    [![rear main body without fan mounts][img_rear_none]{ width="360" }][img_rear_none]

For the dual 40mm fan version, you will also need to print [40mm fan cages][fans] and (optionally) TPU gaskets.

- [:material-git: GitHub Folder][git_main_body_rear]
- This component is available with heat set inserts.

## Trays

Trays are used for mounting parts internally. There are four (4) types of trays:

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays in red.</figcaption>
</figure>

- Power supply tray (PSU tray)
- MCU tray
- Lower bay tray
- CPU tray

Tray templates are available in both `STEP` and Fusion 360 format to add support for new products.

### PSU Tray

[![power supply tray][img_psu]{ width="480" }][img_psu]

Power supply (PSU) trays slide up from underneath the case. Currently two power supplies are supported; a template is availabe to add support for more.

Large (tall) power supplies require the use of a [base extension shim](#base-extensions).

- [:material-git: GitHub Folder][git_psu]
- Supported power supplies:
    - [Mean Well LRS-350 series][git_psu_lrs350]
    - [Mean Well RSP-500 series][git_psu_rsp500] (prelimary, requires base extensions)

### MCU Tray

[![mcu tray][img_mcu]{ width="480" }][img_mcu]

MCU trays mount a microcontroller unit--your 3D printer board.

- [:material-git: GitHub Folder][git_mcu]
- [List of supported MCUs][mcu]

### Lower Bay Trays

[![lower bay tray][img_lower_bay]{ width="480" }][img_lower_bay]

The lower bay is an area to mount parts like buck converters and MOSFETs. There are four dedicated lower bay trays locations and two more that can occupy an unused CPU tray bay.

There are  of these trays: Short and Long. A Long length tray covers the mount points of two Short trays and must be mounted from front to back of the case.

- [:material-git: GitHub Folder][git_lower_bay]
- [List of supported lower bay parts][lower_bay]

### CPU Tray

[![cpu tray][img_cpu]{ width="480" }][img_cpu]

The CPU tray is an optional mount for a Raspberry Pi or other SoC. There are two bays for CPU trays; one is on each side of the case.

An unused bay is replaced by a [Side Panel](#side-panels). A short lower bay tray can also be installed in an unused CPU bay.

- [:material-git: GitHub Folder][git_cpu]
- [List of supported CPUs][cpu]

## Panels

<figure markdown>
  [![callout of panels and fan cage][img_panels]{ width="640" }][img_panels]
  <figcaption>The six types of panels.</figcaption>
</figure>

- Front panel
- Display panel
- Lid
- Rear panel
- Side panel
- Bottom panel

Panels cover the outside of OmniBox and mount of a range of options. Front, side, and rear panels are typically used for connectors, fans, and ventilation.

There is a blank `STEP` and Fusion 360 template for each panel category to allow users to create new panels.

### Front Panel

[![front panel][img_front_panel]{ width="480" }][img_front_panel]

The front panel serves as an air vent and location to put a MicroSD card reader extension. USB extensions are also a common accessory.

- [:material-git: GitHub Folder][git_front_panel]
- [Supported parts][panel_mounts]

### Side Panel

[![side panel][img_side]{ width="480" }][img_side]

Side panel(s) replace a CPU tray and often mount connectors or fans. A blank side panel can also be used.

- [:material-git: GitHub Folder][git_side_panel]
- [Supported parts][panel_mounts]

### Bottom Panel

[![bottom panel][img_bottom]{ width="480" }][img_bottom]

The bottom panels act as a cover for the underside of the case. A fully enclosed option is available to keep dust out.

- [:material-git: GitHub Folder][git_bottom_panel]

### Display Panel

[![display panel][img_display]{ width="480" }][img_display]


This area mounts LCD displays, from the basic 128x64 character display to Raspbery Pi TFTs.

- [:material-git: GitHub Folder][git_display]
- [List of supported displays][displays]

### Lid(s)

[![img_lid][img_lid]{ width="480" }][img_lid]

The lid is both a way into your case and a configurable panel. There are two types of lids: short and long lids. You can either print one (1) long lid or two (2) short lids.

- [:material-git: GitHub Folder][git_lid]
- See the README in the GitHub folder for a list of supported configurations.

### Rear Panel

[![rear panel][img_rear]{ width="480" }][img_rear]

The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is also available for customization.

Rear panels with panel mounted connectors are an active area of work.

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| [:material-git: `Generic`][git_generic_rear]  | These have large holes for passing wires through and come in a number of common variations. | ...You want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [:material-git: `Custom`][git_custom_rear]   | Designed for users of common printer configurations. | ...Your printer has a configuration available. |
| [:material-git: `Micro Fit 3`][git_molex_rear]    | Use Molex Micro Fit 3 panel mounted connectors. Pinout diagrams for each panel are included. | ...You plan to create a wiring harness for an enclosed printer. |
| [:material-git: `Template`][git_rear_template] | A Fusion 360 template with profiles for panel mounted connectors and fans. | ...You want to create your own panel. |

## Other Components

### Fans

[![external fan cages][img_external_fan]{ width="480" }][img_external_fan]

Externally mounted fans use fan cages to cover the fan blades. There are a large number of fan sizes supported, each with a matching TPU fan gasket. The gaskets are optional and serve to reduce noise.

Internally mounted fans are also available, but are limited to 40mm fans.

- [:material-git: GitHub Folder][git_fans]
- List of [supported fans][fans]

### Base Extensions

[![base extension is highlighted in blue][img_base_extension]{width="480"}][img_base_extension]
    
Larger power supplies require the addition of a base extension shim. This mounts between the base and the bottom panel.

- [:material-git: GitHub Folder][git_base_extension]

### Power Switch

[![rocker switch is highlighted in blue][img_switch]{width="480"}][img_switch]

OmniBox uses a common 30x11mm [:material-cart: snap-in SPST rocker switch][bom_switch] to turn on and off. This is the same switch found on many 3D printers, particularly Creality.

### IEC C14 Power Socket

[![iec socket is highlighted in blue][img_iec]{width="480"}][img_iec]

Power is provided through a standard [:material-cart: fused IEC C14 power socket][bom_iec].

[fans]:  support/fans.md
[panel_mounts]:  support/panel_mounts.md
[displays]:  support/displays.md
[mcu]:  support/mcu.md
[lower_bay]: support/lower_bay.md
[cpu]: support/cpu.md
[img_overview]: img/components/overview.png
[img_core]: img/components/core.png
[img_trays]: img/components/trays.png
[img_panels]: img/components/panels.png
[img_crossbar]: img/components/crossbar.png
[img_main_front]: img/components/main_front.png
[img_main_rear]: img/components/main_rear.png
[img_base_front]: img/components/base_front.png
[img_base_rear]: img/components/base_rear.png
[img_base_unified]: img/components/base_unified.png
[img_base_extension]: img/components/base_extension.png
[img_mcu]: img/components/mcu.png
[img_cpu]: img/components/cpu.png
[img_lower_bay]: img/components/lower_bay.png
[img_front_panel]: img/components/front_panel.png
[img_display]: img/components/display.png
[img_lid]: img/components/lid.png
[img_side]: img/components/side.png
[img_rear]: img/components/rear.png
[img_bottom]: img/components/bottom.png
[img_external_fan]: img/components/external_fan.png
[img_psu]: img/components/psu.png
[img_front_40]: img/components/front_40mm.png
[img_front_60]: img/components/front_60mm.png
[img_rear_none]: img/components/rear_none.png
[img_rear_dual]: img/components/rear_40mm.png
[img_switch]: img/components/switch.png
[img_iec]: img/components/iec.png