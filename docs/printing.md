---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has common settings for printing OmniBox and a printed component checklist. See the [guided tour][tour] for help choosing the correct parts.

## 3D Printing Settings

### General Settings

These settings are consistent for all parts but the optional fan gaskets.

| Setting                   | Value        | Notes |
|---------------------------|--------------|------|
| **Layer Height**          | 0.2-0.24mm   | Coarser settings have not been tested. |
| **Adaptive Layer Height** | Optional     | Can improve appearance and reduce print time.    |
| **Perimeters (Walls)**    | 1.2mm+       | 3 perimeters with a 0.4mm nozzle. 1.5mm+ results in solid main body side walls. |
| **Infill**                | 20-25%       | Cubic is a good tradeoff for time and durability. |
| **Material**              | PLA/PLA+     | See note below. |
| **Nozzle Diameter**       | 0.4mm, 0.6mm | If you print a case with a different nozzle size, please share your results! |

!!! note "Note: Materials"
    - The case can be printed in PETG but may take longer.
    - TPU is only used with fan gaskets, which are optional.

### Settings Specific to Core Components

- Supports must be on.
- Support blockers are recommended for all zip tie anchors and fastener holes.
- Use a brim or adhesive.
- Cantilever bed printers (e.g., Ender 5 Pro) should move large parts to the supported side of the bed.

## Printed Component Checklist

This is a checklist of *types* parts to print. See the [Guided Tour][tour] for help selecting the right STL files from the git repository.

### Core

| Component                                                        | Quantity | Required | Notes  |
|------------------------------------------------------------------|----------|----------|--------|
| [:material-git: Base - Front][git_base_front]                    | 1        | Yes      |        |
| [:material-git: Base - Rear][git_base_rear]                      | 1        | Yes      |        |
| [:material-git: Main Body - Crossbar][git_main_body_crossbar]    | 1        | Yes      |        |
| [:material-git: Main Body - Front][git_main_body_front]          | 1        | Yes      | See the [tour][tour] on choosing a version to print. |
| [:material-git: Main Body - Rear][git_main_body_rear]            | 1        | Yes      | See the [tour][tour] on choosing a version to print. |
| [:material-git: Base Extension][git_base_extension]              | 1        | See note | Required when using a Mean Well RSP-500 power supply, otherwise optional. |

### Trays

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: PSU Tray][git_psu]              | 1        | Yes      |        |
| [:material-git: MCU Tray][git_mcu]              | 1        | Yes      |        |
| [:material-git: CPU Tray][git_cpu]              | 0-1      | No       | If unused, replace with an extra side panel. |
| [:material-git: Lower Bay Trays][git_lower_bay] | 0-6      | No       | Type and quantity are specific to configuration. |

### Panels

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: Display Mount][git_display]     | 1        | Yes      |       |
| [:material-git: Lid][git_lid]                   | 1-2      | Yes      | One (1) long lid or two (2) short lids. |
| [:material-git: Rear Panel][git_rear_panel]     | 1        | Yes      |       |
| [:material-git: Bottom Panel][git_bottom_panel] | 1        | Yes      |       |
| [:material-git: Side Panel][git_side_panel]     | 1-2      | Yes      | One (1) with a CPU tray, two (2) without. |

### Other Components

| Component                                       | Quantity | Required | Notes  |
|-------------------------------------------------|----------|----------|--------|
| [:material-git: Fan Cages][git_fans]            | See note | Yes      | Quantity and type depend on configuration. |
| [:material-git: Fan Gaskets][git_fans]          | See note | No       | Optional add-on to fan cages. |

[tour]: tour.md "Visual Guided Tour"