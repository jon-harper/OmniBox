---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 2022-08-04
---

{% import 'format.md' as format with context %}

## Introduction

This is a visual tour of an OmniBox to demonstrate the Core parts, Trays, Panels, and how they all fit together.

<figure markdown>
  [![overview of an omnibox][img_overview]][img_overview]{ width="640" }
  <figcaption>A finished OmniBox.</figcaption>
</figure>

The configuration in the image above will be our example in this guide. We will start with the Core components and move on to the trays and panels that make OmniBox so modular. 

### Links

Links on this site to external resources have prefix icons to identify what they do:

- :material-git: The git icon is used for download links.
- :octicons-checklist-24: The list icon is for links to the [Options & Support][support] section.
- :material-cart: A shopping cart identifies a link to the [Sourcing Guide][sourcing].

### Heat Set Inserts

Many OmniBox components come with the option of using heat set inserts to attach other parts. These `STL`
files have names ending in `HSI`. Files ending with `Stock` in the name do not need inserts.

## Core Components

Core components form the basis of every case. Parts like the MCU do not directly attach to the Core case; instead, user
parts are attached to trays and panels, which then mount on the Core case.

<figure markdown>
  [![the core of an OmniBox][img_core]][img_core]
  <figcaption>The assembled core components of an OmniBox.</figcaption>
</figure>

There are two (2) types of Core components, the Base and the Main Body. Both of these are typically printed in halves
that are then assembled. Users with large (>315mm) beds can print Unified versions of both the Base and Main Body.

### Main Body

Most major components are attached to the Main Body as panels or installed inside of it as trays.

The Main Body contains dozens of zip tie anchors for wire routing, as well as four wall mounts for 3-position Wago 221
lever connectors.

### Base

The Base serves as a cover and mount for the power supply. It helps with wire routing and acts as a foundation
for the Main Body.

The Base can be printed in a 36mm or 42mm deep version--this number refers to the depth availabe for the PSU.

## Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays: MCU, CPU, PSU, and lower bay.</figcaption>
</figure>

Trays mount electronics most of your case's electronics.

- [:octicons-checklist-24: MCUs][mcu] are mounted directly underneath the lid for easy access.
- [:octicons-checklist-24: CPUs][cpu] sit on trays that can slide out from the side of the case.
- [:octicons-checklist-24: Power supplies (PSUs)][psu] are inserted from below as part of the Base.
- [:octicons-checklist-24: Lower Bay Trays][lower_bay] occupy the middle of the case and are used for miscellaneous parts (e.g., solid state relays, buck converters).

## Panels

Panels form the exterior of your case. These mount displays, [fans][fans], and [panel-mounted connector extensions][panel_mounts] like USB ports and 
SD card readers. Lids can be put to a wide variety of uses, as well.

<figure markdown>
  [![external panels][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

- [:octicons-checklist-24: Display Panels][displays] mount LCD and TFT displays.
- [:octicons-checklist-24: Bottom Panels][bottom_panels] protect the PSU and allow airflow, if needed.
- [:octicons-checklist-24: Front Panels][front_panels] are a user-facing panel for MicroSD, USB ports, or even LED lights.
- [:octicons-checklist-24: Lids][lids] serve many purposes, including mounting large fans and/or a handle.
- [:octicons-checklist-24: Rear Panels][rear_panels] pass-through wiring to your printer and can mount medium-sized fines.
- [:octicons-checklist-24: Side Panels][side_panels] are convenient air inlets and connector panels.

## Other Components

### Fans

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
Externally mounted fans use fan cages to cover the fan blades. There are a large number of fan sizes supported, each with a matching TPU fan gasket. The gaskets are optional and serve to reduce noise.

Internal mounts for 40 and 50mm fans are available.

[:octicons-checklist-24: Fans][fans]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![external fan cages][img_fans]][img_fans]
</div>
</div>

[panel_mounts]:  support/panel_mounts.md
[fans]:  support/fans.md
[displays]:  support/display.md
[mcu]:  support/mcu.md
[lower_bay]: support/lower_bay.md
[cpu]: support/cpu.md
[psu]: support/psu.md
[support]: support/index.md
[sourcing]: sourcing.md
[side_panels]: support/side.md
[front_panels]: support/front.md
[rear_panels]: rear.md
[side_panels]: support/side.md
[lids]: support/lid.md
[bottom_panels]: support/bottom.md

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