---
title: Lower Bay Trays
summary: Instructions for installing lower bay trays.
authors: Jon Harper
date: 2024-02-28
steps:
  lower_bay_long:
    - txt: |
        1) Snap the two (2) Wago connectors in place.
      img: ../img/assembly/trays/lower_long1.webp
      img_txt: Insert Wago connectors.
    - txt: |
        2) Attach the buck converter to the tray with two (2) M3 x 6mm screws.
      img: ../img/assembly/trays/lower_long2.webp
      img_txt: Install the buck converter.
    - txt: |
        3) Position the tray in the case. Large trays are often installed in the
        middle of the case, out of the way of side panels or CPU trays.
      img: ../img/assembly/trays/lower_long3.webp
      img_txt: Position the tray.
    - txt: |
        4) Secure the tray in place with four (4) M3 x 6mm screws.
      img: ../img/assembly/trays/lower_long4.webp
      img_txt: Secure with screws.
  lower_bay_short:
    - txt: |
        1) Set the buck converter on the tray's standoffs and secure with two (2) M3 x 6mm screws. It is a good idea to ensure the converter's voltage level is set at this point.
      img: ../img/assembly/trays/lower_short1.webp
      img_txt: Install the buck converter.
    - txt: |
        2) Position the tray in the lower bay. In this case, the tray will not fit next to the Raspberry Pi, so it is placed in the back.
      img: ../img/assembly/trays/lower_short2.webp
      img_txt: Position the tray.
    - txt: |
        3) Secure the tray to the case with four (4) M3 x 6mm screws.
      img: ../img/assembly/trays/lower_short3.webp
      img_txt: Secure with screws.
---

{% import 'assembly.md' as assy %}

## Overview

Lower bay trays can be mounted in one of six (6) locations for short trays and one of three (3) locations for long trays. This flexibility is useful when planning ahead (e.g., a buck converter can be located near the device it powers for shorter wiring).

{{ assy.overview_video(meta.video_folder + 'lower_bay.mp4') }}

## Long Trays

Long trays can be mounted in the front, middle, or back of the lower bay. They can only be mounted with the long side oriented side-to-side.

As an example of a Long tray, we'll install a buck converter for the Raspberry Pi and a pair of 5 position Wago connectors.

### Materials

| Parts                       | Qty | Note                            |
|-----------------------------|-----|---------------------------------|
| M3 x 6mm machine screws     | 6   |                                 |
| Wago 221-415 Lever Nuts     | 2   |                                 |
| SSLHONG 5V/3A Buck Converter with USB C | 1 | |
| :material-printer-3d-nozzle: `Lower Bay Tray - SSLHONG Buck - Long - HSI.stl` | 1 | |

### Directions
                                                            
{{ assy.render_steps(steps.lower_bay_long, '480px') }}

## Short Trays

Short trays can be mounted in any one of six (6) locations in the lower bay. Short trays do not always fit next to an occupied CPU bay.

In the example below, we'll install another buck converter on a short tray.

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 6mm machine screws   | 6   |                                 |
| LM2596 Buck Converter     | 1   |                                 |
| :material-printer-3d-nozzle: `Lower Bay Tray - Generic LM2596 - Short Single Tray.stl` | 1   | |

### Directions
                                                            
{{ assy.render_steps(steps.lower_bay_short, '480px') }}

## Reference

[![illustration][lower_bay_final]{ width="560" }][lower_bay_final]

[lower_bay_final]: ../img/assembly/trays/lower_final.webp