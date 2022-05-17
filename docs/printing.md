---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

## Components

### General Parts

These parts form the basis of every control case.

- Base: 
    - [Front][1]
    - [Back][2]
- Main body:
    - [Front][3]
    - [Back][4]
    - [Front crossbar][5]
    - 2x [40mm fan cages][6]

### Customizable Parts

The list below link to repository folders. You will need to choose the right `.STL` based on your configuration and preferences.

- Trays:
    - [MCU][7]
    - [CPU][8]
    - [Lower bay trays][13] for buck converters, SSRs, etc.
- [Display mount][9]
- [Lid][10]
- [Rear panel][11] (see below)
- [Front grill/SD card extension mount][12]

!!! note
    Templates in both Fusion and STEP format are provided for most of the case to allow customization as needed. If a STEP file is available but not a Fusion archive, this is possibly because the design was recently modified.

### Rear Panel Configuration

This is a very user-specific file. Included are two stock `.STL` files. Both are for a typical Ender 3/Ender 5 type printer with 5-pin ABL and 3-pin lights; the `Enclosed Ender` file has an additional thermistor port and two extra fan ports.

There is a template available for customization, as well.

## Print Settings

| Setting            | Value  | Note |
|--------------------|--------|------|
| Layer Height       | 0.2mm  | I have not attempted printed at any coarser a resolution than 0.2mm. I would not recommend going finer. For the main body and base, it should be possible to print at 0.24 or 0.28mm. |
| Perimeters (Walls) | 3      | Walls should be at least 1.2mm thick or screws will not grab well. |
| Infill             | 20-25% | Cubic is generally a good choice. |
| Material           | PLA+   | PETG is somewhat brittle and will take longer to print. |
| Nozzle Diameter    | 0.4mm  | 0.6mm should also work. If you print a case with a different nozzle size, please share your results! |

[1]: https://github.com/jon-harper/OmniBox/blob/main/Base/Base%20-%20Front.stl
[2]: https://github.com/jon-harper/OmniBox/blob/main/Base/Base%20-%20Back.stl
[3]: https://github.com/jon-harper/OmniBox/blob/main/Main%20Body/Main%20Body%20-%20Front.stl
[4]: https://github.com/jon-harper/OmniBox/blob/main/Main%20Body/Main%20Body%20-%20Rear.stl
[5]: https://github.com/jon-harper/OmniBox/blob/main/Main%20Body/Main%20Body%20-%20Front%20Crossbar.stl
[6]: https://github.com/jon-harper/OmniBox/blob/main/Main%20Body/40mm%20Fan%20Cage.stl
[7]: https://github.com/jon-harper/OmniBox/tree/main/MCU
[8]: https://github.com/jon-harper/OmniBox/tree/main/CPU
[9]: https://github.com/jon-harper/OmniBox/tree/main/Display
[10]: https://github.com/jon-harper/OmniBox/tree/main/Lid
[11]: https://github.com/jon-harper/OmniBox/tree/main/Rear%20Panel
[12]: https://github.com/jon-harper/OmniBox/tree/main/Front%20Panel
[13]: https://github.com/jon-harper/OmniBox/tree/main/Lower%20Bay