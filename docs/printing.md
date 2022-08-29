---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has commonly used settings for printing OmniBox and a printed part checklist. See the [guided tour](tour.md) for help choosing the correct parts.

## Print Settings

These settings are consistent for all parts.

| Setting            | Value       | Note |
|--------------------|-------------|------|
| Layer Height       | 0.2-0.24mm  | Adaptive layer heights can be used. Coarser settings have not been tested. |
| Perimeters (Walls) | 3           | Walls should be at least 1.2mm thick. |
| Infill             | 20-25%      | Cubic is a good tradeoff of time and durability. |
| Material           | PLA or PLA+ | PETG is somewhat brittle and may take longer to print on many printers. |
| Nozzle Diameter    | 0.4mm       | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

## Print Checklist

This is a checklist of parts to print. Most of these parts have variations; see the [guided tour](tour.md) for help selecting the right STL files from the git repository.

| Component                                                                                                  | Quantity | Required | Notes |
|------------------------------------------------------------------------------------------------------------|----------|----------|-------|
| [:material-alpha-c-box-outline: :material-alpha-b-box: :material-alpha-f-box: Base - Front][1]             | 1        | Yes      |       |
| [:material-alpha-c-box-outline: :material-alpha-b-box: :material-alpha-r-box: Base - Rear][2]              | 1        | Yes      |       |
| [:material-alpha-c-box-outline: :material-alpha-b-box: :material-alpha-e-box: Base - Front Extension][19]  | 1        | See note | Required when using a Mean Well RSP-500 power supply. |
| [:material-alpha-c-box-outline: :material-alpha-b-box: :material-alpha-e-box: Base - Rear Extension][20]   | 1        | See note | Required when using a Mean Well RSP-500 power supply. |
| [:material-alpha-c-box-outline: :material-alpha-m-box: :material-alpha-c-box: Main Body - Crossbar][3]     | 1        | Yes      |       |
| :material-alpha-c-box-outline: :material-alpha-m-box: :material-alpha-f-box: Main Body - Front             | 1        | Yes      | See the [tour][21] on choosing a version to print. |
| :material-alpha-c-box-outline: :material-alpha-m-box: :material-alpha-r-box: Main Body - Rear              | 1        | Yes      | See the [tour][21] on choosing a version to print. |
| [:material-alpha-t-box-outline: :material-alpha-m-box: MCU Tray][7]                 | 1        | Yes      |       |
| [:material-alpha-t-box-outline: :material-alpha-c-box: CPU Tray][8]                 | 1        | No       | Blank cover plate can be used instead. |
| [:material-alpha-p-box-outline: :material-alpha-d-box: Display Mount][9]            | 1        | Yes      |       |
| [:material-alpha-p-box-outline: :material-alpha-d-box: Lid][10]                     | 1-2      | Yes      | One full-length lid or two half-length lids. |
| [:material-alpha-p-box-outline: :material-alpha-d-box: Rear Panel][11]              | 1        | Yes      |       |
| [:material-alpha-t-box-outline: :material-alpha-l-box: Lower Bay Trays][13]         | 0-4      | See note | Type and quantity are specific to configuration. |
| [:material-alpha-f-box-outline: :material-alpha-c-box: Fan Cages][6]                | See note | Yes      | Quantity and size depend on configuration. |
| [:material-alpha-f-box-outline: :material-alpha-g-box: Fan Gaskets][6]          | See note | No       | Quantity and size depend on configuration and pair with fan cages. |

[1]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front.stl
[2]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear.stl
[3]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Crossbar.stl
[4]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20LRS-350
[5]: https://github.com/jon-harper/OmniBox/tree/main/Core/Mean%20Well%20RSP-500
[6]: https://github.com/jon-harper/OmniBox/tree/main/Fan%20Cages
[7]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU
[8]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[9]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[10]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel
[12]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel
[13]: https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay
[14]: https://github.com/jon-harper/OmniBox/tree/main/Core/
[15]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Generic
[16]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Custom
[17]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Molex
[18]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel/Template
[19]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front%20Extension.stl
[20]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear%20Extension.stl
[21]: tour.md#core-parts-with-variants