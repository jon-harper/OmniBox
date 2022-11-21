---
title: Core Assembly
summary: Instructions for assembling the Core of an OmniBox.
authors: Jon Harper
date: 2022-10-29
---

So far we have assembled the Base. Next we'll add the Main Body. This is made of front and rear pieces that fasten to one another and the Base.

## Attach the Main Body

??? overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/main_floor.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

=== "As Illustrated"

    | Parts                        | Qty | Note                            |
    |------------------------------|-----|---------------------------------|
    | #6 x 3/4" sharp point screws | 8   |                                 |
    | [:material-git: `Main Body - Front - HSI - 40mm Internal.stl`][git_main_body_front] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: `Main Body - Rear - HSI - Dual 40mm Fans.stl`][git_main_body_rear]  | 1   | :material-printer-3d-nozzle: Printed |


=== "Generic"

    | Parts                        | Qty | Note                            |
    |------------------------------|-----|---------------------------------|
    | #6 x 3/4" sharp point screws | 8   |                                 |
    | [:material-git: Main Body - Front][git_main_body_front] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: Main Body - Rear][git_main_body_rear]  | 1   | :material-printer-3d-nozzle: Printed |

### Directions

<figure markdown>
  [![illustration][main1]{width="480"}][main1]
  <figcaption>1. Set the front and rear Main Bodies over the base and the align the edges.</figcaption>
</figure>

<figure markdown>
  [![illustration][main2]{width="480"}][main2]
  <figcaption>2. Begin inserting #6 screws to the base, tightening about halfway. Before fastening each screw, check that the main body and base are still lined up.</figcaption>
</figure>

<figure markdown>
  [![illustration][main3]{width="480"}][main3]
  <figcaption>3. Continue fastening screws halfway until all eight (8) are partially inserted.</figcaption>
</figure>

!!! note "Note: Alignment"
    If inserting the screws becomes difficult, back out and check:

    - That both halves of the main body are still correctly aligned; and
    - The alignment of the screws inserted so far (i.e., that they are not canted).
    

<figure markdown>
  [![illustration][main4]{width="480"}][main4]
  <figcaption>4. Check for any alignment problems between the Base and Main Body. When satisfied, finish tightening the screws down completely.</figcaption>
</figure>

### Finished Reference

[![illustration][main_final]{width="640"}][main_final]

## Secure and Align the Center

??? overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/main_center.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 8mm machine screws   | 6   | Can use 10mm screws instead.    |

### Directions

<figure markdown>
  [![illustration][center1]{width="480"}][center1]
  <figcaption>1. Insert an M3 x 8mm screw in the top hole on one side of the rear Main Body. Fasten it to the mating hole on the front Main Body.</figcaption>
</figure>

<figure markdown>
  [![illustration][center2]{width="480"}][center2]
  <figcaption>2. Repeat with the top hole on the other side of the Main Body, again fastening from back to front.</figcaption>
</figure>

<figure markdown>
  [![illustration][center3]{width="480"}][center3]
  <figcaption>3. Use two (2) more M3 screws to fill in the bottom two screw holes on one side.</figcaption>
</figure>

<figure markdown>
  [![illustration][center4]{width="480"}][center4]
  <figcaption>4. Repeat with the final two (2) screw holes on the opposite side.</figcaption>
</figure>

### Finished Reference

[![illustration][center_final]{width="640"}][center_final]

## Add Fans

??? overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/fans.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

The illustrated examples are 40mm Internal Fan for the front and Dual 40mm Fans for the rear.

#### Front

=== "40mm Internal Fan (Illustrated)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 16mm machine screws  | 4   |                                 |
    | 40x40x10mm axial fan      | 1   |                                 |

=== "60mm External Fan"

    The linked fan cages are for a 15mm thick 60mm fan. 20mm and 25mm fans require a different cage.

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 25mm machine screws  | 4   | Use screws 10mm longer than fan depth. |
    | 60x60x15mm axial fan      | 1   |                                 |
    | [:material-git: 60mmx15mm Fan Cage][git_fans_6015] | 2 | :material-printer-3d-nozzle: Printed |
    | [:material-git: 60mmx15mm Fan Gasket][git_fans_6015] | 2 | :material-printer-3d-nozzle: Printed TPU, Optional |

#### Rear

=== "Dual 40mm Fans (Illustrated)"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 20mm machine screws  | 8   |                                 |
    | 40x40x10mm axial fan      | 2   |                                 |
    | [:material-git: 40mmx10mm Fan Cage][git_fans_4010] | 2 | :material-printer-3d-nozzle: Printed |
    | [:material-git: 40mmx10mm Fan Gasket][git_fans_4010] | 2 | :material-printer-3d-nozzle: Printed TPU, Optional |

=== "No Rear Fans"

    No additional materials are needed for this configuration.

### Directions

<figure markdown>
  [![illustration][internal_fan1]{width="480"}][internal_fan1]
  <figcaption>1. Place a 40mm fan in the Front Main Body intake. Most users will prefer the fan wires to trail off towards the rear of the case.</figcaption>
</figure>

<figure markdown>
  [![illustration][internal_fan2]{width="480"}][internal_fan2]
  <figcaption>2. Attach with M3 x 16mm screws. If using a fan that has counterbored holes, shorter screws will be needed (10-12mm).</figcaption>
</figure>

<figure markdown>
  [![illustration][external_fan1]{width="480"}][external_fan1]
  <figcaption>3. Set a 40mm fan in the external fan cage. If using a TPU gasket, cover the fan with the gasket. You may wish to cut a notch in the gasket for the fan wiring.</figcaption>
</figure>

<figure markdown>
  [![illustration][external_fan2]{width="480"}][external_fan2]
  <figcaption>4. Insert the fan wiring through the intake, then line up the fan assembly with the mounting holes.</figcaption>
</figure>

<figure markdown>
  [![illustration][external_fan3]{width="480"}][external_fan3]
  <figcaption>5. Secure the fan and cage with four (4) M3 x 20mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][external_fan4]{width="480"}][external_fan4]
  <figcaption>6. Repeat steps 3-5 for the second fan.</figcaption>
</figure>

### Finished Reference

[![illustration][external_fan_final]{width="640"}][external_fan_final]

## Attach Crossbar

??? overview
    <iframe src="https://jon-harper.github.io/OmniBox/video/0.9.9/crossbar.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials 

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 20mm machine screws  | 2   |                                 |
| Main Body - Crossbar | 1   | :material-printer-3d-nozzle: Printed |

### Directions

<figure markdown>
  [![illustration][crossbar1]{width="480"}][crossbar1]
  <figcaption>1. Hold the crossbar between the screw holes at the top of the front main body. Note that the lip should face forward.</figcaption>
</figure>

<figure markdown>
  [![illustration][crossbar2]{width="480"}][crossbar2]
  <figcaption>2. Fasten the crossbar in place with two (2) M3 x 20mm screws. Tightness can be adjusted to help square the sides of the case body.</figcaption>
</figure>

### Finished Reference

[![illustration][crossbar_final]{width="640"}][crossbar_final]

[base]:         base.md "Base Assembly"
[trays]:        trays.md "Tray Assembly"
[panels]:       panels.md "Panel Assembly"
[checklist]:    ../printing.md#print-checklist "Print Checklist"

[main1]:        ../img/assembly/core/main/main1.png
[main2]:        ../img/assembly/core/main/main2.png
[main3]:        ../img/assembly/core/main/main3.png
[main4]:        ../img/assembly/core/main/main4.png
[main_final]:   ../img/assembly/core/main/main_final.png

[center1]:      ../img/assembly/core/center/center1.png
[center2]:      ../img/assembly/core/center/center2.png
[center3]:      ../img/assembly/core/center/center3.png
[center4]:      ../img/assembly/core/center/center4.png
[center_final]: ../img/assembly/core/main/main_final.png

[internal_fan1]: ../img/assembly/core/fans/internal_fan1.png
[internal_fan2]: ../img/assembly/core/fans/internal_fan2.png
[internal_fan_final]: ../img/assembly/core/fans/internal_fan_final.png
[external_fan1]: ../img/assembly/core/fans/external_fan1.png
[external_fan2]: ../img/assembly/core/fans/external_fan2.png
[external_fan3]: ../img/assembly/core/fans/external_fan3.png
[external_fan4]: ../img/assembly/core/fans/external_fan4.png
[external_fan_final]: ../img/assembly/core/fans/external_fan_final.png

[crossbar1]:    ../img/assembly/core/crossbar/crossbar1.png
[crossbar2]:    ../img/assembly/core/crossbar/crossbar2.png
[crossbar_final]: ../img/assembly/core/crossbar/crossbar_final.png
