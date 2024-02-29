---
title: Side Panels
summary: Installing side panels for an OmniBox.
authors: Jon Harper
date: 2022-10-30
---

{% import 'assembly.md' as assy %}

Each case has four (4) locations for a side panel. If you have an SoC CPU, one side panel is already occupied by the CPU tray. In this case, you will instead need three (3) side panels.

## Overview

{{ assy.overview_video(meta.video_folder + 'side.mp4') }}

## Materials

These lists assume three (3) side panels are needed.

=== "As Illustrated"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 6   |                                 |
    | M3 x 8mm machine screws   | 12  | May substitute 10mm or 12mm.    |
    | M3 x 15mm machine screws  | 4   | May substitute 16mm.            |
    | 40mm x 10mm Axial Fan     | 1   |                                 |
    | RJ-45 Extension (panel mount) | 1   |                             |
    | USB Extension (panel mount) | 2   |                               |
    | [:material-git: `Side Panel - Internal 40mm Fan - OmniBox Logo.stl`][git_40mm_side_panel] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: `Side Panel - RJ-45 & Dual USB.stl`][git_rj45_usb_side_panel] | 1   | :material-printer-3d-nozzle: Printed |
    | [:material-git: `Side Panel - Blank.stl`][git_blank_side_panel] | 1   | :material-printer-3d-nozzle: Printed |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 8mm machine screws   | 12  | May substitute 10mm or 12mm.    |
    | [:material-git: Side Panel][git_side_panel] | 3   | :material-printer-3d-nozzle: Printed |

## Directions
                                                            
<figure markdown>
  [![illustration][side1]][side1]
  <figcaption>1. Use four (4) 15mm screws to attach the 40mm fan to the Internal 40mm Fan side panel. Here the fan is used as an intake.</figcaption>
</figure>

<figure markdown>
  [![illustration][side2]{width="480"}][side2]
  <figcaption>2. Place the assembled side panel against the case body. Note that the top and bottom screw holes are not symmetrical. This fan will act as a second intake in the front, opposite the one on the Raspberry Pi.</figcaption>
</figure>

<figure markdown>
  [![illustration][side3]{width="480"}][side3]
  <figcaption>3. Fasten with four (4) M3 screws at least 8mm long. </figcaption>
</figure>

<figure markdown>
  [![illustration][side4]][side4]
  <figcaption>4. The next side panel is for RJ-45 and USB panel mounted extensions. First determine the correct orientation for the RJ-45 socket.</figcaption>
</figure>

<figure markdown>
  [![illustration][side5]][side5]
  <figcaption>5. Secure with two 6mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][side6]][side6]
  <figcaption>6. The USB connectors do not have a fixed orientation. The USB connector will insert slightly into the panel mount. Secure the extensions with 6mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][side7]{width="480"}][side7]
  <figcaption>7. Slide the panel in place and fasten with four (4) 8mm screws.</figcaption>
</figure>

<figure markdown>
  [![illustration][side8]{width="480"}][side8]
  <figcaption>8. Attach the remaining (blank) panel with the remaining four (4) 8mm screws.</figcaption>
</figure>

## Reference

[![illustration][side_final]][side_final]

[side1]: ../img/assembly/panels/side/side1.webp
[side2]: ../img/assembly/panels/side/side2.webp
[side3]: ../img/assembly/panels/side/side3.webp
[side4]: ../img/assembly/panels/side/side4.webp
[side5]: ../img/assembly/panels/side/side5.webp
[side6]: ../img/assembly/panels/side/side6.webp
[side7]: ../img/assembly/panels/side/side7.webp
[side8]: ../img/assembly/panels/side/side8.webp
[side_final]: ../img/assembly/panels/side/side_final.webp