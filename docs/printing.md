---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

## Print Settings

These settings are consistent for all parts.

| Setting            | Value       | Note |
|--------------------|-------------|------|
| Layer Height       | 0.2-0.24mm  | I would not recommend going finer; I have not tried 0.28 or coarser. |
| Perimeters (Walls) | 3           | Walls should be at least 1.2mm thick or screws will not grab well. |
| Infill             | 20-25%      | Cubic is generally a good choice. |
| Material           | PLA or PLA+ | PETG is somewhat brittle and will take longer to print. |
| Nozzle Diameter    | 0.4mm       | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

## Components

### Core Parts

These parts form the basis of every control case and can be found in the [`Core`][14] folder in the GitHub repository.

You will need to print the following:

- 1x [Base - Front][1]
- 1x [Base - Rear][2]
- 1x [Main Body - Front][3]
- 1x [Main Body - Front crossbar][5]

### Rear Main Body

The rear main body is part of the [`Core`][14] parts, but comes in two versions. The default has two 40mm fan cutouts with optional TPU gaskets.

Alternatively, there is a rear main body that lacks fan cutouts. *Only* use the rear body without fans if you are using a rear panel that mounts a 60mm or larger fan.

You will need to print one of the following two lists:

**Default**:

- 1x [Main Body - Rear][4]
- 2x [40mm fan cages][6]
- (Optional) 2x [40mm TPU gaskets][16]

**Without Fans**

- 1x [Main Body - Rear No Fans][17]

### Customizable Parts

The list below link to repository folders. You will need to choose the right `.STL` based on your configuration and preferences. Each folder has a `readme.md` with help choosing the right file and any attribution.

- Trays:
    - 1x [MCU][7]
    - 1x [CPU][8]
    - (Optional) 2x [Lower bay trays][13] for buck converters, SSRs, etc.
- Panels:
    - 1x [Display mount][9]
    - 1x [Lid][10]
    - 1x [Rear panel][11] (*see below*)
    - 1x [Front panel][12]

!!! note
    Templates in `STEP` format are provided for most of the case to allow customization as needed. Where possible, a Fusion archive file is also provided.

### Rear Panel Configuration

This is a very user-specific panel and the most customizable part of the case. The [`Rear Panel`][11] has multiple subfolders.

- Most users will want to use a `Generic` panel. These have large holes for passing wires through and come in a number of common variations.
- The `Molex` folder contains files for preconfigured rear panels that mount Molex Micro Fit 3 connectors. Wiring diagrams for each panel are included.
- The `Template` folder contains a Fusion template with profiles for panel mounted connectors and fans. Users who want to create their own panel should start here.

A more detailed guide to choosing a rear panel can be found in the [`Rear Panel`][11] README file.

## Print Checklist

| Part                       | Qty | Required  | Notes |
|----------------------------|-----|-----------|-------|
| Base - Front               | 1   | Yes       |       |
| Base - Rear                | 1   | Yes       |       |
| Main Body - Front          | 1   | Yes       |       |
| Main Body - Front crossbar | 1   | Yes       |       |
| Main Body - Rear           | 1   | Yes       | Default or Without Fans |
| MCU Tray                   | 1   | Yes       |       |
| CPU Tray                   | 1   | Yes       | Cover plate can be used instead |
| Display Mount              | 1   | Yes       |       |
| Lid                        | 1   | Yes       |       |
| Rear Panel                 | 1   | Yes
| 40mm fan cages             | 2   | Maybe     | Required if using the Default Main Body |
| 40mm TPU gaskets           | 2   | No        |       |
| Lower Bay Trays            | 2   | No        |       |

[1]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front.stl
[2]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear.stl
[3]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Front.stl
[4]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Rear.stl
[5]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Front%20Crossbar.stl
[6]: https://github.com/jon-harper/OmniBox/blob/main/Core/40mm%20Fan%20Cage.stl
[7]: https://github.com/jon-harper/OmniBox/tree/main/Trays/MCU
[8]: https://github.com/jon-harper/OmniBox/tree/main/Trays/CPU
[9]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Display
[10]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Lid
[11]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Rear%20Panel
[12]: https://github.com/jon-harper/OmniBox/tree/main/Panels/Front%20Panel
[13]: https://github.com/jon-harper/OmniBox/tree/main/Trays/Lower%20Bay
[14]: https://github.com/jon-harper/OmniBox/tree/main/Core/
[15]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Rear%20Panel/Rear%20Panel%20-%20Enclosed%20Ender.stl
[16]: https://github.com/jon-harper/OmniBox/blob/main/Panels/Rear%20Panel/40mm%20TPU%20Fan%20Gasket.stl 
[17]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Rear%20No%20Fans.stl