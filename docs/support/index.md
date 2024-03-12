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
- A **variant** is a modified version of a component, such as a version of the above tray that takes heat set inserts.
- For simplicity, components and variants are called **parts**. 

Each part has an entry containing a bill of materials and other important information. Some parts have more than one printed
piece; the BOM lists all printed pieces necessary and a download link.

The layout of this documentation is standardized, and most sections are organized by the name of the electronic component
a part is designed to mount.

Below are explanations of the information you'll find in each part entry.

## Fit Testing

Before a part is merged into the `main` branch, it has to be tested. Parts
that are waiting for fit testing are marked like this:

!!! caution "Fit Test Pending: Issue #NNN"

"#NNN" is a link to the open fit test issue on GitHub. If you print a part waiting for fit testing, please report your results!

## Badges

Icon badges provide many details about a part at a glance.

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

Front and Rear parts can be printed in place of a Unified part. Unlike Short parts, Front and Rear parts
are not interchangeable. This badge applies to Bases, Main Bodies, and Bottom Panels.
</div>
<div markdown class="card">
**Heat Set Insert**

{{ badges.hsi() }}

Indicates a part requires heat set inserts.
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

The current revision of a part, if applicable.
</div>
</div>

### Bases and PSUs

<div markdown class="grid">
<div markdown class="card">
**Switch**

<div markdown>{{ badges.switch('Rocker')}} {{ badges.switch('Toggle')}} {{ badges.switch('None')}}</div>

Identifies the type of power switch(es) compatible with a given power supply or base.
</div>
<div markdown class="card">
**Depth**

<div markdown>{{ badges.base_depth('36mm')}} {{ badges.base_depth('42mm') }}</div>

For a base, this is the available depth for mounting a power supply. For a PSU, indicates the
depth required.
</div>
<div markdown class="card">
**IEC C14**

<div markdown>{{ badges.iec(False) }} {{ badges.iec(True) }} </div>

These badges indicate if a Base mounts an IEC C14 power inlet.
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

## Support Sections

### General

| Topic | Description |
|-------|-------------|
| [:octicons-checklist-24: Panel Mounts][panel_mounts] | Supported types of panel-mounted connectors. |
| [:octicons-checklist-24: Fans][fans] | Types of fans with internal or external mounts. |

### Core

| Component | Description |
|-----------|-------------|
| [:octicons-checklist-24: Base][base] | Mounts the power supply and bottom panel(s); acts as a foundation for the Main Body. |
| [:octicons-checklist-24: Main Body][main_body] | Mounts most trays and panels; serves as the heart of the case. |

### Trays

| Tray Type | Description |
|-----------|-------------|
| [:octicons-checklist-24: MCU Trays][mcu] | MCUs are mounted directly underneath the lid for easy access. |
| [:octicons-checklist-24: CPU Trays][cpu] | Trays with an integrated panel; can slide out from the side of the case. |
| [:octicons-checklist-24: PSU Trays][psu] | Power supplies are inserted from below as part of the Base. |
| [:octicons-checklist-24: Lower Bay Trays][lower_bay] | Mount other miscellaneous parts (e.g., solid state relays, buck converters). |

### Panels

| Panel Type | Description |
|------------|-------------|
| [:octicons-checklist-24: Display Panels][display] | Mount LCD and TFT displays. |
| [:octicons-checklist-24: Bottom Panels][bottom]   | Protect the PSU and allow airflow, if needed. |
| [:octicons-checklist-24: Front Panels][front]     | User-facing panel for small ports and lights. |
| [:octicons-checklist-24: Lids][lid]               | Serve many purposes, including mounting large fans and/or a handle. |
| [:octicons-checklist-24: Rear Panels][rear]       | Pass-through wiring to your printer and can mount medium-sized fans. |
| [:octicons-checklist-24: Side Panels][side]       | Act as air inlets and connector panels. |\

[base]:         base.md         "Base options"
[main_body]:    main_body.md    "Main Body options"
[panel_mounts]: panel_mounts.md "Supported panel mounts"
[cpu]:          cpu.md          "Supported SBC CPUs"
[mcu]:          mcu.md          "Supported MCUs"
[psu]:          psu.md          "Supported PSUs"
[display]:      display.md      "Supported displays"
[lower_bay]:    lower_bay.md    "Supported lower bay hardware"
[fans]:         fans.md         "Supported fans"
[front]:        front.md        "Front Panel options"
[rear]:         rear.md         "Rear Panel options"
[side]:         side.md         "Side Panel options"
[lid]:          lid.md          "Lid options"
[bottom]:       bottom.md       "Bottom Panel options"

[tour]:         ../tour.md      "Visual Guided Tour"
[templates]:    ../upgrade/templates.md "List of tray and panel templates"
[img_trays]:  ../img/components/trays.webp
[img_panels]:  ../img/components/panels.webp