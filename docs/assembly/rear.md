---
title: Rear Panel and Wiring
summary: Adding the rear panel and wiring the MCU.
authors: Jon Harper
date: 2022-11-03
---

We are close to completion, so the rear panel and MCU wiring are next.

## Rear Panel

## Overview

<video controls="">
    <source src="{{meta.video_folder}}rear.mp4" type="video/mp4">
</video>

### Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 8   |                                 |
    | M3 x 25mm machine screws  | 4   |                                 |
    | 60mm x 15mm axial fan     | 1   |                                 |
    | [:material-git: `Generic No USB with Fan.stl`][git_generic_rear] | 1  | :material-printer-3d-nozzle: Printed |
    | [:material-git: `6015 Fan Cage.stl`][git_fans_6015] | 1 | :material-printer-3d-nozzle: Printed |
    | [:material-git: `6015 Fan Gasket.stl`][git_fans_6015] | 1 | :material-printer-3d-nozzle: Printed **TPU**, optional |

=== "Stock"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 8   | May substitute 10mm or 12mm.    |
    | Rear Panel                | 1  | :material-printer-3d-nozzle: Printed |

=== "HSI"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 8   |                                 |
    | Rear Panel                | 1   | :material-printer-3d-nozzle: Printed |

### Directions

<figure markdown>
  [![illustration][fan1]{width="480"}][fan1]
  <figcaption>1. Put the fan, cage, and gasket together as shown.</figcaption>
</figure>

<figure markdown>
  [![illustration][fan2]{width="480"}][fan2]
  <figcaption>1. Push the fan's wiring through the cutout at the bottom. Fasten the fan cage assembly in place with four (4) M3 x 30mm screws.</figcaption>
</figure>
                                                            
<figure markdown>
  [![illustration][rear1]{width="480"}][rear1]
  <figcaption>1. Fit the rear panel against the back of the case.</figcaption>
</figure>

<figure markdown>
  [![illustration][rear2]{width="480"}][rear2]
  <figcaption>1. Fasten in place using eight (8) M3 screws.</figcaption>
</figure>

### Reference

[![illustration][rear_final]][rear_final]

## MCU Wiring

Before we install the display and lid, complete all remaining wiring for the MCU and any other components. The possible combinations of MCUs and printers (and their types of wiring harnesses!) are too large to fit this guide. Below are tips and links to other resources. This section will grow with time.

### Safety 

- Double-check your work.
- Be prepared to cut power instantly during both power on and testing the printer.
- **Consider safing your printer against ground faults!**
    - Grounding to earth protects in case of a number of issues, e.g., a short in the bed touching the frame.
    - This is very important for AC-powered beds.
    - Connect your frame to the AC ground (usually a yellow or green wire, **not** the black neutral wire).
    - Do not assume your power supply case is safely earthed—test with a multimeter.
    - [TH3D has a page with helpful videos on the subject][ground_guide].

<figure markdown>
  [![illustration][earth]{width="480"}][earth]
  <figcaption>Grounding-to-earth requires connecting your frame to this wire, directly or indirectly.</figcaption>
</figure>

### General Tips

- Double-check your work as you go.
- Label connectors with where they attach to the MCU board for easy removal and reconnection later (e.g., `TB` for the bed thermistor header).
- Check connector pins:
    - Many connector pins are not designed for frequent removal: wires may pull free from the pin or pin from the connector.
    - Pin can become damaged or come loose during removal.
    - JST XH connectors are particularly prone to pin issues (usually used for fans, thermistors, and endstops).
- Zip tie anchors:
    - The zip tie anchors in the sides of the case are helpful for securing longer wires.
    - If you are crimping your own wires, extra length can be used to keep the wiring clean.

<figure markdown>
  [![illustration][wiring]{width="480"}][wiring]
  <figcaption>Ex: Each connector is labeled and zip-tied out of the way.</figcaption>
</figure>

!!! tip "Before Continuing"
    It is a good idea to perform initial power on tests now.

[fan1]: ../img/assembly/panels/rear/fan1.webp
[fan2]: ../img/assembly/panels/rear/fan2.webp
[rear1]: ../img/assembly/panels/rear/rear1.webp
[rear2]: ../img/assembly/panels/rear/rear2.webp
[rear_final]: ../img/assembly/panels/rear/rear_final.webp

[earth]: ../img/assembly/earth.webp
[wiring]: ../img/assembly/wiring.webp