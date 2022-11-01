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

### Table of Contents

This guide is divided into three main sections:

#### Part 1: :material-alpha-c-box: Core & :material-alpha-t-box: :material-alpha-p-box-outline: PSU

1. :material-alpha-t-box: :material-alpha-p-box-outline: PSU Tray & :material-alpha-c-box: :material-alpha-b-box-outline: Base
2. AC Wiring
3. :material-alpha-c-box: :material-alpha-m-box-outline: Main Body

#### Part 2: :material-alpha-t-box: Trays & Internal Wiring

1. [:material-alpha-t-box: :material-alpha-c-box-outline: CPU Tray][cpu]
2. [:material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay][lower_bay]
3. [:material-alpha-t-box: :material-alpha-m-box-outline: MCU][mcu]
4. Initial Power-up Test

#### Part 3: :material-alpha-p-box: Panels & Closing Up 

1. :material-alpha-p-box: :material-alpha-f-box-outline: Front Panel & :material-alpha-p-box: :material-alpha-f-box-outline: Side Panel(s)
2. Rear Panel & Display
3. Complete Wiring
4. Bottom Panels and Lid(s)

Instructions are for the 0.9.9 release. If you have an older or newer version, some details may differ.

### Format

Each section of the assembly has four parts:

- A short (3-10 second) optional video showing the combined assembly steps of that section. These videos are meant to give an overview of the following steps.
- A list of materials used and quantity
- Step-by-step illustrated instructions
- A final reference image

All graphics can be enlarged to see detail by clicking or tapping.

### Time

Assembly takes approximately two (2) hours.

This estimate assumes that you:

- Have printed all [necessary parts][checklist]; and
- Have never assembled an OmniBox.

This estimate does *not* include:

- Time needed to run and attach wiring;
- Power up and configuration tests; and
- Time needed for heat set insert (HSI) installation, if necessary.

!!! note "Heat Set Inserts"
    There are 24 inserts. Experienced users following this guide should be able to install all inserts in less than 30 minutes.
    
    Experience in installing inserts saves time during installation and lowers the chances of destroying a printed part. If you plan to use inserts and have not practiced, it is recommended that you print at least one (TODO PRACTICE BLOCK) for practice.

### Configurations

These instructions are cover a generic OmniBox configuration. For example, the size, location, and number of fans in your configuration may vary, but the methods of mounting both internal and external fans are covered.

This guide cannot cover every mounting combination for trays and panels; however, the git repository has Bill of Material information for mounting components to their respective tray or panel.

Areas where the :material-alpha-c-box: Core variants may differ from instructions are specifically called out.

## Techniques

Assembly relies on a few concepts that are reused through this guide.

### Fasteners

Screws thread directly into the walls of the plastic where heat set inserts are not used.

For example, lower bay trays attach to the main body with M3 screws. The trays have holes larger than the diameter of the screw, but the holes in the standoff are *smaller*. This lets the screw "bite" the plastic of the standoff and the screw head to clamp down on the tray.

### Orientation

Images for assembly are provided from a limited set of overhead/angled perspectives. The component (or components) used in the current step is highlighted in blue.

### Fans

The procedure for both internal and external fan mounting is covered in the guide.

External fan cages and gaskets come in a number of sizes, but all sizes follow an identical procedure to mount.

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