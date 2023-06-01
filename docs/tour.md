---
title: Guided Tour
summary: Tour and overview of OmniBox
authors: Jon Harper
date: 2022-08-04
---

## Introduction

This is a visual tour of an OmniBox. This page demonstrates:

1. The core parts of OmniBox and their variations;
2. Trays and panels; and
3. How these pieces fit together.

### Overview

<figure markdown>
  [![overview of an omnibox][img_overview]][img_overview]{ width="640" }
  <figcaption>A finished OmniBox.</figcaption>
</figure>

The configuration in the image above will be our example in this guide. We will start with the Core components and move on to the trays and panels that make OmniBox so modular. 

### Links

Links on this site to external resources have prefix icons to identify what they do:

- :material-git: The git icon is used for links to the OmniBox GitHub. 
- :material-cart: identifies an example link to a shopping site.

Internal page links in this tour are marked with an :material-directions: arrow sign.

## Core Components

Core components form the basis of every case. End-user parts normally do not attach to core components; instead, components are attached to trays and panels, which then mount on the Core case.

!!! important
    Most Core components come with the option of using heat set inserts to attach most trays and panels. These `STL` files have "HSI" in the name.

<figure markdown>
  [![the core of an OmniBox][img_core]][img_core]
  <figcaption>The core components of an OmniBox with fans and power supply mounted.</figcaption>
</figure>

There are two types of Core components: Base and Main Body. A typical OmniBox build has two parts for the base and three for the main body. The Unified base can be printed instead of the front and rear pieces.

<div markdown class="jh-grid-container jh-grid-3">
<div markdown>
**Base**

- [:material-directions: Front Base](#front-base)
- [:material-directions: Rear Base](#rear-base)
- [:material-directions: Unified Base](#unified-base)
</div>
<div markdown>
**Main Body**

- [:material-directions: Crossbar](#main-body-crossbar)
- [:material-directions: Front Main Body](#front-main-body)
- [:material-directions: Rear Main Body](#rear-main-body)
</div>
</div>

### Base

The Base serves as a cover and mount for the power supply. It helps with wire routing and acts as a rigid base for the rest of the Core case.

#### Front Base

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
This is the front of two halves. All versions come with front air vents and optional 40mm fan mounts.

The Front can be printed to fit a 30mm x 11mm rocker switch or a 12mm toggle switch.

[:material-git: Front Base Files][git_base_front]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![front base][img_base_front]][img_base_front]
</div>
</div>

#### Rear Base

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The back half mounts a fused IEC power plug and part of the [Rear Panel](#rear-panel).

This component is available with heat set inserts.

[:material-git: Rear Base Files][git_base_rear]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![front base][img_base_rear]][img_base_rear]
</div>
</div>

#### Unified Base

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The base can be printed as a single piece instead halves on printers with a bed at least 300mm on one axis.

A version is available for the RSP-500. This file is 10mm taller than the normal base to account for the height of the PSU.

This component is available with heat set inserts.

[:material-git: Unified Base Files][git_base_unified]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![front base][img_base_unified]][img_base_unified]
</div>
</div>

### Main Body

#### Main Body Crossbar

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
This is a crossbar that joins and covers the joint between the lids and front display.

This component is available with heat set inserts.

Two versions 

[:material-git: Crossbar Files][git_main_body_crossbar]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![stock crossbar][img_crossbar]{ width="360" }][img_crossbar]
</div>
</div>

#### Front Main Body

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The front half of the Main Body mounts the display and front panel.

This component is available with heat set inserts.

[:material-git: Front Main Body Files][git_main_body_front]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![front main body with internal fan][img_main_front]][img_main_front]
</div>
</div>

#### Rear Main Body

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The rear half of the Main Body is the largest single piece of the case and operates with two levels. The lower level has CPU and lower bay trays. The upper level mounts the MCU.

This component is available with heat set inserts.

[:material-git: Rear Main Body Files][git_main_body_rear]{ .md-button }
</div>
<div markdown class="jh-card">
=== "Dual 40mm Fans"

    [![rear main body with dual fans][img_rear_dual]{ width="360" }][img_rear_dual]

    You will also need to print [:material-directions: 40mm fan cages](#fans) and (optionally) TPU gaskets for this variation.

=== "No Fan Mounts"

    [![rear main body without fan mounts][img_rear_none]{ width="360" }][img_rear_none]

    This versions of the rear main body *requires* either rear panel or lid-mounted fans.
</div>
</div>

## Trays

Trays are used for mounting parts internally. There are four (4) types of trays.

Templates are available in both `STEP` and Fusion 360 formats to add support for new products.

!!! note
    PSU trays are a new feature and do not yet have a template.

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays in red.</figcaption>
</figure>

**Trays**

- [:material-directions: PSU Tray](#psu-tray)
- [:material-directions: MCU Tray](#mcu-tray)
- [:material-directions: Lower Bay Trays](#lower-bay-trays)
- [:material-directions: CPU Tray](#cpu-tray)

### PSU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
Power supply (PSU) trays slide up from underneath the case.

Large (tall) power supplies require the use of an [:material-directions: extended Unified Base](#unified-base) or a [:material-directions: base extension](#base-extensions).

[:material-git: PSU Tray Files][git_psu]{ .md-button }

[:octicons-checklist-24: Supported PSUs][psu]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![power supply tray][img_psu]][img_psu]
</div>
</div>

### MCU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
MCU trays mount a microcontroller unit--your 3D printer board. These are 

[:material-git: MCU][git_mcu]{ .md-button }

[:octicons-checklist-24: Supported MCUs][mcu]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![mcu tray][img_mcu]][img_mcu]
</div>
</div>

### Lower Bay Trays

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The lower bay is an area to mount parts like buck converters and MOSFETs. There are two dedicated lower bay trays locations and four more that can occupy an unused CPU tray bay.

These trays can be Short or Long. A Long tray covers the mount points of two Short trays and must be mounted from side-to-side in the case.

[:material-git: Lower Bay][git_lower_bay]{ .md-button }

[:octicons-checklist-24: Supported Lower Bay Components][lower_bay]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![lower bay tray][img_lower_bay]][img_lower_bay]
</div>
</div>

### CPU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The CPU tray is an optional mount for a Raspberry Pi or other SBC. There are two bays for CPU trays; one is on each side of the case.

An unused bay is replaced by a [:material-directions: Side Panel](#side-panels). A short lower bay tray can also be installed in an unused CPU bay.

[:material-git: CPU][git_cpu]{ .md-button }

[:octicons-checklist-24: Supported SBCs][cpu]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![cpu tray][img_cpu]][img_cpu]
</div>
</div>

## Panels

<figure markdown>
  [![callout of panels and fan cage][img_panels]{ width="640" }][img_panels]
  <figcaption>The six types of panels, visible in grey.</figcaption>
</figure>

<div markdown class="jh-grid-container jh-grid-3">
<div markdown class="jh-grid-para">
**General Panels**

- [:material-directions: Display panel](#display-panel)
- [:material-directions: Lid](#lids)
- [:material-directions: Bottom panel](#bottom-panel)
</div>
<div markdown class="jh-grid-para">
**Connector Panels**

- [:material-directions: Front panel](#front-panel)
- [:material-directions: Rear panel](#rear-panel)
- [:material-directions: Side panel](#side-panel)
</div>
</div>

Panels cover the outside of OmniBox and mount of a range of options. Front, side, and rear panels are typically used for connectors, fans, and ventilation.

There is a blank `STEP` and Fusion 360 template for each panel category to allow users to create new panels.

### Front Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The front panel serves as an air vent and location to put a MicroSD card reader extension. USB extensions are also a common accessory.

[:material-git: Front Panel][git_front_panel]{ .md-button }

[Panel Mounts][panel_mounts]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![front panel][img_front_panel]][img_front_panel]
</div>
</div>


### Side Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
A side panel replaces a CPU tray and often mounts connectors or fans. A blank side panel can be used if necessary.

[:material-git: Side Panel][git_side_panel]{ .md-button }

[Panel Mounts][panel_mounts]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![side panel][img_side]][img_side]
</div>
</div>

### Bottom Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The bottom panels act as a cover for the underside of the case. A fully enclosed option is available to keep dust out.

[:material-git: Bottom Panel][git_bottom_panel]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![bottom panel][img_bottom]][img_bottom]
</div>
</div>

### Display Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
This area mounts LCD displays, from the basic 128x64 character display to Raspbery Pi TFTs.

[:material-git: Display][git_display]{ .md-button }

[:octicons-checklist-24: Supported Displays][displays]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![display panel][img_display]][img_display]
</div>
</div>

### Lid(s)

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The lid is both a way into your case and a configurable panel. There are two types of lids: short and long lids. You can either print one (1) long lid or two (2) short lids.

[:material-git: Lid][git_lid]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![img_lid][img_lid]][img_lid]
</div>
</div>

### Rear Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
The rear panel is used for ventilation, passing wiring out of your case, and optionally an additional fan. There are stock configurations available to suit common uses. A template is available for customization.

Rear panels with panel mounted connectors are an active area of work.

[:material-git: Rear Panel][git_rear_panel]{ .md-button }

[Panel Mounts][panel_mounts]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![rear panel][img_rear]][img_rear]
</div>
</div>

## Other Components

Several other components deserve mention in this tour; not all of these are 3D printed parts.

- [:material-directions: Fans](#fans)
- [:material-directions: Base Extensions](#base-extensions)
- [:material-directions: Power Switches](#power-switch)
- [:material-directions: IEC C14 Power Sockets](#iec-c14-power-socket)

### Fans

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
Externally mounted fans use fan cages to cover the fan blades. There are a large number of fan sizes supported, each with a matching TPU fan gasket. The gaskets are optional and serve to reduce noise.

Internally mounted fans are also available, but are limited to 40mm fans.

[:material-git: Fans][git_fans]{ .md-button }

[:octicons-checklist-24: Supported Fans][fans]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![external fan cages][img_external_fan]][img_external_fan]
</div>
</div>

### Base Extensions

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
Larger power supplies require the addition of a base extension shim (or a [:material-directions: extended Unified Base](#unified-base)). This mounts between the base and the bottom panel.

[:material-git: Extension Shim][git_base_extension]{ .md-button }
</div>
<div markdown class="jh-grid-img">
[![base extension is highlighted in blue][img_base_extension]][img_base_extension]
</div>
</div>


### Power Switch

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
OmniBox supports two types of master power switches: a 30x11mm [:material-cart: snap-in SPST rocker switch][bom_switch] or [:material-cart: 12mm toggle switch][bom_toggle_switch].

A cover is available for rocker switches to prevent accidental power-off.

[:material-git: Rocker Switch Protector][git_switch_cover]{ .md-button }
</div>
<div markdown class="jh-card">
=== "Rocker Switch"
    [![rocker switch is highlighted in blue][img_switch]][img_switch]
=== "Toggle Switch"
    [![toggle switch is highlighted in blue][img_toggle_switch]][img_toggle_switch]
</div>
</div>

### IEC C14 Power Socket


<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
Power is provided through a standard [:material-cart: fused IEC C14 power socket][bom_iec].
</div>
<div markdown class="jh-grid-img">
[![iec socket is highlighted in blue][img_iec]][img_iec]
</div>
</div>

[fans]:  support/fans.md
[panel_mounts]:  support/panel_mounts.md
[displays]:  support/displays.md
[mcu]:  support/mcu.md
[lower_bay]: support/lower_bay.md
[cpu]: support/cpu.md
[psu]: support/psu.md
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