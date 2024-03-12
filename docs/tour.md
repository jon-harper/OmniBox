---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 2022-08-04
---

{% import 'format.md' as format with context %}

## Introduction

This is a short tour of an OmniBox to demonstrate the Core parts, Trays, Panels, and how they all fit together.
The configuration in the image above will be our example in this guide. We will start with the Core components,
then discuss the trays and panels that make OmniBox so modular. 

<figure markdown>
  [![overview of an omnibox][img_overview]][img_overview]{ width="640" }
  <figcaption>Render of a finished OmniBox.</figcaption>
</figure>

!!! note "Note: Links"
    Links often have icons that identify what they link to:

    - :material-git: The git icon is used for download links.
    - :octicons-checklist-24: The list icon is for links to the [Options & Support][support] section.
    - :material-cart: A shopping cart identifies a link to the [Sourcing Guide][sourcing].

### Stock vs. Heat Set Inserts

Most OmniBox STL files come in both `Stock` and `HSI` versions. Files without either in the name are assumed
Stock.

Stock files thread screws into bare plastic, which wear out over time. This issue can be temporarily resolved
by replacing screws with longer screws (which reach further back and grab 'fresh' plastic).

Heat set inserts (HSIs) are an alternative. Inserts are more expensive and time-consuming to install,
but last much longer and speed-up assembly and disassembly of the case.

If using HSIs, an M3 soldering iron tip for heat set inserts is recommended to aid insert installation.

## Core Components

Core components form the basis of every case. Parts like the MCU attach to trays, while external parts
like displays and USB connectors attach to panels. These trays and panels are then installed to the Core case.

<figure markdown>
  [![the core of an OmniBox][img_core]][img_core]
  <figcaption>The assembled core components of an OmniBox.</figcaption>
</figure>

Core components are divided into Bases and Main Bodies. Both of these are typically printed in halves
that are assembled into a large whole. Users with large (>315mm) beds can print Unified versions of
both the Base and Main Body.

### Main Body

Most electronics are attached to the Main Body (as panels) or installed inside (as trays).

The Main Body contains dozens of zip tie anchors for wire routing, as well as built-in wall mounts for 3-position Wago 221
lever connectors.

[:octicons-checklist-24: Main Bodies][main_body]{.md-button}

### Base

The Base is a cover and mount for the power supply and a foundation for the Main Body. It comes in 36mm or 42mm deep
versions--this number refers to the depth availabe for the PSU. The Base is usually printed with a cutout for an
IEC C14 power inlet. It can also be printed with one of several power switch options.

[:octicons-checklist-24: Bases][base]{.md-button}

## Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays: MCU, CPU, PSU, and lower bay.</figcaption>
</figure>

Trays mount most of your case's electronics.

- [:octicons-checklist-24: MCU Trays][mcu] are mounted directly underneath the lid for easy access.
- [:octicons-checklist-24: CPU Trays][cpu] have a small exterior panel and fit in the side of the case.
- [:octicons-checklist-24: PSU Trays][psu] mount power supplies and are inserted from below the Base.
- [:octicons-checklist-24: Lower Bay Trays][lower_bay] occupy the middle of the case and are used for any other parts (e.g., solid state relays, buck converters).

## Panels

Panels form the exterior of your case. These mount displays, [fans][fans], and [panel-mounted connector extensions][panel_mounts] like USB ports and 
SD card readers.

<figure markdown>
  [![external panels][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

- [:octicons-checklist-24: Display Panels][displays] mount LCD and TFT displays.
- [:octicons-checklist-24: Bottom Panels][bottom_panels] protect the PSU and allow airflow, if needed.
- [:octicons-checklist-24: Front Panels][front_panels] are a user-facing panel for MicroSD, USB ports, or even LED lights.
- [:octicons-checklist-24: Lids][lids] serve many purposes, including mounting large fans and/or a handle.
- [:octicons-checklist-24: Rear Panels][rear_panels] pass-through wiring to your printer and can mount medium-sized fines.
- [:octicons-checklist-24: Side Panels][side_panels] are convenient air inlets and connector pan els.

## Other Components

### Fans

Fans can be mounted internally or externally. External fans have printed cages to protect the fan blades, along with optional TPU gaskets.

Internal mounts are available for 40 and 50mm fans. These are generally used with [Side Panels][side_panels].

[:octicons-checklist-24: Fans][fans]{ .md-button }

[panel_mounts]:     support/panel_mounts.md "Supported panel mounts"
[fans]:             support/fans.md         "Supported fans"
[displays]:         support/display.md      "Supported displays"
[mcu]:              support/mcu.md          "Supported MCUs"
[lower_bay]:        support/lower_bay.md    "Supported lower bay parts"
[cpu]:              support/cpu.md          "Supported SBC CPUs"
[psu]:              support/psu.md          "Supported PSUs"
[support]:          support/index.md        "Options & Support Overview"
[front_panels]:     support/front.md        "Front Panel options"
[rear_panels]:      support/rear.md         "Rear Panel options"
[side_panels]:      support/side.md         "Side Panel options"
[lids]:             support/lid.md          "Lid options"
[bottom_panels]:    support/bottom.md       "Bottom Panel options"
[main_body]:        support/main_body.md    "Main Body options"
[base]:             support/base.md         "Base options"
[sourcing]:         sourcing.md             "Sourcing Guide"

[img_overview]: img/components/overview.webp
[img_core]: img/components/core.webp
[img_trays]: img/components/trays.webp
[img_panels]: img/components/panels.webp
[img_crossbar]: img/components/crossbar.webp
[img_main_front]: img/components/main_front.webp
[img_main_rear]: img/components/main_rear.webp
[img_base_front_rocker]: img/components/base_front_rocker.webp
[img_base_front_toggle]: img/components/base_front_toggle.webp
[img_base_rear]: img/components/base_rear.webp
[img_base_unified]: img/components/base_unified.webp
[img_base_extension]: img/components/base_extension.webp
[img_mcu]: img/components/mcu.webp
[img_cpu]: img/components/cpu.webp
[img_lower_bay]: img/components/lower_bay.webp
[img_front_panel]: img/components/front_panel.webp
[img_display]: img/components/display.webp
[img_lid]: img/components/lid.webp
[img_side]: img/components/side.webp
[img_rear]: img/components/rear.webp
[img_bottom]: img/components/bottom.webp
[img_fans]: img/components/fans.webp
[img_psu]: img/components/psu.webp
[img_rear_none]: img/components/rear_none.webp
[img_rear_quad]: img/components/rear_quad.webp
[img_rocker_switch]: img/components/switch_rocker.webp
[img_toggle_switch]: img/components/switch_toggle.webp
[img_iec]: img/components/iec.webp