---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

## Print Settings

These settings are consistent for all parts.

| Setting            | Value  | Note |
|--------------------|--------|------|
| Layer Height       | 0.2mm  | I have not attempted printed at any coarser a resolution than 0.2mm. I would not recommend going finer. For the main body and base, it should be possible to print at 0.24 or 0.28mm. |
| Perimeters (Walls) | 3      | Walls should be at least 1.2mm thick or screws will not grab well. |
| Infill             | 20-25% | Cubic is generally a good choice. |
| Material           | PLA or PLA+   | PETG is somewhat brittle and will take longer to print. |
| Nozzle Diameter    | 0.4mm  | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

## Components

### Core Parts

These parts form the basis of every control case and can be found in the [`Core`][14] folder in the GitHub repository. You will need to print one (1) of each.

- [Base - Front][1]
- [Base - Rear][2]
- [Main Body - Front][3]
- [Main Body - Front crossbar][5]

### Rear Main Body

The rear main body is part of the [`Core`][14] parts, but comes in two versions. The default has two 40mm fan cutouts with optional TPU gaskets.

Alternatively, there is a rear main body that lacks fan cutouts. This should *only* be used if you are using a customized rear panel that mounts a 60mm or larger fan.

**With Fans**:

- 1x [Main Body - Rear][4]
- 2x [40mm fan cages][6]
- (Optional) 2x [40mm TPU gaskets][16]

**Without Fans**

- 1x [Main Body - Rear No Fans][17]

### Customizable Parts

The list below link to repository folders. You will need to choose the right `.STL` based on your configuration and preferences. Some folders have a `readme.md` file that offers additional information or attribution.

You will only need to print one (1) of each of these.

- Trays:
    - [MCU][7]
    - [CPU][8]
    - [Lower bay trays][13] for buck converters, SSRs, etc.
- Panels:
    - [Display mount][9]
    - [Lid][10]
    - [Rear panel][11] (*see below*)
    - [Front grill/SD card extension mount][12]

!!! note
    Templates in `STEP` format are provided for most of the case to allow customization as needed. Where possible, a Fusion archive file is also provided.

### Rear Panel Configuration

This is a very user-specific panel and the most customizable part of the case. The [`Rear Panel`][11] has multiple subfolders.

- Most users will want to use a `Generic` panel. These have large holes for passing wires through and come in a number of common variations.
- The `Molex` folder contains files for preconfigured rear panels that mount Molex Micro Fit 3 connectors. Wiring diagrams for each panel are included.
- The `Template` folder contains a Fusion template with profiles for panel mounted connectors and fans. Users who want to create their own panel should start here.

A more detailed guide to choosing a rear panel can be found in the [`Rear Panel`][11] README file.

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