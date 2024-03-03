---
title: Core Assembly
summary: Instructions for assembling the Core of an OmniBox.
authors: Jon Harper
date: 2022-10-29
steps:
  attach:
    - txt: |
        1) Set the front and rear Main Bodies over the base and the align the edges.<br>
        Note: the support ghosts are caused by a software bug; supports should be removed.
      img: ../img/assembly/core/core1.webp
      img_txt: Align the main body over the base.
    - txt: |
        2) Begin inserting screws to the base, only partially tightening.<br>
        Stock: tighten woodscrews about halfway.<br>
        HSI: tighten to finger tightness.
      img: ../img/assembly/core/core2.webp
      img_txt: Begin tightening screws.
    - txt: |
        3) Continue inserting and partially tightening until all eight (8) are inserted.
      img: ../img/assembly/core/core3.webp
      img_txt: Continue installing screws.
    - txt: | 
        4) Check for any alignment problems between the Base and Main Body. When satisfied, finish tightening the screws down completely.
      img: ../img/assembly/core/core4.webp
      img_txt: Finish tightening.
  center:
    - txt: |
        1) Insert an M3 x 8mm screw in the top hole on one side of the rear Main Body. Fasten it to the mating hole on the front Main Body.
      img: ../img/assembly/core/center1.webp
      img_txt: Insert a first screw in the top hole.
    - txt: |
        2) Repeat with the top hole on the other side of the Main Body, again fastening from back to front.
      img: ../img/assembly/core/center2.webp
      img_txt: Insert a screw in the opposite top hole.
    - txt: |
        3) Use two (2) more M3 screws to fill in the remaining screw holes on one side.
      img: ../img/assembly/core/center3.webp
      img_txt: Fill out the holes on one side.
    - txt: |
        4) Repeat with the final two (2) screw holes on the opposite side.
      img: ../img/assembly/core/center4.webp
      img_txt: Fill out the remaining holes.
  crossbar:
    - txt: |
        1) Hold the crossbar between the screw holes at the top of the front main body. Note that the lip should face forward.
      img: ../img/assembly/core/crossbar1.webp
      img_txt: Align the crossbar
    - txt: |
        2) Fasten the crossbar in place with two (2) M3 x 16mm screws. Tightness can be adjusted to help square the sides of the case body.
      img: ../img/assembly/core/crossbar2.webp
      img_txt: Fasten with two screws.
---

{% import 'assembly.md' as assy %}

Next we'll add the front and rear halves of the Main Body to the Base.

## Attach the Main Body

{{ assy.overview_video(meta.video_folder + 'main_floor.mp4') }}

### Materials

=== "As Illustrated (HSI)"
    | Parts                        | Qty | Note                            |
    |------------------------------|-----|---------------------------------|
    | M3 x 6mm SHCS                | 8   |                                 |
    | :material-printer-3d-nozzle: `Main Body - Front - HSI.stl` | 1 |     |
    | :material-printer-3d-nozzle: `Main Body - Rear - HSI.stl`  | 1 |     |
=== "Stock"
    | Parts                        | Qty | Note                            |
    |------------------------------|-----|---------------------------------|
    | #6 x 3/4" sharp point screws | 8   |                                 |
    | :material-printer-3d-nozzle: `Main Body - Front - Stock.stl` | 1 |   |
    | :material-printer-3d-nozzle: `Main Body - Rear - Stock.stl`  | 1 |   |
### Directions

!!! note "Note: Alignment"
    If inserting the screws becomes difficult, back out and check:

    - That both halves of the main body are still correctly aligned; and
    - That the inserted screws are straight and not canted to the side.

    If using heat set inserts, double-check that the inserts in the Base are not crooked, as well.

{{ assy.render_steps(steps.attach, '480px') }}

### Reference

[![illustration][core_final]{width="640"}][core_final]

## Join the Main Body

{{ assy.overview_video(meta.video_folder + 'main_center.mp4') }}

### Materials

| Parts                     | Qty | Note                            |
|---------------------------|-----|---------------------------------|
| M3 x 8mm SHCS   | 6   | |

### Directions

{{ assy.render_steps(steps.center, '480px') }}

### Reference

[![illustration][center_final]{width="640"}][center_final]

## Attach the Crossbar

{{ assy.overview_video(meta.video_folder + 'crossbar.mp4') }}

### Materials 

=== "As Illustrated (HSI)"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 16mm SHCS  | 2   |                                 |
    | :material-printer-3d-nozzle: `Main Body - Crossbar - HSI.stl` | 1 | |
=== "Stock"
    | Parts                     | Qty | Note                            |
    |---------------------------|-----|---------------------------------|
    | M3 x 20mm SHCS  | 2   |                                 |
    | :material-printer-3d-nozzle: `Main Body - Crossbar - Stock.stl` | 1 | |

### Directions

{{ assy.render_steps(steps.crossbar, '480px') }}

### Reference

[![illustration][crossbar_final]{width="640"}][crossbar_final]

[base]:         base.md "Base Assembly"
[trays]:        trays.md "Tray Assembly"
[panels]:       panels.md "Panel Assembly"
[checklist]:    ../printing.md#print-checklist "Print Checklist"
[crossbar_final]: ../img/assembly/core/crossbar_final.webp
[center_final]: ../img/assembly/core/center_final.webp
[core_final]: ../img/assembly/core/core_final.webp