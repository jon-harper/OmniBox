---
title: Support Overview
summary: Introduction to OmniBox product support.
authors: Jon Harper
date: 2022-07-03
prefix: ../
---

{%- import 'badges.md' as badges with context -%}

OmniBox has a large number of available components, many with multiple variants. Some of these have several printed pieces.
Simply:

- A **component** is a common design, such as an MCU tray for a Bigtreetech SKR E3.
- A **variant** is a modified version of the stock component, such as a version of the above tray that takes heat set inserts.
- For simplicity, components and variants are **parts**. 

Each part has an entry containing a bill of materials and other important information. Some parts have more than one printed
piece; the BOM lists all printed pieces necessary and a download link.

The layout of this documentation is standardized, and most sections are organized by the name of the electronic component
a part is designed to mount.

Below are explanations of the information you'll find in the Options & Support section.

## Fit Testing

Before a component (such as a tray or panel) is merged into the `main` branch, it has to be tested. Parts
that are waiting for fit testing are marked like so:

!!! caution "Fit Test Pending: Issue #NNN"

If you print one of these parts, please report your results! There is usually an open [:material-git: issue on GitHub][git_issues] for that hardware component.

## Badges

Icon badges provide key details about a part at a glance.

### Basics

<div markdown class="grid">
<div markdown class="card">
**Size**

<div markdown>{{ badges.size('Short') }} {{ badges.size('Long') }} </div>

Indicates the size of a part; this applies to lower bay trays and lids. Two (2) Short parts replace one (1) Long part.
</div>
<div markdown class="card">
**Unified**

{{ badges.unified() }}

Indicates a part is a single piece that replaces front and rear halves. Unified parts require large build plates.
</div>
<div markdown class="card">
**Front and Rear**

<div markdown> {{ badges.front() }} {{ badges.rear() }} </div>

Front and Rear parts can be printed in place of a Unified part. Front and Rear parts are not
interchangeable, unlike Short parts. Applies to Base, Main Bodies, and Bottom Panels.
</div>
<div markdown class="card">
**Heat Set Insert**

{{ badges.hsi() }}

Indicates a component or variant requires heat set inserts.
</div>
</div>

### Credits

<div markdown class="grid">
<div markdown class="card">
**Author**

{{ badges.author('Name/Handle')}}

Links to a public profile for the creator of a contributed part.
</div>
<div markdown class="card">
**Origin**

{{ badges.origin('Name/Handle') }}

If a part is derived from someone else's work, this links to their public profile.
</div>
</div>

### Versioning

<div markdown class="grid">
<div markdown class="card">
**Template**

{{ badges.template('template_version')}}

All parts are based upon templates. These are useful in determining compatibility between parts and Core versions.
See the [Templates][templates] page for more.
</div>
<div markdown class="card">
**Version**

{{ badges.version('part_version')}}

The current revision of a part. Part versions are are imprinted on newer components.
</div>
</div>

### Bases and PSUs

<div markdown class="grid">
<div markdown class="card">
**Switch**

{{ badges.switch('Rocker')}}

Identifies the type of power switch(es) compatible with a given power supply or base.
</div>
<div markdown class="card">
**Depth**

{{ badges.base_depth('36mm')}}

Either 36 or 42mm. For a base, this is the available depth for mounting a power supply. For a PSU, indicates the
depth required.
</div>
<div markdown class="card">
**IEC**

{{ badges.no_iec() }}

This is only used for Bases that do *not* mount an IEC power inlet.
</div>
</div>

### Panel-specific

<div markdown class="grid">
<div markdown class="card">
**Display**

<div markdown>{{ badges.display('CPU') }} {{ badges.display('MCU') }}</div>

Indicates whether a display panel mounts a display that connects to a CPU or MCU.
</div>
<div markdown class="card">
**Fan, Vent**

<div markdown> {{ badges.fan() }} {{ badges.vent() }} </div>

Fan badges indicate that a part has a fan mount; vent badges signal that a part has cutouts for airflow.
</div>
<div markdown class="card">
**Panel Mount**

{{ badges.extension('USB C, RJ-45') }}

These badges list the types of panel mounts available on a given part.
</div>
</div>

## Component Types

### Trays

<figure markdown>
  [![the three types of trays][img_trays]{ width="640" }][img_trays]
  <figcaption>The four types of trays: MCU, CPU, PSU, and lower bay.</figcaption>
</figure>

Trays mount electronics most of your case's electronics.

- [MCUs][mcu] are mounted directly underneath the lid for easy access.
- [CPUs][cpu] sit on trays that can slide out the side of the case.
- [Power supplies (PSUs)][psu] are inserted from below.
- [Lower Bay Trays][lower_bay] are used for parts such as buck converters and solid state relays. These occupy the middle of the case.

### Panels

Panels are generally used for displays, [fans][fans], and [panel-mounted connector extensions][panel_mounts] like USB ports and 
SD card readers. Lids can be put to a wide variety of uses, as well.

<figure markdown>
  [![external panels][img_panels]{ width="640" }][img_panels]
  <figcaption>Panels cover the outside of the case.</figcaption>
</figure>

- [Display Panels][display] mount LCD and TFT displays.
- [Bottom Panels][bottom] protect the PSU and allow airflow, if needed.
- [Front Panels][front] are a user-facing panel for MicroSD, USB ports, or even LED lights.
- [Lids][lid] serve many purposes, including mounting large fans and/or a handle.
- [Rear Panels][rear] pass-through wiring to your printer and can mount medium-sized fines.
- [Side Panels][side] are convenient air inlets and connector panels.

[panel_mounts]: panel_mounts.md
[cpu]: cpu.md
[mcu]: mcu.md
[psu]: psu.md
[display]: display.md
[lower_bay]: lower_bay.md
[fans]: fans.md
[tour]: ../tour.md
[front]: front.md
[rear]: rear.md
[side]: side.md
[lid]: lid.md
[bottom]: bottom.md
[templates]: ../upgrade/templates.md
[img_trays]:  ../img/components/trays.webp
[img_panels]:  ../img/components/panels.webp