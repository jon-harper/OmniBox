---
title: Core
summary: Instructions for core body assembly.
authors: Jon Harper
date: 2022-07-31
---

## 1. Base

You will need:

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M4 x 16mm screws          | 4   | Can substitute with M4 x 20mm   |
| M3 x 16mm screws          | 2   | Can substitute with M3 x 20mm   |
| M3 hex nuts               | 2   |                                 |
| SPST toggle switch        | 1   |                                 |
| IEC C14 socket with fuse  | 1   |                                 |
| Printed front base        | 1   | [Base - Front.stl][3]           |
| Printed rear base         | 1   | [Base - Rear.stl][4]            |

Directions

| Step | Example |
|------|---------|
| The front and rear parts of the base both have two (2) holes on each side. Use the four (4) M4 screws to fasten them together. **Note:** Make sure the sawtooth air vents on both halves are facing the same direction, as in the picture. | [![assembled base][1]][1] |
| Push the power switch into the cutout in the front of the base. The sides of the switch will compress until it snaps into place. | [![power switch insertion][2]][2] |
| Insert the IEC socket into the rear base, followed by the M3 x 16mm screws.| [![inserted IEC socket and M3 screws][5]][5] |
| There are two pockets for hex nuts opposing the M3 screws. One hex nut at a time, press a nut in place while turning the opposing screw. Once the threads of the screw catch the nut, continue threading until the nut is tight. | [![tightened hex nuts][6]][6] |
| Now is a good time to run the AC wiring for the power supply. Zip tie anchors are available for the wire run from socket to switch and back to power supply. | [![power supply with cleaned up wiring][7]][7] |

## 2. Main Body

You will need:

| Parts                     | Qty | Note                              |
|---------------------------|-----|-----------------------------------|
| M3 x 8mm screws           | 6   | Can substitute M3 x 10mm or 12mm. |
| #6 x 3/4" screws          | 8   | See note below.                   |
| M3 x 16mm screws          | 2   | Can substitute M3 x 20mm.         |
| M4 x 6mm screws           | 4   | See caution below.                |
| Printed front main body   | 1   | [Main Body - Front No Fans.stl][9] used here. |
| Printed rear main body    | 1   | [Main Body - Rear with 40mm Exhausts.stl][10] used here. |
| Printed crossbar          | 1   | [Main Body - Crossbar][8]         |
| A power supply unit (PSU) | 1   |                                   |

Notes and Cautions:

!!! note
    Sharp point screws are easier to use than machine scews for attaching the main body and base. For this you can use #6 x 3/4" screws (SAE) or M3 x 20mm (metric) screws found at any hardware store. If these are not convenient or available, machine screws will work in their place.
    
!!! caution
    Always stop if you feel resistance when fastening screws to the power supply.
    
    Screws longer than 8mm may touch components in the power supply and short or damage them. Most models have no extra cleareance for overtightening if 8mm screws are used; thus we advice 6mm for safety.

Directions:

| Step | Example |
|------|---------|
| Using six (6) M3 x 8mm screw, add a screw at a time to fasten the rear body to the front. Alternate sides with each screw. **Note**: Insert the screws from the back to the front of the case. | [![inserting m3 screws][11]][11]
| Here we have all six screws inserted. | [![finished][12]][12]|
| Line up the holes on the top of the power supply with the main body. The holes pointed at in the picture need to align. | [![power supply location][13]][13] |
| Mount the power supply using four (4) M4 x 8mm screws. | [![power supply location][14]][14] |
| Place the assembled main body on top of the base. Using your long machine or sheet metal screws, partially thread one screw near one of the rear corners and an opposing front corner. | [![first two screws][15]][15] |
| Fasten the main body and base together with your long M3 screws or sheet metal screws. | [![remaining screws inserted][16]][16] |
| Place the crossbar in place at the joint between the lid and display mounts. Take note of the orientation in the picture. | [![crossbar assembly][17]][17]
| Attach the crossbar with an M3 x 16mm screw in each side. | [![crossbar assembly][18]][18]

## 3. Fans

Fan locations and sizes vary by configuration. This step is specific to the configuration assembled in this guide. The length of screws needed and printed parts will vary, but the method of mounting fans used here is identical for all fan sizes.

!!! note
    60mm and smaller fans are mounted with M3 screws. 80mm and larger user M4 screws.

You will need:

| Parts                     | Qty | Note                              |
|---------------------------|-----|-----------------------------------|
| M3 x 20mm screws          | 8   |                                   |
| 40x40x10mm fans           | 2   | Can use 4015 or 4020 fans with the correct fan cage and gasket. |
| Printed 40mm fan cage     | 2   | [4010 Fan Cage.stl][19]           |
| Printed TPU gasket        | 2   | Optional. [4010 Fan Gasket, TPU.stl][20] |

| Step | Example |
|------|---------|
| Place a fan inside the cage. The stickered side of the motor indicates direction of airflow, so we have it facing towards the fan grill. | [![fan inside the mounting cage, sticker side up][21]][21] |
| (Optional) If you are using TPU gaskets, place a gasket over the fan and cage. Carefully cut out a small space for the wire to pass through. | [![tpu gasket over the fan and cage][22]][22] |
| Insert the fan's wires through the cutout in the main body. Partially thread in two (2) M3 x 20mm screws on opposing sides of the fan cage. | [![fan with screws][24]][24]
| Insert and thread the other two (2) M3 screws. Ensure the fan's wires do not pinch or bind, then finish tightening all four (4) screws. | [![fans installed][25]][25] |
| Repeat the above process for the second fan. | [![fan wires][26]][26] |

[1]: ../img/assembly/base_assembled.jpg
[2]: ../img/assembly/base_switch.jpg
[3]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Front.stl
[4]: https://github.com/jon-harper/OmniBox/blob/main/Core/Base%20-%20Rear.stl
[5]: ../img/assembly/base_iec.jpg
[6]: ../img/assembly/base_hex_nuts.jpg
[7]: ../img/assembly/base_wiring.jpg
[8]: https://github.com/jon-harper/OmniBox/blob/main/Core/Main%20Body%20-%20Crossbar.stl
[9]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Front%20No%20Fans.stl
[10]: https://github.com/jon-harper/OmniBox/blob/main/Core/Mean%20Well%20LRS-350/Main%20Body%20-%20Rear%20with%2040mm%20Exhausts.stl
[11]: ../img/assembly/main_halves_1.jpg
[12]: ../img/assembly/main_halves_2.jpg
[13]: ../img/assembly/psu_holes.jpg
[14]: ../img/assembly/psu_finished.jpg
[15]: ../img/assembly/core_1.jpg
[16]: ../img/assembly/core_2.jpg
[17]: ../img/assembly/crossbar_1.jpg
[18]: ../img/assembly/crossbar_2.jpg
[19]: https://github.com/jon-harper/OmniBox/blob/main/Fan%20Cages/40mm%20x%2010mm%20Fan/4010%20Fan%20Cage.stl
[20]: https://github.com/jon-harper/OmniBox/blob/main/Fan%20Cages/40mm%20x%2010mm%20Fan/4010%20Fan%20Gasket%2C%20TPU.stl
[21]: ../img/assembly/fan_cage.jpg
[22]: ../img/assembly/fan_gasket.jpg
[24]: ../img/assembly/fan_screws1.jpg
[25]: ../img/assembly/fan_screws2.jpg
[26]: ../img/assembly/fan_finished.jpg