---
title: Base Assembly
summary: Instructiosn for assembling the base and PSU tray.
authors: Jon Harper
date: 2022-10-29
---

In this section we will assemble the :material-alpha-c-box: :material-alpha-b-box-outline: Base and :material-alpha-t-box: :material-alpha-p-box-outline: PSU Tray.

## Power Supply Tray

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 16mm machine screws  | 2   | Can use screws up to 20mm.      |
| Compatible power supply   | 1   | Ex: Mean Well LRS-350           |
| Printed :material-alpha-t-box: :material-alpha-p-box-outline: PSU Tray halves  | 1   | Both left and right STLs.       |

| Steps | Illustration |
|-------|--------------|
| Orient the power supply so that the terminals are facing away from you and oriented upwards. | ![illustratino][psu1] |
| Place the  | ![illustration][psu2] |
|  | ![illustration][psu3] |
|  | ![illustration][psu4] |
|  | ![illustration][psu5] |


## Prepare the Base

You will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 12mm machine screws  | 2   | Can use screws up to 20mm.      |
| M3 x 16mm machine screws  | 4   | Four per fan.                   |
| 40mm x 10mm axial fan     | 0-3 | Optional, up to three.          |
| SPST toggle switch        | 1   |                                 |
| IEC C14 socket with fuse  | 1   |                                 |
| :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-f-box-outline: Base - Front | 1   | [Base - Front.stl][git_base_front] |
| :material-alpha-c-box: :material-alpha-b-box-outline: :material-alpha-r-box-outline: Base - Rear  | 1   | [Base - Rear.stl][git_base_rear]   |

!!! note
    The [unified base][git_base_unified] replaces both the front and rear bases and requires no additional parts.

| Steps | Illustration |
|-------|--------------|
| | ![illustration][base1] |
| | ![illustration][base2] |
| | ![illustration][base3] |
| | ![illustration][base4] |
| | ![illustration][base5] |

## Combine Base and PSU

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 16mm machine screws  | 6   | Can use screws up to 20mm.      |

| Steps | Illustration |
|-------|--------------|
| Turn the PSU tray assembly so that the PSU terminals are oriented downards and away from you. | ![illustration][psu6] |
| Setup the base halves and power supply, lining up the screw holes in the base with the side of the PSU tray. | ![illustration][base6] |
| Use the 16mm M3 screws to attach the base to the PSU tray. | ![illustration][base7] |

[trays]: trays.md "Tray Assembly"
[panels]:  panels.md "Panel Assembly"
[checklist]: ../printing.md#print-checklist "Print Checklist"

[psu1]: ../img/assembly/psu/psu1.png
[psu2]: ../img/assembly/psu/psu2.png
[psu3]: ../img/assembly/psu/psu3.png
[psu4]: ../img/assembly/psu/psu4.png
[psu5]: ../img/assembly/psu/psu5.png
[psu6]: ../img/assembly/psu/psu6.png

[base1]: ../img/assembly/base/base1.png
[base2]: ../img/assembly/base/base2.png
[base3]: ../img/assembly/base/base3.png
[base4]: ../img/assembly/base/base4.png
[base5]: ../img/assembly/base/base5.png
[base6]: ../img/assembly/base/base6.png
[base7]: ../img/assembly/base/base7.png