---
title: Side Panels
summary: Installing side panels for an OmniBox.
authors: Jon Harper
date: 2024-02-28
steps:
  side_fan:
    - txt: |
        1) Orient the fan against the panel. Consider both direction of airflow and the fan's wiring.
      img: ../img/assembly/panels/side1.webp
      img_txt: Orient the fan
    - txt: |
        2) Attach the fan with four (4) M3x16mm screws.
      img: ../img/assembly/panels/side2.webp
      img_txt: Secure the fan.
    - txt: |
        2) Place the assembled side panel against the case body. Note that the top and bottom screw holes are not symmetrical. This fan will act as a second intake in the front, opposite the one on the Raspberry Pi tray.
      img: ../img/assembly/panels/side3.webp
      img_txt: Position the panel.
    - txt: |
        3) HSI: Fasten the panel with four (4) M3x6mm screws.<br>Stock: Fasten the panel with four (4) M3 x 8mm screws.
      img: ../img/assembly/panels/side4.webp
      img_txt: Fasten the panel in place.
---

{% import 'assembly.md' as assy %}

Each case has four (4) locations for a side panel. If you have a CPU tray installed, one side panel is already
occupied. In this case, you will instead need three (3) side panels.

You will need to install all of your side panels in this section. We will demonstrate the installation of a
single side panel as an example.

## Overview

{{ assy.overview_video(meta.video_folder + 'side.mp4') }}

## Materials

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 4  |                                  |
    | M3 x 16mm SHCS            | 4  |                                  |
    | 50x12mm Fan               | 1  |                                  |
    | :material-printer-3d-nozzle: `Side Panel - 50mm Fan - Grill - HSI.stl` | 1 | |
=== "As Illustrated (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS             | 4  |                                  |
    | M3 x 16mm SHCS            | 4  |                                  |
    | 50x12mm Axial Fan         | 1  |                                  |
    | :material-printer-3d-nozzle: `Side Panel - 50mm Fan - Grill - HSI.stl` | 1 | |
=== "Blank Panel (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS   | 4   |                                 |
    | :material-printer-3d-nozzle: `Side Panel V2 - Blank.stl` | 1 | |
=== "Blank Panel (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS   | 4   |                                 |
    | :material-printer-3d-nozzle: `Side Panel V2 - Blank.stl` | 1 | |

## Directions

{{ assy.render_steps(steps.side_fan, '480px') }}

## Reference

[![illustration][side_final]][side_final]

[side_final]: ../img/assembly/panels/side_final.webp