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

!!! note
    There are 24 inserts. Experienced users following this guide should be able to install all inserts in less than 30 minutes.
    
    Gaining some experience with inserts saves time later and lowers the chances of damaging a printed part. If you plan to use inserts and have not practiced, it is recommended that you print at least one [practice block][git_hsi_practice] to gain a level of comfort.

#### 2. :material-alpha-c-box: Core & :material-alpha-t-box: :material-alpha-p-box-outline: PSU

Assembly starts in earnest by building the Base around the PSU and wiring it up. This acts as a first layer of the case that we will build upwards from.

The section finishes by installing the Main Body.

#### 3. :material-alpha-t-box: :material-alpha-c-box-outline: CPU & :material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays

The second layer of the case adds the SoC CPU and lower bay components. By the end of this section, all electronics not mounted on a panel will be installed and wired.

#### 4. :material-alpha-t-box: :material-alpha-m-box-outline: MCU & :material-alpha-p-box: Panels

At this point, assembly centers around the MCU, final wiring, and closing up the case.

### Format

Each section of the assembly has four parts:

- A short (3-10 second) optional video showing the combined assembly steps of that section. These videos are meant to give an overview of the following steps.
- A list of materials used and quantity
- Step-by-step illustrated instructions
- A final reference image

All graphics can be enlarged to see detail by clicking or tapping.

### Time

Most of the case can be assembled in approximately two (2) hours.

This estimate assumes that you:

- Have printed all [necessary parts][checklist]; and
- Have never assembled an OmniBox.

This estimate does *not* include:

- Time needed to run and attach wiring;
- Power up and configuration tests; and
- Time needed for heat set insert (HSI) installation, if applicable.

### Configurations

These instructions are cover a generic OmniBox configuration. For example, the size, location, and number of fans in your configuration may vary, but the methods of mounting both internal and external fans are covered.

This guide cannot cover every mounting combination for trays and panels; however, the git repository has Bill of Material information for mounting components to their respective tray or panel.

Areas where the :material-alpha-c-box: Core variants may differ from instructions are specifically called out.

## Techniques

Assembly relies on a few concepts that are reused through this guide.

### Fastening Screws

Screws thread directly into the walls of the plastic where heat set inserts are not used.

For example, lower bay trays attach to the main body with M3 screws. The trays have holes larger than the diameter of the screw, but the holes in the standoff are *smaller*. This lets the screw "bite" the plastic of the standoff and the screw head to clamp down on the tray.

### Example Image Orientation

Images for assembly are provided from a limited set of overhead/angled perspectives. The component (or components) used in the current step is highlighted in blue.

### Mounting Fans

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
