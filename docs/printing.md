---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has common settings for printing OmniBox and a printed component checklist. See the [guided tour][tour] for help choosing the correct parts.

## 3D Printing Settings

### General Settings

These settings are consistent for all parts.

| Setting            | Value       | Note |
|--------------------|-------------|------|
| Layer Height       | 0.2-0.24mm  | Coarser settings have not been tested. |
| Adaptive Layer Height | Optional | Can improve appearance and reduce print time.    |
| Perimeters (Walls) | 1.2mm+      | 3 perimeters with a 0.4mm nozzle. 1.5mm+ results in solid main body side walls. |
| Infill             | 20-25%      | Cubic is a good tradeoff for time and durability. |
| Material           | PLA/PLA+    | PETG may take longer to print on many printers but is still possible. |
| Nozzle Diameter    | 0.4mm       | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

### Settings Specific to :material-alpha-c-box: Core

- Supports should be left on.
- Support blockers are recommended for all zip tie anchors and can be used for fastener holes, as well.
- Use a brim or adhesive. Lifting can cause misalignment of the finished case body.
- Cantilever bed printers (e.g., Ender 5 Pro) should move large bodies towards to the supported side of the bed.

## Printed Component Checklist

This is a checklist of *types* parts to print. See the [guided tour][tour] for help selecting the right STL files from the git repository.

| Component                                                                                                  | Quantity | Required | Notes  |
|------------------------------------------------------------------------------------------------------------|----------|----------|--------|
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front][git_base_front] | 1 | Yes    |        |
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear][git_base_rear] | 1 | Yes      |        |
| [:material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar][git_main_body_crossbar] | 1 | Yes | |
| [:material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front][git_main_body_front] | 1 | Yes | See the [tour][tour] on choosing a version to print. |
| [:material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear][git_main_body_rear] | 1 | Yes | See the [tour][tour] on choosing a version to print. |
| [:material-alpha-t-box: :material-alpha-m-box-outline: MCU Tray][git_mcu]                 | 1        | Yes      |       |
| [:material-alpha-t-box: :material-alpha-c-box-outline: CPU Tray][git_cpu]                 | 1        | See note | If unused, replace with an extra side panel. |
| [:material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays][git_lower_bay]    | 0-6      | No       | Type and quantity are specific to configuration. |
| [:material-alpha-p-box: :material-alpha-d-box-outline: Display Mount][git_display]  | 1        | Yes      |       |
| [:material-alpha-p-box: :material-alpha-l-box-outline: Lid][git_lid]                | 1-2      | Yes      | One (1) long lid or two (2) short lids. |
| [:material-alpha-p-box: :material-alpha-r-box-outline: Rear Panel][git_rear_panel]  | 1        | Yes      |       |
| [:material-alpha-p-box: :material-alpha-b-box-outline: Bottom Panel][git_bottom_panel] | 1        | Yes      |       |
| [:material-alpha-p-box: :material-alpha-s-box-outline: Side Panel][git_side_panel]  | 1        | Yes      |       |
| [:material-alpha-f-box: :material-alpha-c-box-outline: Fan Cages][git_fans]                | See note | Yes      | Quantity and size depend on configuration. |
| [:material-alpha-f-box: :material-alpha-g-box-outline: Fan Gaskets][git_fans]          | See note | No       | Quantity and size depend on configuration; pairs with a fan cage. |
| [Base Extension][git_base_extension] | 1 | See note | Required when using a Mean Well RSP-500 power supply, otherwise optional. |

[tour]: tour.md "Visual Guided Tour"