---
title: Trays
summary: OmniBox tray assembly intructions.
authors: Jon Harper
date: 2022-07-31
---

*Intro section*

## 1. CPU Tray

If you are using a SoC CPU, you will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 6mm screws           | 4   |                                 |
| M3 x 8mm screws           | 4   |                                 |
| Compatible CPU            | 1   | Here we use a Raspberry Pi 3B+  |
| Printed CPU tray          | 1   | [CPU Tray - RPi 3B Plus.stl][1] |

Otherwise, you will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 8mm screws           | 4   |                                 |
| Unused CPU tray cover     | 1   | [Unused CPU Tray Cover.stl][2]  |

Notes:

!!! note
    The instructions below are for installing with a CPU. Skip to the last step for the unused CPU tray cover.

!!! note
    The Raspberry Pi comes with M2.5 screw holes, but can be bored out easily with M3 screws.

| Step | Example |
|------|---------|
| Mount the Raspberry Pi with 6mm M3 screws to the tray. | [![raspberry pi installation][5]][5] |
| Slide the tray into the side bay on the left side. | [![tray location][6]][6] |
| Use M3 x 8mm screws to fasten the tray in place. | [![tray location][7]][7] |

## 2. Lower Bay

Lower bay trays are specific to each configuration. You may need several trays or none at all. In the example below, we demonstrate mounting a tray with a DROK 5A buck converter.

You will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 8mm screws           | 4   |                                 |
| M3 x 6mm screws           | 2-4 | Can use any length up to 12mm for this tray. |
| DROK 5A Buck Converter    | 1   |                                 |
| Printed lower bay tray    | 1   | [Lower Bay - DROK 5A Buck with LED.stl][3] |

| Step | Example |
|------|---------|
| Attach your component to the tray using at least two (2) M3 x 6mm screws | [![buck converter attached to tray][8]][8] |
| Place the tray in the lower bay. If using a full-length tray, it must be oriented front to back, as in the picture. | [![full-length tray correctly placed][9]][9] |
| Attach the tray with four (4) M3 x 8mm screws. | [![attached tray][10]][10] |

## 3. MCU Tray

You will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 6mm screws           | 4   |                                 |
| M4 x 8mm screws           | 4   |                                 |
| An MCU                    | 1   | Here we use a BigTreeTech Octopus |
| Printed MCU tray          | 1   | [MCU Tray - Octopus.stl][4]

!!! note
    The MCU tray has four M4 screw holes on the sides. Take note of the orientation of your board on the tray and where it will end up before mounting. Try to align your SD card connector toward the front and power connectors toward the back.

| Step | Example |
|------|---------|
| Attach your MCU with the four (4) M3 x 6mm screws to the tray. | [![mounting the mcu][11]][11] |
| Place the tray in the case and check that it is oriented correctly. Secure the tray with four (4) M4 x 8mm screws. | [![screws attached][12]][12] |


Before going further, it's a good time to connect the PSU to the devices we just added. **Be careful of polarity.**

[1]: https://github.com/jon-harper/OmniBox/blob/main/Trays/CPU/Raspberry%20Pi%203B%20Plus/CPU%20Tray%20-%20RPi%203B%20Plus.stl
[2]: https://github.com/jon-harper/OmniBox/blob/main/Trays/CPU/Unused%20CPU%20Tray%20Cover.stl
[3]: https://github.com/jon-harper/OmniBox/blob/main/Trays/Lower%20Bay/DROK%205A%20Buck%20with%20LED/Lower%20Bay%20-%20DROK%205A%20Buck%20with%20LED.stl
[4]: https://github.com/jon-harper/OmniBox/blob/main/Trays/MCU/BTT%20Octopus/MCU%20Tray%20-%20Octopus.stl
[5]: ../img/assembly/cpu_tray.jpg
[6]: ../img/assembly/cpu_insert.jpg
[7]: ../img/assembly/cpu_finished.jpg
[8]: ../img/assembly/lower_bay_tray.jpg
[9]: ../img/assembly/lower_bay_placement.jpg
[10]: ../img/assembly/lower_bay_finished.jpg
[11]: ../img/assembly/mcu_placement.jpg
[12]: ../img/assembly/mcu_finished.jpg