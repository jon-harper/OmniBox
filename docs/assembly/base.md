---
title: Base and PSU
summary: Instructions for assembling the base and PSU tray.
authors: Jon Harper
date: 2022-10-29
---

Assembly of the case starts with the Base and PSU Tray.

## PSU Tray

??? overview
    <video controls="">
        <source src="{{meta.video_folder}}psu.mp4" type="video/mp4">
    </video>

### Materials

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M4 x 6mm machine screws   | 4   | No longer than 8mm.             |
    | Mean Well LRS-350-24      | 1   |                                 |
    | [:material-git: PSU Tray][git_psu_lrs350]  | 1   | :material-printer-3d-nozzle: Printed, 2 files. |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M4 x 6mm machine screws   | 4-8 | No longer than 8mm.             |
    | Compatible power supply   | 1   |  |
    | PSU Tray                  | 1   | :material-printer-3d-nozzle: Printed, 2 files. |

### Directions

<figure markdown>
  [![illustration][psu1]{width="480"}][psu1]
  <figcaption>1. Set the power supply with the terminals are facing downwards and away from you.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu2]{width="480"}][psu2]
  <figcaption>2. Place the right PSU tray mount against the right side of the power supply. The printed 'R' should face upwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu3]{width="480"}][psu3]
  <figcaption>3. Use two (2) M4 screws to attach the tray mount.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu4]{width="480"}][psu4]
  <figcaption>4. Set the left tray mount against the opposite side of the power supply. The 'L' should face upwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][psu5]{width="480"}][psu5]
  <figcaption>5. Secure using two (2) M4 screws.</figcaption>
</figure>

### Reference

[![illustration][psu_final]{width="640"}][psu_final]

## Prepare the Base

??? overview
    <video controls="">
        <source src="{{meta.video_folder}}base_prep.mp4" type="video/mp4">
    </video>

### Materials

=== "As Illustrated"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 2   |                                 |
    | M3 x 16mm machine screws  | 4   | Four per fan.                   |
    | 40mm x 10mm axial fan     | 1   | Optional, up to three.          |
    | SPST rocker switch        | 1   |                                 |
    | IEC C14 socket with fuse holder | 1   |                           |
    | Fuse, Glass, 5x20mm, Fast Blow | 1 | |                            |
    | [:material-git: `Base - Front.stl`][git_base_front] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: `Base - Rear - HSI.stl`][git_base_rear]  | 1   | :material-printer-3d-nozzle: Printed |

=== "Generic"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 2   |                                 |
    | SPST toggle switch        | 1   |                                 |
    | IEC C14 socket with fuse holder | 1   |                           |
    | Fuse, Glass, 5x20mm, Fast Blow | 1 | |                            |
    | [:material-git: Base - Front][git_base_front] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: Base - Rear][git_base_rear]  | 1   | :material-printer-3d-nozzle: Printed |

!!! note "Note: Unified Base"
    The [:material-git: unified base][git_base_unified] replaces both the front and rear bases and requires no additional parts.

### Directions

<figure markdown>
  [![illustration][base_prep1]{width="480"}][base_prep1]
  <figcaption>1. Slide the toggle switch into the open slot on the front base. The flaps on the side compress and snap the switch in place once inserted.</figcaption>
</figure>

!!! note
    The front vents mount up to three fans. In this example we will use one (1). 
    
    Repeat the next two (2) steps for any additional fans.

!!! caution
    The fan(s) will press directly against the floor of the main body once it is installed. If the wiring passes upwards through a strain relief notch in the fan case, the wires will be trapped between the fan and case body. Either turn the fan 90 degrees or the remove the wiring from the strain relief notch.

<figure markdown>
  [![illustration][base_prep2]{width="480"}][base_prep2]
  <figcaption>2. Place a 40mm fan against the front vent. Most users will need this as an exhaust.</figcaption>
</figure>

!!! note "Note: Airflow Direction"
    The direction of airflow for most fans is towards base of the motor. Most fans have a sticker on this side of the motor. In this case, the sticker should face towards the vent.

<figure markdown>
  [![illustration][base_prep3]{width="480"}][base_prep3]
  <figcaption>3. Attach the fan with four (4) M3 x 16mm screws.</figcaption>
</figure>

!!! important "Important: Screw Lengths"
    The holes for internally mounted fans are 6mm deep. Screws should never be longer than 16mm for a 40mm x 10mm fan.

    If your fan has a counterbore for the screw head, use a 10mm or 12mm screw instead.

!!! note
    The next two steps are necessary if:

    - The IEC socket does not have a fuse; or
    - The IEC socket has a fuse of the wrong capacity for your configuration.

    [This guide][fuse_guide] can help get you started. Consult with a professional if uncertain what capacity fuse you should use.

<figure markdown>
  ![illustration][iec1]
  <figcaption>4. Slide out the fuse holder cover.</figcaption>
</figure>

<figure markdown>
  ![illustration][iec2]
  <figcaption>5. Insert a fuse into the fuse holder. If necessary, remove the fuse that came with the socket.</figcaption>
</figure>

<figure markdown>
  [![illustration][base_prep4]{width="480"}][base_prep4]
  <figcaption>6. Replace the cover and slide the power switch socket into the rear of the base.</figcaption>
</figure>

<figure markdown>
  [![illustration][base_prep5]{width="480"}][base_prep5]
  <figcaption>7. Secure with two (2) M3 x 8mm screws.</figcaption>
</figure>

### Reference

[![illustration][base_prep_final]{width="640"}][base_prep_final]

## Combine Base and PSU

??? overview
    <video controls="">
        <source src="{{meta.video_folder}}base.mp4" type="video/mp4">
    </video>

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 12mm machine screws  | 8   |                                 |

### Directions

<figure markdown>
  [![illustration][psu_final]{width="480"}][psu_final]
  <figcaption>1. Turn the PSU tray assembly so that the PSU terminals are oriented downards and away from you.</figcaption>
</figure>

<figure markdown>
  [![illustration][base1]{width="480"}][base1]
  <figcaption>2. Place the base pieces around the PSU tray. The edges should fit together. Note that the power supply terminals are facing downwards.</figcaption>
</figure>

<figure markdown>
  [![illustration][base2]{width="480"}][base2]
  <figcaption>3. Use eight (8) 12mm M3 screws to attach the base to the PSU tray.</figcaption>
</figure>

### Reference

[![illustration][base_final]{width="640"}][base_final]

[psu1]: ../img/assembly/trays/psu/psu1.webp
[psu2]: ../img/assembly/trays/psu/psu2.webp
[psu3]: ../img/assembly/trays/psu/psu3.webp
[psu4]: ../img/assembly/trays/psu/psu4.webp
[psu5]: ../img/assembly/trays/psu/psu5.webp
[psu_final]: ../img/assembly/trays/psu/psu_final.webp

[iec1]: ../img/assembly/iec/iec1.webp
[iec2]: ../img/assembly/iec/iec2.webp

[base_prep1]: ../img/assembly/core/base/base_prep1.webp
[base_prep2]: ../img/assembly/core/base/base_prep2.webp
[base_prep3]: ../img/assembly/core/base/base_prep3.webp
[base_prep4]: ../img/assembly/core/base/base_prep4.webp
[base_prep5]: ../img/assembly/core/base/base_prep5.webp
[base_prep_final]: ../img/assembly/core/base/base_prep_final.webp

[base1]:        ../img/assembly/core/base/base1.webp
[base2]:        ../img/assembly/core/base/base2.webp
[base_final]:   ../img/assembly/core/base/base_final.webp