---
title: 0.9.10 Release (Testing)
summary: Changelog for the current and past releases of OmniBox
authors: Jon Harper
date: 2022-10-09
---

The current beta release is 0.9.10, released on 2023-XX-XX.

## New Features

### Major New Features

- Added two (2) new CPU bays for a total of four (4).
- Changed heat set insert support to M3 x 5mm x 4mm (Voron-style).

### Additional Improvements

- Crossbar version added with HSI support.
- Long lower bay trays now mount sideways.
- Numerous additional zip tie anchors, particularly to the front main body.
- Lower bay tray guides take up significantly less room.
- Added support for 12mm and 12.5mm toggle switches.

### New Hardware Support

| Hardware                          | Mount Location(s) | Notes |
|-----------------------------------|-------------------|-------|
| Creality 2.X MCUs                 | MCU Tray          |       |
| 50mm x 10mm fans                  | Any panel         | Contributed by [MaffooClock][contrib_maffooclock]. |
| FYSETC Spider                     | MCU Tray          | Contributed by [Killajoedotcom][contrib_killajoedotcom]. |
| MKS Monster8                      | MCU Tray          | Fit test needed. |
| MKS Skipr                         | MCU Tray          | Fit test needed. |
| Mean Well LRS-25-5                | Lower bay tray    | Contributed by [Mr Meh][contrib_mr_meh]. |
| BIGTREETECH 5" Pi TFT             | Display Panel     | Contributed by [MaffooClock][contrib_maffooclock]. |

## Fixes

- [Issue #91][1]: Display template is faulty
- [Issue #81][2]: Lower bay tray standoffs need a fillet
- [Issue #59][3]: Micro Fit 3 pinouts for rear panels are missing

## Documentation & Repository

- [Documentation site](https://jon-harper.github.io/OmniBox)
    - Added basic contribution information.
<!-- - Assembly Guide -->
<!-- - [Repository](https://github.com/jon-harper/OmniBox) -->
    
## Gallery


[1]: https://github.com/jon-harper/OmniBox/issues/91
[2]: https://github.com/jon-harper/OmniBox/issues/81
[3]: https://github.com/jon-harper/OmniBox/issues/59