---
title: Lower Bay Trays
summary: Instructions for installing lower bay trays.
authors: Jon Harper
date: 2022-10-30
---

## Overview

Lower bay trays can be mounted in one of six (6) locations for short trays and one of three (3) locations for long trays. This flexibility is useful when planning ahead (e.g., a buck converter can be located near the device it powers for shorter wiring).

<video controls="">
    <source src="https://jon-harper.github.io/OmniBox/video/0.9.9/lower_bay.mp4" type="video/mp4">
</video>

## Long Trays

Long trays can be mounted in the front, middle, or back of the lower bay. They can only be mounted with the long side oriented sideways.

### Materials

=== "As Illustrated"

    | Parts                       | Qty | Note                            |
    |-----------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws     | 8   |                                 |
    | Wago 221-413 Lever Nuts     | 4   |                                 |
    | [:material-git: `Lower Bay Tray - Wago Nuts - 8x3P.stl`][git_wago_221] | 1   | :material-printer-3d-nozzle: Printed |


=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | Compatible hardware       | 1   |                                 |
    | Long Lower Bay Tray       | 1   | :material-printer-3d-nozzle: Printed  |

    Only screws for mounting the tray are specified in the generic materials list.

### Directions
                                                            
<figure markdown>
  [![illustration][long1]{width="480"}][long1]
  <figcaption>1. Snap the Wago connectors in place. We leave half of the tray unoccupied for future expansion.</figcaption>
</figure>

<figure markdown>
  [![illustration][long2]{width="480"}][long2]
  <figcaption>2. Determine the best location for the tray. Here, it is set in the center to shorten wiring.</figcaption>
</figure>

<figure markdown>
  [![illustration][long3]{width="480"}][long3]
  <figcaption>3. Secure with four (4) M4 x 6mm screws.</figcaption>
</figure>

## Short Trays

Short trays can be mounted in any one of six (6) locations in the lower bay. Short trays do not always fit next to an occupied CPU bay.

### Materials


=== "As Illustrated"
    
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 6   |                                 |
    | LM2596 Buck Converter     | 1   |                                 |
    | [:material-git: `Lower Bay Tray - Generic LM2596 - Short Single Tray.stl`][git_basic_lm2596] | 1   | :material-printer-3d-nozzle: Printed |

=== "Generic"

    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 6mm machine screws   | 4   |                                 |
    | Compatible hardware       | 1   |                                 |
    | Short Lower Bay Tray      | 1   | :material-printer-3d-nozzle: Printed |

    Only screws for mounting the tray are specified in the generic materials list.

### Directions
                                                            
<figure markdown>
  [![illustration][short1]{width="480"}][short1]
  <figcaption>1. Set the buck converter on the tray's standoffs and secure with four (4) M4 x 6mm screws. It is a good idea to ensure the converter's voltage level is set at this point.</figcaption>
</figure>

<figure markdown>
  [![illustration][short2]{width="480"}][short2]
  <figcaption>2. Determine the best location for the tray in the lower bay. In this case, the tray will not fit next to the Raspberry Pi, so it is placed in the back.</figcaption>
</figure>

<figure markdown>
  [![illustration][short3]{width="480"}][short3]
  <figcaption>3. Secure the tray to the case with four (4) M4 x 6mm screws.</figcaption>
</figure>

## Reference

![illustration][lower_bay_final]

[long1]: ../img/assembly/trays/lower_bay/long1.webp
[long2]: ../img/assembly/trays/lower_bay/long2.webp
[long3]: ../img/assembly/trays/lower_bay/long3.webp

[short1]: ../img/assembly/trays/lower_bay/short1.webp
[short2]: ../img/assembly/trays/lower_bay/short2.webp
[short3]: ../img/assembly/trays/lower_bay/short3.webp
[lower_bay_final]: ../img/assembly/trays/lower_bay/lower_bay_final.webp