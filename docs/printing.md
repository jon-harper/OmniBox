---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has common settings for printing OmniBox and a printed component checklist. See the [guided tour][tour] for help choosing the correct parts.

## Recommended Materials

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
**:octicons-check-circle-fill-16:{.jh-green} Modified PLA**

OmniBox prints best with modified PLA, usually called **PLA+** or **PLA Pro**.

</div>
<div markdown class="jh-grid-para">
**:octicons-x-circle-fill-16:{.jh-red} Unmodified PLA**

Sometimes called **Basic PLA**, unmodified PLA prints easily but is a rigid and weak material. Unmodified PLA prints at lower temperatures and is usually cheaper than modified PLA. *Use modified PLA instead*.
</div>
<div markdown class="jh-grid-para">
**:octicons-check-circle-fill-16:{.jh-green} PETG**

Printing in PETG typically takes longer than PLA but otherwise produces good results.
</div>
</div>
 
!!! note
    Fan gaskets are an optional noise reducer and require TPU.

## 3D Print Settings

These settings are consistent for all parts except the TPU fan gaskets.

| Setting                   | Value        | Notes |
|---------------------------|--------------|------|
| **Layer Height**          | 0.16-0.25mm  | Coarser settings have not been tested. |
| **Adaptive Layer Height** | Optional     | Can improve appearance and reduce print time.    |
| **Perimeters (Walls)**    | [*See below*](#material-specific-settings)   | Correct value depends on material. |
| **Infill**                | 20-25%       | Cubic is a good tradeoff for time and durability. |
| **Nozzle Diameter**       | 0.4mm, 0.6mm | If you print a case with a different nozzle size, please share your results! |
| **Support Overhang Angle** | >= 60 degrees | This reduces print time & support material. |

### Material-Specific Settings

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
**PLA**

Print with 1.2mm or thicker walls (3 perimeters with a 0.4mm nozzle). 1.5mm+ results in solid Main Body side walls.

</div>
<div markdown class="jh-grid-para">
**PETG**

Use 1.6mm walls/perimeters (1.8mm for 0.6mm nozzles).
</div>
</div>

### Support Settings

- Supports must be on for the main body.
- The base may be printed without supports.
- Support blockers are recommended for all zip tie anchors and fastener holes.

### General Tips

- For large parts (e.g., the rear main body) use a brim, adhesive, or both.
- Cantilever bed printers (where the bed is supported by a single Z stepper; e.g., Ender 5 Pro) should move heavier prints to the supported side of the bed.
- If printing in a drafty room, consider a partial enclosure to help layer adhesion.
- Long lids will fit on 220x220mm beds if printed without a skirt or brim.

## Printed Component Checklist

This is a checklist of types parts to print. See the [Guided Tour][tour] for help selecting the right STL files from the git repository.

### Core: Base

Print a Front Base and a Rear Base. A Unified Base may be printed instead if you have a print bed with least 300mm on one axis.

See the [Base section of the Tour](tour.md#base) for more information.

<div markdown class="jh-grid-container jh-grid-2">
<div markdown class="jh-grid-para">
**Front & Rear**

[:material-git: Base - Front][git_base_front]

[:material-git: Base - Rear][git_base_rear]
</div>
<div markdown class="jh-grid-para">
**Unified and Unified Extended**

[:material-git: Base - Unified][git_base_unified]
</div>
</div>

### Core: Main Body

Print one (1) version of each of the Crossbar, Front Main Body, and Rear Main Body. See the [Main Body section of the Tour](tour.md#main-body) for help choosing versions to print.

[:material-git: Main Body - Crossbar][git_main_body_crossbar]

[:material-git: Main Body - Front][git_main_body_front]

[:material-git: Main Body - Rear][git_main_body_rear]


### Trays

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: PSU Tray][git_psu]              | 1        | Yes      |        |
| [:material-git: MCU Tray][git_mcu]              | 1        | Yes      |        |
| [:material-git: CPU Tray][git_cpu]              | 0-1      | No       | Typically only one (1). Takes the place of a side panel. |
| [:material-git: Lower Bay Trays][git_lower_bay] | 0-6      | No       | Type and quantity are specific to configuration. |

### Panels

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: Display Mount][git_display]     | 1        | Yes      |       |
| [:material-git: Lid][git_lid]                   | 1-2      | Yes      | One (1) long lid or two (2) short lids. |
| [:material-git: Rear Panel][git_rear_panel]     | 1        | Yes      |       |
| [:material-git: Bottom Panel][git_bottom_panel] | 1        | Yes      |       |
| [:material-git: Side Panel][git_side_panel]     | 3-4      | Yes      | Four (4) side panels, minus the number of CPU trays installed. |

### Other Components

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: Fan Cages][git_fans]            | Varies | Yes      | Quantity and type depend on configuration. |
| [:material-git: Fan Gaskets][git_fans]          | Varies | No       | Optional add-on to fan cages. |
| [:material-git: Power Switch Cover][git_switch_cover] | 1  | No       | Recommended cover for rocker switches. |

[tour]: tour.md "Visual Guided Tour"