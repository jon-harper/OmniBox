---
title: Templates
summary: Information on panel and tray templates
authors: Jon Harper
date: 2023-07-26
---

As of v0.9.10, all trays and panels have templates except the PSU tray. Trays and panels generally have STEP files available for modification, as well.

## Trays

### MCU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: MCU Tray Template][git_mcu_template]{ .md-button }

- Introduced: v0.9
- Current version: v2, introduced with v0.9.9
- Notes:
    - v1 trays are forward-compatible.
    - v2 trays are not backwards-compatible.
</div>
<div markdown class="jh-grid-img">
[![product picture][img_mcu_tray]][img_mcu_tray]
</div>
</div>

### CPU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: CPU Tray Template][git_cpu_template]{ .md-button }

- Introduced: v0.9
- Current version: v2, introduced with v0.9.9
- Notes:
    - v1 and v2 trays are freely interchangeable.
</div>
<div markdown class="jh-grid-img">
[![CPU tray illustration][img_cpu_tray]][img_cpu_tray]
</div>
</div>

### PSU Tray

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
!!! note
    A publicly available template for PSU trays is not yet available.

- Introduced: v0.9.9
- Current version: v1, introduced with v0.9.9
- Notes: OmniBox releases prior to 0.9.9 did not use PSU trays.
</div>
<div markdown class="jh-grid-img">
[![PSU illustration][img_psu_tray]][img_psu_tray]
</div>
</div>

## Panels

### Bottom Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Bottom Panel Template][git_bottom_template]{ .md-button }

- Introduced: v0.9.9
- Current version: v2, introduced with v0.9.10
- Notes: 
    - v1 and v2 panels are freely interchangeable.
</div>
<div markdown class="jh-grid-img">
[![Bottom panel illustration][img_bottom]][img_bottom]
</div>
</div>

### Display Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Display Panel Template][git_display_template]{ .md-button }

- Introduced: v0.9
- Current version: v3, introduced with v0.9.10
- Notes:
    - v1 display panels use M4 screws and are not compatible.
    - v2 and v3 display panels use M3 screws and are freely interchangeable.
</div>
<div markdown class="jh-grid-img">
[![Display panel illustration][img_display]][img_display]
</div>
</div>

### Front Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Front Panel Template][git_front_template]{ .md-button }

- Introduced: v0.9
- Current version: v1
</div>
<div markdown class="jh-grid-img">
[![front panel illustration][img_front]][img_front]
</div>
</div>

### Lid

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Lid Template][git_lid_template]{ .md-button }

- Introduced: v0.9
- Current version: v2, introduced with v0.9.7
- Notes:
    - v1 and v2 are not compatible.
</div>
<div markdown class="jh-grid-img">
[![lid illustration][img_lid]][img_lid]
</div>
</div>

### Rear Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Rear Panel Template][git_rear_template]{ .md-button }

- Introduced: v0.9
- Current version: v3, introduced with 0.9.10
- Notes:
    - v1 is incompatible with later versions.
    - v2 and v3 are interchangeable.
</div>
<div markdown class="jh-grid-img">
[![rear panel illustration][img_rear]][img_rear]
</div>
</div>

### Side Panel

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">

[:material-git: Side Panel Template][git_side_template]{ .md-button }

- Introduced: v0.9.9
- Current version: v1
</div>
<div markdown class="jh-grid-img">
[![side panel illustration][img_side]][img_side]
</div>
</div>

[img_mcu_tray]: ../img/components/mcu.webp
[img_cpu_tray]: ../img/components/cpu.webp
[img_lower_bay]: ../img/components/lower_bay.webp
[img_psu_tray]: ../img/components/psu.webp
[img_display]: ../img/components/display.webp
[img_front]: ../img/components/front_panel.webp
[img_bottom]: ../img/components/bottom.webp
[img_rear]: ../img/components/rear.webp
[img_lid]: ../img/components/lid.webp
[img_side]: ../img/components/side.webp