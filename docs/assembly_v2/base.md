---
title: Base and PSU
summary: Instructions for assembling the base and PSU tray.
authors: Jon Harper
date: 2022-10-29
---

We will start by assembling the :material-alpha-c-box: :material-alpha-b-box-outline: Base and :material-alpha-t-box: :material-alpha-p-box-outline: PSU Tray.

## PSU Tray

??? note "Video Overview"
    <iframe src="https://jon-harper.github.io/OmniBox/video/psu.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M4 x 6mm machine screws   | 4   | No longer than 8mm.             |
| Compatible power supply   | 1   | Illustrated: Mean Well LRS-350-24 |
| :material-alpha-t-box: :material-alpha-p-box-outline: PSU Tray  | 1   | :material-printer-3d-nozzle: Printed, 2 files. |

### Directions

<figure markdown>
  [![illustration][psu1]{width="480"}][psu1]
  <figcaption>1. Set the power supply so that the terminals are facing away from you and oriented downwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu2]{width="480"}][psu2]
  <figcaption>2. The right PSU tray mount is marked with an 'R'. Place it against right side of the power supply with the 'R' facing upwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu3]{width="480"}][psu3]
  <figcaption>3. Use two (2) M4 screws to attach the tray mount.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu4]{width="480"}][psu4]
  <figcaption>4. Set the left tray mount against the other side of the power supply. The 'L' should face upwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu5]{width="480"}][psu5]
  <figcaption>5. Secure using two (2) M4 screws.</figcaption>
</figure>

### Finished Reference

[![illustration][psu_final]{width="640"}][psu_final]

## Prepare the Base

??? note "Video Overview"
    <iframe src="https://jon-harper.github.io/OmniBox/video/base_prep.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 8mm machine screws   | 2   |                                 |
| M3 x 16mm machine screws  | 4   | Four per fan.                   |
| 40mm x 10mm axial fan     | 0-3 | Optional, up to three.          |
| SPST toggle switch        | 1   |                                 |
| IEC C14 socket with fuse  | 1   |                                 |
| :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front | 1   | :material-printer-3d-nozzle: Printed |
| :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear  | 1   | :material-printer-3d-nozzle: Printed |

!!! note
    The [unified base][git_base_unified] replaces both the front and rear bases and requires no additional parts.

### Directions

<figure markdown>
  [![illustration][base_prep1]{width="480"}][base_prep1]
  <figcaption>1. Slide the toggle switch into the open slot on the front base. The flaps on the side compress and snap the switch in place once inserted.</figcaption>
</figure>

!!! note
    The front vents mount up to three fans. It is up to you how many fans to use; in this example we will use one (1). Repeat the next two (2) steps for any additional fans.

<figure markdown>
  [![illustration][base_prep2]{width="480"}][base_prep2]
  <figcaption>2. Place a 40mm fan against the front vent and align with the screw holes. Most users will want the airflow entering from the front.</figcaption>
</figure>

!!! note
    On most fans, the direction of airflow is towards the sticker on the motor. In this case, the sticker should face away from the vent.

!!! caution
    Once the main body is installed, the fan will press directly against the floor. If the fan wiring passes *upwards* through a strain relief notch in the fan case, the wiring will become trapped between the fan and case body. Either turn the fan 90 degrees or the remove the wiring from the strain relief notch.

<figure markdown>
  [![illustration][base_prep3]{width="480"}][base_prep3]
  <figcaption>3. Attach the fan with four (4) M3 x 16mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][base_prep4]{width="480"}][base_prep4]
  <figcaption>Insert the IEC power switch socket into the rear of the base.</figcaption>
</figure>

<figure markdown>
  [![illustration][base_prep5]{width="480"}][base_prep5]
  <figcaption>Secure with two (2) M3 x 8mm screws.</figcaption>
</figure>

### Finished Reference

[![illustration][base_prep_final]{width="640"}][base_prep_final]

## Combine Base and PSU

??? note "Video Overview"
    <iframe src="https://jon-harper.github.io/OmniBox/video/base.mp4" frameborder="0" width="100%" height="600px" allowfullscreen></iframe>

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 12mm machine screws  | 6   | Can use screws up to 20mm.      |

### Directions

<figure markdown>
  [![illustration][psu_final]{width="480"}][psu_final]
  <figcaption>Turn the PSU tray assembly so that the PSU terminals are oriented downards and away from you.</figcaption>
</figure>

<figure markdown>
  [![illustration][base1]{width="480"}][base1]
  <figcaption>Place the base pieces around the PSU tray. The edges should fit together. Note that the power supply terminals are facing downwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][base2]{width="480"}][base2]
  <figcaption>Use six (6) 12mm M3 screws to attach the base to the PSU tray.</figcaption>
</figure>

### Finished Reference

[![illustration][base_final]{width="640"}][base_final]

[psu1]: ../img/assembly/trays/psu/psu1.png
[psu2]: ../img/assembly/trays/psu/psu2.png
[psu3]: ../img/assembly/trays/psu/psu3.png
[psu4]: ../img/assembly/trays/psu/psu4.png
[psu5]: ../img/assembly/trays/psu/psu5.png
[psu_final]: ../img/assembly/trays/psu/psu_final.png
[vid_psu]: ../video/psu.mp4

[base_prep1]: ../img/assembly/core/base/base_prep1.png
[base_prep2]: ../img/assembly/core/base/base_prep2.png
[base_prep3]: ../img/assembly/core/base/base_prep3.png
[base_prep4]: ../img/assembly/core/base/base_prep4.png
[base_prep5]: ../img/assembly/core/base/base_prep5.png
[base_prep_final]: ../img/assembly/core/base/base_prep_final.png
[vid_prep]: ../video/base_prep.mp4

[base1]:        ../img/assembly/core/base/base1.png
[base2]:        ../img/assembly/core/base/base2.png
[base_final]:   ../img/assembly/core/base/base_final.png
[vid_base]: ../video/base.mp4