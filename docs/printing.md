---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has common settings for printing OmniBox and a printed component checklist. See the [guided tour][22] for help choosing the correct parts.

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

This is a checklist of *types* parts to print. See the [guided tour][22] for help selecting the right STL files from the git repository.

| Component                                                                                                  | Quantity | Required | Notes |
|------------------------------------------------------------------------------------------------------------|----------|----------|-------|
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front][1]             | 1        | Yes      |       |
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear][2]              | 1        | Yes      |       |
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-e-box-outline: Base - Front Extension][19]  | 1        | See note | Required when using a Mean Well RSP-500 power supply. |
| [:material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-e-box-outline: Base - Rear Extension][20]   | 1        | See note | Required when using a Mean Well RSP-500 power supply. |
| [:material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-c-box-outline: Main Body - Crossbar][3]     | 1        | Yes      |       |
| :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-f-box-outline: Main Body - Front             | 1        | Yes      | See the [tour][21] on choosing a version to print. |
| :material-alpha-c-box: :material-alpha-m-box-outline: :material-alpha-r-box-outline: Main Body - Rear              | 1        | Yes      | See the [tour][21] on choosing a version to print. |
| [:material-alpha-t-box: :material-alpha-m-box-outline: MCU Tray][7]                 | 1        | Yes      |       |
| [:material-alpha-t-box: :material-alpha-c-box-outline: CPU Tray][8]                 | 1        | See note | Blank cover plate can be used instead. |
| [:material-alpha-p-box: :material-alpha-d-box-outline: Display Mount][9]            | 1        | Yes      |       |
| [:material-alpha-p-box: :material-alpha-d-box-outline: Lid][10]                     | 1-2      | Yes      | One full-length lid or two half-length lids. |
| [:material-alpha-p-box: :material-alpha-d-box-outline: Rear Panel][11]              | 1        | Yes      |       |
| [:material-alpha-t-box: :material-alpha-l-box-outline: Lower Bay Trays][13]         | 0-4      | No       | Type and quantity are specific to configuration. |
| [:material-alpha-f-box: :material-alpha-c-box-outline: Fan Cages][6]                | See note | Yes      | Quantity and size depend on configuration. |
| [:material-alpha-f-box: :material-alpha-g-box-outline: Fan Gaskets][6]          | See note | No       | Quantity and size depend on configuration and pair with fan cages. |

[1]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front.stl              "Git: Core/Base - Front.stl"
[2]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear.stl               "Git: Core/Base - Rear.stl"
[3]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Crossbar.stl    "Git: Core/Main Body - Crossbar.stl"
[4]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20LRS-350             "Git: Core/Mean Well LRS-350/"
[5]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20RSP-500             "Git: Core/Mean Well RSP-500/"
[6]: https://github.com/jon-harper/OmniBox/tree/main/Fans                                   "Git: Fans/"
[7]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU                              "Git: Trays/MCU"
[8]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU                              "Git: Trays/CPU"
[9]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display                         "Git: Panels/Display/"
[10]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid                            "Git: Panels/Lid/"
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel                   "Git: Panels/Rear Panel/"
[12]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel                  "Git: Panels/Front Panel/"
[13]: https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay                     "Git: Panels/Lower Bay/"
[14]: https://github.com/jon-harper/OmniBox/tree/main/Core/                                 "Git: Core/"
[15]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Generic           "Git: Rear Panels/Generic/"
[16]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Custom            "Git: Rear Panels/Custom/"
[17]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Molex             "Git: Rear Panels/Molex/"
[18]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Template          "Git: Rear Panel/Template/"
[19]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front%20Extension.stl "Git: Core/Base - Front Extension.stl"
[20]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear%20Extension.stl  "Git: Core/Base - Rear Extension.stl"
[21]: tour.md#core-parts-with-variants "Visual Guided Tour: Core Parts with Variants"
[22]: tour.md "Visual Guided Tour"