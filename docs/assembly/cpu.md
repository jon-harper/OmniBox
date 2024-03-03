---
title: CPU
summary: Instructions and considerations when installing the CPU Tray.
authors: Jon Harper
date: 2024-02-28
steps:
  cpu:
    - txt: |
        1) Orient the 40mm fan. Take into account both airflow direction and the location of the fan's wiring.
      img: ../img/assembly/trays/cpu1.webp
      img_txt: Position the fan.
    - txt: |
        2) Fasten the fan in place with four (4) M3 x 15mm screws.
      img: ../img/assembly/trays/cpu2.webp
      img_txt: Secure the fan.
    - txt: |
        3) Place the Raspberry Pi on the CPU tray with the headers facing away from the fan.
      img: ../img/assembly/trays/cpu3.webp
      img_txt: Orient the Raspberry Pi.
    - txt: |
        4) Fasten with four (4) M3 x 6mm screws. The holes are for M2.5 screws but will bore out easily for M3 screws.
      img: ../img/assembly/trays/cpu4.webp
      img_txt: Secure the Raspberry Pi.
    - txt: |
        5) Slide the assembly into the case. The front CPU bays offer more room for connectors, but any CPU bay work.
      img: ../img/assembly/trays/cpu5.webp
      img_txt: Insert the CPU tray.
    - txt: |
        6) Install with four screws.<br>HSI: M3 x 6mm<br>Stock: M3 x 8mm
      img: ../img/assembly/trays/cpu6.webp
      img_txt: Secure the tray.
---

{% import 'assembly.md' as assy %}

This section is optional. If you are not using a SoC CPU like a Raspberry Pi, use a fourth [side panel][side] in that assembly section.

## Overview

{{ assy.overview_video(meta.video_folder + 'cpu.mp4') }}

## Materials

=== "As Illustrated (HSI)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 8   |                                 |
    | M3 x 15mm machine screws  | 4   | May substitute 14mm.            |
    | Raspberry Pi 4B           | 1   |                                 |
    | 40mm x 10mm Axial Fan     | 1   |                                 |
    | :material-printer-3d-nozzle: `RPi Universal Tray w 40mm Fan - HSI.stl` | 1 | |

=== "Stock"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 8mm machine screws   | 4   |                                 |
    | M3 x 15mm machine screws  | 4   | May substitute 14mm.            |
    | 40mm x 10mm Axial Fan     | 1   |                                 |
    | Compatible SoC CPU        | 1   |                                 |
    | :material-printer-3d-nozzle: `RPi Universal Tray with 40mm Fan.stl` | 1 | |

!!! warning "Warning: M3 x 16mm screws"
    If you must use M3 x 16mm screws for the 40mm fan, *do not overtighten* or you may deform the outer panel surface.

## Directions
                                                            
{{ assy.render_steps(steps.cpu, '480px') }}

## Reference

[![illustration][cpu_final]][cpu_final]

[side]: side.md

[cpu_final]: ../img/assembly/trays/cpu_final.webp