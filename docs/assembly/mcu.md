---
title: MCU Tray
summary: Instructions for installing the MCU tray.
authors: Jon Harper
date: 2024-02-29
steps:
  mcu:
    - txt: |
        1. Place your MCU on the tray and align the mounting holes.
      img: todo
      img_txt: Position the MCU.
    - txt: |
        2. Use four (4) 6mm screws to secure the MCU.
      img: todo
      img_txt: Attach the MCU.
    - txt: |
        3. Set the MCU tray on the pillars in the case. The board's power connectors should orient to the back of the case or to the side.
      img: todo
      img_txt: Position the MCU tray.
    - txt: |
        4. Fasten the tray with four (4) M3 x 6mm screws.
      img: todo
      img_txt: Attach the tray.
---

{% import 'assembly.md' as assy %}

## MCU Installation

###  Overview

{{ assy.overview_video(meta.video_folder + 'mcu.mp4') }}

### Materials

=== "As Illustrated (HSI)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 8   |                                 |
    | BIGTREETECH SKR 2         | 1   |                                 |
    | :material-printer-3d-nozzle: `MCU Tray - BTT SKR v2 - HSI.stl` | 1 | |

=== "As Illustrated (Stock)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 8mm machine screws   | 4   |                                 |
    | BIGTREETECH SKR 2         | 1   |                                 |
    | :material-printer-3d-nozzle: `MCU Tray - BTT SKR v2.stl` | 1 |    |

### Directions

!!! important
    Larger trays (e.g. the BIGTREETECH Octopus series or the Manta M8P) will only fit in the case if the
    board is oriented one way, as the trays are not symmetrical. Check which direction fits in the case
    before securing the MCU to the tray.

{{ assy.render_steps(steps.mcu, '480px') }}

### Reference

[![illustration][mcu_final]][mcu_final]
