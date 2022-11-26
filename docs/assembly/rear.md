---
title: Rear Panel and Wiring
summary: Adding the rear panel and wiring the MCU.
authors: Jon Harper
date: 2022-11-03
---

## Rear Panel

??? overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/rear.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 8   |                                 |
    | [:material-git: Rear Panel - Generic, No USB, No Fan][git_generic_rear] | 1  | :material-printer-3d-nozzle: Printed |

=== "Generic"

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
  [![illustration][rear1]{width="480"}][rear1]
  <figcaption>1. Fit the rear panel against the back of the case.</figcaption>
</figure>

<figure markdown>
  [![illustration][rear2]{width="480"}][rear2]
  <figcaption>1. Fasten in place using eight (8) M3 screws.</figcaption>
</figure>

### Finished Reference

![illustration][rear_final]

## MCU Wiring

Before we install the lid, all remaining wiring for the MCU and any other components should be completed. The combinations of MCUs and printers (and their types of wiring harnesses!) is too large to fit this guide. Below are tips and links to other resources. This section will grow with time.

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


[rear1]: ../img/assembly/panels/rear/rear1.png
[rear2]: ../img/assembly/panels/rear/rear2.png
[rear_final]: ../img/assembly/panels/rear/rear_final.png

[earth]: ../img/assembly/earth.png
[wiring]: ../img/assembly/wiring.jpg