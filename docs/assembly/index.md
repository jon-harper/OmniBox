---
title: Getting Started
summary: Guide to assembling the OmniBox.
authors: Jon Harper
date: 2022-10-26
---

## Welcome

Welcome to the Assembly Guide for OmniBox. This page covers:

- An overview of what to expect;
- Accounting for differences in configuration from this guide; and
- Best practices during assembly.

!!! important "Version Note"
    Instructions in this Guide are for **Release 0.9.9**. Details may differ for older or newer versions of OmniBox.

## Table of Contents

The OmniBox Assembly Guide is divided into four main sections:

### 1. Heat Set Inserts (HSI)

This section introduces HSIs, using them, and installing them in the case. Skip this section if you did not print an HSI case.

### 2. Core & PSU

Assembly starts by building the Base around the PSU tray. This acts as a first layer of the case that we will build upwards from.

### 3. CPU & Lower Bay Trays

The second layer of the case adds the SoC CPU and lower bay components. By the end of this section, the "floor" of the case and front panel will be installed.

### 4. MCU & Panels

At this point, assembly centers around the MCU, wiring, and closing up the case.

### Format

Each section of assembly guide has four parts:

- A short (5-15 second) video overview of the section;
- A materials list;
- Step-by-step instructions; and
- A final reference image.

Most graphics can be enlarged to see detail.

### Time

Most of the case can be assembled in approximately two (2) hours.

This estimate assumes that you:

- Have printed all [necessary parts][checklist]; and
- Have never assembled an OmniBox.

This estimate does *not* include:

- Heat set insert (HSI) installation, if applicable;
- Time needed for wiring; and
- Power up & testing.

### Configurations

These instructions are for a generic OmniBox configuration with at least one of every type of tray, panel, or fan mounting. Details may differ from your build, but the common aspects of assembly are covered. For example, the size, location, and number of fans in your configuration may vary, but the methods of mounting both internal and external fans are covered.

Areas where the Core variants may differ from instructions are specifically called out.

## Techniques

Assembly relies on a few general techniques reused throughout this guide.

### Fastening Screws

Screws thread directly into the walls of the printed plastic (where heat set inserts are not used).

For example, lower bay trays attach to the main body with M3 screws. The trays have holes larger than the diameter of the screw, but the holes in the standoff are smaller. The screw "bites" the plastic of the standoff and the screw head to clamps down on the tray.

!!! note
    Parts of the case that are frequently removed have deeper-than-necessary screw holes. You can use replace your screws with longer ones to get "fresh" plastic for the threads as the walls wear down.

    For example, over time you may need to switch from 8mm to 10mm screws. This is most common with the lid, as it is removed most often.

### Example Illustrations

Illustrations for assembly are provided from isometric (angled and over-or-under) perspectives. The relevant parts for the current step are highlighted in each illustration.

### Materials Lists

Tabbed lists are used in this guide for materials lists in most sections. This separates materials used in the example from a generic list common to every build. It is also used where materials required are different for stock and HSI cases.

Printed parts are always notated.

For example, from the display panel section:

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 8mm machine screws   | 4   | May substitute 10mm or 12mm.    |
    | Generic 12864 LCD         | 1   | Comes with many Creality printers. |
    | [:material-git: `Display Panel - Generic 12864.stl`][git_generic_12864] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: Display Knob][git_display_knob] | 1 | :material-printer-3d-nozzle: Printed, Optional |


=== "Stock"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 10mm machine screws  | 4   | May also use 12mm.              |
    | Compatible LCD display    | 1   |                                 |
    | Display Panel             | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: Display Knob][git_display_knob] | 1 | :material-printer-3d-nozzle: Printed, Optional |

=== "HSI"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 4   |                                 |
    | Compatible LCD display    | 1   |                                 |
    | Display Panel             | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: Display Knob][git_display_knob] | 1 | :material-printer-3d-nozzle: Printed, Optional |

<div align="center" markdown>
## :material-directions: Ready?

Go to the [next page][hsi_base] if you printed a case with heat set inserts, or jump to [building the base][base] otherwise.
</div>
    
[hsi_base]: hsi_base.md     "Assembly: Rear Base Heat Set Inserts"
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