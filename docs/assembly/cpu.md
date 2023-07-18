---
title: CPU
summary: Instructions and considerations when installing the CPU Tray.
authors: Jon Harper
date: 2022-10-30
---

This section is optional. If you are not using a SoC CPU like a Raspberry Pi, use a second [side panel][side] in the next assembly section.

## Overview

<video controls="">
    <source src="{{meta.video_folder}}cpu.mp4" type="video/mp4">
</video>

## Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 8mm machine screws   | 4   | May substitute 10mm or 12mm.    |
    | M3 x 15mm machine screws  | 4   | May substitute 16mm.            |
    | Raspberry Pi 4B           | 1   |                                 |
    | 40mm x 10mm Axial Fan     | 1   |                                 |
    | Assembled SPI cable       | 1   |                                 | 
    | [:material-git: Universal Raspberry Pi CPU Tray][git_rpi_universal] | 1   | :material-printer-3d-nozzle: Printed |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 4   | May substitute 10mm or 12mm.    |
    | M3 x 6mm machine screws   | N/A | Most SoC CPUs use four (4).     |
    | Compatible SoC CPU        | 1   |                                 |
    | [:material-git: CPU Tray][git_cpu] | 1   | :material-printer-3d-nozzle: Printed |

!!! warning "Warning: M3 x 16mm screws"
    If using M3 x 16mm screws for the 40mm fan, *do not overtighten* or you may deform the outer panel surface.

!!! note "Note: Micro Fit 3 Connector"
    The illustrated CPU tray has a cutout for a 2 Row, 6-position Molex Micro Fit 3 connector. This cutout can be wired to connect devices to the SoC CPU, such as an accelerometer.

    Assembling and wiring this cable is beyond the scope of this guide, but the cable can be made from DuPont-terminated breadboard wires.
## Directions
                                                            
<figure markdown>
  [![illustration][cpu1]{width="480"}][cpu1]
  <figcaption>1. Orient the 40mm fan and fasten with four (4) M3 x 15mm screws. If substituting with 16mm screws *do not overtighten.</figcaption>
</figure>

<figure markdown>
  [![illustration][cpu2]{width="480"}][cpu2]
  <figcaption>2. Place the Raspberry Pi on the tray. The headers should face away from the fan.<figcaption>
</figure>

<figure markdown>
  [![illustration][cpu3]{width="480"}][cpu3]
  <figcaption>3. Fasten with four (4) M3 x 6mm screws. The holes are for M2.5 screws but will bore out easily for M3 screws.<figcaption>
</figure>

<figure markdown>
  <figcaption>4. (Not pictured) Connect the SPI cable to the Raspberry Pi. Make sure you double-check the pins are in the right position. <figcaption>
</figure>

<figure markdown>
  [![illustration][cpu4]{width="480"}][cpu4]
  <figcaption>5. Snap the Micro Fit 3 connector into the CPU tray panel.<figcaption>
</figure>


<figure markdown>
  [![illustration][cpu5]{width="480"}][cpu5]
  <figcaption>6. Slide the CPU into the case. In this example, we use the front right CPU bay.</figcaption>
</figure>

<figure markdown>
  [![illustration][cpu6]{width="480"}][cpu6]
  <figcaption>7. Secure with four (4) M3 x 8mm screws.</figcaption>
</figure>

## Reference

![illustration][cpu_final]

[side]: side.md

[cpu1]: ../img/assembly/trays/cpu/cpu1.webp
[cpu2]: ../img/assembly/trays/cpu/cpu2.webp
[cpu3]: ../img/assembly/trays/cpu/cpu3.webp
[cpu4]: ../img/assembly/trays/cpu/cpu4.webp
[cpu5]: ../img/assembly/trays/cpu/cpu5.webp
[cpu6]: ../img/assembly/trays/cpu/cpu6.webp
[cpu_final]: ../img/assembly/trays/cpu/cpu_final.webp
[vid_cpu]: ../video/cpu.mp4