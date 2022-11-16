---
title: Getting Started
summary: Guide to assembling the OmniBox.
authors: Jon Harper
date: 2022-10-26
---

## Overview

Welcome to the Assembly Guide for OmniBox. This page covers:

- An overview of what to expect;
- Accounting for differences in configuration from this guide; and
- Best practices during assembly.

!!! important "Version Note"
    Instructions in this Guide are for **Release 0.9.9**. Details may differ for older or newer versions of OmniBox.

### Table of Contents

The OmniBox Assembly Guide is divided into four main sections:

#### 1. Heat Set Inserts (HSI)

This section introduces HSIs, using them, and installing them in the case.

Skip this section if you did not print an HSI case.

Experienced users following this guide should be able to install all inserts in less than 30 minutes.

Gaining experience with inserts saves time and lowers the chances of printed part damage. If you are using inserts for the first time, it is recommended that you print at least one [practice block][git_hsi_practice] to gain a level of comfort.

#### 2. Core & PSU

Assembly starts in earnest by building the Base around the PSU and wiring it up. This acts as a first layer of the case that we will build upwards from.

The section finishes by installing the Main Body.

#### 3. CPU & Lower Bay Trays

The second layer of the case adds the SoC CPU and lower bay components. By the end of this section, the "floor" of the case and front panel will be installed.

#### 4. MCU & Panels

At this point, assembly centers around the MCU, wiring, and closing up the case.

### Format

Each section of the assembly has four parts:

- A short (3-15 second) optional video;
- A list of materials used and quantity;
- Step-by-step illustrated instructions; and
- A final reference image.

All graphics can be enlarged to see detail by clicking or tapping.

### Time

Most of the case can be assembled in approximately two (2) hours.

This estimate assumes that you:

- Have printed all [necessary parts][checklist]; and
- Have never assembled an OmniBox.

This estimate does *not* include:

- Heat set insert (HSI) installation, if applicable;
- Time needed for wiring; and
- Power up/initial tests.

### Configurations

These instructions are cover a generic OmniBox configuration. For example, the size, location, and number of fans in your configuration may vary, but the methods of mounting both internal and external fans are covered.

This guide cannot cover every mounting combination for trays and panels; however, the git repository has Bill of Material information for mounting components to their respective tray or panel.

Areas where the Core variants may differ from instructions are specifically called out.

## Techniques

Assembly relies on a few general techniques reused throughout this guide.

### Fastening Screws

Screws thread directly into the walls of the plastic where heat set inserts are not used.

For example, lower bay trays attach to the main body with M3 screws. The trays have holes larger than the diameter of the screw, but the holes in the standoff are smaller. The screw "bites" the plastic of the standoff and the screw head to clamps down on the tray.

!!! note
    Parts of the case that are frequently removed have deeper-than-necessary screw holes. You can use replace your screws with longer ones to get "fresh" plastic for the threads as the walls wear down.

    For example, over time you may need to switch from 8mm to 10mm screws. This is most common with the lid, as it is removed most often.

### Example Illustrations

Illustrations for assembly are provided from isometric (angled and over-or-under) perspectives. The relevant parts for the current step are highlighted in each illustration.

### Mounting Fans

The procedure for both internal and external fan mounting is covered in the guide. External fan cages and gaskets come in a number of sizes, but all sizes attach externally with the same type of cage.

Note that fans 60mm and smaller use M3 screws; larger fans require M4 screws.

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