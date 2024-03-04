---
title: Rear Panel and Wiring
summary: Adding the rear panel and wiring the MCU.
authors: Jon Harper
date: 2022-11-03
steps:
  rear:
    - txt: |
        1) Put the fan inside of the cage and the gasket on top, as shown.
      img: ../img/assembly/panels/rear1.webp
      img_txt: Put the fan cage together.
    - txt: |
        2) Push the fan's wiring through the cutout at the bottom. Fasten the fan cage assembly in place with four (4) M3 x 30mm screws.
      img: ../img/assembly/panels/rear2.webp
      img_txt: Secure the fan cage assembly.
    - txt: |
        3) Fit the rear panel against the back of the case.
      img: ../img/assembly/panels/rear3.webp
      img_txt: Positon the rear panel.
    - txt: |
        4) Fasten in place using eight (8) M3 screws.
      img: ../img/assembly/panels/rear4.webp
      img_txt: Secure the panel.
---

{% import 'assembly.md' as assy %}

The rear panel and MCU wiring are next.

## Rear Panel

## Overview

{{ assy.overview_video(meta.video_folder + 'rear.mp4') }}

### Materials

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 8   |                                 |
    | M3 x 20mm SHCS            | 4   |                                 |
    | 60mm x 15mm axial fan     | 1   |                                 |
    | :material-printer-3d-nozzle: `Rear Panel - Generic USB B with Fan.stl` | 1  |  |
    | :material-printer-3d-nozzle: `6015 Fan Cage.stl` | 1  |  |
    | :material-printer-3d-nozzle: `6015 Fan Gasket.stl` | 1  | Printed with **TPU**, Optional |
=== "Generic (Stock)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm SHCS             | 8   | May substitute 10mm or 12mm.    |
    | :material-printer-3d-nozzle: `Generic No USB.stl` | 1  | Basic example. |

=== "Generic (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS             | 8   |                                 |
    | :material-printer-3d-nozzle: `Generic No USB.stl` | 1  | Basic example. |

### Directions

{{ assy.render_steps(steps.rear, '480px') }}


### Reference

[![illustration][rear_final]][rear_final]

## MCU Wiring

Before we install the display and lid, complete all remaining wiring for the MCU and any other components. The possible combinations of MCUs and printers (and their types of wiring harnesses!) are too large to fit this guide. Below are tips and links to other resources. This section will grow with time.

### Safety 

- Double-check your work.
- Be prepared to cut power instantly during both power on and testing the printer.
- **Consider safing your printer against ground faults!**
    - Grounding to earth protects in case of an electrical short.
    - This is crucial for AC-powered beds.
    - Connect your frame to the AC ground (usually a yellow or green wire, **not** the black neutral wire).
    - Do not assume your power supply case is safely earthed; always test with a multimeter.
    - [TH3D has a page with helpful videos on the subject][ground_guide].

<figure markdown>
  [![illustration][earth]{width="480"}][earth]
  <figcaption>Grounding-to-earth requires connecting your frame to this wire, directly or indirectly.</figcaption>
</figure>

### General Tips

- Connect anything in the lower bay first to avoid having to remove the MCU later.
- Double-check your work as you go.
- Label connectors with where they attach to the MCU board for easy removal and reconnection later.
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
    It is a good idea to perform initial power on tests before moving on to the next section.

[rear_final]: ../img/assembly/panels/rear_final.webp

[earth]: ../img/assembly/earth.webp
[wiring]: ../img/assembly/wiring.webp