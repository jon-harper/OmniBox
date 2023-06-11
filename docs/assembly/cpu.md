---
title: CPU
summary: Instructions and considerations when installing the CPU Tray.
authors: Jon Harper
date: 2022-10-30
---

This section is optional. If you are not using a SoC CPU like a Raspberry Pi, use a second [side panel][side] in the next assembly section.

## Overview

<video controls="">
    <source src="https://jon-harper.github.io/OmniBox/video/0.9.9/cpu.mp4" type="video/mp4">
</video>

## Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 8mm machine screws   | 4   | May substitute 10mm or 12mm.    |
    | Raspberry Pi 4B           | 1   |                                 |
    | [:material-git: Raspberry Pi 4B CPU Tray][git_rpi_4b] | 1   | :material-printer-3d-nozzle: Printed |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 4   | May substitute 10mm or 12mm.    |
    | M3 x 6mm machine screws   | N/A | Most SoC CPUs use four (4).     |
    | Compatible SoC CPU        | 1   |                                 |
    | CPU Tray | 1   | :material-printer-3d-nozzle: Printed |
    
## Directions
                                                            
<figure markdown>
  [![illustration][cpu1]{width="480"}][cpu1]
  <figcaption>1. Set the Raspberry Pi on the tray and slide it forward into the side panel.</figcaption>
</figure>

<figure markdown>
  [![illustration][cpu2]{width="480"}][cpu2]
  <figcaption>2. Fasten with four (4) M3 x 6mm screws. The holes are for M2.5 screws but will bore out easily for M3 screws.<figcaption>
</figure>

<figure markdown>
  [![illustration][cpu3]{width="480"}][cpu3]
  <figcaption>3. Slide the CPU into the case. In this example, we use the right CPU bay.</figcaption>
</figure>

<figure markdown>
  [![illustration][cpu4]{width="480"}][cpu4]
  <figcaption>4. Secure with four (4) M3 x 8mm screws.</figcaption>
</figure>

## Reference

![illustration][cpu_final]

[side]: side.md

[cpu1]: ../img/assembly/trays/cpu/cpu1.png
[cpu2]: ../img/assembly/trays/cpu/cpu2.png
[cpu3]: ../img/assembly/trays/cpu/cpu3.png
[cpu4]: ../img/assembly/trays/cpu/cpu4.png
[cpu_final]: ../img/assembly/trays/cpu/cpu_final.png
[vid_cpu]: ../video/cpu.mp4