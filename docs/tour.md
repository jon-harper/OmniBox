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

| Part                  | Printed Qty | STL      |
|-----------------------|-------------|----------|
| Base - Front          | 1           | [STL][1] |
| Base - Rear           | 1           | [STL][2] |
| Main Body - Crossbar  | 1           | [STL][3] |

#### Base - Front

This is part of a pair that covers the power supply. There is a 30mm x 11mm rocker switch cutout in front, as well as air vents and an optional 40mm fan.

#### Base - Rear 

The back covers the rest of the power supply and mounts a fused IEC power plug.

#### Main Body - Crossbar

This is a simple crossbar that covers the joint between the lids and front display.

### Core Parts with Variants

Your power supply (PSU) will mount underneath the main body. The [`Core`][14] folder has one subfolder for each supported PSU.

#### Main Body - Front

The front main body comes in two variations to choose from. Print only one (1) version.

If you print the version with a 60mm intake fan, you will need to print the appropriate [fan cage][6] and (optionally) a TPU gasket.

| Variation                                | LRS-350 STL | RSP-500 STL | Description |
|------------------------------------------|-------------|-------------|-------------|
| `Main Body - Front with 40mm Intake.stl` | [STL][]    | [STL][]    | The default version of the case with intake vents and a concealed 40mm fan. |
| `Main Body - Front with 60mm Intake.stl` | [STL][]    | [STL][]    | Mounts an external 60mm intake fan. |

#### Main Body - Rear

### Main Body

The front and rear main body each have variations in the number and type of fans mounted. These parts also mount your power supply (PSU).


Pictured is the default configuration with a 40mm front intake and two 40mm rear exhausts. More about this is discussed in the [printing guide][4].

## Trays

[![the three types of trays][2]][2]

1. MCU tray
2. Full length lower bay tray
3. CPU tray

### MCU Tray

MCU trays mount a microcontroller unit--your 3D printer board.

### Lower Bay

The lower bay is a configurable area to mount parts like buck converters and MOSFETs.

### CPU Tray

The CPU tray is an optional mount for a Raspberry Pi. There is a plain cover if you do not use a Raspberry Pi or other SoC CPU.

## Panels and Fan Cages

[![panels and fan cages][3]][3]

1. Front panel
2. Display panel
3. Lid
4. Rear panel (not visible)
5. Fan cage

### Front Panel

The front panel serves as an air vent and location to put an SD card reader extension. USB panel mount extensions are also a common accessory.

### Display Panel

This area mounts numberous types of displays, from the basic 128x64 display to Raspbery Pi TFTs.

### Lid

The lid is both a way into your case and a configurable panel. There are half-length lids available, as well.

Examples:

1. A full-length lid with a handle;
2. A half-length lid in front with a handle and a half-length lid in back with a fan.

### Rear Panel

The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is also available for customization.

Rear panels with panel mounted connectors are an active area of work.

### Fan Cage

Externally mounted fans use cages cages to cover the fan blades. There are a large number of fan sizes supported.

[1]: img/printed_parts/core.png
[2]: img/printed_parts/trays.png
[3]: img/printed_parts/panels.png
[4]: printing.md#core-parts-with-variants
[5]: support/boards.md
[6]: https://github.com/jon-harper/OmniBox/tree/main/Fan%20Cages
[14]: https://github.com/jon-harper/OmniBox/tree/main/Core/
