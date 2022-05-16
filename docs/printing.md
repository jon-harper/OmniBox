---
title: Printing Guide
summary: Guide to selecting and printing files for the OmniBox.
authors: Jon Harper
date: 2022-05-15
---

## Components

### General Parts

These parts form the basis of every control case.

- Base: [front][1] and [back][2]
- Main body: [front][3], [back][4], [front crossbar][5]
- Fan Cages: 2x [40mm fan cages][6]

### Customizable Parts

Be sure to pick out the right STL for your component.

- Trays for the [MCU][7] and [CPU][8]
- [Display mount][9]
- [Lid][10]
- [Rear panel][11] for exhaust, fans, and wiring connections. See below.
- A [front grill/SD card extension mount][12]
- Buck converters, SSRs, and the like can be mounted on [lower bay trays][13]

!!! note
    Templates in both Fusion and STEP format are provided for most of the case to allow customization as needed. If a STEP file is available but not a Fusion archive, this is possibly because the design was recently modified.

### Rear Panel Configuration

This is a very printer-specific file. Included are two stock `.STL` files: a typical Ender 3 or Ender 5 type printer with 5-pin ABL and 3-pin lights, and the same setup with the addition of one extra thermistor port and two extra fan ports (to be used in an enclosure). There is a template available for customization, as well.

## Print Settings

| Setting            | Value  | Note |
|--------------------|--------|------|
| Layer Height       | 0.2mm  | I have not attempted printed at any coarser a resolution than 0.2mm. I would not recommend going finer. For the main body and base, it should be possible to print at 0.24 or 0.28mm. |
| Perimeters (Walls) | 3      | Walls should be at least 1.2mm thick or screws will not grab well |
| Infill             | 20-25% | Cubic is generally a good choice. |
| Material           | PLA+   | PLA will work as well. PETG is somewhat brittle and will take longer. |
| Nozzle Diameter    | 0.4mm  | 0.6mm nozzle should work. If you print a case with a different nozzle size, please share your results! |

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