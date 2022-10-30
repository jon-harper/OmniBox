---
title: Getting Started
summary: Guide to assembling the OmniBox.
authors: Jon Harper
date: 2022-10-26
---

## Overview

This guide is divided into four sections:

- [:material-alpha-c-box: :material-alpha-b-box-outline: Core - Base][1]: Assembly of the base and power supply
- [:material-alpha-c-box: :material-alpha-m-box-outline: Core - Main Body][2]: Addition of the front & rear main body
- [:material-alpha-t-box: Trays][3]: Lower bay, CPU, and MCU tray assembly
- [:material-alpha-p-box: Panels][4]: Displays, lids, front & rear panels

Instructions are for the 0.9.9 release. If you have an older or newer version, some details may differ.

### Time

Assembly takes approximately two hours for the stock version without brass heat set inserts.

This estimate assumes that you:

- Have printed all [necessary parts][5], and
- Have never assembled an OmniBox.

Estimated time does not include the time needed to run and attach wiring.

### Configurations

These instructions are cover a generic OmniBox configuration. The size, location, and number of fans in your configuration may vary, for example, but the method of mounting both internal and external fans is covered.

This guide cannot cover every mounting combination for trays and panels; however, the git repository should have Bill of Material information for mounting components to their respective tray or panel.

Areas where the :material-alpha-c-box: Core variants may differ from instructions are specifically called out.

## Techniques

Assembly relies on a few concepts that are reused through the process.

### Fasteners

If you are not assembling a case with heat set inserts (HSI), note that screws thread directly into the walls of the plastic.

For example, displays attach to the main body with M3 screws. Display panels have holes larger than the diameter of the screw, but the holes in the main body are *smaller*. This lets the screw "bite" the plastic of the main body and hold the display between the screw head and main body.

### Orientation

Images for assembly are provided from one of three perspectives. The part discussed in the current step is highlighted.

### Fans

Fan cages come in a number of sizes but all follow a similar pattern for assembly.

Note: fans 60mm and smaller use M3 screws. Larger fans require M4 screws.

[1]: base.md "Base Assembly"
[2]: main_body.md "Main Body Assembly"
[3]: trays.md "Tray Assembly"
[4]:  panels.md "Panel Assembly"
[5]: ../printing.md#print-checklist "Print Checklist"