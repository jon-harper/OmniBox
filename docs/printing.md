---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

This page has commonly used settings for printing OmniBox and a guide to choosing which files to print. There is a printed part checklist at the end.

## Print Settings

These settings are consistent for all parts.

| Setting            | Value       | Note |
|--------------------|-------------|------|
| Layer Height       | 0.2-0.24mm  | Adaptive layer heights can be used. Coarser settings have not been tested. |
| Perimeters (Walls) | 3           | Walls should be at least 1.2mm thick. |
| Infill             | 20-25%      | Cubic is a good tradeoff of time and durability. |
| Material           | PLA or PLA+ | PETG is somewhat brittle and may take longer to print on many printers. |
| Nozzle Diameter    | 0.4mm       | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

## Core Components

Core components form the basis of every electronics case. They can be found in the [`Core`][14] folder in the GitHub repository.

There are five (5) Core components: three (3) universal parts and two (2) that have variations.

### Universal Core Parts

These parts are required. They do not have variations.

| Part                  | Printed Qty | STL      |
|-----------------------|-------------|----------|
| Base - Front          | 1           | [STL][1] |
| Base - Rear           | 1           | [STL][2] |
| Main Body - Crossbar  | 1           | [STL][3] |

### Core Parts with Variants

Your power supply (PSU) will mount underneath the main body. The [`Core`][14] folder has one subfolder for each supported PSU.

In the next two sections, you will choose a front main body file and rear main body file. Use the files from the folder that matches your PSU model.

| Supported PSU Folder   | Commonly Found In | Notes |
|------------------------|-----------|-------|
| [Mean Well LRS-350][4] | Creality Ender 3, Ender 5 Pro, many others | Landy LRS-350 PSUs are compatible. |
| [Mean Well RSP-500][5] | Creality Ender 5 Plus | |

#### Front Main Body

The front main body comes in two variations to choose from. Print only one (1) version.

If you print the version with a 60mm intake fan, you will need to print the appropriate [fan cage][6] and (optionally) a TPU gasket.

| Variation                                | Description |
|------------------------------------------|-------------|
| `Main Body - Front with 40mm Intake.stl`  | The default version of the case with intake vents and a concealed 40mm fan. |
| `Main Body - Front with 60mm Intake.stl` | Mounts an external 60mm intake fan. |

#### Rear Main Body

The rear main body also has two variations. If you print the default version that mounts 40mm fans, you will also need to print two (2) [fan cages][6] and (optionally) TPU gaskets.

| Variation                                 | Description |
|-------------------------------------------|-------------|
| `Main Body - Rear with 40mm Exhausts.stl` | The default version with two 40mm fan exhausts. |
| `Main Body - Rear No Fans.stl`            | Optional version. Requires exhaust fan(s) on rear panel or lid. |

## Customizable Parts

The list below link to folders. You will need to choose the right `.STL` based on your configuration and preferences. Each folder has a `readme.md` with help choosing the right file and any attribution credits.

| Trays           | Qty     | Folder Link | Notes     |
|-----------------|---------|-------------|-----------|
| MCU             | 1       | [Link][7]   |           |
| CPU             | 1       | [Link][8]   |           |
| Lower bay trays | Up to 4 | [Link][14]  | Optional. |

| Panels        | Qty | Folder Link | Notes |
|---------------|-----|-------------|-------|
| Display Mount | 1   | [Link][9]   |       |
| Front Panel   | 1   | [Link][12]  |       |
| Lid           | 1-2 | [Link][10]  | See directions below. |
| Rear Panel    | 1   | [Link][11]  | See directions below. |


!!! note
    Templates in `STEP` format are provided for most of the case to allow customization as needed. Where possible, a Fusion archive file is also provided.

### Lids

There are two types of lids: full-length and half-length lids. You can either print one (1) full-length lid or two (2) half-length lids.

### Rear Panels

This is a user-specific panel with plenty of options, including making your own. The [`Rear Panel`][11] folder has multiple subfolders.

| Folder           | Description | Use If... |
|------------------|-------------|-----------|
| [`Generic`][15]  | These have large holes for passing wires through and come in a number of common variations. | ...You want a simple, off-the-shelf solution and there is not a custom panel that suits. |
| [`Custom`][16]   | Designed for users of common printer configurations. | ...Your printer has a configuration available. |
| [`Molex`][17]    | Use Molex Micro Fit 3 panel mounted connectors. Wiring diagrams for each panel are included. | ...You plan to create a wiring harness for an enclosed printer. |
| [`Template`][18] | A Fusion template with profiles for panel mounted connectors and fans. | ...You want to create your own panel. |

A more detailed guide to choosing a rear panel can be found in the [`Rear Panel`][11] README file.

## Print Checklist


| Part                  | Printed Qty | Required | Notes |
|-----------------------|-------------|----------|-------|
| Base - Front          | 1           | Yes      | |
| Base - Rear           | 1           | Yes      | |
| Main Body - Crossbar  | 1           | Yes      | |
| Main Body - Front     | 1           | Yes      | Two versions available. |
| Main Body - Rear      | 1           | Yes      | Two versions available. |
| MCU Tray              | 1           | Yes      |       |
| CPU Tray              | 1           | No       | Cover plate can be used instead. |
| Display Mount         | 1           | Yes      |       |
| Lid                   | 1-2         | Yes      | One full-length or two half-length lids. |
| Rear Panel            | 1           | Yes      |       |
| Lower Bay Trays       | 1-4         | No       | Type and quantity specific to configuration. |
| Fan Cages             | (varies)    | No       | Quantity and size depend on configuration. |
| Fan Gaskets           | (varies)    | No       | Optional; quantity and size depend on configuration. |


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