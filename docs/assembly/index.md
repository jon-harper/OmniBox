---
title: Getting Started
summary: Guide to assembling the OmniBox.
authors: Jon Harper
date: 2022-10-26
---

Welcome to the Assembly Guide for OmniBox. This introduction page covers what to expect during
assembly.

!!! note "Version Note"
    Instructions in this guide are for **Release v0.9.11**. Details may differ from older or newer versions of OmniBox.

## Format

Sections of the assembly guide have four parts:

- A short (5-15 second) video overview,
- A materials list,
- Step-by-step illustrated instructions, and
- A final reference image.

## Time

### Heat Set Inserts

Time required to install inserts, if applicable, varies by the total number used. As inserts are installed,
individuals typically become more comfortable and installation time *per insert* goes down. Allow at least
forty-five (45) minutes for installation, even for experienced users.

### Case Assembly

Most of the case can be assembled in approximately two (2) hours. This estimate assumes that the case is
assembled in one sitting and that all printed parts and hardware are ready.

This estimate does **not** include wiring or power on testing.

## Contents

The Assembly Guide is divided into four major sections:

1. Heat Set Insert installation: if applicable.
2. Core & PSU: Building the basic case.
3. CPU & Lower Bay Trays: Filling out the lower bay.
4. MCU & Panels: Installing the MCU and closing up.

## Configurations

This Assembly Guide covers how to install every *type* of tray and panel, but cannot cover all possible configurations. 
The guide covers all aspects common to a build, such as installing internal and external fans, and most common
build scenarios. Both stock and HSI fasteners are listed throughout assembly.

### Materials Lists

There are seperate materials lists for HSI and Stock configurations. Many panels have "Blank" materials lists that
contain only the fasteners needed to mount a blank panel. 

The Front Panel materials list is a good example:

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 8mm SHCS             | 2   |                                 |
    | :material-printer-3d-nozzle: `Front Panel - MicroSD, Slats.stl`   | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Body.stl`  | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Cap.stl`   | 1 |  |
=== "As Illustrated (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4   |                                 |
    | M3 x 10mm SHCS            | 2   | May substitute 12mm or longer.  |
    | :material-printer-3d-nozzle: `Front Panel - MicroSD, Slats.stl`   | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Body.stl`  | 1 |  |
    | :material-printer-3d-nozzle: `MicroSD Extension Holder Cap.stl`   | 1 |  |
=== "Blank Panel (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS             | 2   |     |
    | :material-printer-3d-nozzle: `Front Panel - Blank.stl` | 1 |  |
=== "Blank Panel (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 10mm SHCS            | 2   | May substitute 12mm.            |
    | :material-printer-3d-nozzle: `Front Panel - Blank.stl` | 1 |  |

<figure markdown>
## :material-directions: Ready?
</figure>

Go to the [next page][hsi_tips] for heat set inserts builds, or jump ahead to [building the base][base]
otherwise.

[hsi_tips]: hsi_tips.md     "Assembly: HSI Introduction & Tips"
[base]:     base.md         "Assembly: Base and PSU"
[core]:     core.md         "Assembly: Main Body"
[mcu]:      mcu.md          "Assembly: MCU Tray"
[cpu]:      cpu.md          "Assembly: CPU Tray"
[lower_bay]:lower_bay.md    "Assembly: Lower Bay Tray(s)"
[front]:    front.md        "Assembly: Front Panel"
[side]:     side.md         "Assembly: Side Panel(s)"
[rear]:     rear.md         "Assembly: Rear Panel"
[lid]:      lid.md          "Assembly: Lid(s)"
[bottom]:   bottom.md       "Assembly: Bottom Panels"
[checklist]: ../printing.md#printed-component-checklist "Printed Component Checklist"
[parts]: ../support/index.md "Supported Parts List"