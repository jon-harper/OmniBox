---
title: Front Panel
summary: Assembling the front panel.
authors: Jon Harper
date: 2022-11-03
---


## Overview

<video controls="">
    <source src="https://jon-harper.github.io/OmniBox/video/0.9.9/front.mp4" type="video/mp4">
</video>

## Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | M3 x 10mm machine screws  | 2   | May substitute 12mm.            |
    | [:material-git: `Front Panel - MicroSD, Slats.stl`][git_front_sd_no_usb] | 1  | :material-printer-3d-nozzle: Printed |
    | [:material-git: `LANMU MicroSD Holder Body.stl`][git_front_sd_no_usb] | 1  | :material-printer-3d-nozzle: Printed |
    | [:material-git: `LANMU MicroSD Holder Cap.stl`][git_front_sd_no_usb] | 1  | :material-printer-3d-nozzle: Printed |
    | [:material-cart: ELECTOP MicroSD Reader Extension][bom_electop_micro_sd] | 1   | See note. |

    !!! note "Note: MicroSD Reader Extension"
        Each MCU tray entry mentions if a short (6" LANMU) or long (18" ELECTOP) reader extension is needed. The illustrated SKR 2 requires a long extension.

        The assembly process for both is identical.

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 10mm machine screws  | 2   | May substitute 12mm.            |
    | Front Panel | 1  | :material-printer-3d-nozzle: Printed |

!!! note "Note: LED Backing Panel"
    If you are using the LED backer, you will need to substitute M3 x 12mm screws in place of the two (2) M3 x 8mm.

## Directions

<figure markdown>
  [![illustration][reader1]{ width="480"}][reader1]
  <figcaption>1. Carefully pry open the outer plastic shell around the MicroSD card reader extension. Discard the shell.</figcaption>
</figure>

<figure markdown>
  <figcaption>2. (Not pictured) Place the MicroSD extension PCB in the holder body. The ribbon cable should be flush with the lip on the back of the holder.</figcaption>
</figure>

<figure markdown>
  [![illustration][front1]][front1]
  <figcaption>3. Place the holder cap on top of the extension and holder body.</figcaption>
</figure>

<figure markdown>
  [![illustration][front2]][front2]
  <figcaption>4. Use two M3 x 6mm screws to fasten the cap in place.</figcaption>
</figure>

<figure markdown>
  [![illustration][front3]{width="480"}][front3]
  <figcaption>5. Slot the assembly into the front panel. Vertical orientation does not matter.</figcaption>
</figure>

<figure markdown>
  [![illustration][front4]{width="480"}][front4]
  <figcaption>6. Secure with two (2) M3 x 6mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][front5]{width="480"}][front5]
  <figcaption>5. Push the front panel into place on the case body. Slip the SD card extension cable through first.</figcaption>
</figure>

<figure markdown>
  [![illustration][front6]{width="480"}][front6]
  <figcaption>6. Attach the panel with two (2) M3 x 10mm screws.</figcaption>
</figure>

## Reference

![illustration][front_final]

[front1]: ../img/assembly/panels/front/front1.png
[front2]: ../img/assembly/panels/front/front2.png
[front3]: ../img/assembly/panels/front/front3.png
[front4]: ../img/assembly/panels/front/front4.png
[front5]: ../img/assembly/panels/front/front5.png
[front6]: ../img/assembly/panels/front/front6.png
[front_final]: ../img/assembly/panels/front/front_final.png
[reader1]: ../img/assembly/misc/reader1.webp